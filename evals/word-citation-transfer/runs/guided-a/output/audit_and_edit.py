from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import hashlib, json

BASE=Path('/TEST_WORKDIR/runs/guided-a')
OUT=BASE/'output'
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
B='http://schemas.openxmlformats.org/officeDocument/2006/bibliography'
NS={'w':W,'b':B}
q=lambda n:'{'+W+'}'+n
sha=lambda b:hashlib.sha256(b).hexdigest()

def text(el):
    return ''.join('\n' if e.tag==q('br') else e.text or '' for e in el.iter() if e.tag in [q('t'),q('delText'),q('br')])

def audit(path):
    r={'file':str(path),'sha256':sha(path.read_bytes()),'paragraphs':[], 'fields':[], 'source_records':[], 'parts':{},'structure':{}}
    with ZipFile(path) as z:
        r['parts']={i.filename:sha(z.read(i.filename)) for i in z.infolist()}
        for name in z.namelist():
            if not name.endswith('.xml'): continue
            root=etree.fromstring(z.read(name))
            if name.startswith('customXml/') and root.tag=='{'+B+'}Sources':
                r['stored_style']=dict(root.attrib)
                for s in root:
                    record={etree.QName(e).localname:e.text for e in s if len(e)==0}
                    record['authors']=[{'first':p.findtext('b:First',namespaces=NS),'last':p.findtext('b:Last',namespaces=NS)} for p in s.findall('.//b:Person',NS)]
                    r['source_records'].append(record)
            if name.startswith('word/'):
                count_tags=['ins','del','delText','moveFrom','moveTo','moveFromRangeStart','moveToRangeStart','pPrChange','rPrChange','sectPrChange','tblPrChange','trackRevisions','tbl','txbxContent','altChunk','drawing','object','sdt','fldSimple','footnoteReference','endnoteReference','commentReference','bookmarkStart','bookmarkEnd']
                r['structure'][name]={tag:len(root.findall('.//w:'+tag,NS)) for tag in count_tags}
                stack=[]
                for i,p in enumerate(root.findall('.//w:p',NS),1):
                    if name not in ('word/document.xml','word/footnotes.xml') and not text(p):continue
                    loc=f'{name} paragraph {i}'
                    anc=p.getparent()
                    if anc.tag==q('footnote'):loc=f'{name} footnote {anc.get(q("id"))} paragraph {i}'
                    r['paragraphs'].append({'location':loc,'text':text(p)})
                    for e in p.iter():
                        if e.tag==q('fldChar'):
                            typ=e.get(q('fldCharType'))
                            if typ=='begin':stack.append({'location':loc,'instruction':'','result':'','state':'instruction','begin_attributes':dict(e.attrib)})
                            elif typ=='separate':
                                assert stack, (path,loc)
                                stack[-1]['state']='result'
                            elif typ=='end':
                                assert stack, (path,loc)
                                f=stack.pop(); f.pop('state');r['fields'].append(f)
                        elif stack and e.tag==q('instrText'):stack[-1]['instruction']+=e.text or ''
                        elif stack and stack[-1]['state']=='result' and e.tag in [q('t'),q('br')]:stack[-1]['result']+= '\n' if e.tag==q('br') else e.text or ''
                assert not stack,(path,name,'unclosed field')
        r['package_xml_parse']='all XML parts parsed'
        r['zip_crc_test']=z.testzip()
    return r

before={name:audit(BASE/'inputs'/name) for name in ['case-a.docx','case-b.docx']}
(OUT/'before-ledger.json').write_text(json.dumps(before,indent=2,ensure_ascii=False))
original=BASE/'inputs/case-b.docx'
revised=OUT/'revised-b.docx'
with ZipFile(original) as zin:
    blob=zin.read('word/document.xml')
    old=b'The catalogue containss two registers '
    new=b'The catalogue contains two registers '
    assert blob.count(old)==1
    root=etree.fromstring(blob)
    p=root.find('w:body',NS).findall('w:p',NS)[2]
    assert p[0].tag==q('r') and p[0][0].tag==q('t')
    assert p[0][0].text==old.decode()
    assert len(p[0])==1
    assert p[1].find('w:fldChar',NS).get(q('fldCharType'))=='begin'
    with ZipFile(revised,'w') as zout:
        for info in zin.infolist():
            data=zin.read(info.filename)
            if info.filename=='word/document.xml':data=data.replace(old,new,1)
            zout.writestr(info,data)

after=audit(revised)
b=before['case-b.docx']
assert list(b['parts'])==list(after['parts'])
changed=[n for n in b['parts'] if b['parts'][n]!=after['parts'][n]]
assert changed==['word/document.xml']
assert b['fields']==after['fields']
assert b['source_records']==after['source_records']
assert b['structure']==after['structure']
assert b['stored_style']==after['stored_style']
with ZipFile(original) as x,ZipFile(revised) as y:
    assert y.read('word/document.xml')==x.read('word/document.xml').replace(old,new,1)
    assert all(x.getinfo(n)==y.getinfo(n) or x.read(n)==y.read(n) for n in x.namelist() if n!='word/document.xml')
validation={'changed_members':changed,'exact_only_document_xml_change':{'from':old.decode(),'to':new.decode()},'all_other_uncompressed_members_byte_identical':True,'fields_before_after_identical':True,'field_count':len(after['fields']),'source_records_before_after_identical':True,'structure_before_after_identical':True,'stored_style_before_after_identical':True,'saved_docx_closed_and_reopened_with_zipfile':True,'native_application_open_refresh_save_reopen':False,'inputs_unchanged':all(sha((BASE/'inputs'/n).read_bytes())==v['sha256'] for n,v in before.items()),'output_sha256':after['sha256']}
(OUT/'after-ledger.json').write_text(json.dumps(after,indent=2,ensure_ascii=False))
(OUT/'verification.json').write_text(json.dumps(validation,indent=2))
print(json.dumps(validation,indent=2))
