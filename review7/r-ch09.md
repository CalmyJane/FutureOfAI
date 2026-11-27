# Review 7: Chapter 9 (Information, Media and Democracy)

## Verdict
Ready to print once two small SHOULD fixes are made. I found nothing wrong, misquoted or legally risky. The 2026 material is accurate against its sources: Meta's threat report quotes, the OpenAI October report, Pew's synthetic-sample study, the Talarico items, the Brazil and Texas results, Penske, the CMA, TAKE IT DOWN enforcement and the EU Code of Practice signatories. One statement about Apple's SynthID support became out of date in late October 2026. One attribution sentence about Storm-1516 is slightly looser than its sources.

## MUST change before printing
None.

## SHOULD change

### S1. Apple's SynthID support has shipped
- Where: textbook/chapters/ch09.md:85
- Text now: "The announcement did not mention C2PA, but said Apple would add support for Google's SynthID watermark in a later software update [@apple2026apple]."
- Problem: OUTDATED. Apple shipped SynthID marking in iOS 27.2 at the end of October 2026. Image Playground images and some Apple Intelligence photo edits now carry the watermark. The book says it is current to late November 2026, so the future tense is a month out of date.
- Evidence: Apple Newsroom, 9 Sept 2026, footnote 6: "SynthID will be available in a software update later this year". MacRumors, 26 Oct 2026, "iPhone AI Images and Edits Now Have a Hidden Watermark" (https://macrumors.com/2026/10/26/iphone-synthid-watermarks): images made with Image Playground and some photos edited with Apple Intelligence "now include a SynthID watermark" in iOS 27.2. 9to5Mac, 28 Oct 2026 (https://9to5mac.com/2026/10/28/ios-27-2-just-upgraded-apple-photos-in-two-ways-heres-whats-new/).
- Change to: "The announcement did not mention C2PA, but said Apple would support Google's SynthID watermark; an update in late October 2026 began adding it to images made or substantially edited with Apple's own AI tools [@apple2026apple; @macrumors2026iphone]."
  New bib entry (ch09.bib):
  ```
  @misc{macrumors2026iphone,
    author = {{MacRumors}},
    title = {{iPhone} {AI} Images and Edits Now Have a Hidden Watermark},
    year = {2026},
    howpublished = {MacRumors, 26 October 2026 (on iOS 27.2)},
    url = {https://macrumors.com/2026/10/26/iphone-synthid-watermarks},
    urldate = {2026-11-27}
  }
  ```
  If you would rather not add a source this late, a lighter fix works: "said Apple would add support for Google's SynthID watermark, which it began doing in a software update in late October 2026."

### S2. Storm-1516 attribution: say who found what
- Where: textbook/chapters/ch09.md:128
- Text now: "NewsGuard reported that the videos showed many signs of AI generation, and researchers at Clemson University and the analytics firm Graphika linked them to Storm-1516, a Russian influence network [@breach2026russian; @politifact2026russian]."
- Problem: UNCLEAR (attribution of a foreign state operation). The two sources do not have Clemson and Graphika making the same finding.
  - PolitiFact quotes Clemson's Darren Linvill, who says the video "is the work of Storm-1516".
  - In PolitiFact, Graphika says only that the posting account "very likely" impersonated a real Facebook user.
  - FDD says Graphika "had previously tied those amplifiers to Storm-1516". That refers to the accounts that amplified the post, not to the video itself.
  - FDD also says NewsGuard found that "the format and the amplification pattern of this operation match Storm-1516".
  The current sentence slightly overstates Graphika's part.
- Evidence: PolitiFact, 22 Oct 2026 (bib URL): Linvill, "the video is the work of Storm-1516". FDD, 26 Oct 2026 (bib URL): Graphika "had previously tied those amplifiers to Storm-1516, a Russian influence network"; NewsGuard: "both the format and the amplification pattern of this operation match Storm-1516."
- Change to: "NewsGuard reported that the videos showed many signs of AI generation and matched the pattern of Storm-1516, a Russian influence network; a Clemson University researcher attributed them to that network, and the analytics firm Graphika had earlier tied the accounts amplifying them to it [@breach2026russian; @politifact2026russian]."

### S3. Code of Practice signatories: say which section the companies signed
- Where: textbook/chapters/ch09.md:233
- Text now: "The Commission's published list of signatories counted 103 for the providers' section and 219 for the deployers', among them Anthropic, Google, Meta, Microsoft and OpenAI [@europeancommission2026strong]."
- Problem: UNCLEAR. The five companies appear only in the providers' section, not the deployers'. "Among them", placed straight after "the deployers'", reads as if they had signed that section.
- Evidence: Commission news item, last updated 18 Nov 2026 (bib URL): Section 1 (providers) has 103 signatories, Section 2 (deployers) has 219, and there are 266 unique signatories. Anthropic, Google, Meta, Microsoft and OpenAI appear in the Section 1 list.
- Change to: "The Commission's published list of signatories counted 103 for the providers' section, among them Anthropic, Google, Meta, Microsoft and OpenAI, and 219 for the deployers' [@europeancommission2026strong]."

## Could not verify
- Meta's figure that AI content was "less than 1%" of fact-checked election misinformation (2024). This is a long-standing figure that I did not recheck.
- Hungary (EDMO/Political Capital) survey figure of 52%, and the wording of the Colombia EU EOM final report. I did not fetch either source.
- Pew digital twins: 46% versus 34% Trump approval (pew2026can). I did not open that page. Pew's companion report was otherwise confirmed.

## Checked and confirmed
- Meta H2 2026 threat report (PDF copy): "from an occasional tactic employed by the most resourced actors to a near-standard component of influence operation tradecraft"; "behavioral detection approaches remain effective against AI-enabled influence operations".
- OpenAI, 8 Oct 2026: Russia-origin "Dark Clark" and Iran-origin "Bogus Bylines". AI made workflows easier, and operations that land content in real outlets reach the most people.
- International AI Safety Report 2026: real-world use for influence/manipulation "is documented but not yet widespread".
- Google SynthID post, 7 Oct 2026, updated 29 Oct: partners "OpenAI, NVIDIA, Kakao, and Apple"; "over 180 billion images and videos"; detector covers image, video and audio.
- Apple iPhone 18 Pro release, 9 Sept 2026: opt-in Reference mode, signed sensor data, "unalterable reference image", no mention of C2PA, SynthID promised.
- Pew, 30 Sept 2026: Claude Opus 4.6 was the best model with 12.4 points average error; "far less politically diverse"; 86% versus 45% on billionaires; "no current or future plans"; panel restricted to 2025 typology respondents.
- Reuters via Express Tribune, Mar 2026: NRSC Talarico ad labelled "AI-generated" in small type; Loudoun County GOP; Collins campaign in Georgia; no federal regulation; 28 states (Public Citizen).
- Talarico deepfake posted 20 Oct 2026 on X; the real man denied it was him.
- Talarico won the Texas Senate seat on 3 Nov 2026. Lula won the 25 Oct 2026 run-off against Flávio Bolsonaro.
- Penske v. Google: dismissed 30 Sept 2026 by Judge Mehta, "an expectation is not an agreement", without prejudice.
- CMA, 3 June 2026: a conduct requirement covering opt-outs from AI features and attribution with clear links.
- TAKE IT DOWN Act: first conviction 9 Apr 2026 (an Ohio man); FTC enforcement from 19 May 2026.
- Ofcom/Grok: investigation opened 12 Jan 2026 and narrowed on 14 Oct 2026; no provisional finding by late November.
- Arithmetic:
  - base-rate example: 990 true and 10,000 false alarms, so 91% of alarms are false;
  - watermark z-test: SD of 7.07, threshold of about 128.3 green tokens, one-sided P(z > 4) ≈ 3.2 × 10⁻⁵.
- Cross-references to Section 2.8 (AUC), Chapter 3 (attention), Chapter 7 (open weights), Section 11.4 (fraud), Section 13.6 and Chapter 10 (detector bias) all resolve. Chapter 11 points back to Section 9.8 for Grok, which is consistent.

## Tally
Claims checked: 48 / confirmed: 45 / wrong: 0 / outdated: 1 (plus 2 unclear wordings)
