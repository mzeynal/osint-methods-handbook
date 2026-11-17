# Part 8. Case management, analysis and reporting

## 8.1 Case management: logs, structure, tools

Good documentation turns an investigation from a set of finds into verifiable work. If you cannot show where a fact came from, you cannot use it.

### Five logs

| Log | What to record | Why |
| --- | --- | --- |
| Tasks and questions (PIR) | Key questions, the client's decision, deadlines, limits | Not to drift from the goal |
| Hypotheses | The version, arguments for and against, what to check, status | Not to lose alternatives |
| Sources | Address, date and time of access, what was extracted, type (primary or secondary), reliability | Verifiability and reproducibility |
| Evidence | File, hash, from where, when, by whom, where stored | Authenticity of materials |
| Decisions and contacts | Legal and ethical decisions, approvals, correspondence | Protection when questions and disputes arise |

Templates are in the [templates](../templates/) folder.

### Case folder structure

```text
CASE_2026-xxx/
  00_brief/            questions, limits, approvals
  01_logs/             hypotheses, sources, evidence, decisions
  02_raw/              original files (read-only)
  03_page_archive/     screenshots, archive copies
  04_data/             tables, exports, graphs
  05_analysis/         notes, hypothesis tables
  06_reports/          drafts and final versions
  99_closure/          closure checklist, list of deleted materials
```

File names: date, short description, version, for example `2026-10-17_post-channel_v1.png`. Originals are not edited; work on copies.

### Tools (G: choose by task and budget)

| Task | Classes of solution |
| --- | --- |
| Notes and knowledge base | Note-taking apps with links and versions; shared documents with history |
| Saving web pages | Extensions and services for capturing pages with metadata; local archiving tools; manual screenshots with address and time |
| Link graphs | Specialised link-analysis programs, graph databases, free visualisers |
| Tables and data | Spreadsheets; scripts; databases for large sets |
| Collaboration | Task systems and shared stores with access control |
| Versioning | Version control systems for scripts and notes |

Selection criteria: reproducibility, storage security, licence, price, sustainability of the project. A catalogue of living tools is kept, for example, by Bellingcat.

### Working as a team

- **Roles:** case lead, analysts, a reviewer, and where needed a lawyer and a native speaker.
- **Handover:** every new participant reads the logs rather than listening to a retelling.
- **Review:** a second analyst checks the key conclusions before release.
- **Daily check-ins:** briefly: what was found, which versions are being checked, which risks.
- **Closing the case:** a checklist ([templates/case-closure-checklist.md](../templates/case-closure-checklist.md)): deleting unneeded data, archiving, a final review.

### Retention and deletion

Define the retention period for case materials and the procedure for protecting and deleting them. Personal data collected "just in case" are to be deleted (section 1.2).

## 8.2 Analysis and the report

The main task of a report is to answer the client's question so that the reader understands what can and cannot be believed. The quantity of what was found is secondary.

### Analysis of competing hypotheses

When there are several versions, list them in a table and assess each by the evidence that **refutes** it, not only the evidence that supports it (G). The version that wins is not the one with the most confirmations but the one with the fewest refutations. The full method (diagnosticity of evidence, indicators, scenarios, assessment of intent) is in section 8.4.

| Evidence | Hypothesis A | Hypothesis B | Hypothesis C |
| --- | --- | --- | --- |
| Fact 1 | Consistent | Contradicts | Consistent |
| Fact 2 | Neutral | Consistent | Contradicts |

### Cognitive traps

- **Confirmation bias:** looking only for what is consistent with the version.
- **Anchoring:** the first detail found defines the picture.
- **Availability effect:** vivid stories seem more probable.
- **Narrative bias:** the wish to arrange facts into a pretty story.
- **Mirror imaging:** assuming the subject acts as you would.
- **Groupthink:** the team agrees in order to avoid argument.

Measures: a designated devil's advocate, stopping conditions set in advance, and review by someone who did not take part in the work.

### The language of confidence

Words such as "possibly" are understood differently by different readers. Use a single scale tied to ranges of probability (G: a guide used in analytic services):

| Wording | Approximate probability |
| --- | --- |
| Almost certain | 95–99% |
| Highly likely | 80–95% |
| Likely | 55–80% |
| Roughly even chance | 45–55% |
| Unlikely | 20–45% |
| Highly unlikely | 5–20% |
| Almost ruled out | 1–5% |

Assess **source reliability** and **information credibility** separately: a good source may report something doubtful and a bad one something true.

### Report structure

1. **The main conclusion first.** An answer to the client's question in 2–3 sentences with the confidence level.
2. **Basis.** Three to five key arguments with sources.
3. **Alternatives.** What else could explain the facts and why it was rejected.
4. **Gaps and limits.** What is not established, where data are unavailable (a closed platform, no imagery).
5. **Recommendations.** What steps are needed next.
6. **Appendices.** Chronology, graph, source logs.

### Writing for the reader

- Short sentences, concrete verbs, no "according to some data".
- Every fact has a footnote to its source; every assumption is marked as an assumption.
- Distinguish "established", "probable", "not established".
- Visualisations (maps, diagrams) are captioned, with a date and a source.
- Terms and abbreviations are explained on first use.

### Review and checking

- **Fact-checking:** check every statement, by sample or in full, against the source log.
- **Red team:** a colleague tries to refute the key conclusions.
- **Legal and ethical review** before handing over and publication.
- **Right of reply:** if the report concerns a person or organisation and may harm them, give them a chance to respond.

### Corrections

Mistakes are inevitable. Set a procedure: what to do if you find an error after release (inform the client, correct it, mark the date and substance of the correction, check whether the error affected the conclusions). Hidden corrections destroy trust.

## 8.3 Link analysis module: from graph to evidence

A line on a graph is not a fact but a statement. Every such statement must have a type, a direction, a period, a source, a confidence level and alternative explanations. This module teaches how to tell a confirmed link from an assumption, to explain what exactly it means, to place it on a timeline and to test other versions.

### How a link is recorded

| Field | What to record |
| --- | --- |
| Nodes A and B | The name and identifier of each (number, date of birth, page address) |
| Type and direction | Who owns, manages, pays or serves whom |
| Period | From which date to which date the link existed; the date of observation |
| Source | A primary document or a secondary one; address, access date, hash of the copy |
| Independence | How many independent chains of sources confirm it |
| Confidence | Confirmed, probable, possible, unconfirmed, refuted |
| What the link does not prove | Write it explicitly, for example "does not prove common ownership" |
| Alternative explanations | At least two, one of them innocent |
| What to check next | An observation that will tell the explanations apart |

### Types of link: what they assert and what they do not prove

| Type | What it shows | What it does not prove | Typical sources | Weight |
| --- | --- | --- | --- | --- |
| Shareholding | A formal right to income and votes | Actual control and the beneficiary | Registers, extracts | A direct document |
| Officer (director, secretary, signatory) | A formal management role | Ownership; the person's independence (nominees exist) | Registers | Direct, with a caveat about nominees |
| Power of attorney, right to represent | Authority to act on behalf of | Ownership | Register documents | A strong sign of control |
| Financial (credit, guarantee, pledge, payment) | Economic dependence | Common control (ordinary commerce is possible) | Register of charges, financial statements, court documents | Strong if the terms are non-market |
| Operational (customer, supplier, agent, contractor) | Business interaction | Dependence and control | Port data, procurement, contracts | Weak or medium |
| Address (shared address, floor, phone) | A match of contact details | A common owner | Registers | Weak, depends on the type of address |
| Technical (domain, hosting, analytics, code) | A common technical basis | Ownership | WHOIS, DNS, scanners, page code | Weak; a unique identifier is stronger |
| Personal (kinship, shared past) | A personal relationship | A business link | Publications, registers, media | Medium |
| Social (subscription, mention) | Contact | Acquaintance, a business link | Social networks | Weak |
| Chronological (events at the same time) | Possible coordination | Causation | Registers, news | Weak, strengthens in combination |

### Link confidence scale and rules for changing it

- **Confirmed:** a primary document or at least two independent sources; the identity of the parties is established; the period is known.
- **Probable:** several independent indirect signs of different types; a simple innocent explanation is unlikely.
- **Possible:** one sign or several signs of the same type.
- **Unconfirmed:** the claim was found, the check was not done.
- **Refuted:** there are data that contradict it.

Rules:

1. Confidence grows only through independent sources of different origin.
2. **Signs of the same type do not add up.** Three matches on one address are one sign.
3. A unique identifier weighs more than a shared feature.
4. The link must have existed on the relevant date.
5. The existence of a simple innocent explanation reduces confidence.

### Chronology of links

A link has a period, and events must be lined up on a common timeline. Build a table "date — event — source — which links it affects". Consistency checks:

- **Possibility.** A person cannot be a director before the company was registered.
- **Sequence.** What came first: the sanctions listing or the transfer of shares.
- **Window.** What happened in the 30 days before and after a significant event (sanctions publication, a claim, an inspection).
- **Durability.** Did the link survive the event or break.
- **Overlapping periods.** Do the periods of one person's participation in several companies coincide.

### Alternative explanations: a mandatory step

For every significant link write the innocent and the significant explanations, then ask: **what observation would tell them apart?** That is the next step of verification. If there is no distinguishing observation, leave the link "possible" and do not build a conclusion on it.

### Worked case: several companies use one address

**Short answer: a shared address by itself proves almost nothing.** What explanations are possible:

| Explanation | How to check | What should be visible |
| --- | --- | --- |
| The address of a registration agent or a virtual office | How many companies are listed at the address; who the secretary is | Dozens or hundreds of companies, one secretary |
| A business centre or coworking space | What is at the address (map, sites, photos) | Many tenants, different industries |
| A group of companies under common management | Shared persons, finances, documents | See the list of signs below |
| A family business | Kinship of the owners | The same surnames, joint transactions |
| An outdated or erroneous address | Cross-checking with other sources and archives | A different address in the financial statements and on the site |
| An address for registering "paper" structures | Whether there is operating activity and staff | No signage, no website, no personnel |

**What is needed to establish common ownership or actual control.** Signs by strength:

| Strength | Signs |
| --- | --- |
| Strong | A common beneficiary in the ownership register; the same individual (identity confirmed) as shareholder or director of several companies; mention of a "group" or consolidation in audited financial statements; cross guarantees, pledges and loans on non-market terms; shared signatories of bank accounts (from court documents); the right to appoint and remove directors (articles, shareholders' agreement); a court ruling on affiliation; a public statement by the owner |
| Medium | Overlapping directors and secretaries, if they are not a professional agent; unique technical identifiers (analytics, code elements); a shared website, brand, phone, corporate e-mail; transfers of assets and staff between companies; synchronised corporate actions (a change of director or a transfer of shares on the same day) |
| Weak | A shared address (especially an agent's); a shared domain registrar or hosting; similar names; close registration dates; a shared notary or agent |

**Algorithm.**

1. Determine the type of address: how many companies are on it, who the agent is. For a mass address the weight of the sign is close to zero.
2. Find the overlapping individuals (directors, shareholders, signatories) and confirm their identity (section 3.1).
3. Find financial links: pledges, guarantees, loans, payments, shared creditors.
4. Find documents about the group: financial statements, procurement and credit questionnaires, disclosures to regulators.
5. Find unique technical identifiers, then check the innocent explanation (one web developer, a shared contractor).
6. Compare corporate actions by time.
7. State the conclusion separately: the link as a **fact** ("the address matches": confirmed) and the link as a **meaning** ("there is common control": probable, possible, not established).

**Control and ownership.** Formal ownership can be read from a register. Actual control is shown by decisions: who appoints directors, who signs, in whose hands money and resources are concentrated, who pays on obligations. A conclusion about control needs data on decisions and money, not only on addresses and names.

### Network metrics: with caution

Node degree, betweenness and cluster density suggest where to look. But often the "central" node is simply the better-documented one. A metric is a lead for checking, not proof.

### Typical mistakes

- Treating a line on a graph as proof.
- Adding up signs of the same type.
- Not stating the period of a link.
- Not recording what the link does not prove.
- Taking an agent's address for the address of a group.
- Mixing formal ownership and actual control.
- Building a conclusion on one chain of sources retold by different outlets.

## 8.4 Intelligence analysis: from explanation to assessment and forecast

An investigation answers the questions "what happened" and "who is behind it". Analysis answers the next ones: what it means, what is likely to happen, and how well founded the assessment is. A forecast is never a fact: it is an assessment with named assumptions, a time frame, a test criterion and conditions for revision.

### The analytic pipeline

1. **Question:** the client's decision, horizon, criterion.
2. **Assumptions:** what we take as given and what happens if it is wrong.
3. **Hypotheses:** including "nothing unusual" and "data error".
4. **Matrix of competing hypotheses** with an assessment of the diagnosticity of evidence.
5. **Red team:** an independent attempt to refute the leading version.
6. **Assessment:** probability and, separately, confidence.
7. **Indicators, scenarios and conditions for revision.**

### Step 1. The analytic question

| Weak wording | Strong wording |
| --- | --- |
| What is known about company X? | How likely is it that X is controlled by person Y, and how will the risk of the deal change in the next six months? |
| Is there a link to sanctions? | Does X have a link to persons on the list before and after the date of listing, and does the exposure persist now? |
| Will there be a restructuring? | Is it likely that by 31 March a register entry will appear on a transfer of X's shares below the control threshold? |

### Step 2. Testing assumptions

| Assumption | What it rests on | If wrong | How to check |
| --- | --- | --- | --- |
| The register reflects real ownership | The register entry | Nominee holders hide the beneficiary | Powers of attorney, courts, financial statements |
| Two persons with the same name are one person | A name match | Misidentification | Date of birth, an independent identifier |
| The date of the share transfer equals the date of the decision | The date of the entry | The decision came earlier, the entry later | Minutes, disclosures, news |
| The source's data are complete | The source seems comprehensive | Invisible participants | Alternative sources, gaps |

### Steps 3–4. The matrix of competing hypotheses

Evidence is **diagnostic** if it is consistent in different ways with different hypotheses. A fact that is consistent with all versions (for example a shared agent's address) distinguishes nothing and should not change the assessment. Rules:

- Count not confirmations but **contradictions**: keep the version with the fewest serious contradictions as the leading one.
- Weigh evidence by reliability and independence.
- Test sensitivity: would the ranking change if the strongest piece of evidence were removed?
- For the leading versions write the observation that would tell them apart.

An illustrative example (a fictional situation): 14 days after a company is added to a sanctions list its shares are transferred to a holding with unknown beneficiaries.

| Evidence | H1: planned reorganisation | H2: reaction to sanctions while keeping control | H3: sale to an independent buyer | H4: data error |
| --- | --- | --- | --- | --- |
| Transfer 14 days after listing | N | C | N | N |
| The buyer is a holding with unknown beneficiaries | N | C | I | N |
| The former director stays in office | C | C | I | N |
| The deal price is not disclosed | N | C | N | N |
| The website, staff and bank details are unchanged | C | C | I | N |
| There is no second transfer entry in the register | N | N | N | C |

(C — consistent, N — neutral, I — inconsistent.) Conclusion: H3 has three contradictions, H4 has none but explains little; what tells the leading H1 and H2 apart is an observation about motive and timing: the appearance of new structures, changes of managers, the earlier practice of reorganisations.

### Probability and confidence are two different dimensions

Probability is our estimate of the chance of an event on the word scale (section 8.2). **Confidence** is the quality of the basis of that estimate.

| Confidence | Signs |
| --- | --- |
| High | Several independent reliable sources; consistency; no significant gaps |
| Medium | The sources are reliable but part of the data is indirect or incomplete; there are gaps that do not change the conclusion |
| Low | One chain of sources, contradictions, critical gaps |

Wording: "**Likely** (55–80%), **medium** confidence: the basis is …; the key gap is …".

### Indicators and warning signs

An indicator is an observable event that confirms or refutes a hypothesis or signals a change in the situation. A good indicator is observable in open sources, specific, has a threshold and a time limit and is tied to a hypothesis or scenario.

| Indicator | Where to observe | Threshold | What it means |
| --- | --- | --- | --- |
| A new company at the address or with the details of a sanctioned one | Registers, domains, procurement | Any entry after the listing date | A possible successor |
| A transfer of shares near the control threshold (49/51) | Registers | Any change | Possible fragmentation of control |
| A change of director or secretary | Registers | Any change among key persons | Preparation for a change of structure |
| Removal or addition of a pledge or guarantee | Registers of encumbrances | Any entry | A change in economic links |
| A change of flag, manager or vessel name | Vessel registers, AIS | Any change | Moving away from sanctions risk |
| AIS gaps | AIS services | More than a day without a signal | Possible transhipment at sea |
| Appearance on lists | Sanctions lists | Any listing | Escalation of risk |
| A change of auditor, delayed financial statements | Registers, financial statements | A change or overdue filing | Deteriorating transparency |

For each indicator set how often to check it (weekly, monthly), a record of the result and an action agreed in advance for when it triggers.

### Scenario analysis

Scenarios are needed when the future depends on several uncertain factors and a single "best forecast" misleads.

1. Set the question and the horizon (for example six months).
2. List 5–10 factors that affect the outcome.
3. Choose **two uncertainties** that are both important and hard to predict; these are the axes.
4. Build a 2×2 matrix: four scenarios.
5. Describe each as a coherent "if… then…" chain and give it a name.
6. Name the early signs (indicators) for each.
7. Estimate rough probabilities and justify them.
8. Decide what would change the assessment and what is worth doing in any scenario.

|  | Axis: network's readiness to restructure (low) | Axis: network's readiness to restructure (high) |
| --- | --- | --- |
| Axis: regulatory pressure (low) | Scenario A: status quo | Scenario B: quiet rebuild |
| Axis: regulatory pressure (high) | Scenario C: direct action against the company | Scenario D: rapid exit and successors |

A template for describing a scenario: name, conditions, probability, early signs, effect on the client, recommended actions.

### How to justify a forecast

- **Base rates.** How often does such an event happen in similar situations? Do not name a probability "from the ceiling": use public reviews and your own closed cases.
- **Decomposition.** Break the event into conditional steps and estimate each.
- **Adjustment.** Move the estimate away from the base rate in small steps on the basis of specific evidence.
- **Testability.** Word the forecast so that it can be assessed: a time limit, a criterion, a source for checking.
- **Forecast log.** Record the estimate, date, criterion and outcome; periodically calculate how often "likely" and "highly likely" forecasts come true (calibration) (G).
- **Revision.** State the conditions under which the estimate will be revised.

### Assessing threats and intent

A simple framework: a threat is defined by **capabilities** (resources, intermediaries, jurisdictions, infrastructure), **intent** (the wish and readiness to act) and **conditions** (weaknesses of control, windows, dependence on banks and regulators). Intent is the weakest link: it cannot be derived from capabilities alone. Distinguish "can" from "will".

| Component | What to assess | Signs | Typical error |
| --- | --- | --- | --- |
| Capabilities | What the actor has to act with | Companies, accounts, vessels, intermediaries, experience | Treating capabilities as intent |
| Intent | What the actor wants to do | Statements, preparatory actions (registrations in advance), history, motives | Attributing intent on the logic of "I would do it this way" |
| Conditions | What helps or hinders | Weak oversight, windows, dependence on intermediaries | Ignoring external constraints |

Look for signs of intent in preparatory actions (a new registration before the event, advance transfers, changes of managers), and for counter-signs in the absence of actions that would be logical if there were intent. Wording: "We assess with moderate confidence that X is likely to continue operating through structure Y over the next six months because…; the key gap is …".

### Structured analytic techniques

| Technique | When to apply |
| --- | --- |
| Assumption check | At the start of work and before a conclusion |
| Competing hypotheses | When there is more than one version |
| Red team | Before releasing significant conclusions |
| Pre-mortem | Imagine the conclusion turned out wrong in six months: why? |
| What if | Testing the conclusion's resilience to a change in a key fact |
| Indicators | For monitoring after release |
| Scenarios | When the future is uncertain |
| Network analysis | For links and roles (section 8.3) |

### Template for an analytic assessment

**Assessment** (one sentence) → **probability and confidence** → **basis** (3–5 arguments) → **assumptions** → **alternatives** → **indicators** → **what would change the assessment** → **gaps**.

### Typical mistakes

- One scenario instead of several.
- A forecast without a time limit and a test criterion.
- Probability words without a scale; mixing probability and confidence.
- Substituting capabilities for intent.
- Fitting indicators to an already formed version.
- Refusing to revise the assessment when new data arrive.

## 8.5 Report formats: one client question, four formats

The format is chosen by the question and the reader. Any report answers the client's question in its first lines; a list of what was found is not yet a report. For every finding check: **what does this mean for the client's decision?** If there is no answer, the finding goes into an appendix.

| Format | Reader | Question it answers | Length | Main requirement |
| --- | --- | --- | --- | --- |
| Analytic brief | A manager, an investment committee | What to do and how confident we are | 1 page | The conclusion in the first two lines |
| Detailed investigation report | The client, a lawyer, compliance | What is established, how we know it and what we do not know | 10–30 pages | Every conclusion with evidence and alternatives |
| Technical report with appendices | A reviewer, a colleague, a lawyer, a regulator | Can the result be repeated and defended | By the volume of methods | Reproducibility |
| Corporate network profile | Compliance, a bank, an investor | Who controls the network, how it is built and what the risk is | 2–4 pages plus appendices | Structure, links, currency |

**Choosing by the client's question.**

| Client's question | Main format | In addition |
| --- | --- | --- |
| Should we go ahead with the deal? | Brief | Network profile |
| What exactly is established and on what basis? | Detailed report | A brief for management |
| Can this be shown to a regulator or a court? | Technical report | Logs and hashes |
| Who is behind the network and how do we monitor it? | Network profile | Indicators and update dates |

### Format A. A one-page analytic brief

```markdown
# [Topic]: analytic brief
Date · Author · Classification · Assessment valid until

QUESTION: the decision the client is taking.
CONCLUSION: 1–2 sentences; probability and confidence.
BASIS:
1. Argument with a source.
2. Argument with a source.
3. Argument with a source.
ALTERNATIVES: what else is possible and why it is less likely.
INDICATORS: what would change the assessment, where to observe it.
RECOMMENDATION: action, deadline, owner.
GAPS: what is unknown and what to do about it.
SOURCES: 3–5 key ones; the full log in the appendix.
```

Rules: 300–400 words; no background; no more than three arguments; numbers and dates instead of adjectives; all abbreviations spelled out. Typical mistakes: a chronology instead of a conclusion, a list of sources instead of an argument, probability words without a scale, a recommendation without a deadline.

### Format B. A detailed investigation report

1. **Executive summary** (up to a page): the question, conclusion, confidence, recommendations.
2. **Task and limits:** what was sought, what was not, constraints.
3. **Methodology and sources:** brief; details in the appendix.
4. **Main conclusions** for each of the client's questions: the conclusion, evidence, confidence, alternatives.
5. **Description of findings** by layer: people, companies, assets, finances, infrastructure.
6. **Chronology.**
7. **Analysis:** competing hypotheses, indicators, scenarios (if requested).
8. **Limits and gaps.**
9. **Recommendations and next steps.**
10. **Appendices:** the link table, the graph, the logs.

Rules: every conclusions section begins with the answer; next to each statement a reference to the evidence; separate "established", "probable" and "not established"; put disputed points in boxes with alternative explanations.

### Format C. A technical report with appendices

Purpose: so that another specialist can repeat the work and confirm the result.

| Section | Content |
| --- | --- |
| 1. Purpose and questions | What was being tested |
| 2. Environment and tools | Versions, dates, search engines, region and language, settings |
| 3. Methods step by step | Queries, parameters, order, the reason for the choice |
| 4. Results of the checks | What was found, where, how confirmed |
| 5. Data processing | Normalisation, deduplication, formulas |
| 6. Confidence for each conclusion | The scale and the justification |
| 7. Limits | Unavailable sources, delays, possible distortions |
| 8. How to repeat | A short instruction |

Appendices: **A** query log; **B** source log; **C** evidence log with hashes; **D** data tables; **E** graph and link table; **F** scripts and library versions; **G** records of legal and ethical decisions.

Rule: observations and conclusions are separated. Where a fact is needed there must be no interpretation.

### Format D. A corporate network profile

The profile is the network's "passport", which can be updated and used for screening.

1. **Summary:** who it is, what it does, who controls it (with confidence), the main risks, a recommendation.
2. **Ownership and control diagram** with link types and confidence levels.
3. **Register of legal entities:** name, jurisdiction, number, date, status, address, role in the network.
4. **Register of people:** name, identifiers, roles, periods, identification confidence.
5. **Link table** in the format of section 8.3.
6. **Assets and operations.**
7. **Finances:** what is known, related parties, red flags.
8. **Sanctions, courts, regulators, adverse media** with the dates of list versions.
9. **Chronology of key events.**
10. **Assessment:** hypotheses, probability and confidence, indicators, scenarios.
11. **Gaps and next steps.**
12. **Source log.**

Updating rule: every profile carries a snapshot date and a list of indicators on which the profile is revisited.

### How the formats relate

All four formats are built from the same logs and one link table. The practical order of work: technical report (facts and methods) → network profile → detailed report → brief (read first, written last).

### Report quality test

1. Does the first paragraph answer the client's question?
2. Is the main conclusion visible in the first three sentences?
3. Are facts separated from assessments, and assessments from recommendations?
4. Does each conclusion have a source, a confidence level and alternatives?
5. Are the gaps named, and what to do about them?
6. Can a colleague repeat the work from the logs?
7. Does the text contain details that are not needed for the decision (or are dangerous for people)?

### Typical mistakes

- One and the same long text for all readers.
- Findings without a conclusion ("here is what we found").
- A conclusion without a source and without a confidence level.
- Recommendations unconnected with the conclusions.
- Hidden assumptions.
- No snapshot date and no period of validity of the assessment.
