"""Report whether a page changed since the last run (hash of the whole body).

Usage: python page_monitor.py URL [--state state.txt]
On dynamic pages the hash changes because of ads and timestamps; for real
monitoring hash only the block of text you care about (see the `extract` hook).
Check the site's terms before automated access and keep a pause between runs.
"""
import argparse, hashlib, pathlib
import requests


def page_changed(url, state_file='state.txt', extract=lambda body: body, session=requests):
    body = extract(session.get(url, timeout=30).text)
    digest = hashlib.sha256(body.encode('utf-8')).hexdigest()
    p = pathlib.Path(state_file)
    old = p.read_text().strip() if p.exists() else None
    p.write_text(digest)
    return old is not None and old != digest


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('url'); ap.add_argument('--state', default='state.txt')
    a = ap.parse_args()
    print('changed' if page_changed(a.url, a.state) else 'no change (or first run)')
