# OSINT Methods for Verification and Due Diligence: a working handbook

Study notes on open-source research as a method: how to frame a question, search, archive, verify media, check companies and people on a lawful basis, keep logs and write a report. Built on public sources, with the legal and ethical limits drawn explicitly.

> **How this was made.** Compiled by Murad Zeynal with AI assistance and public sources, as a learning project. It is not professional or legal advice. Statements that depend on current events are marked as unverified (see below); the methodology does not depend on them.

Companion project: [KYC, EDD and Corporate Intelligence: a working guide](https://github.com/mzeynal/kyc-edd-guide).

## Contents

| Part | What it covers |
| --- | --- |
| [1. Foundations](docs/01-foundations.md) | What OSINT is, how an investigation works, law and ethics, investigator safety |
| [2. Search as a craft](docs/02-search-and-archives.md) | Search engines and operators, archives, preserving content |
| [3. People and identity](docs/03-people-and-identity.md) | Identifiers, social platforms, messengers, link graphs, false correlations, limits of de-anonymisation |
| [4. Media](docs/04-media.md) | Verifying images and video, AI-generated content, geolocation, satellite imagery |
| [5. Technical OSINT](docs/05-technical-osint.md) | Domains, DNS, certificates, leaks, transport, short corporate course |
| [6. Special topics](docs/06-special-topics.md) | Regional platforms, conflict and human rights documentation |
| [7. AI and automation](docs/07-ai-and-automation.md) | What to delegate and what not, small scripts |
| [8. Case management and reporting](docs/08-case-management-and-reporting.md) | Logs, link analysis, competing hypotheses, intelligence analysis, report formats |
| [9. Corporate and financial investigations](docs/09-corporate-and-financial.md) | Ownership and control, statements, assets, screening, red flags |
| [10. Practice cards](docs/10-practice-cards.md) | Checks with consent and on public data |
| [Templates](templates/) | Logs, analytic brief, link record, case structure, closure checklist |
| [Scripts](scripts/) | Archive lookup, certificate logs, evidence log, page monitor |
| [Update snapshot](updates/2026-11.md) | Dated, **unverified** snapshot of tools, access and rules |

Suggested order for a beginner: Part 1 → sections 2.1–2.2 → 4.1 → 4.3 → Part 8 → templates. The rest as tasks arise.

## Five practical conclusions

1. **Do not trust a single access route.** Any platform, API or imagery provider can disappear or be restricted within a week. For every data layer keep a backup.
2. **Archive immediately.** A search-engine cache is no longer insurance, and platform content disappears fast.
3. **Check provenance before content.** When fakes are cheap, the first question about any file is who published it first and when.
4. **Record your own limits.** If data is missing because access is closed, that is a gap in the report, not "nothing found".
5. **Law and ethics are part of the method.** Biometrics, leaks and the collection of data on people need a decision before work starts, not after a find.

## How to read the marks

| Mark | Meaning |
| --- | --- |
| **S** | From search results or secondary summaries: the page was not opened in full, so check figures and wording against the primary source |
| **G** | General knowledge, not checked against fresh sources: verify before use, especially prices, tool availability and rules |

No fact in this edition is marked as directly verified. Statements without a mark are methodological recommendations that do not depend on current events.

## Limits

- This does not help to harass, stalk or expose private individuals, obtain access to other people's accounts and systems, or use stolen data. Where methods lie close to this boundary, the boundary is drawn explicitly.
- It is not legal advice: rules on data, biometrics and access to systems depend on the country. Get a lawyer's review before commercial use.
- The tool lists are incomplete and age quickly; rely on living catalogues and take from the text the logic of choice.
- Third-party datasets and services have their own terms. For example, aggregated sanctions data from OpenSanctions is free for non-commercial use only; check the licence of any data source before using it in client work. No third-party data is included in this repository.
- All names in examples and scripts are fictitious.

## Corrections

Spotted an error or a stale fact? Open an issue. Corrections to S and G items are especially welcome.

## License

Text and templates: [CC BY 4.0](LICENSE-docs.md). Code in `scripts/`: [MIT](LICENSE).
