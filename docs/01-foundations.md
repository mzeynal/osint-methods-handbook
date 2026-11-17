# Part 1. Foundations

## 1.1 What OSINT is and how an investigation works

OSINT (open-source intelligence) is the collection, verification and analysis of information that is publicly and lawfully available, in order to answer a specific question. The key word is "question": collecting data without a question is accumulating rubbish.

Several disciplines come together under OSINT and often work in combination:

| Direction | Object | Typical sources | Where in this handbook |
| --- | --- | --- | --- |
| Social (SOCMINT) | People, communities, narratives | Social networks, forums, messengers | Part 3 |
| Visual and geospatial | Photos, video, places, events | Maps, imagery, street-level panoramas | Part 4 |
| Technical | Domains, servers, leaks | DNS, certificates, scanners | Part 5 |
| Corporate and financial | Companies, owners, assets | Registers, courts, sanctions | Section 5.4, Part 9 |
| Transport | Vessels, aircraft, routes | AIS, ADS-B, registers | Section 5.3 |
| Verification | Authenticity of material | All of the above | Part 4 |

### The investigation cycle

1. **Framing the question.** Who the client is, what decision they will take, what accuracy is needed, what deadlines and prohibitions apply. One to three key questions (PIR) and supporting ones are written down (a template is in the appendix).
2. **Collection plan.** For each question: which sources may answer it, what output is expected, what risks exist (legal, safety, reputational).
3. **Collection.** Work to the plan with mandatory recording: what was found, where, when, how it was saved.
4. **Processing.** Normalising names and dates, translation, transcription, OCR, file hashing.
5. **Analysis.** Versions, verification, confidence assessment, finding gaps.
6. **Report.** An answer to the question that was asked, not a retelling of what was found.
7. **Feedback.** What worked, which sources proved valuable, what to change next time.

The cycle is not linear: analysis often sends you back to collection. Note every return in the log and the reason for it.

### The first 30 minutes on a new task

1. Restate the question in your own words and make sure you understand the decision behind it.
2. Check the legal and ethical limits (section 1.2).
3. Write 2–4 starting hypotheses, including deliberately opposite ones.
4. Build a table of "question — source — expected output — risk".
5. Set up the working environment and logs (section 1.3, Part 8).
6. Set stopping conditions: how much time and which sources are enough.
7. Archive at once whatever you found in the first minutes: pages change quickly.

### Typical mistakes at the start

- Starting with tools instead of the question.
- Looking for confirmation of the first version and not looking for refutations.
- Not recording where a fact came from ("I saw it somewhere").
- Mixing personal and work accounts.
- Not defining when the task is solved and "digging" endlessly.

## 1.2 Law and ethics

"The information is open" decides nothing legally or ethically. Open information may have been obtained unlawfully, used to cause harm, or collected in a way that bypasses rules protecting people. The decision is made before collection and revisited as work proceeds.

### What is lawful: four questions

1. **Access.** Do you see the material without bypassing protection? Logging in with other people's or leaked credentials, guessing passwords, bypassing passwords and blocks is almost everywhere treated as unauthorised access to a system (G).
2. **Terms of service.** Breaking a platform's rules (automated collection, fake accounts) is not always a crime, but leads to blocking and sometimes to lawsuits. Treat the terms as a limit on method.
3. **Data about people.** If you collect personal data, data protection laws apply. In the EU that is GDPR: lawful purpose, minimisation, limited retention, stricter requirements for sensitive categories and data on criminal charges (G). Exemptions for journalistic and research purposes differ by country.
4. **Biometrics.** Article 5 of the EU AI Act prohibits systems that create or expand facial recognition databases by untargeted scraping of images from the internet or CCTV, and prohibits biometric categorisation by race, political opinions, religion and similar traits; the prohibitions have applied since 2 February 2025, and the European Commission published guidance on 4 February 2025 (S). A Future of Privacy Forum analysis (March 2026) notes that the ban concerns untargeted scraping, while other cases are governed by GDPR (S). In practice: do not build your own face databases and do not use face-search services on private individuals without a legal assessment.

### Zones of the permissible

| Zone | Examples | How to proceed |
| --- | --- | --- |
| Permissible when the rules are followed | Searching open profiles of public figures; checking a company in registers; verifying a video; analysing satellite imagery | Record the source and purpose; minimise data |
| Contested | A profile of a private person for a hiring or deal check; monitoring closed communities; face search | Legal assessment first; a written basis; limited scope |
| Impermissible | Logging in to other people's accounts; using stolen passwords; surveillance of a specific person; publishing a home address; deception to obtain closed data | Do not do it; tell the client the task is outside the limits |

### Ethics: a harm check

Before naming a person, publishing an address or passing a conclusion to the client, ask yourself:

- What harm would an error cause, and to whom? Do I need this person, or only the structure?
- Is the evidence sufficient (at least two independent sources for an identification)?
- Is there a public interest, and is the intrusion proportionate?
- Are data of minors, victims or witnesses being disclosed?
- Has the person been given a chance to reply (right of reply)?
- Could the finding be used to harass someone?

Bellingcat's principles for data collection and its editorial standards are published on its site and are a good model for internal rules (S).

### Practical rules

- Write the purpose and legal basis of each case in the first lines of the log.
- Do not collect data "just in case".
- Distinguish a person who became public by their own choice from a private person who happens to be near a case.
- If a task requires breaking the law or the rules, decline and record the reason.
- Discuss difficult cases with a lawyer and a second analyst, not alone.

## 1.3 Investigator safety (OpSec)

There are three kinds of danger for an investigator: technical (infection, interception, data leakage), informational (the subject learns they are being looked at) and physical or legal (pressure, threats, lawsuits). Protection starts with a threat model: from whom and from what you are protecting yourself.

### Threat model: five questions

1. Who might take an interest in your work (the subject, their circle, a platform, a provider, an employer, a state)?
2. What exactly do they need to know (what you are looking for, who you are, where you are, what you found)?
3. What do you lose in a leak (the result, sources, people's safety, reputation)?
4. What are your weak points (personal accounts, habits, devices, colleagues)?
5. What happens if you are exposed (the plan of action)?

### Working environment

- **Separation.** Use a separate browser profile for investigations and a virtual machine or separate device for risky tasks. Do not log in to personal accounts in the same environment.
- **Images.** Ready-made virtual machines for OSINT cut setup time, but check the image's source (S).
- **Browser.** An ad and tracker blocker, unneeded extensions off, separate profiles, data cleared after sessions. A "private mode" is not anonymity: it does not hide you from the site or the provider.
- **Network.** A VPN and Tor solve different tasks and have a cost: some sites block them, and changing country can change the content shown. Choose deliberately and record from which point you looked.
- **Storage.** Disk encryption, a password manager, multi-factor authentication, backups, a separate protected store for case materials.

### How you give yourself away: leak vectors

| Vector | How it appears | What to do |
| --- | --- | --- |
| Platform notifications | Profile views on LinkedIn, stories, "read" receipts in messengers (G) | Do not log in from personal accounts; check platform settings |
| Tracking links | A link in a message or document tells the author who opened it and when | Open unknown links in an isolated environment |
| Content loading | An image or document that pulls a resource from the subject's server | Block remote content, open files offline in an isolated environment |
| Browser fingerprint | A combination of browser parameters makes you recognisable | Separate profiles; do not mix personal and work |
| Reuse of accounts | One e-mail or phone on a "work" and a personal account | Separate addresses and numbers for investigations, where lawful |
| File metadata | The report keeps the author's name, path, software version | Clean metadata before handing over |
| Habits | Working hours, language, writing style | Be aware of them and do not reveal more than needed in public messages |

### Research ("clean") profiles

Some platforms show data only to logged-in users. Using a separate profile for observation is ethically and legally contested: platforms often forbid fake accounts, and deceiving people to obtain closed information is not acceptable (section 1.2). The permissible minimum: a profile that does not pretend to be another person, does not contact the subject and does not bypass access limits.

### If you are discovered or threatened

1. Stop work on the case and keep evidence of the contact.
2. Tell your manager or client and a lawyer.
3. Change passwords, check devices and access.
4. Assess the risk to yourself, your family, sources and people in the case materials.
5. Do not answer with threats and do not enter a correspondence without a team decision.
6. If the threat is real, contact law enforcement and organisations supporting journalists and researchers in your country.

### Psychological safety

Work with violence, disappearances and harassment leaves a mark. Agree boundaries in advance: session length, the right to refuse, discussion with colleagues, access to a specialist. More in section 6.2.
