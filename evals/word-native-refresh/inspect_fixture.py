from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
import json,sys,hashlib
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
B='http://schemas.openxmlformats.org/officeDocument/2006/bibliography'
N={'w':W,'b':B}
p=Path(sys.argv[1]);r={'file':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'source_parts':[],'fields':[],'visible_paragraphs':[],'revision_counts':{},'inspected_word_xml_parts':[]}
with ZipFile(p) as z:
 for name in z.namelist():
  if name.endswith('.xml'):
   root=E.fromstring(z.read(name))
   if root.tag=='{'+B+'}Sources':
    src=[]
    for s in root.findall('b:Source',N):
     src.append({'tag':s.findtext('b:Tag',namespaces=N),'guid':s.findtext('b:Guid',namespaces=N),'type':s.findtext('b:SourceType',namespaces=N),'authors':[{'first':x.findtext('b:First',namespaces=N),'last':x.findtext('b:Last',namespaces=N)} for x in s.findall('.//b:Person',N)],'title':s.findtext('b:Title',namespaces=N),'year':s.findtext('b:Year',namespaces=N),'city':s.findtext('b:City',namespaces=N),'publisher':s.findtext('b:Publisher',namespaces=N)})
    r['source_parts'].append({'part':name,'attributes':dict(root.attrib),'sources':src})
   if name.startswith('word/'):
    r['inspected_word_xml_parts'].append(name)
    if root.findall('.//w:p',N):
     r['visible_paragraphs'] += [{'part':name,'path':root.getroottree().getpath(x),'text':''.join(x.itertext()) if False else ''.join(x.xpath('.//w:t/text()',namespaces=N))} for x in root.findall('.//w:p',N)]
    r['revision_counts'][name]={'insertions':len(root.findall('.//w:ins',N)),'deletions':len(root.findall('.//w:del',N))}
    stack=[]
    for el in root.iter():
     if el.tag=='{'+W+'}fldChar':
      typ=el.get('{'+W+'}fldCharType')
      if typ=='begin':
       stack.append({'part':name,'path':root.getroottree().getpath(el),'region':'table' if any(a.tag=='{'+W+'}tbl' for a in el.iterancestors()) else 'body','instruction':'','cache':'','has_separator':False,'closed':False,'locked':el.get('{'+W+'}fldLock'),'dirty':el.get('{'+W+'}dirty')})
      elif typ=='separate' and stack:stack[-1]['has_separator']=True
      elif typ=='end' and stack:
       x=stack.pop();x['closed']=True;x['instruction']=x['instruction'].strip();r['fields'].append(x)
     elif el.tag=='{'+W+'}instrText' and stack: stack[-1]['instruction']+=el.text or ''
     elif el.tag=='{'+W+'}t' and stack and stack[-1]['has_separator']:stack[-1]['cache']+=el.text or ''
     elif el.tag=='{'+W+'}fldSimple':r['fields'].append({'part':name,'path':root.getroottree().getpath(el),'instruction':el.get('{'+W+'}instr'),'cache':''.join(el.xpath('.//w:t/text()',namespaces=N)),'kind':'simple'})
    r['fields'].extend(stack)
out=p.with_suffix('.inventory.json');out.write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({'file':p.name,'source_parts':r['source_parts'],'fields':r['fields']},indent=2))
