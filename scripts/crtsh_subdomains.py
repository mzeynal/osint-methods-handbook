"""List names seen in certificate transparency logs for a domain (crt.sh).

Usage: python crtsh_subdomains.py example.com
The service may be slow or rate-limit requests. Passive collection only.
"""
import sys
import requests


def crtsh_subdomains(domain, session=requests):
    r = session.get('https://crt.sh/', params={'q': '%.' + domain, 'output': 'json'}, timeout=60)
    r.raise_for_status()
    names = set()
    for row in r.json():
        for n in row['name_value'].split('\n'):
            names.add(n.strip().lower())
    return sorted(names)


if __name__ == '__main__':
    print('\n'.join(crtsh_subdomains(sys.argv[1])))
