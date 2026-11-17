# Part 3. People and identity

Working with data about people is the riskiest part of OSINT: it is where mistakes and harm come most easily. This part describes the methods used when checking public figures and counterparties and in public-interest investigations, and draws the boundaries at once (section 1.2).

## 3.1 Identifiers, usernames, e-mail, phone numbers

### Identifiers and their strength

| Identifier | Strength as an anchor | Typical traps |
| --- | --- | --- |
| Government number, registration number | Very high | Typos; different people with similar numbers in different countries |
| Numeric profile identifier (ID) | High | Links change format |
| E-mail address | High | Shared mailboxes; forwarded addresses |
| Phone number | Medium | Numbers are resold and reassigned |
| Username | Medium or low | One handle used by different people; reuse and takeover |
| Photograph | Medium | Other people's photos, avatars, generated faces |
| First and last name | Low | Namesakes; transliterations |
| Address | Medium | Mass-registration addresses; outdated data |

### Usernames

Searching one handle across many platforms is a classic technique. Special utilities and catalogues exist for it (for example projects that try hundreds of sites; G). Rules:

- A matching handle is a hypothesis, not a conclusion: check the avatar, bio, links, language, activity times, mutual followers.
- Look for **reuse**: people change their handle, avatar, bio phrases and e-mail less often than it seems.
- Allow for **takeover**: an abandoned handle may have been taken by someone else.
- Record creation and activity dates: a handle may have belonged to different people in different periods.

### E-mail

- Check the format and the domain; corporate domains often reveal affiliation.
- Open information: profiles linked to the address, avatars, public mentions. Do not use password-recovery functions to check whether an account exists, and do not try to log in to someone else's account (section 1.2).
- Leak databases may show that an address took part in an incident. Rules of use are in section 5.2.

### Phone numbers

- Normalise the number to international format; determine the country and the type (mobile, landline).
- Search for the number in open listings, profiles and documents.
- Checking whether a number is present in messengers (an account, a profile photo) involves sensitive data: the check may notify the owner and may break the service's rules (G). Use it deliberately.

### Three levels of identity

One of the main mistakes is mixing levels:

1. **Account** (a profile on a platform).
2. **Persona** (a set of accounts run by one party under one "role").
3. **Person** (a real individual).

Proving an "account — persona" link is easier than "persona — person", and the thresholds of proof differ. To move to a person you need at least two independent anchors (for example a unique identifier and confirmation from a reliable source) and a check of alternative explanations.

### Traps

- **Namesakes.** Always look for a second indicator.
- **Fake profiles** and copied avatars.
- **Outdated data:** the address or phone number changed long ago.
- **Generated faces** on fake profiles (section 4.2).
- **Confirmation bias:** you found a profile that "fits" and stopped looking for others.

## 3.2 Social platforms: what is observable and how to work

Each platform has its own logic, access rules and blind spots. General principles: first determine what is publicly visible without logging in; then what is visible after logging in; and only then what requires special rights. Access conditions change quickly, so the facts below are dated.

### Data access (S, as of late 2026)

- **X.** Academic-level access has been removed; reportedly reading is paid (USD 0.005 per post, a limit of 3 million a month).
- **Reddit.** On 5 August 2026 it announced a gradual restriction of its public API.
- **Meta (Facebook, Instagram).** Meta Content Library is a research tool, successor to CrowdTangle; access only for vetted academic and non-profit researchers, and work happens inside Meta's protected environment. The Meta Ad Library exists thanks to EU transparency requirements.
- **TikTok.** A Research API for vetted researchers; the vetting takes at least four weeks.
- **EU DSA.** Article 40(12) obliges very large platforms to provide data to vetted researchers; a January 2026 audit (Bekavac, Mayer) showed that data in the Meta and TikTok APIs lose completeness through narrower coverage, removed metadata and operational limits.

Takeaway: research APIs do not replace what an ordinary user sees. Compare API data with what is visible in the interface, and do not call a sample complete.

### Platforms and techniques

| Platform | What is useful | Features and risks |
| --- | --- | --- |
| X | Search by user, dates, replies; timeline, replies, quotes | Login requirements and paid data access; content is deleted; archive immediately (G) |
| Facebook, Instagram | Public pages, groups, geotags, stories (while available); Ad Library | No open global search; much is closed; story view marks (G) |
| LinkedIn | Professional connections, positions, job ads | Profile-view notifications; the terms prohibit automated collection (G) |
| YouTube | Descriptions, comments, upload date, channel history | Upload date is not filming date; frame-by-frame tools are needed for video checks (section 4.1) |
| TikTok | Video, sounds, hashtags, geotags | Content and search are personalised; data access is restricted (S) |
| Reddit | Discussions, a user's comment history | API restrictions (S); deleted content often disappears |
| Bluesky, Mastodon | Open protocols, public streams | Decentralised; ease of automation depends on the server (G) |
| GitHub | Repositories, commits, e-mail addresses in metadata, issues | Commit metadata often contains the author's name and e-mail; use with care (G) |
| Forums, reviews, marketplaces | Traces of everyday habits, deals, contacts | Often contain personal data of third parties; minimise (G) |
| Chinese platforms | See section 6.1 | Censorship and language determine what is visible |
| Telegram, messengers | See section 3.3 | Special rules and risks |

### Universal techniques

- **Time analysis.** Posting times and timestamps help estimate time zone and routine; remember that platforms show time differently and users may be in different zones.
- **Account age and history.** A recently created account with heavy activity is a sign of coordination or a bot.
- **Network signs.** Shared followers, simultaneous posts, identical wording.
- **Deleted content.** Look in archives (section 2.2) and in other users' replies.
- **Geotags and backgrounds.** Geotags are often imprecise; compare with imagery (section 4.3).
- **Profile metadata.** The numeric profile identifier, registration date (if shown), linked URLs.

### Practical rules

- Work with public content; do not join closed communities under a false pretext (section 1.2).
- Record not only the text but also the limits: "visible only after login", "part of the comments hidden".
- Do not use data of third parties (relatives, friends) beyond what is needed.
- For platforms where access is paid or closed, state it in the report as a limitation.

## 3.3 Telegram and messengers

Telegram is one of the main sources for investigations of wars, politics, cybercrime and regions where other platforms are blocked or unpopular. It is also one of the riskiest in terms of ethics and safety. The description below rests on general knowledge (G); check the current client features and rules before you start.

### What is observable

| Object | What is visible | What to consider |
| --- | --- | --- |
| Public channels | Messages, dates, view counters, reactions, pinned messages | The owner can delete and edit; save immediately |
| Public groups | Members' messages, replies, attachments | Participants may be private individuals; minimise data |
| Forwards | The source of a forwarded message (unless hidden) | Allows you to build chains of spread |
| Profiles | Name, username, bio, avatar, sometimes last activity | A username can be changed; the numeric identifier is more stable |
| Message links | A permanent link to a specific message | The basis for citation and archiving |
| Bots | Public bots and their descriptions | Many are used to collect or sell data; do not use them to obtain other people's personal data |

The web preview of public channels lets you read them without an account, and some search engines and directories index channels (G). For a quick look that is often enough.

### Working techniques

1. **Forward chains.** Establish the original source and the time of first appearance. This is the basis of analysing how narratives spread and of verifying authenticity.
2. **Numeric identifiers.** Save them with every find; usernames change.
3. **Channel statistics.** Third-party services show follower growth, reach and posting frequency (G); the data are indicative.
4. **Time analysis.** Posting, editing and deletion times in a channel.
5. **Links.** Shared administrators, forwards between channels, repeated ad blocks and invitation links.
6. **Media.** Check files in the usual way (section 4.1): Telegram often strips metadata on forwarding.

### Limits and ethics

- **Joining closed groups.** Deception to join and collecting members' data breaches ethical principles and often the rules; lawfulness depends on the country and the purpose. Do not do it without a team decision and a lawyer.
- **Phone numbers.** Account registration is tied to a number; buying "disposable" numbers and using other people's numbers may break the law and the rules (G).
- **Automation.** Client libraries allow channels to be read programmatically (G), but they require an account and compliance with limits; mass collection of members' personal data is unacceptable (section 1.2).
- **Traces.** Joining, subscribing and read marks are visible to administrators in some modes; account for this in the threat model (section 1.3).
- **Safety.** Files and links from channels are sometimes malicious. Open them in an isolated environment.

### Other messengers (G)

- **WhatsApp.** Channels are public, ordinary chats are closed; public invitation links are sometimes indexed. Checking whether a number is on the service is sensitive (section 3.1).
- **Signal, Viber, WeChat and others.** Most content is closed; public sources are limited to links, invitation posts and mentions elsewhere.
- **Discord.** Public servers with open access by invitation; it is important to save the identifiers of users, servers and channels.

### The rule

In closed messengers the investigator works with what was obtained lawfully and without deception: public channels, links, material shared by sources, and open mentions.

## 3.4 Link graphs, false correlations and de-anonymisation

### The link graph

A graph consists of nodes (people, organisations, accounts, domains, addresses, assets) and edges (ownership, management, kinship, subscription, payment, joint appearance). Its purpose is not a pretty picture but an answer to the question: who is linked to whom and how reliable each link is.

**Rules for building one.**

1. Every edge has a type, a period, a source and a confidence level.
2. Distinguish confirmed and assumed links (different line styles).
3. Do not draw a link without a source.
4. Do not mix different types of link in one edge (a subscription is not an acquaintance).
5. Simplify the graph from time to time: keep what affects the conclusion.
6. Save a version of the graph for every report date.

**Questions to put to the graph.** Who is the bridge between groups? What connects these two clusters? Which nodes appeared recently? What disappeared? Are there nodes with only one link (a possible blind spot)?

### False correlations

| Source of error | What it looks like | How to check |
| --- | --- | --- |
| Homophily | People with similar interests follow the same accounts but do not know each other | Look for direct signs of acquaintance |
| Shared hosting, address, provider | Sites on one server belong to different people | Check whether it is shared public hosting or an agent's address |
| Shared templates | Identical texts because of shared templates or copying | Compare unique wording and metadata |
| Matching names | The same name for different people | A second independent indicator |
| Salience effect | The most visible nodes seem central | Check data absent from public results |
| Age of a link | The link existed long ago and ended | Check the dates |

### Stylometry and behavioural signs

Investigators sometimes try to link texts by different authors through style, activity times and mistakes. This is a weak indicator: style can be imitated and coincidences are random (G). Stylometry results are acceptable as a hypothesis and always need independent confirmation.

### De-anonymisation: the limits of the permissible

Identifying an anonymous author is the most responsible act in OSINT. It can save people (for example in an investigation of threats or fraud) and wreck the life of an innocent person. A practical framework:

| Question | Acceptable if | Unacceptable if |
| --- | --- | --- |
| Purpose | Investigating harm to others, fraud, threats; checking a public figure | Revenge, harassment, curiosity, "exposing" for attention |
| Subject | A public figure or a person whose actions affect others | A private individual unconnected with the event |
| Method | Public data, independent confirmations | Bypassing protection, using leaks, deception |
| Confirmation | At least two independent anchors, alternatives checked | A single "resemblance" |
| Publication | The minimum necessary; right of reply; an editor's or lawyer's decision | An address, family, workplace without need |
| Consequences | Risk to the subject and third parties assessed | Not assessed |

**The second-look rule.** Before a person is named, the result must pass an independent check by a colleague who did not take part in the investigation and tries to refute it.

**Alternatives.** Often it is enough to show the structure (a network of accounts, a pattern of spread) without naming a specific person. Name someone only if the conclusion loses its meaning without the name and the confirmation is reliable.
