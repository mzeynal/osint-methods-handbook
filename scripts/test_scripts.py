"""Smoke tests on synthetic local data only (no live services).  Run: python test_scripts.py"""
import hashlib, json, pathlib, tempfile, threading, http.server, os
from evidence_log import log_evidence
from page_monitor import page_changed
from wayback_latest import wayback_latest
from crtsh_subdomains import crtsh_subdomains

class Fake:
    def __init__(self, payload=None, text=''): self.p, self.t = payload, text
    def get(self, *a, **k):
        o = self; 
        class R:
            text = o.t
            def raise_for_status(s): pass
            def json(s): return o.p
        return R()

d = pathlib.Path(tempfile.mkdtemp())
f = d / 'a.txt'; f.write_bytes(b'hello')
e = log_evidence(f, 'https://example.com/x', 'synthetic', d / 'log.jsonl')
assert e['sha256'] == hashlib.sha256(b'hello').hexdigest()
assert json.loads((d / 'log.jsonl').read_text())['note'] == 'synthetic'

st = d / 'state.txt'
assert page_changed('u', st, session=Fake(text='v1')) is False   # first run
assert page_changed('u', st, session=Fake(text='v1')) is False
assert page_changed('u', st, session=Fake(text='v2')) is True
page_changed('u', st, extract=lambda b: b[:1], session=Fake(text='v3'))
assert page_changed('u', st, extract=lambda b: b[:1], session=Fake(text='v4')) is False  # extract hook: only first char hashed

assert wayback_latest('example.com', Fake({'archived_snapshots': {'closest': {'url': 'http://archive/x'}}})) == 'http://archive/x'
assert wayback_latest('example.com', Fake({'archived_snapshots': {}})) is None
rows = [{'name_value': 'A.example.com\nb.example.com'}, {'name_value': 'a.example.com'}]
assert crtsh_subdomains('example.com', Fake(rows)) == ['a.example.com', 'b.example.com']
print('all tests passed')
