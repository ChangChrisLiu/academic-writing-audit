"""Compare the fixture with an agent's narrow prose edit, without refreshing fields."""
from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
import json,hashlib,argparse
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
N={'w':W}
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def parts(p):
 with ZipFile(p) as z:return {n:z.read(n) for n in z.namelist()}
def fields(blob):
 found=[]
 for part,data in sorted(blob.items()):
  if not(part.startswith('word/') and part.endswith('.xml')):continue
  root=E.fromstring(data);stack=[]
  for e in root.iter():
   if e.tag=='{'+W+'}fldChar':
    typ=e.get('{'+W+'}fldCharType')
    if typ=='begin':
     p=next((a for a in e.iterancestors() if a.tag=='{'+W+'}p'),None)
     ps=p.find('w:pPr/w:pStyle',N) if p is not None else None
     region='footnote' if part.endswith('/footnotes.xml') else ('caption' if ps is not None and ps.get('{'+W+'}val')=='Caption' else 'body')
     stack.append(dict(part=part,region=region,code='',cache='',separated=False,closed=False,begin_attributes=dict(e.attrib)))
    elif typ=='separate' and stack:stack[-1]['separated']=True
    elif typ=='end' and stack:f=stack.pop();f['closed']=True;found.append(f)
   elif e.tag=='{'+W+'}instrText' and stack:stack[-1]['code']+=e.text or ''
   elif e.tag=='{'+W+'}t' and stack and stack[-1]['separated']:stack[-1]['cache']+=e.text or ''
   elif e.tag=='{'+W+'}br' and stack and stack[-1]['separated']:stack[-1]['cache']+='\n'
   elif e.tag=='{'+W+'}fldSimple':found.append(dict(part=part,kind='simple',code=e.get('{'+W+'}instr'),xml=E.tostring(e,method='c14n').decode()))
  found+=stack
 return found
def compare(before,after):
 b=parts(before);a=parts(after);bf=fields(b);af=fields(a)
 expected=E.fromstring(b['word/document.xml']);n=0
 for t in expected.iter('{'+W+'}t'):
  if 'containss' in (t.text or ''):n+=t.text.count('containss');t.text=t.text.replace('containss','contains')
 checks={
 'expected_single_typo_in_input':n==1,
 'same_package_part_names':set(a)==set(b),
 'all_non_document_parts_byte_identical':{k:v for k,v in a.items() if k!='word/document.xml'}=={k:v for k,v in b.items() if k!='word/document.xml'},
 'document_xml_only_expected_prose_change':E.tostring(expected,method='c14n')==E.tostring(E.fromstring(a['word/document.xml']),method='c14n'),
 'all_field_signatures_preserved':bf==af,
 'seven_fields_remain_complete':len(af)==7 and all(f.get('closed') and f.get('separated') for f in af),
 'four_citations_including_footnote_and_caption':sum(f['code'].strip().startswith('CITATION ') for f in af)==4 and sum(f['region']=='footnote' for f in af)==1 and any(f['region']=='caption' and f['code'].strip().startswith('CITATION ') for f in af),
 }
 return dict(before_sha256=sha(before),after_sha256=sha(after),checks=checks,all_pass=all(checks.values()),before_fields=bf,after_fields=af,native_word_refresh_tested=False)
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('before',type=Path);parser.add_argument('after',type=Path);parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
 result=compare(args.before,args.after);args.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'checks':result['checks'],'all_pass':result['all_pass']},indent=2));raise SystemExit(not result['all_pass'])
