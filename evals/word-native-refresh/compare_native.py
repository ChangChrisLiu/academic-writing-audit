from pathlib import Path
import json, re
root=Path(__file__).resolve().parent
before=json.loads((root/'before.inventory.json').read_text())
after=json.loads((root/'native-refreshed.inventory.json').read_text())
def sources(x):
 return {s['tag']:s for p in x['source_parts'] for s in p['sources']}
def core_fields(x):
 return [f for f in x['fields'] if f['instruction'].split()[0] in ['CITATION','BIBLIOGRAPHY']]
def keyed(x):
 out={}
 for f in core_fields(x):
  tokens=f['instruction'].split();key=tokens[1] if tokens[0]=='CITATION' else 'BIBLIOGRAPHY'
  out.setdefault(key,[]).append(f)
 return out
b=keyed(before);a=keyed(after);src=sources(after)
checks={
 'source_identities_preserved':sources(before)==src,
 'field_instructions_preserved':sorted(f['instruction'] for f in before['fields'])==sorted(f['instruction'] for f in after['fields']),
 'no_unexpected_fields':len(after['fields'])==len(core_fields(after)),
 'citation_and_bibliography_targets_preserved':{k:len(v) for k,v in b.items()}=={k:len(v) for k,v in a.items()},
 'two_citation_fields_and_one_bibliography':len(core_fields(after))==3 and set(a)=={'Orchid2024','Vale2025','BIBLIOGRAPHY'},
 'fields_structurally_complete':all(f.get('kind')=='simple' or (f.get('closed') and f.get('has_separator')) for f in core_fields(after)),
 'no_pending_caches':all('AWAITING WORD REFRESH' not in f['cache'] for f in core_fields(after)),
 'body_and_table_citation_regions_preserved':all(a.get(k) and a[k][0].get('region')==b[k][0].get('region') for k in ['Orchid2024','Vale2025']),
}
rows=[]
for tag in ['Orchid2024','Vale2025']:
 f=a.get(tag,[{}])[0];s=src.get(tag,{});cache=f.get('cache','')
 display_matches=bool(s) and all(author['last'].lower() in cache.lower() for author in s['authors']) and s['year'] in cache
 rows.append({'source_tag':tag,'region':f.get('region'),'field_code':f.get('instruction'),'displayed_citation':cache,'citation_matches_source':display_matches})
checks['displayed_citations_match_sources']=all(x['citation_matches_source'] for x in rows)
bib=a.get('BIBLIOGRAPHY',[{}])[0].get('cache','')
for row in rows:
 s=src.get(row['source_tag'],{}); title=s.get('title',''); year=s.get('year','')
 row['reference_entry_present']=bool(title and year) and title.lower() in bib.lower() and year in bib
 row['title_occurrences_in_bibliography']=bib.lower().count(title.lower()) if title else 0
checks['each_citation_has_one_bibliography_entry']=all(x['reference_entry_present'] and x['title_occurrences_in_bibliography']==1 for x in rows)
# This is a deliberately closed two-source fixture. Extra text or entries still require visual review.
checks['each_embedded_source_is_cited']=set(src)=={x['source_tag'] for x in rows}
report={'scope':'Constructed two-source fixture; these structural/display checks require a separate actual native execution record and visual review.','before_sha256':before['sha256'],'after_sha256':after['sha256'],'checks':checks,'mappings':rows,'bibliography_display':bib,'configured_source_style':[p['attributes'] for p in after['source_parts']],'style_edition':'Not inferred from XML version number or parenthetical appearance.','unexpected_fields':[f for f in after['fields'] if f not in core_fields(after)],'all_static_checks_pass':all(checks.values())}
(root/'native-comparison.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2));raise SystemExit(not all(checks.values()))
