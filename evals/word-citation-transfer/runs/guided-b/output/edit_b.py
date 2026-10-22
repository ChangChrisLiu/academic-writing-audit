from pathlib import Path
from zipfile import ZipFile
from lxml import etree
from inspect_packages import snapshot, NS, W, BASE
import json
source=BASE/'inputs'/'case-b.docx'
out=BASE/'output'/'revised-b.docx'
before=snapshot(source)
old=b'The catalogue containss two registers '
new=b'The catalogue contains two registers '
with ZipFile(source) as zin:
 raw=zin.read('word/document.xml')
 assert raw.count(old)==1
 root=etree.fromstring(raw)
 p=root.findall('.//w:p',NS)[2]
 node=p.find('w:r/w:t',NS)
 assert node.text==old.decode()
 assert p[0].tag==f'{{{W}}}r'
 assert not node.xpath('ancestor::w:fldSimple | ancestor::w:ins | ancestor::w:del',namespaces=NS)
 assert not p[0].findall('.//w:fldChar',NS)
 assert out.exists()==False
 with ZipFile(out,'w') as zout:
  zout.comment=zin.comment
  for info in zin.infolist():
   data=zin.read(info.filename)
   if info.filename=='word/document.xml':data=data.replace(old,new,1)
   zout.writestr(info,data)
after=snapshot(out)
changed=[name for name in before['members'] if before['members'][name]!=after['members'][name]]
assert changed==['word/document.xml']
assert before['fields']==after['fields']
assert before['sources']==after['sources']
assert before['relationships']==after['relationships']
assert before['stored_style']==after['stored_style']
assert before['xml_checks']==after['xml_checks']
with ZipFile(source) as zin, ZipFile(out) as zout:
 assert zin.namelist()==zout.namelist()
 assert zout.read('word/document.xml')==zin.read('word/document.xml').replace(old,new,1)
 assert zout.testzip() is None
 assert zin.comment==zout.comment
 for i,j in zip(zin.infolist(),zout.infolist()):
  for attr in ('date_time','compress_type','comment','extra','internal_attr','external_attr','create_system'):
   assert getattr(i,attr)==getattr(j,attr),(i.filename,attr)
assert before['sha256']==snapshot(source)['sha256']
(BASE/'output'/'inventory-after.json').write_text(json.dumps(after,indent=2))
log={'operation':'one ordinary text replacement outside fields','before_text':old.decode(),'after_text':new.decode(),'before_sha256':before['sha256'],'after_sha256':after['sha256'],'changed_parts':changed,'same_member_order':True,'all_other_member_payloads_identical':True,'document_xml_equals_exact_one_replacement':True,'field_records_equal':before['fields']==after['fields'],'source_records_equal':before['sources']==after['sources'],'relationships_equal':before['relationships']==after['relationships'],'style_equal':before['stored_style']==after['stored_style'],'field_count_before':len(before['fields']),'field_count_after':len(after['fields']),'native_application_open':False,'native_application_refresh':False,'native_application_save':False,'native_application_reopen':False,'saved_package_reopened_and_inspected':True}
(BASE/'output'/'edit-verification.json').write_text(json.dumps(log,indent=2))
print(json.dumps(log,indent=2))
