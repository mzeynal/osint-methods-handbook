# Part 4. Media: verification, AI, geolocation, satellites

## 4.1 Verifying images and video

The first question for any file is: **what is it, where is it from, and when and by whom was it first published?** The content is checked only after the provenance.

### Workflow

1. **Provenance.** Find the earliest publication. For an image: reverse search in at least two or three systems (Google Lens, Yandex, TinEye, Bing; G) and search by video key frames. For video: frame-by-frame extraction and key-frame search (tools of the InVID-WeVerify family; G).
2. **Claimed context.** What does the publication assert (date, place, event)? That is a hypothesis to test.
3. **Technical data.** File metadata (EXIF and equivalents; ExifTool; G). Most platforms strip them, so their absence is normal. The presence of metadata does not prove authenticity: it is easily changed.
4. **Content.** Compare with the claim: weather, lighting and shadows, signs and language, clothing, vehicles and plates, sockets, road markings, architecture, vegetation.
5. **Independent confirmations.** Other angles, satellite imagery, weather data, eyewitness accounts, transport data (section 5.3).
6. **Conclusion.** Authenticity and context are assessed separately: a file can be genuine but wrongly captioned.

### Provenance and content: two different questions

| Question | Answer | What next |
| --- | --- | --- |
| The file is genuine but the claimed context is false | Old material passed off as fresh | Report the real date and place |
| The file has been altered | Editing, retouching, splicing | Describe the alteration; find the original |
| The file is generated | AI | Section 4.2 |
| The file is genuine and the context is correct | — | Confirmed, with caveats about the limits of the check |

### Metadata and C2PA

**C2PA (Content Credentials).** An open standard that attaches signed information about provenance and edit history to a file. Know the limits: the information disappears if a platform does not preserve it; support differs between platforms; trust depends on who signed; the absence of C2PA does not mean forgery (S). Current adoption is described in [updates/2026-11.md](../updates/2026-11.md).

### Tools and their limits

| Tool | What for | Limitations |
| --- | --- | --- |
| Reverse image search | Provenance, repeats | Indexes differ; new and private material is not found |
| ExifTool and equivalents | Metadata | Often empty; can be altered |
| Frame-by-frame video analysis | Key frames for search | Quality depends on compression |
| Error level analysis (ELA) and similar | Suspicious areas | Many false positives; not proof |
| Maps, imagery, panoramas | Place comparison | Section 4.3 |

### The most common mistakes

- Treating the absence of metadata as a sign of forgery.
- Taking the upload date for the filming date.
- Trusting reverse search: "not found" does not mean "no original exists".
- Using one tool and drawing a conclusion.
- Checking only the content and forgetting the provenance.

## 4.2 AI generation and deepfakes

Generating plausible images, video and voice has become accessible, which has made the "provenance first" rule stricter. Technical means of checking provenance have appeared at the same time. None of them is universal.

### Provenance checks: SynthID and C2PA

SynthID is an invisible mark that some AI developers embed in images, video, audio and text produced by their models. Which detectors are publicly available, and from which vendors, changes quickly: see [updates/2026-11.md](../updates/2026-11.md) (not verified).

### What each mechanism proves

|  | SynthID | C2PA (Content Credentials) |
| --- | --- | --- |
| Essence | An invisible mark inside the file | Signed provenance information attached to the file |
| What it confirms | The file was created or modified by a model that uses SynthID | The history of creation and edits, if the metadata survived and the signature is trustworthy |
| What it does not confirm | Origin from other models, and authenticity of content | Authenticity of the content by itself |
| Weak points | Does not detect content without the mark; false positives and misses are possible; heavy processing weakens the signal | Metadata is lost on forwarding; platforms support it unevenly |

**The main rule.** The absence of a mark or signature proves nothing. The presence of a mark proves only origin from a marked model, not that what the image shows is untrue.

### Signs of generation and editing (G)

- Illogical details: fingers, teeth, ears, jewellery, text on signs, licence plates, repeating background elements.
- Violations of physics: shadows, reflections, perspective, lighting, relative sizes.
- Uniform skin and textures, a "too clean" background.
- Video: lip movement not matching the sound, flickering outlines, unnatural expression, continuity breaks between frames.
- Context: no other angle, no original source, no eyewitnesses.

Signs age quickly as models improve; rely on provenance and independent confirmation, not on "gut feel".

### Audio

Voice clones are used for fraud and disinformation. To check audio, spectrograms are used: in synthetic fragments the high-frequency part sometimes cuts off faster than in live speech; this can be seen in free audio editors (for example Audacity) (S). It is an indicator, not proof. Also: comparison with known voice recordings, analysis of the noise background, checking accompanying video, finding the original source.

### The "liar's dividend"

Where fakes are cheap, genuine material is easily declared fake. The investigator checks not only the doubtful but also what has been declared false without grounds. Record the grounds on which authenticity was confirmed.

### Verification workflow

1. Find the file's earliest appearance (section 4.1).
2. Check provenance marks: C2PA and available detectors; record the result and the limits.
3. Analyse the content (the signs above), but do not conclude from them alone.
4. Find independent confirmations or refutations.
5. Assess confidence separately for "genuine file" and "correct context".
6. Save the file, its hash and a verification record (section 8.1).

## 4.3 Geolocation and chronolocation

Geolocation is determining where a photo or video was taken from visual cues; chronolocation is determining when. It is a basic verification skill and one of the best ways to train attentiveness.

### Workflow

1. **Extract the clues.** Write down everything visible: landscape, buildings, signs and language, road markings and signs, poles and wires, vegetation, vehicles and plates, sky and weather, shadows, sockets and household details, clothing.
2. **Narrow the region.** Country → region → city → district. Each narrowing must rest on a specific clue, not on a "feeling".
3. **Find candidates.** Maps, satellite imagery, street panoramas, OpenStreetMap data, local maps (Yandex, Baidu, Naver and others; G).
4. **Match small features.** Roof shapes, building layout, a road bend, a river curve, the horizon relief, the placement of signs.
5. **Confirm with at least two independent matches.** One similar building is not proof.
6. **Document.** Coordinates, comparison frames, sources, a confidence assessment, versions used and rejected.

### Types of clues

| Category | What to look at | What it gives |
| --- | --- | --- |
| Language and script | Alphabet, spelling, dialect words, phone codes | Country, region |
| Roads | Driving side, markings, signs, kerbs, surface | Country, regional standards |
| Infrastructure | Poles, transformers, traffic lights, bus stops | Country, provider, city |
| Nature | Plants, soil, relief, climate | Region, altitude, season |
| Buildings | Materials, styles, roofs, height | District, era |
| Transport | Models, plates, taxi colours, route signs | Country, city |
| Sky and light | Sun, cloud, shadows | Time of day, latitude, season |
| Small things | Sockets, appliances, packaging, advertising | Country, market |
| People | Clothing, gestures | Only as a weak hint |

### Chronolocation

From the length and direction of shadows you can estimate the time of day and season when the place is known; sun-position and shadow calculators help (G). Additional signs: archived weather data, events in the background, the state of vegetation, building work, advertising. A conclusion about time is always stated as a range.

### Tools (G)

| Task | Examples |
| --- | --- |
| Maps and imagery | Google Maps and Earth, Bing Maps, OpenStreetMap, regional maps |
| Street panoramas | Google Street View, Mapillary, regional services |
| Map data queries | Overpass Turbo (searching OSM objects by attributes) |
| Shadows and sun | Sun-position and shadow calculators |
| Relief | Apps that identify mountain peaks from a silhouette |
| Historical imagery | Historical layers in Google Earth, archive aerial photographs |

### Confidence assessment

| Level | Criterion |
| --- | --- |
| Confirmed | At least two independent unique features match and the camera orientation is established; the point on the map is reproducible |
| Probable | Several features match but none is unique; alternatives are implausible |
| Possible | The general picture fits but few matches |
| Not established | The versions could not be narrowed |

### Training

Bellingcat publishes regular geolocation challenges (S). They are an excellent way to train the eye; be sure to read participants' write-ups to see other routes to the answer.

## 4.4 Satellite imagery and remote sensing

Images from space let you check claims about events, find objects, assess changes on the ground, and confirm or refute eyewitness material. Access to commercial imagery can become sharply uneven.

### Sources

| Type | Examples | What it gives | Note |
| --- | --- | --- | --- |
| Free optical | Sentinel-2 (Copernicus programme), Landsat | Regular coverage, the general state of terrain, fires, crops | Resolution of the order of 10–30 m (G); not suitable for small objects |
| Radar | Sentinel-1 | Imaging through cloud and at night, surface change | Needs interpretation skill (G) |
| Thermal and fires | NASA fire data | Detecting fire sources | Thermal signals only (G) |
| Commercial high resolution | Planet, Vantor (formerly Maxar), Airbus, Satellogic | Detail down to individual objects | Paid; the access regime changes |
| Viewers | Web viewers of open data, Google Earth | Quick viewing and historical layers | The capture date is always needed |

### Access restrictions

Commercial providers can delay, restrict or withhold imagery of conflict regions, sometimes at a government's request. What applied in 2026 is in [updates/2026-11.md](../updates/2026-11.md) (not verified).

**What this means for practice.**

1. Do not rely on one provider; know the backups in advance.
2. Check which region it is: restrictions depend on the "area of interest".
3. Put an entry in the report: "imagery of the region on date X is unavailable for reason Y"; that is a gap, not the absence of an event.
4. Free Sentinel and Landsat remain available, but their resolution suits large-scale change, not individual objects.
5. Remember that restriction of access is itself information: analysts have used it as an indicator in other contexts (for example, retouched areas on Chinese maps became a lead for an investigation into camps in Xinjiang; S).

### Change analysis

1. Choose two images of one place with different dates; make sure they are comparable (angle, season, lighting).
2. Overlay and compare: new buildings, craters, cleared areas, vehicle tracks, vegetation changes.
3. Estimate the height of objects from shadows; estimate scale from the length of similar objects (G).
4. Document: sources, dates, resolution, imaging angle.

### Mistakes

- Taking the publication date in a viewer for the capture date.
- Confusing clouds, shadows and damage.
- Forgetting the different resolution of the images being compared.
- Not allowing that what is visible may be a decoy or a temporary object.

### Ethics

Detailed imagery makes it possible to plan strikes; that is exactly why providers introduce restrictions. When publishing analysis from a conflict zone, assess the risk to people and operations.
