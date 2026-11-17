# Part 2. Search as a craft

## 2.1 Search engines, operators and what has changed

Good search underpins every other skill. An investigator who can frame queries finds what others consider "non-existent".

### What changed recently (S, as of late 2026)

- **The `cache:` operator does not work.** Cache links disappeared from Google results in December 2023 – January 2024, and the operator was removed from the documentation on 17 September 2024 (S). Tutorials that still mention it are out of date.
- **`related:` was removed** from the documentation in 2023 (S).
- **`&num=100` has not worked since September 2025.** Google said it was never an officially supported feature (S). Results have to be paged ten at a time; the next page is set with `&start=10`, `&start=20` and so on (S).
- **The AI block at the top of results** summarises sources and "guesses" intent, so direct queries produce false negatives. The `&udm=14` parameter in the results address shows plain "web" results; many researchers add it to their default search address (S).
- **Operator reliability.** One 2026 test found that `site:`, `-site:` and `intitle:` worked in 100% of checks, `inurl:` in about 74%, `related:` in 44%, while `cache:` returns nothing (S). Re-check the result on your own queries.

### Core operators (G: behaviour differs between engines)

| Operator | What it does | Example |
| --- | --- | --- |
| `"phrase"` | Exact phrase match | `"Ivan Petrov" director` |
| `site:` | Search within a domain | `site:gov.uk "annual report"` |
| `-site:` | Exclude a domain | `"Name" -site:example.com` |
| `filetype:` | File type | `filetype:pdf "staff list"` |
| `intitle:` | Words in the title | `intitle:"tender" 2026` |
| `inurl:` | Words in the address | `inurl:profile "name"` |
| `-word` | Exclude a word | `bank -jobs` |
| `OR` or `\|` | Alternative | `"LLC" OR "Ltd"` |
| `before:` and `after:` | Date limits | `"name" after:2025-01-01` |

Other systems (G): Bing has its own operators, for example for language and location; Yandex supports language, document type and date limits and indexes Russian-language and some regional sources well; Baidu is necessary for material from China; DuckDuckGo, Brave, Startpage and others give alternative indexes. Use at least two search engines for every question: indexes differ, and that is normal.

### Query-building method

1. **From broad to narrow.** Start with the name and context, then add refinements.
2. **Name variants.** Write down all transliterations and abbreviations of each name (section 3.1).
3. **Exclusions.** Remove domains that add noise (aggregators, directories), not words that may matter.
4. **Time slices.** Separate queries for different periods often find what drowns in the general results.
5. **Language.** Repeat queries in the languages of the region; machine translation is fine for queries, not for conclusions.
6. **Result types.** Check images, video, news, books, academic papers and patents separately.
7. **Query log.** Record the query, the engine, the date and the result; without it the search cannot be reproduced.

### Query recipes

| Task | Query template |
| --- | --- |
| An organisation's documents | `site:domain filetype:pdf` then refining words |
| Mentions of an organisation outside its own site | `"organisation name" -site:domain` |
| A person's profile on a specific platform | `site:platform "name"` |
| Procurement, contracts, registers | `"name" filetype:xls OR filetype:pdf tender contract` |
| Old versions of material | Query the archives (section 2.2), not the search engine |
| Publicly accessible files opened by mistake | Use only to assess your own risk or for responsible disclosure; do not download other people's sensitive data (section 5.2) |

### Specialised searches

Google Scholar and Google Books for publications, Patents for patents, Google Alerts and equivalents for monitoring, image search for provenance (section 4.1). For each task it helps to know which specialised databases exist in your country (registers, courts, procurement).

## 2.2 Archives, caches and preserving content

Pages change and disappear, and search caches no longer help. So the main rule of the modern investigator is: **save first, analyse later**.

### What is left

| Tool | What it gives | Note |
| --- | --- | --- |
| Wayback Machine (Internet Archive) | Historical page snapshots, an on-demand page-saving function | Not everything is saved; dynamic content and comments are often lost; a page can be removed at the owner's request (G) |
| archive.today (archive.ph) | An on-demand page snapshot, often including layout | The service depends on availability; terms and mirrors change (G) |
| Common Crawl | An open archive of web crawls for large samples | For bulk analysis rather than viewing a single page (G) |
| National web archives | National library archives | Coverage depends on the country (G) |
| Your own copies | Screenshot, full page copy, file | The only option you control |

Google's cache is gone (section 2.1), so for "deleted" pages only archives and your own copies are reliable.

### Preservation protocol

1. **Immediately, before further action:** archive the page in an external archive and take a full-size screenshot showing the address and the time.
2. **Save separately** comments, counters, publication date and time, and the author's name and identifier: archives handle dynamic content poorly.
3. **Media files:** download them if the law and the service's terms allow, and compute the hash (section 8.1).
4. **Identifiers:** page address, post identifier, username and the numeric profile identifier. Names change, numeric identifiers are more often permanent. Bellingcat's Xiaohongshu guide directly advises saving the profile's unique identifier from the address (S).
5. **Log entry:** what was saved, where it is stored, when, with what.
6. **Double saving:** an external archive and a local copy; if one is unavailable, you have the other.

### Monitoring changes

If you need to notice that a page changed or disappeared, use page-watching services or your own script (section 7.2). For every watched page record: the address, what exactly is tracked (the whole text, a specific block), the check frequency and the action when it changes.

### Typical mistakes

- Archiving only the home page and not the specific item.
- Relying on "I'll find it in the archive later".
- Not recording the time: without it you cannot prove you saw the page in that state.
- Not checking that the archive copy actually contains the needed fragment.
- Keeping evidence on a single device.
