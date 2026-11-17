"""Append a file's SHA-256, source and note to a JSON-lines evidence log.

Usage: python evidence_log.py FILE SOURCE_URL "note" [--log evidence_log.jsonl]
"""
import argparse, hashlib, json, pathlib, time


def log_evidence(path, source_url, note, log='evidence_log.jsonl'):
    data = pathlib.Path(path).read_bytes()
    entry = {
        'file': str(path),
        'sha256': hashlib.sha256(data).hexdigest(),
        'source': source_url,
        'note': note,
        'logged_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
    }
    with open(log, 'a', encoding='utf-8') as f:
        f.write(json.dumps(entry, ensure_ascii=False) + '\n')
    return entry


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('file'); ap.add_argument('source'); ap.add_argument('note')
    ap.add_argument('--log', default='evidence_log.jsonl')
    a = ap.parse_args()
    print(json.dumps(log_evidence(a.file, a.source, a.note, a.log), ensure_ascii=False))
