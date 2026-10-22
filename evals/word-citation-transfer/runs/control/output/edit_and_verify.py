from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
import hashlib, json, posixpath
base=Path('/TEST_WORKDIR/runs/control')
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','b':'http://schemas.openxmlformats.org/officeDocument/2006/bibliography'}
w='{'+ns['w']+'}'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
inputs={p.name:sha(p) for p in (base/'inputs').iterdir() if p.is_file()}
src=base/'inputs'/'case-b.docx'
out=base/'output'/'revised-b.docx'
with ZipFile(src) as z:
 original=z.read('word/document.xml')
 root=E.fromstring(original)
 matches=root.xpath('//w:t[contains(text(),"containss")]',namespaces=ns)
 assert len(matches)==1 and matches[0].text=='The catalogue containss two registers '
 # Prove the target text occurs outside any complex or simple field.
 depth=0
 for e in root.iter():
  if e.tag==w+'fldChar':
   typ=e.get(w+'fldCharType')
   if typ=='begin':depth+=1
   if typ=='end':depth-=1
  if e is matches[0]:
   assert depth==0
   assert not e.xpath('ancestor::w:fldSimple',namespaces=ns)
 assert original.count(b'containss')==1
 changed=original.replace(b'containss',b'contains')
 assert changed.replace(b'The catalogue contains two registers ',b'The catalogue containss two registers ')==original
 with ZipFile(out,'w') as dest:
  dest.comment=z.comment
  for item in z.infolist():
   dest.writestr(item,changed if item.filename=='word/document.xml' else z.read(item.filename))
with ZipFile(src) as old,ZipFile(out) as new:
 assert old.namelist()==new.namelist()
 differences=[n for n in old.namelist() if old.read(n)!=new.read(n)]
 assert differences==['word/document.xml']
 assert new.read('word/document.xml')==old.read('word/document.xml').replace(b'containss',b'contains')
 assert new.testzip() is None

def inspect(p):
 with ZipFile(p) as z:
  found=[]
  for part in z.namelist():
   if not(part.startswith('word/') and part.endswith('.xml')):continue
   r=E.fromstring(z.read(part));stack=[]
   for e in r.iter():
    if e.tag==w+'fldChar':
     typ=e.get(w+'fldCharType')
     if typ=='begin':stack.append({'part':part,'instruction':'','cached_text':'','separate':False})
     elif typ=='separate':
      assert stack and not stack[-1]['separate']
      stack[-1]['separate']=True
     elif typ=='end':
      assert stack and stack[-1]['separate']
      found.append(stack.pop())
    elif e.tag==w+'instrText' and stack:stack[-1]['instruction']+=e.text or ''
    elif e.tag==w+'t' and stack and stack[-1]['separate']:stack[-1]['cached_text']+=e.text or ''
    elif e.tag==w+'br' and stack and stack[-1]['separate']:stack[-1]['cached_text']+='\n'
   assert not stack,part
  r=E.fromstring(z.read('customXml/item1.xml'))
  sources=[]
  for s in r.findall('b:Source',ns):
   record={k:s.findtext('b:'+k,namespaces=ns) for k in ['Tag','Guid','Title','Year','RefOrder']}
   record['authors']=[dict(first=n.findtext('b:First',namespaces=ns),last=n.findtext('b:Last',namespaces=ns)) for n in s.findall('.//b:Person',ns)]
   sources.append(record)
  tags=[s['Tag'] for s in sources]
  assert len(tags)==len(set(tags))
  for f in found:
   if f['instruction'].strip().startswith('CITATION '):
    assert f['instruction'].strip().split()[1] in tags
  doc=E.fromstring(z.read('word/document.xml'))
  return {'sha256':sha(p),'fields':found,'field_count':len(found),'sources':sources,'stored_style':dict(r.attrib),'body_paragraphs':len(doc.xpath('/w:document/w:body/w:p',namespaces=ns)),'bookmarks':doc.xpath('//w:bookmarkStart/@w:name',namespaces=ns),'unlisted_story_parts':[n for n in z.namelist() if any(t in n for t in ['header','footer','endnotes','comments'])]}
a=inspect(base/'inputs'/'case-a.docx');b=inspect(src);rev=inspect(out)
assert b['fields']==rev['fields']
assert b['sources']==rev['sources']
assert b['stored_style']==rev['stored_style']
assert inputs=={p.name:sha(p) for p in (base/'inputs').iterdir() if p.is_file()}
result={'input_hashes':inputs,'changed_members':differences,'unchanged_member_count':17,'edit':'One occurrence of containss -> contains in ordinary prose; document.xml bytes otherwise identical.','case_a':a,'case_b':b,'revised_b':rev,'checks':'ZIP integrity, exact edit bytes, identical member names, all other members byte-identical, balanced complex fields, unique source tags, citation tags resolve, identical original/revised field instructions and cached results.'}
(base/'output'/'verification.json').write_text(json.dumps(result,indent=2))
print(json.dumps({'changed_members':differences,'input_hashes':inputs,'revised_sha256':rev['sha256'],'case_a_fields':a['field_count'],'case_b_fields':b['field_count'],'revised_fields':rev['field_count'],'checks':result['checks']},indent=2))
