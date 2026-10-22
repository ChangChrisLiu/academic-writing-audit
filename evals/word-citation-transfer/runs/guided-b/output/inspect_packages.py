from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import hashlib, json, posixpath
BASE=Path('/TEST_WORKDIR/runs/guided-b')
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
B='http://schemas.openxmlformats.org/officeDocument/2006/bibliography'
NS={'w':W,'b':B}
def snapshot(path):
 result={'file':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
 with ZipFile(path) as z:
  result['members']={i.filename:hashlib.sha256(z.read(i.filename)).hexdigest() for i in z.infolist()}
  result['xml_checks']={}; result['paragraphs']=[]; result['fields']=[]; result['relationships']={}
  for name in z.namelist():
   if not name.endswith(('.xml','.rels')): continue
   root=etree.fromstring(z.read(name))
   if name.endswith('.rels'):
    rels=[]
    for e in root:
     item=dict(e.attrib)
     if e.get('TargetMode')!='External':
      partbase='' if name=='_rels/.rels' else name.split('/_rels/')[0]
      target=posixpath.normpath(posixpath.join(partbase,e.get('Target')))
      item['resolved_target']=target; item['present']=target in z.namelist()
     rels.append(item)
    result['relationships'][name]=rels
   result['xml_checks'][name]={tag:len(root.findall('.//w:'+tag,NS)) for tag in ['ins','del','moveFrom','moveTo','delText','tbl','txbxContent','altChunk','drawing','pict','object','fldSimple','fldChar','instrText','footnoteReference','endnoteReference','commentReference','headerReference','footerReference','vanish','webHidden','trackRevisions']}
   if name.startswith('word/') and root.findall('.//w:p',NS):
    for n,p in enumerate(root.findall('.//w:p',NS),1):
     style=p.find('w:pPr/w:pStyle',NS)
     text=''.join(('\n' if e.tag==f'{{{W}}}br' else e.text or '') for e in p.iter() if e.tag in (f'{{{W}}}t',f'{{{W}}}delText',f'{{{W}}}br'))
     result['paragraphs'].append({'part':name,'paragraph':n,'style':style.get(f'{{{W}}}val') if style is not None else None,'text':text})
     stack=[]
     for e in p.iter():
      if e.tag==f'{{{W}}}fldChar':
       kind=e.get(f'{{{W}}}fldCharType')
       if kind=='begin': stack.append({'part':name,'paragraph':n,'instruction':'','result':'','phase':'instruction','markers':[dict(e.attrib)]})
       elif kind=='separate':
        assert stack; stack[-1]['phase']='result';stack[-1]['markers'].append(dict(e.attrib))
       elif kind=='end':
        assert stack; f=stack.pop();f['markers'].append(dict(e.attrib)); del f['phase']; result['fields'].append(f)
      elif e.tag==f'{{{W}}}instrText' and stack: stack[-1]['instruction']+=e.text or ''
      elif e.tag in (f'{{{W}}}t',f'{{{W}}}br') and stack and stack[-1]['phase']=='result':stack[-1]['result']+=('\n' if e.tag==f'{{{W}}}br' else e.text or '')
     assert not stack
  src=etree.fromstring(z.read('customXml/item1.xml'))
  result['stored_style']=dict(src.attrib)
  result['sources']=[]
  for s in src.findall('b:Source',NS):
   record={etree.QName(e).localname: ''.join(e.itertext()) for e in s if etree.QName(e).localname!='Author'}
   record['people']=[{etree.QName(x).localname:x.text for x in p} for p in s.findall('.//b:Person',NS)]
   result['sources'].append(record)
 return result
if __name__=='__main__':
 snapshots={k:snapshot(BASE/'inputs'/f'case-{k}.docx') for k in ('a','b')}
 (BASE/'output'/'inventory-before.json').write_text(json.dumps(snapshots,indent=2))
 for k,s in snapshots.items():
  print('CASE',k,'HASH',s['sha256'],'STYLE',s['stored_style'])
  print('SOURCES',json.dumps(s['sources']))
  print('PARAGRAPHS',json.dumps(s['paragraphs']))
  print('FIELDS',json.dumps(s['fields']))
  print('NONZERO COUNTS',json.dumps({part:{k:v for k,v in counts.items() if v} for part,counts in s['xml_checks'].items() if any(counts.values())}))
  print('BROKEN RELS',[r for rs in s['relationships'].values() for r in rs if r.get('present')==False])
