"""Independent static evidence inspection. Writes only to this assessment folder."""
from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
import collections
import hashlib
import json
import posixpath
from urllib.parse import unquote

BASE = Path('/TEST_WORKDIR')
OUT = BASE / 'assessment'
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
B = 'http://schemas.openxmlformats.org/officeDocument/2006/bibliography'
NS = {'w': W, 'b': B}
WQ = '{' + W + '}'
sha = lambda data: hashlib.sha256(data).hexdigest()

def inspect(path):
    with ZipFile(path) as z:
        bad_member = z.testzip()
        order = z.namelist()
        parts = {n: z.read(n) for n in order}
        zipinfo = {i.filename: {k: getattr(i, k) for k in ('date_time', 'compress_type', 'create_system', 'create_version', 'extract_version', 'flag_bits', 'volume', 'internal_attr', 'external_attr')} for i in z.infolist()}
    roots = {n: E.fromstring(data) for n, data in parts.items() if n.endswith(('.xml', '.rels'))}
    fields, structural_errors, paragraphs = [], [], []
    for name, root in roots.items():
        if not (name.startswith('word/') and name.endswith('.xml')):
            continue
        ps = list(root.iter(WQ + 'p'))
        p_index = {p: i + 1 for i, p in enumerate(ps)}
        for p in ps:
            texts = []
            for e in p.iter():
                if e.tag == WQ + 't': texts.append(e.text or '')
                elif e.tag == WQ + 'br': texts.append('\n')
                elif e.tag == WQ + 'footnoteReference': texts.append('[footnote:' + e.get(WQ + 'id') + ']')
            if texts:
                paragraphs.append({'part': name, 'paragraph': p_index[p], 'text': ''.join(texts)})
        stack = []
        for e in root.iter():
            if e.tag == WQ + 'fldChar':
                kind = e.get(WQ + 'fldCharType')
                if kind == 'begin':
                    p = next((a for a in e.iterancestors() if a.tag == WQ + 'p'), None)
                    st = p.find('w:pPr/w:pStyle', NS) if p is not None else None
                    region = 'footnote' if name == 'word/footnotes.xml' else 'caption' if st is not None and st.get(WQ + 'val') == 'Caption' else 'body'
                    stack.append({'part': name, 'paragraph': p_index.get(p), 'region': region, 'instruction': '', 'cache': '', 'markers': [dict(e.attrib)], 'separate': False, 'closed': False})
                elif not stack:
                    structural_errors.append(f'{name}: {kind} marker without open field')
                elif kind == 'separate':
                    if stack[-1]['separate']: structural_errors.append(f'{name}: repeated separate marker')
                    stack[-1]['separate'] = True
                    stack[-1]['markers'].append(dict(e.attrib))
                elif kind == 'end':
                    f = stack.pop()
                    f['markers'].append(dict(e.attrib))
                    f['closed'] = True
                    fields.append(f)
            elif e.tag == WQ + 'instrText' and stack:
                stack[-1]['instruction'] += e.text or ''
            elif e.tag == WQ + 't' and stack and stack[-1]['separate']:
                stack[-1]['cache'] += e.text or ''
            elif e.tag == WQ + 'br' and stack and stack[-1]['separate']:
                stack[-1]['cache'] += '\n'
            elif e.tag == WQ + 'fldSimple':
                fields.append({'part': name, 'simple_field': E.tostring(e).decode()})
        if stack: structural_errors.append(f'{name}: {len(stack)} unclosed fields')
    rels = []
    for name, root in roots.items():
        if not name.endswith('.rels'): continue
        directory = '' if name == '_rels/.rels' else str(Path(name).parent.parent)
        for e in root:
            r = dict(e.attrib)
            r['part'] = name
            if r.get('TargetMode') != 'External':
                r['resolved_part'] = posixpath.normpath(posixpath.join(directory, unquote(r['Target']))).lstrip('/')
                r['target_present'] = r['resolved_part'] in parts
            rels.append(r)
    source_roots = [(n, r) for n, r in roots.items() if r.tag == '{' + B + '}Sources']
    sources = []
    for name, root in source_roots:
        for e in root.findall('b:Source', NS):
            sources.append({'part': name, **{k: e.findtext('b:' + k, namespaces=NS) for k in ['Tag', 'Guid', 'Title', 'Year', 'Publisher', 'RefOrder']}, 'authors': [{'first': a.findtext('b:First', namespaces=NS), 'last': a.findtext('b:Last', namespaces=NS)} for a in e.findall('.//b:Person', NS)]})
    citation_fields = [f for f in fields if f.get('instruction', '').strip().startswith('CITATION ')]
    source_tags = [s['Tag'] for s in sources]
    citation_tags = [f['instruction'].split()[1] for f in citation_fields]
    doc = roots['word/document.xml']
    notes = roots['word/footnotes.xml']
    interesting_tags = ['tbl', 'txbxContent', 'drawing', 'object', 'altChunk', 'ins', 'del', 'moveFrom', 'moveTo', 'pPrChange', 'rPrChange', 'sectPrChange', 'trackRevisions']
    flags = {tag: sum(len(r.findall('.//' + WQ + tag)) for r in roots.values()) for tag in interesting_tags}
    info = {
        'path': str(path), 'sha256': sha(path.read_bytes()), 'zip_crc_failure': bad_member,
        'member_count': len(order), 'members': order, 'xml_parts_parsed': len(roots),
        'fields': fields, 'field_errors': structural_errors, 'field_count': len(fields),
        'citation_count': len(citation_fields), 'citation_regions': dict(collections.Counter(f['region'] for f in citation_fields)),
        'source_count': len(sources), 'sources': sources, 'citation_tags': citation_tags,
        'all_citation_tags_resolve': all(t in source_tags for t in citation_tags),
        'source_tags_unique': len(source_tags) == len(set(source_tags)),
        'stored_style': [dict(r.attrib) for _, r in source_roots],
        'paragraphs': paragraphs, 'main_paragraph_count': len(doc.findall('.//' + WQ + 'p')),
        'footnotes': [{'id': n.get(WQ + 'id'), 'type': n.get(WQ + 'type')} for n in notes],
        'note_anchors': [dict(n.attrib) for n in doc.findall('.//' + WQ + 'footnoteReference')],
        'bookmarks_start': [dict(n.attrib) for n in doc.findall('.//' + WQ + 'bookmarkStart')],
        'bookmarks_end': [dict(n.attrib) for n in doc.findall('.//' + WQ + 'bookmarkEnd')],
        'relationships': rels, 'all_internal_targets_present': all(r.get('target_present', True) for r in rels),
        'structure_indicator_counts': flags,
    }
    return info, parts, order, zipinfo

fixtures = {}
fixture_data = {}
for case in ['a', 'b']:
    result = inspect(BASE / 'fixtures' / f'case-{case}.docx')
    fixtures[case] = result[0]
    fixture_data[case] = result

runs = {}
for run in ['guided-a', 'guided-b', 'control']:
    input_matches = {p.name: sha(p.read_bytes()) == sha((BASE / 'fixtures' / p.name).read_bytes()) for p in (BASE / 'runs' / run / 'inputs').iterdir() if p.is_file()}
    after, a, ao, ai = inspect(BASE / 'runs' / run / 'output' / 'revised-b.docx')
    before, b, bo, bi = fixture_data['b']
    changed = [n for n in bo if a.get(n) != b[n]]
    exact = a['word/document.xml'] == b['word/document.xml'].replace(b'The catalogue containss two registers ', b'The catalogue contains two registers ', 1)
    checks = {
        'all_four_inputs_match_fixtures': len(input_matches) == 4 and all(input_matches.values()),
        'case_a_input_byte_identical': input_matches['case-a.docx'],
        'same_member_names_and_order': ao == bo,
        'zip_entry_metadata_identical': ai == bi,
        'only_document_xml_changed': changed == ['word/document.xml'],
        'document_xml_exact_one_prose_replacement': exact,
        'all_other_17_member_payloads_identical': len(changed) == 1 and len(bo) == 18,
        'seven_complete_fields_identical': after['fields'] == before['fields'] and len(after['fields']) == 7 and not after['field_errors'] and all(f.get('separate') and f.get('closed') for f in after['fields']),
        'four_citations_body_caption_note_preserved': after['citation_count'] == 4 and after['citation_regions'] == {'body': 2, 'caption': 1, 'footnote': 1},
        'six_sources_and_ids_preserved': after['sources'] == before['sources'] and after['source_count'] == 6,
        'bookmarks_preserved': after['bookmarks_start'] == before['bookmarks_start'] and after['bookmarks_end'] == before['bookmarks_end'],
        'footnote_and_source_relationships_preserved': after['relationships'] == before['relationships'] and after['all_internal_targets_present'],
        'note_anchors_preserved': after['note_anchors'] == before['note_anchors'],
        'zip_integrity_and_xml_parse_pass': after['zip_crc_failure'] is None,
    }
    png = BASE / 'runs' / run / 'output' / ('render-b' if run == 'guided-b' else 'rendered-b') / 'page-1.png'
    pdf = png.parent / 'revised-b.pdf'
    runs[run] = {'input_matches': input_matches, 'checks': checks, 'all_checks_pass': all(checks.values()), 'changed_members': changed, 'artifact': after, 'render_png': str(png), 'render_png_sha256': sha(png.read_bytes()), 'render_pdf': str(pdf), 'render_pdf_sha256': sha(pdf.read_bytes())}

result = {'method': 'Independently parsed current original fixtures and each actual revised DOCX. Did not rely on run verification files for the checks.', 'native_word_refresh_tested': False, 'fixtures': fixtures, 'runs': runs}
(OUT / 'artifact_checks.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({'fixtures': {case: {'sha256': d['sha256'], 'fields': d['field_count'], 'citation_regions': d['citation_regions'], 'sources': d['source_count'], 'all_internal_targets_present': d['all_internal_targets_present'], 'structure_indicator_counts': d['structure_indicator_counts']} for case, d in fixtures.items()}, 'runs': {run: {'checks': r['checks'], 'sha256': r['artifact']['sha256'], 'render_png_sha256': r['render_png_sha256']} for run, r in runs.items()}}, indent=2))
