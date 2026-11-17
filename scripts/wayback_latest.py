"""Print the closest archived copy of a page (Internet Archive availability API).

Usage: python wayback_latest.py example.com
Polite use: one request per call; do not loop without pauses.
"""
import sys
import requests

API = 'https://archive.org/wayback/available'


def wayback_latest(url, session=requests):
    r = session.get(API, params={'url': url}, timeout=30)
    r.raise_for_status()
    snap = r.json().get('archived_snapshots', {}).get('closest')
    return snap['url'] if snap else None


if __name__ == '__main__':
    print(wayback_latest(sys.argv[1]) or 'no archived copy found')
