# Review 6: Chapter 9 (Information, Media and Democracy)

## Verdict

Ready to print. I found nothing wrong, misquoted or legally risky enough to block printing. The 2026 material is consistent with the sources and current to late November 2026. That includes the Talarico deepfake and the Senate result, Brazil's run-off, the ChatGPT DSA designation, the Penske dismissal, the Pew digital-twin study, the Costello correction, the SynthID Detector launch, the Apple Reference Image launch and the xAI renaming. The worked arithmetic is correct. Four small precision fixes are listed below.

## MUST change before printing

None.

## SHOULD change

### S1. Brazil TSE ruling: what the 4-3 vote decided, and "stay online"
- Where: textbook/chapters/ch09.md:128
- Text now: "In September, however, the court ruled by four votes to three that the deepfake ban applies only to material that counts as electoral propaganda, and let an AI video of the jailed former president Jair Bolsonaro endorsing his son Flávio stay online [@conjur2026deepfake]."
- Problem: UNCLEAR. Reports of the 1 September 2026 ruling say the 4-3 split was on rejecting the fine sought against Flávio Bolsonaro, and that the deepfake definition passed 5-2. The reports describe the fine being rejected. None that I found says the court decided to let the video "stay online".
- Evidence: Congresso em Foco, 2 Sept 2026, https://www.congressoemfoco.com.br/noticia/121875/tse-rejeita-multa-a-flavio-bolsonaro-e-define-criterio-para-deepfake: "TSE rejeita multa a Flávio Bolsonaro e define critério para deepfake". The article says the fine decision was 4-3, and that the ban applies only when content is electoral propaganda. Digital Policy Alert event 43365 says the court "ruled ... that the deepfake ban applies only to content characterised as electoral propaganda".
- Change to: "In September, however, the court declined, by four votes to three, to fine Flávio Bolsonaro over an AI video of his jailed father, the former president Jair Bolsonaro, endorsing him, and held that the deepfake ban applies only to material that counts as electoral propaganda [@conjur2026deepfake]."

### S2. SpaceXSI: an announced name, not yet a settled brand
- Where: textbook/chapters/ch09.md:246
- Text now: "...here Grok's developer, which was renamed from xAI to SpaceXAI in July 2026 after its merger with SpaceX and has used the brand SpaceXSI since October, after Musk said on 4 October that the name would change [...]"
- Problem: UNCLEAR. The July rename to SpaceXAI is confirmed (Engadget). The SpaceXSI change was announced by Musk on 4 October. Secondary reports conflict on whether, and when, it was adopted. The sentence is also very long, and it puts two clauses about the AI Act and the UK offence in the middle of the company history.
- Evidence: Khaleej Times (Oct 2026) says Musk "gave no additional details about the change or a timeline". Engadget, July 2026: "xAI is now officially known as SpaceXAI".
- Change to: "...but it binds the provider of the generating system itself, as the UK's offence of supplying intimate-image generators now also does. Here that provider is Grok's developer. It was renamed from xAI to SpaceXAI in July 2026 after its merger with SpaceX, and on 4 October Musk said it would become SpaceXSI [@reuters2026concerns; @engadget2026xai; @frank2026why; @xai2026grok47]."

### S3. Code of Practice signatory counts: date them
- Where: textbook/chapters/ch09.md:233
- Text now: "By mid-November 2026 the Commission's list counted 103 signatories to the providers' section and 219 to the deployers'"
- Problem: UNSUPPORTED (dating). The Commission page that gives 103 and 219 (266 unique signatories) is dated 31 July 2026. Its own text speaks of "about 190" signatories at the end of July, and the list "is updated on an ongoing basis". I could not confirm that the figures were still those in mid-November.
- Evidence: https://digital-strategy.ec.europa.eu/en/news/strong-backing-code-practice-transparency-ai-generated-content (dated 31 July 2026): providers 103, deployers 219, unique 266.
- Change to: "The Commission's published list of signatories counted 103 for the providers' section and 219 for the deployers'" (or re-check the live list and state its date).

### S4. Hungary: who ran the "puppet" videos
- Where: textbook/chapters/ch09.md:126
- Text now: "...as the governing Fidesz party did before the parliamentary election in April 2026, for example in videos showing the opposition leader Péter Magyar as a puppet of Ukraine's president."
- Problem: UNCLEAR. AP attributed the Magyar-as-puppet ads to "a shadowy pro-government organization with Fidesz ties", not to the party itself. Political Capital's assessment of heavy AI use covers Fidesz's own Facebook videos.
- Evidence: AP (Feb 2026, via news4jax): ads "paid for by a shadowy pro-government organization with Fidesz ties, depict Magyar as a puppet of Zelenskyy". EDMO blog (Political Capital): Fidesz AI use went further than any other EU campaign.
- Change to: "...as the governing Fidesz party and allied groups did before the parliamentary election in April 2026, for example in videos showing the opposition leader Péter Magyar as a puppet of Ukraine's president."

## Could not verify

- The EBU/BBC study's "2,709 answers" (line 203). The EBU's public page says "more than 3,000 AI responses". The full report may give 2,709 as the core set. If it does not, use "more than 3,000".
- NewsGuard's "3,749 AI content farms" dated "June 2026" (line 209). The figure appears in the title of NewsGuard's report, but its tracking-centre page still shows 3,006, and I could not confirm the update date.
- That the SynthID partner list, "as updated on 29 October", includes Apple (line 59). At the 7 October launch, Apple support was described as forthcoming.
- Meta's exact August 2026 wording, "a near-standard component of influence operation tradecraft". The report exists (H2 2026, 27 August) and Axios says AI was used in "virtually every" network, but I did not see the quoted wording.
- CNN Brasil's summary of the TSE's 72-hour rule. Agarwal and Sen (2026), 39.8%. Kohli's "180 billion" (it appears in only one secondary source).

## Checked and confirmed

- The Biden robocall: FCC $6m forfeiture order of 26 Sept 2024; Kramer acquitted in June 2025; FCC TCPA declaratory ruling of Feb 2024.
- CETaS quotations. Meta's "less than 1%" and "only incremental" figures. Kapoor and Narayanan: 78 cases, 39 deceptive, seven times as many cheap fakes.
- Nightingale and Farid: 48.2% and 59.0%. Groh: 15,016 participants. Weber-Wulff: 14 tools.
- C2PA founders (Feb 2021). Pixel 10 Content Credentials (Sept 2025). Apple Reference Image on the iPhone 18 Pro (9 Sept 2026), with SynthID support planned.
- SynthID Detector made public in Oct 2026, with OpenAI, Nvidia and Kakao.
- Jovanović et al.: under $50, above 80%.
- Costello et al.: expression of concern of 11 June 2026, then the Science erratum of 22 Oct 2026, which rescinded it.
- Hackenburg, Salvi (64.4%, 81.2%, 26.0–160.7%), Lin and Goldstein figures.
- Pew digital twins (30 Sept 2026): Claude Opus 4.6, 12.4 points, 86% vs 45%, "far less politically diverse", "no current or future plans".
- Talarico: AI video of 20 Oct attributed to Storm-1516 by Graphika and Clemson; Talarico won on 3 Nov 2026.
- Brazil: run-off on 25 Oct 2026, won by Lula. Romania: annulment on 6 Dec 2024; Dan won in May 2025.
- ChatGPT designated a VLOSE on 31 Aug 2026. X fined €120m on 5 Dec 2025.
- CMA conduct requirement of June 2026 (publisher opt-out). Penske suit dismissed on 30 Sept 2026, not with prejudice; "an expectation is not an agreement".
- Code of Practice published on 10 June 2026. AI Act Art. 99(4): €15m or 3%. OSA: £18m or 10%.
- TAKE IT DOWN Act signed on 19 May 2025. Grok: CCDH estimate; Ofcom opened its investigation on 12 Jan 2026; EC proceedings opened on 26 Jan 2026; Ofcom update in Oct 2026.
- xAI renamed SpaceXAI in July 2026.
- International AI Safety Report quotation "documented but not yet widespread".
- OpenAI's October 2026 report: placing stories in established outlets reached more people.
- Arithmetic: base-rate example (990 / 10,990, so 91% of alarms are false); watermark z-test (SD 7.07; z = 4 at about 128 green tokens; p ≈ 3×10⁻⁵).
- Cross-references to Sections 2.8, 9.x, 11.4 and 13.6 and to Chapters 3, 7, 10 and 13 are correct.

## Tally

Claims checked: 78 / confirmed: 70 / wrong: 0 / outdated: 0 / imprecise (SHOULD): 4 / could not verify: 6
