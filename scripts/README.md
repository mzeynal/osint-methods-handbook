# Scripts

Small, passive-collection helpers that illustrate section 7.2 of the handbook.

| Script | What it does |
| --- | --- |
| `wayback_latest.py` | Closest archived copy of a page (Internet Archive) |
| `crtsh_subdomains.py` | Names in certificate transparency logs for a domain |
| `evidence_log.py` | Append a file's SHA-256, source and note to a JSON-lines log |
| `page_monitor.py` | Tell whether a page changed since the last run |

```bash
pip install -r requirements.txt
python test_scripts.py        # offline smoke tests, synthetic data only
python evidence_log.py report.pdf https://example.com/report "downloaded 2026-11-17"
```

**Tested only offline,** with mocked responses and local files. The two network scripts were never run against the live services: endpoints and response formats may have changed, so check them first. Read each service's terms, keep pauses between requests, cache responses, and do not use these scripts to collect personal data about individuals. Keep API keys out of the code (environment variables).
