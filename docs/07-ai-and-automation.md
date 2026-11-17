# Part 7. AI and automation in an investigator's work

## 7.1 AI in the work: what to delegate and what not

Language models and analysis tools speed up routine work but create new risks. The professional position is expressed, for example, in GIJN reviews: AI tools are useful at the start of an investigation as a source of hypotheses, not of evidence (S).

### What can be delegated

| Task | How to use | Risk |
| --- | --- | --- |
| Translation and explaining slang | First-pass translation of documents and posts; explaining unfamiliar terms | Errors of meaning; a native speaker is needed for conclusions |
| Summaries of long documents | A short summary of a report or a court judgment | Omission of something important; check against the text |
| Transcription | Transcribing audio and video | Errors in names and numbers |
| Cleaning up text after OCR | Correcting recognition errors | "Corrections" may appear that were not there |
| Pulling data out of text into a table | Extracting names, dates, amounts | Wrong fields; check a sample by hand |
| Drafting queries and hypotheses | Brainstorming search wording and alternative explanations | Plausible but unfounded ideas; treat them as leads only |
| Help with code | Drafting small scripts | Hidden errors; test on non-confidential data |

### What not to delegate

- **Establishing facts without a source.** Any statement by a model about a person, company or event is a hypothesis.
- **Identifying people from photos.** Legal risks (section 1.2) and a high probability of error.
- **Verifying the authenticity of media.** AI "detectors" are unreliable; rely on provenance and independent data.
- **Legal conclusions** and assessments of guilt.
- **Passing sensitive data** to external services without legal assessment.

### Hallucinations and how to live with them

Models confidently invent links, quotations, case numbers and registration details. Rules:

1. Open and read every link. If the page does not exist or says something else, the conclusion is discarded.
2. Check every quotation against the primary source.
3. Check every number and date against documents.
4. Ask the model to say what it is unsure about, but do not trust that fully.
5. For important conclusions use two independent ways of checking.

### Privacy and security

- Do not paste personal data and client materials into external services without a contract, an understanding of how data are stored and a legal basis; for sensitive tasks consider local models.
- Remember **content-based attacks:** a page or document you show to a model may contain hidden instructions that influence its answer (G). Do not let a model with access to tools carry out actions on instructions from external material.
- Record in the log where and for what AI was used, so the result can be reproduced and explained.

### Example wording

| Poor | Better |
| --- | --- |
| "Who is this person in the photo?" | "Describe the observable details of the photo: clothing, signs, surroundings. Do not guess anything" |
| "Confirm that the company is linked to X" | "List which sources could confirm or refute the company's link to X" |
| "Write a report on the case" | "Here are my notes with sources. Suggest a report structure and find contradictions" |

## 7.2 Automation and scripts

Automation saves hours on repetitive tasks: checking lists, monitoring pages, querying open interfaces, logging. Three rules: **read the terms first** (licences, rules, limits), **collect the minimum of data**, **leave the decision on a conclusion to a person**.

### Limits of automated collection

- A service's terms and its `robots.txt` do not always have the force of law, but breaking them leads to blocking and legal risk. If a service prohibits automated access (some sites do), ask for permission or use licensed data; do not bypass blocks.
- Personal data: automated collection of people's profiles often conflicts with data protection laws (section 1.2).
- A pause between requests and caching are mandatory: do not load other people's servers.
- Do not use automation to log in to accounts or bypass protection.

### Examples (G: illustrations, check before use)

Below are small working starting points in Python. They are meant to show the logic; interface addresses and response formats may change.

**1. The latest archived copy of a page (Internet Archive interface).**

```python
import requests

def wayback_latest(url):
    r = requests.get('https://archive.org/wayback/available',
                     params={'url': url}, timeout=30)
    r.raise_for_status()
    snap = r.json().get('archived_snapshots', {}).get('closest')
    return snap['url'] if snap else None

print(wayback_latest('example.com'))
```

**2. Subdomains from certificate transparency logs.**

```python
import requests

def crtsh_subdomains(domain):
    r = requests.get('https://crt.sh/',
                     params={'q': '%.' + domain, 'output': 'json'}, timeout=60)
    r.raise_for_status()
    names = set()
    for row in r.json():
        for n in row['name_value'].split('\n'):
            names.add(n.strip().lower())
    return sorted(names)
```

The service may respond slowly or limit requests; do not call it in a loop without pauses.

**3. An evidence log with a hash.**

```python
import hashlib, json, time, pathlib

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
```

**4. The simplest page-change monitor.**

```python
import hashlib, pathlib, requests

def page_changed(url, state_file='state.txt'):
    body = requests.get(url, timeout=30).text
    digest = hashlib.sha256(body.encode('utf-8')).hexdigest()
    p = pathlib.Path(state_file)
    old = p.read_text() if p.exists() else None
    p.write_text(digest)
    return old is not None and old != digest
```

Note: on dynamic pages the hash changes because of advertising and time; for real monitoring compare the needed block of text, not the whole page.

### Practical tips

1. **Cache responses** and keep raw data separate from processed data.
2. **Log** each run: script version, time, parameters.
3. **Handle errors:** retries with a growing pause, but no "bombardment".
4. **Check results by hand** on a sample.
5. **Version** scripts and record library versions.
6. **Keep keys** to interfaces outside the code (environment variables, a secrets manager).
7. **Do not publish** collected sets of personal data.
