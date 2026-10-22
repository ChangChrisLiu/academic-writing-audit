from pathlib import Path
import json
r=Path(__file__).resolve().parent
a=json.loads((r/'before.inventory.json').read_text());b=json.loads((r/'after-attempt.inventory.json').read_text())
source_a=[s for p in a['source_parts'] for s in p['sources']]
source_b=[s for p in b['source_parts'] for s in p['sources']]
citations=[f for f in b['fields'] if f['instruction'].startswith('CITATION ')]
tags=[s['tag'] for s in source_b]
ledger=[]
for s in source_b:
 occ=[{'region':f['region'],'part':f['part'],'location':f['path'],'instruction':f['instruction'],'display':f['cache']} for f in citations if f['instruction'].split()[1]==s['tag']]
 ledger.append({'source':s,'occurrences':occ,'identity_evidence':'fixture-sources.xml and the embedded source record','mapping_status':'unique structural target; displayed citation pending refresh','authenticity':'not checked; intentionally fictional','claim_support':'out of scope'})
comparison={'status':'native Word refresh blocked before fixture selection','byte_identical':a['sha256']==b['sha256'],'before_sha256':a['sha256'],'after_attempt_sha256':b['sha256'],'source_identities_equal':source_a==source_b,'field_structure_and_caches_equal':a['fields']==b['fields'],'source_count':len(source_b),'citation_occurrence_count':len(citations),'bibliography_field_count':sum(f['instruction'].startswith('BIBLIOGRAPHY') for f in b['fields']),'all_complex_fields_closed':all(f['closed'] and f['has_separator'] for f in b['fields']),'structurally_missing_targets':[f['instruction'] for f in citations if f['instruction'].split()[1] not in tags],'source_records_without_observed_occurrences':[x['source']['tag'] for x in ledger if not x['occurrences']],'displayed_reference_entries':'not generated; pending marker only','native_refresh_observed':False,'after_attempt_meaning':'Unmodified working-file snapshot after blocked native attempt; not a Word-saved output','layout_refinement':'During construction, inherited title borders were removed and caption text set to black. This authoring-only refinement occurred after the blocked UI attempt. No field code, source record, or initial cache was changed.'}
assert comparison['byte_identical'] and comparison['source_identities_equal'] and comparison['field_structure_and_caches_equal']
assert comparison['source_count']==2 and comparison['citation_occurrence_count']==2 and comparison['bibliography_field_count']==1
assert comparison['all_complex_fields_closed'] and not comparison['structurally_missing_targets'] and not comparison['source_records_without_observed_occurrences']
(r/'comparison.json').write_text(json.dumps(comparison,indent=2)+'\n')
(r/'reference-ledger.json').write_text(json.dumps(ledger,indent=2)+'\n')
print(json.dumps(comparison,indent=2))
