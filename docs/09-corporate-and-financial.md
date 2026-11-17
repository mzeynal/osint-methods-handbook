# Part 9. Corporate and financial investigations: summary

A corporate and financial investigation is the core of due diligence, compliance and audit work. The short course in section 5.4 is developed here into layers: how to read ownership and control, financial statements, cash flows and assets, and how to join these layers into one conclusion. The full treatment, including KYC, EDD, individual background checks and screening procedures, is in the companion guide [KYC, EDD and Corporate Intelligence](https://github.com/mzeynal/kyc-edd-guide); this part keeps only what an OSINT investigator needs at hand.

## 9.1 The task and the data map

| Layer | What it answers | Typical sources |
| --- | --- | --- |
| Company register | Does the entity exist, what is its history | Company registers, extracts |
| Ownership and control | Who owns and who actually decides | Ownership registers, articles, shareholder agreements |
| People | Who the officers are and how they are connected | Officer searches, identity checks |
| Financial statements | Scale, related parties, anomalies | Filings, disclosures |
| Charges and obligations | Credit links and pressure | Registers of charges, notes to statements |
| Courts and regulators | Disputes, measures, bans | Court registers, regulators, debarment lists |
| Sanctions, PEPs, adverse media | Exposure and reputation | Official lists, aggregators, multilingual search |
| Assets | Where the money and use really are | Vessel, aircraft and property registers, AIS, ADS-B |
| Digital and operating traces | Is there real activity | Websites, procurement, vacancies, staff profiles |

### Claim-to-verification

Turn each claim by the company into a record "claim — evidence — status": a stated turnover should leave external traces (contracts, procurement, staff); stated owners must match registers and documents; stated assets must match registers and independent observation.

## 9.2 Ownership and control

The register shows recorded owners, while decisions are made by those who control money, directors and contracts. For a chain "A owns 60% of X, X owns 40% of Y, Y owns 100% of Z" the effective share of A in Z is 0.60 × 0.40 × 1.00 = 24%, below the typical 25% threshold, while under a US-style 50% sanctions rule the answer is different again and a chain of control (more than 50% at each link) breaks at the second link. Always state which rule you used. Look for control without a shareholding (powers to appoint directors, powers of attorney, credit dominance, management contracts, signing rights) and for the "49/51" nominee pattern. Details on the state of registers are in the companion guide and in [updates/2026-11.md](../updates/2026-11.md).

## 9.3 Financial statements and related parties

Compare what is claimed with the statements and with external reality. Useful indicators: days sales outstanding (receivables ÷ revenue × 365), growth of receivables against revenue, cash conversion, revenue per employee, the share of related-party revenue, contingent liabilities (guarantees for related parties), changes of auditor. Each is a question that needs an explanation, not a verdict.

## 9.4 Cash flows and obligations

Payments themselves are rarely visible, but obligations and encumbrances are: registers of charges, notes to the statements, court exhibits and procurement portals. Compare terms with the market: a guarantee without a fee, a loan without interest or term, or a sale of an asset at an understated price point to common interests.

## 9.5 Assets

Title is not use. For a vessel distinguish the registered owner, operator, technical manager and beneficial owner and work by IMO; for aircraft work by the ICAO hex code; for property distinguish titleholder, tenant and manager. Independent traces of use weigh more than a single register entry (sections 5.3 and 4.4).

## 9.6 Screening, courts and regulators

Screen persons and organisations against sanctions lists and PEP data, and record the list version and date. Check courts, regulators and debarment lists; distinguish a charge, a claim and a judgment. Recent changes are in [updates/2026-11.md](../updates/2026-11.md); keep a dated record of every list you used.

## 9.7 Typologies and red flags

- **Shell networks:** hundreds of companies at one address, nominee directors with hundreds of positions, multi-layer ownership across countries, minimal filings.
- **Sanctions evasion:** a new company with the same people and address after a listing, a transfer of shares close to the sanctions date, a change of vessel manager, flag or name, AIS gaps, transit through weakly supervised countries.
- **Statement manipulation:** receivables growing faster than revenue, cash "held by third parties" without confirmation, a high share of related parties, a change of auditor.
- **Procurement risks:** a new company wins large contracts, one winner on many similar tenders, contracts split below thresholds.

A flag becomes a conclusion only in combination with independent indicators; for each flag write the innocent explanation and the observation that would tell the two apart.
