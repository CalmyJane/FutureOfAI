# Whole-book consistency audit 2 — tickets assigned to chapters (verify before changing; some are judgement calls)

## ch01
- T-09: "nearly 40%… by late 2024" US adoption: bring up to date (Bick et al. reweighting: Aug 2024 39.4%→44.6%; Aug 2025 54.6%) or flag as superseded; consistent with ch08.
- T-15: "a model won a gold medal" → "gold-medal-level score" (IMO 2025).
- Undefined: BLEU (l.206, 215) — define in place.
- "His examples overlap with this chapter" (l.247) → rephrase.
- l.276 "A careful claim about 'AI' therefore says…" takes a position — fine, but keep it descriptive.
## ch02
- T-05: Table 2.1 caption "(Section 2.5)" → "(Sections 2.4–2.5)".
- "Two consequences follow." (l.53) → rewrite.
## ch03
- T-20: Golden Gate, superposition, Dallas→Texas, rhyme planning (l.326–328) told in full in ch12 §12.4 → cut ch03 to 1–2 sentences + "Section 12.4".
- T-19: keep RLHF reward-model mechanics and Constitutional AI here (ch12 will shorten).
## ch04
- T-07 HIGH: Astra. ch04 (l.104, 218) says "OpenAI's GPT-6 Astra, released in September 2026… ≥100,000 GB200" (Epoch dataset entry), while ch12 says in Aug 2026 OpenAI could not rule out that an unreleased model Astra reached Critical cyber level and paused training. Verify what Epoch's dataset and OpenAI/Fortune actually say (release status, name "GPT-6 Astra" vs "Astra", dates). Make ch04 state precisely what is known (e.g. "an Epoch AI dataset entry for a model it lists as GPT-6 Astra (September 2026)…"), avoid implying release if unverified, and cross-reference Section 12.7. Don't use it as strong evidence that scaling resumed unless the source supports it.
- T-10: compute stock "3.4× per year since 2022 (Epoch)" vs ch07/ch14 "about 3.3× (AI Index drawing on Epoch)": check both sources; state source with each or harmonise.
- T-11: GPT-4 cost $37m (Epoch, 2023 US$) vs ch07 ~$40m (Cottier): name source and dollar-year (ch04 Table 4.3 caption).
- T-12: GPT-4 forecast "at most 10,000× less compute" (l.43) vs "at most one-thousandth" (l.176): name the metric each time (loss vs HumanEval).
- T-18: keep Cottier data here (ch07 will reference).
- T-04: "already standard in post-training, where a strong model writes worked solutions that a smaller one learns from (Chapter 3)" — Chapter 3 doesn't describe distillation: drop the cross-reference or briefly explain distillation here with a source.
- Undefined before use: "SWE-bench Verified" (l.216 → one-clause gloss, "Chapter 5"), "GB200" (l.104 → gloss), "nats" (l.25 → define), "Arena" (l.185 → gloss).
## ch05
- T-06: add `{#tbl:05-01}`…`{#tbl:05-04}` ids to Table 5.1–5.4 captions.
- T-13: CaMeL "published in 2026" while a 2025 preprint cites it: say "first posted as a preprint in 2025 and published in 2026 (IEEE SaTML)".
- T-16: METR time-horizon passage (l.164) duplicates ch04 §4.7 → cut to two sentences + "Chapter 4".
- Box label "**Case:**" (l.213) → "**Case study:**".
- "Two features of this format shape everything that follows." (l.99); "The discussion here stays at the level of concepts and defences" (l.226) → rewrite/remove.
## ch06
- Undefined: "TPU" (l.31, 63) → one-clause gloss (Google's AI chip; Chapter 7).
## ch07
- T-17: 6ND/DeepSeek-V3 FLOP derivation at l.9 (and l.275) duplicates ch04 §4.1 → back-reference ("Section 4.1") keeping only the result.
- T-18: Cottier cost trend (l.177) duplicates ch04 → reference Section 4.4, keep only new material (Amodei, DeepSeek box).
- T-11: GPT-4 ~$40m (Cottier) — name source and dollar-year.
- T-10: compute stock 3.3× — state source (AI Index/Epoch) consistently with ch04.
- Undefined: "H800" at l.41/47 before explanation at l.108 → gloss at first use.
## ch08
- T-26: "The 2026 Digital Omnibus deferred…" (l.256) → add gloss ("the EU's 2026 amending regulation to the AI Act, Section 13.2").
- "Three further findings bear on the mechanism." (l.112) → rewrite.
## ch09
- T-03: "cross-attention layers (the mechanism described in Chapter 3)" (l.15) → "a variant of the attention mechanism described in Chapter 3, in which…".
- Signposts l.41, 69, 136, 164 ("Two further obstacles…", "Two further limits…", "Two later findings…", "Several features of these experiments limit…") → rewrite.
## ch10
- Undefined: "Hedges' g" (l.114) → define in place.
- "Three further findings sharpen the result." (l.47) → rewrite.
## ch11
- T-01: "Section 14.2 reviews how the two groups have fared…" (l.240) → "Sections 14.1–14.2".
- T-23: endoscopy deskilling numbers (l.189) duplicate ch08 §8.7 → back-reference.
- T-24: Grace et al. 5% median and 38–51% (l.227) also in ch14 → keep briefly or point to Section 14.2.
- T-14: XPT sample (88 superforecasters; 30/29 AI experts in Table 11.4) vs ch14's 89/80 — state that the table uses the subsets that answered these questions.
- "Three features stand out." (l.240); "Several considerations structure the weighing." (l.276) → rewrite.
## ch12
- T-07 HIGH: Astra (see ch04): cross-reference Section 4.4 where Epoch lists a "GPT-6 Astra" entry; make sure the two chapters are consistent and precise about what is verified.
- T-19: RLHF reward-model loss, σ(1) ≈ 73%, "100× fewer parameters" (l.17–25) and Constitutional AI (l.35) duplicate ch03 §3.5 → keep only the KL penalty, over-optimisation and new material here, back-reference Section 3.5 for the mechanics.
- "this chapter" in Figure 12.1 caption (l.51) → rephrase.
- Undefined: "nats" (l.31) → define or back-reference; "ExploitGym" (l.80) → explain in one clause.
## ch13
- T-02: "$285.9 billion in the US against $5.9 billion in the UK (Section 7.7)" — 7.7 doesn't give the UK figure: cite the AI Index directly (remove the section reference or point to it only for the US–China comparison).
## ch14
- T-08: Danish null effects "ruled out effects larger than 1% through 2024" → use the March 2026 revision (">2%") consistent with ch08.
- T-09: "nearly 40%" adoption (l.161 and Table 14.4) → update as in ch01/ch08.
- T-10: compute stock figure — align with ch04/ch07 (state source).
- T-16: METR caveats (l.94, 109) repeat kwa2026clarifying caveats from ch04/ch05 → keep extrapolation, drop the repeated caveat list (back-reference Section 4.7).
- T-21: early predictions (l.13: Dartmouth, Simon 1960, Lighthill quotes) duplicate ch01 → "Chapter 1 traces…" with one sentence.
- T-22: A2A launch text (l.241) copies ch05 → shorten to a back-reference.
- T-23: endoscopy study (l.233) → back-reference to Section 8.7, keep only Pedersen trial.
- T-14: XPT sample sizes: clarify subsets as in ch11.
- Undefined: "FrontierMath" (Table 14.1) → gloss in caption or text.
- "Three caveats limit what the table shows." (l.39); "Three results matter for anyone using the numbers." (l.47) → rewrite.
## Global
- T-25: AUC defined four times (ch02, ch09, ch10, ch12): keep the full definition at first use (ch02 or ch09 as appropriate), elsewhere one clause + back-reference.
