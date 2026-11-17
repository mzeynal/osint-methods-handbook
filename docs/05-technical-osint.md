# Part 5. Technical OSINT and related areas

## 5.1 Domains, DNS, certificates and internet scanners

A website, domain and server leave traces from which you can establish who owns the infrastructure, related resources and history. The description below rests on general knowledge (G): the toolset and its availability change.

### Questions and sources

| Question | Source | Note |
| --- | --- | --- |
| Who registered the domain? | WHOIS and RDAP | Since GDPR owner data is mostly hidden; the registration date, registrar and name servers are useful |
| How did the registration change? | Paid WHOIS archives | Historical records sometimes reveal former owners |
| Where does the domain point? | DNS records A, AAAA, MX, NS, TXT, CNAME | MX and TXT show mail providers and services |
| What subdomains does it have? | Certificate transparency logs, passive DNS | The logs are public; they give a list of issued certificates |
| Who else is on this server? | Reverse IP lookup, passive DNS | Shared hosting gives false links |
| Whose network is it? | Autonomous system number (ASN) data, IP registries | A hosting provider is not the site's owner |
| What is on the page? | Viewing the code, site technologies | Analytics identifiers, pixels, connected services |
| What is exposed to the internet? | Device search engines (Shodan, Censys and equivalents) | Open services and banners are visible; do not use what you find to gain access |
| How did the site look earlier? | Archives (section 2.2) | Old versions often reveal contacts and owners |
| Is the link safe? | Isolated page-analysis services | Do not open suspicious links directly |

### Correlation techniques

- **Analytics and advertising identifiers.** The same Google Analytics, ad-network or pixel identifier on different sites points to a common source of control (G).
- **Favicon hash.** Identical icons on different servers help find related resources through internet scanners (G).
- **Code matches.** Unique comments, script names, file structure.
- **Mail records.** Identical mail-protection settings and providers.
- **Certificates.** One certificate, or one organisation in certificates, across several domains.
- **Timing.** Clusters of domain registrations in a short period, identical name servers.

### Passive and active collection

Passive collection uses what is already published (registers, logs, archives, scanner databases). Active collection sends requests to the target system: port scanning, vulnerability probes, login attempts. Actively scanning other people's systems without permission may be illegal (G). An OSINT investigation stays passive; anything involving access to other people's systems is outside this handbook.

### Typical mistakes

- Treating shared hosting as proof of shared ownership.
- Taking WHOIS data as reliable (it is easily forged or hidden).
- Forgetting that scanner data may be out of date.
- Opening suspicious sites from a personal environment.
- Looking for "vulnerabilities" instead of answering the investigation question.

## 5.2 Leaks and compromised data

Leak databases are both a valuable source and the zone of greatest legal and ethical risk. It matters to distinguish kinds of data and ways of access.

### Kinds and rules

| Kind | What it is | Attitude |
| --- | --- | --- |
| Address-checking services | Show whether an address took part in leaks, without the passwords themselves (G) | Acceptable for checking your own addresses and, for a task, with a lawful basis |
| Paid leak search services | Allow search by domain or address and show credentials (S: investigative newsrooms have used such services) | Only with a lawful basis, a minimisation policy and legal assessment |
| Raw dumps | Files with stolen data | Storing and using stolen data may be illegal; do not use without a lawyer |
| "Stealer" logs | Data from infected devices | Contain fresh passwords and sessions; must not be used to log in under any circumstances |

**The red line:** logging in to any account with found data, even "to check". That is unauthorised access.

### A model for a responsible leak-based publication

A published analysis of leaked credentials is a useful model of method rather than of findings:

- **Method.** Search by an organisation's mail domains in a lawfully accessed leak-search service; analyse the distribution by unit and year.
- **Confirmation.** Check the authenticity of accounts by matching named employees against media and open profiles.
- **Minimisation and protecting people.** Anonymise employees; do not publish passwords as a list.
- **Interpretation.** A leak does not prove a break-in to systems; it usually shows poor digital hygiene.
- **Notification.** Try to warn the owner before publication and record the attempt.
- **Editorial decision.** Weigh the timing and the harm openly.

The scheme: a reproducible method, minimised data, protected people, an attempt to warn the owner and cautious conclusions.

### Responsible disclosure

If you found a vulnerability, an open server or leaked data of an organisation:

1. **Stop** at the minimum necessary: do not download more than needed to confirm the fact.
2. **Do not go inside.** Do not use passwords, do not look at other people's data beyond what is necessary.
3. **Find a contact.** The organisation's security team, a vulnerability disclosure policy page (security.txt), a national incident response team (G).
4. **Report briefly and to the point:** what was found, where, how to verify; no threats or demands.
5. **Allow reasonable time** for a fix; keep the correspondence.
6. **Publish without secrets:** no passwords, personal data or details of exploitation.

### Retention rules

If you have a lawful basis to work with leaked data: encryption, restricted access, a minimum retention period, an access log, a ban on passing it to third parties, and a lawyer's advice before starting.

## 5.3 Transport: vessels, aircraft, ground transport

Vehicle movement is one of the most objective sources: it is measured by instruments, not by words. That is why transport data are good for checking claims.

### Vessels

- **Identifiers.** The IMO number (stays the same when the name and flag change), the MMSI number (changes), the call sign. Work by IMO.
- **Data.** Open services show position from AIS signals; ports, vessel class, history of names and flags. Classification societies and port state control give information on inspections and detentions (G).
- **Roles and ownership.** A vessel has several "masters": the registered owner, operator, commercial manager, technical manager, beneficial owner. For sanctions the whole chain matters (G).
- **Signs of evasion.** AIS gaps, identity spoofing, a flag change to a flag of convenience, ship-to-ship cargo transfer at sea, atypical routes. Record the periods of "silence" and compare them with imagery (section 4.4).

### Aircraft

- **Identifiers.** The registration number (may change), the 24-bit ICAO code (hex) tied to the airframe.
- **Data.** Open ADS-B signal aggregators (Flightradar24 and equivalents; G); national registers (in the US the FAA register; G). Some owners use data-hiding programmes, and military aircraft are often not visible (G).
- **Checking claims.** Compare a claimed movement with independent flight data; this approach is universal.

### Ground transport and other

- Video and photographs with licence plates and markings; vehicle registers depend on the country (G).
- Railways: timetables, public operator data, video from stations.
- Cameras and live streams: time and place, historical recording.
- Weather and seismic data help verify the time of events.

### Workflow

1. Get the object's identifier (IMO, hex, registration number).
2. Collect the history: names, flags, owners, routes.
3. Compare the claimed movement with the data.
4. Find anomalies: gaps, identity changes, atypical ports.
5. Confirm independently: imagery, photographs from the port, documents.
6. Record the limits: delays, unavailable stretches, the possibility of spoofing.

### Mistakes

- Treating a gap in the signal as proof of a violation (there may be a technical reason).
- Confusing names: vessels change names.
- Ignoring the delay and incompleteness of open services' data.
- Forgetting that publishing routes may create a risk for people on board.

## 5.4 Corporate intelligence and the financial trail: a short course

A detailed treatment of this topic (ownership, control, financial statements, cash flows, assets, typologies) is in Part 9. KYC, EDD and background checks of individuals are covered in the companion guide [KYC, EDD and Corporate Intelligence](https://github.com/mzeynal/kyc-edd-guide). Here is only the skeleton.

### Algorithm for a company

1. **Legal entity.** Exact name, legal form, country of registration, registration number. Do not confuse the country of registration with the country of business.
2. **Register extract.** Status, dates, address, directors, shareholders, history of changes.
3. **Financial statements and documents.** Filing deadlines, audit, related parties, charges.
4. **Ownership.** The chain of ownership down to individuals; calculation of the effective share; the state of ownership registers.
5. **Sanctions lists.** Check persons and organisations against sanctions lists; record the list version.
6. **Courts and regulators.** Claims, judgments, warnings, insolvency procedures.
7. **Adverse media.** Multilingual search with an assessment of source quality.
8. **Assets.** Vessels, aircraft, real estate, trademarks.
9. **Conclusion.** Findings with a confidence scale and a list of gaps.

### What changed recently

Registry, sanctions and beneficial-ownership rules change several times a year. A dated, unverified snapshot is in [updates/2026-11.md](../updates/2026-11.md); always check the primary source.

### Where to find details

| Topic | Where |
| --- | --- |
| Company registers, identifiers | Section 9.1 |
| Ownership and control | Section 9.2 |
| Financial statements, cash flows | Sections 9.3, 9.4 |
| Assets, courts, screening | Sections 9.5, 9.6 |
| Typologies and red flags | Section 9.7 |
| KYC, EDD, individual background checks | The [companion guide](https://github.com/mzeynal/kyc-edd-guide) |
