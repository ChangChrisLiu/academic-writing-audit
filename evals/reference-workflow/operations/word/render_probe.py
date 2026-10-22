"""Invoke the packaged renderer while keeping its temporary files in this probe directory."""
from pathlib import Path
import importlib.util, os, sys, tempfile
root=Path(__file__).resolve().parent
tmp=root/'render-temp';tmp.mkdir(exist_ok=True)
for key in ('TMPDIR','TEMP','TMP'):os.environ[key]=str(tmp)
tempfile.tempdir=str(tmp)
spec=importlib.util.spec_from_file_location('packaged_renderer',os.environ['AWA_RENDERER'])
r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)
# Preserve the explicit task-local temp directory. Rendering and binary selection are unchanged.
r._default_macos_tmpdir_for_soffice=lambda:None
r.main()
