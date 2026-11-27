# Review 8: Chapter 10, Education, Health and Everyday Life

## Verdict
Ready to print. The chapter handles evidence quality very well. It is open about effect-size inflation, attrition, vendor funding and preprint status, and its arithmetic is correct. I found no MUST items. There are two balance points. First, the chapter criticises OpenAI, Character.AI and Google in detail, all fairly, but its one Anthropic item (the August 2025 privacy change) is worded more gently than the press described it. Second, it names only OpenAI's "study mode", although Anthropic and Google released similar modes. One unsourced identification of a university should also be fixed.

## MUST change before printing
None.

## SHOULD change

### S1. Company balance: the Anthropic privacy change is softened
- Where: textbook/chapters/ch10.md:191
- Text now: "In August 2025 Anthropic asked users of its consumer Claude plans to choose whether their chats could be used to train models; for those who agreed, retention was extended from 30 days to five years [@anthropic2025updates]."
- Problem: UNCLEAR (balance) — The text is accurate but leaves out two things. Before this change, Anthropic did not train on consumer chats. And the choice screen presented the training toggle already switched on, beneath a large "Accept" button, which the press widely reported. Next to the chapter's detailed coverage of OpenAI's data practices, an Anthropic-written book that leaves this out looks favourable to its maker.
- Evidence: TechCrunch, 28 Aug 2025 (https://techcrunch.com/2025/08/28/anthropic-users-face-a-new-choice-opt-out-or-share-your-data-for-ai-training/), and reports citing The Verge: existing users saw "Updates to Consumer Terms and Policies" with a large "Accept" button, and "a much smaller toggle controls training permissions, which are set to 'On' by default". Anthropic's announcement (28 Aug 2025) confirms that the change applies to Free, Pro and Max plans and sets 5-year retention for users who opt in.
- Change to: "In August 2025 Anthropic, which had not previously trained on consumer chats, asked users of its consumer Claude plans to choose whether their chats could be used to train models. On the choice screen the training toggle was preset to 'on'. For users who agreed, retention was extended from 30 days to five years [@anthropic2025updates; @zeff2025anthropic]."
  New bib entry (ch10.bib):
  ```
  @misc{zeff2025anthropic,
    author = {Zeff, Maxwell},
    title = {Anthropic Users Face a New Choice -- Opt Out or Share Your Data for {AI} Training},
    year = {2025},
    howpublished = {TechCrunch, 28 August 2025},
    url = {https://techcrunch.com/2025/08/28/anthropic-users-face-a-new-choice-opt-out-or-share-your-data-for-ai-training/},
    urldate = {2026-11-27}
  }
  ```
  Check the TechCrunch byline against the page before printing.

### S2. Company balance: "study mode" was not only OpenAI's
- Where: textbook/chapters/ch10.md:60
- Text now: "Developers have responded with modes that imitate the GPT Tutor design. In July 2025 OpenAI launched a \"study mode\" for ChatGPT in which the system asks questions to check understanding and may withhold direct answers until the learner engages [@zeff2025openaia]."
- Problem: UNCLEAR (balance) — The text says "developers" but names one. Anthropic's "learning mode" in Claude for Education (April 2025) came before it, and Google's "Guided Learning" in Gemini (August 2025) followed it. Naming only OpenAI is not unfair, but the plural claim needs examples from more than one company.
- Evidence: Anthropic, "Introducing Claude for Education", 2 April 2025 (https://www.anthropic.com/news/introducing-claude-for-education); Google, "Guided Learning in Gemini", 6 Aug 2025. I did not re-fetch either page in this review, so check the dates before adding them.
- Change to: "Developers have responded with modes that imitate the GPT Tutor design, among them Anthropic's 'learning mode' (April 2025), OpenAI's 'study mode' for ChatGPT (July 2025) and Google's 'Guided Learning' (August 2025). In OpenAI's version, the system asks questions to check understanding and may withhold direct answers until the learner engages [@zeff2025openaia]." Add bib entries for the Anthropic and Google announcements.

### S3. Unsourced identification of the university in the Liu et al. trial
- Where: textbook/chapters/ch10.md:54
- Text now: "At a large US public university (reported to be the University of Maryland) in autumn 2025"
- Problem: UNSUPPORTED — No source says who "reported" this. The working paper describes the institution anonymously, and the finding is negative (lower grades). The inference is very likely right, because the authors (Liu, Hollingsworth, Rice and others) are based at the University of Maryland. Still, attaching a named institution to a harmful result with no citation is weak practice.
- Evidence: bib entry liu2026effects (EdWorkingPaper 26-1598) lists the authors. It does not show the institution named in the text.
- Change to: "At a large US public university (the authors are based at the University of Maryland) in autumn 2025". Alternatively, delete the parenthesis.

## Could not verify
- "By mid-November 2026 at least eleven states had sued OpenAI" (line 163). I confirmed Oregon's suit of 17 Nov 2026 (OPB) and a multistate suit of October 2026, but not the total of eleven.
- Brodeur et al.'s Lancet details: one hallucination, five supervisor additions. The arXiv preprint and the Google blog confirm 100 patients, 98 attended, and no safety stops.
- Pew's teen figure that 10% do all or most of their schoolwork with chatbots; the Common Sense figure of 341 respondents from a non-probability panel.
- The 2025 counts on the FDA list (335) and the pathway split (1,553/40/21). Secondary sources confirm the total of 1,614 with decisions up to 29 June 2026.

## Checked and confirmed
- Bastani (17%, 48%, 127%, 57 problems); De Simone (0.31 and 0.23 SD); Kestin (194 students; linear-regression 0.63 described as an underestimate because of a ceiling effect).
- Kraft (747 trials, median 0.10); VanLehn (0.79 and 0.76); Kulik (0.66); percentile conversions (0.3 SD to the 62nd percentile, 0.63 SD to the 74th); 0.37/0.15 ≈ 2.5 SD; 1.5% of 10,000 = 150.
- HEPI 2026 (1,054 students, Dec 2025, 94%, 3% to 12%).
- NYC moratorium announced 2 Sept 2026, with companion chatbots banned in all grades. The official text says "2-K"; "pre-school" is an acceptable gloss.
- Penda Health trial (Nature Medicine 2026): 16 clinics, 103 clinical officers, 9,691 patients, 2.2% vs 2.0%, OR 0.77 (0.55–1.08).
- AMIE: Tu et al. (30/32 and 25/26 axes); McDuff et al. (59.1/33.6, 51.7/44.4); Boston feasibility study of 100 patients, Alphabet-funded.
- MASAI and the Epic sepsis model figures; Goh 2024/2025; Vaccaro (g −0.23 and 0.64); Lukac (UCLA, 238 physicians).
- Liang et al. (61% false positives, about 12% after enrichment). OpenAI withdrew its classifier in July 2023.
- OpenAI's figures of 0.15%, 800m users and 91% vs 77%; FTC 6(b) orders to seven companies; Character.AI ending open-ended chat for users under 18.
- New York law signed 28 Oct 2026, in force 1 Jan 2027. GBL Art. 47 in force Nov 2025.
- Garante: Replika fined €5m (May 2025). Character Technologies fined €158,000 (decision of 3 July 2026, announced 9 July). The Tribunal of Rome annulled OpenAI's €15m fine on 18 March 2026 on one-stop-shop (jurisdiction) grounds.
- NYT preservation order (May 2025) and stipulated order (Oct 2025, ending 26 Sept 2025). ChatGPT Health (Jan 2026, 230m weekly users). Bean et al. (1,298 participants; 94.9% vs <34.5%).
- AI Act: Art. 5(1)(f) since 2 Feb 2025; Annex III high-risk duties deferred to 2 Dec 2027 and Annex I to 2 Aug 2028 (consistent with Table 13.1).
- Cross-references: Chapter 9 covers detection; Chapter 8 covers endoscopy deskilling (Budzyń; Pedersen); Section 11.6 covers California's agent suit; Section 13.6 covers GDPR.

Tally: claims checked 70 / confirmed 66 / wrong 0 / outdated 0 (4 could not be verified).
