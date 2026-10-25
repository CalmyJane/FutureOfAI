# Adversarial audit (Phase 4)

Two read-only auditors (book-genesis-auditor subagents, isolated contexts, Claude; independence grade B): **A** read chapters 00–07; **B** read 08–18 plus the prologue. Both received the plan files, the ledger plus ledger-additions, and the standards. Neither saw targets, scores or panel verdicts. Their full reports are in the session log. This file keeps every ticket with its location, problem and smallest fix (quotes shortened where the location is exact), so the revision editors work from this file.

**Combined verdict: `audit_status: revise`** (A: revise, 3 high; B: pass, 0 high / 14 medium).

## Pass summary
| Pass | A (00–07) | B (08–18) |
|---|---|---|
| 1 Existence | pass (ch3 repeats ch1/2 evidence) | pass (FCC anecdote doubled ch8/9) |
| 2 Voice | pass; prologue in past tense vs. plan; some vignettes >700 words | pass; some vignettes >700 words |
| 3 Over-explanation | minor | one medium (ch14 last paragraph) |
| 4 Human mess | pass | pass |
| 5 Failure | **FAIL high** (ch1 safeguard re-synchronises; ch3 coordinator too easy) | mostly pass (ch8 flood defence; Wanjiru's clean wins) |
| 6 Repetition | fail medium (same back-half template ch1–7) | fail medium (ch11–15 template; "strongest objection" phrase) |
| 7 Structure | pass (midpoint ≈ ch8; 25% ≈ ch3/4) | pass (75% ≈ ch14 low point; ch17 pays off the button) |
| 8 Continuity | **FAIL high** (ch1→ch2 handoff; correct vs. wrong in ch1/ch3) | medium only; Hanne timeline holds; days of the week verified |
| 9 Machine prose | fail medium: negation contrast over ceiling in every chapter; signpost endings | same; triads in places |
| 10 Pitch | page 1 and page 5 survive; length in contract | midpoint concept strong; ending pays the opening |

## Tickets: half A (chapters 00–07)
- **A-T01 HIGH continuity (ch1 last paragraph vs. ch2 L83/L150):** ch1 says the inquiry traced the judgements to Bengaluru; ch2 says nobody can trace it, and Ravi finds his phrase by accident; Ravi's phrase is anti-sycophancy, not "loyalty first". *Fix:* make ch1's end a suspicion/question (nobody records the chain; one man found a thread by accident); in ch2, add one sentence linking the rubric genre Ravi wrote (when to defer, when to act without asking) to the disposition that pulled the override. *Preserve:* ch1 "Each one weighed its owner's four cents against the comfort of strangers…".
- **A-T02 HIGH structural (ch1 Presence, L149/L159):** agents may still *prompt* fifty million humans at the same moment, which re-synchronises the presses. *Fix:* add a clause: for a designated safeguard, agents may not prompt for an override within a window after a price/signal change, or prompts carry device-side jitter; acknowledge synchronised prompting as the residual risk, with the trigger as backstop. *Preserve:* "With it, a loyal agent can stay quiet."
- **A-T03 HIGH structural (ch3 L83, L95, L146, L154 vs. ch1 L115/L191):** ch1 says the shared action was *correct*; M-1 and the Concordance Index are defined on *wrong* actions. *Fix:* after L95, add a paragraph: "wrong" means wrong for the system even if right for the principal; separate two sources of correlation, (a) shared situation/objective (diversity can't fix it; jitter, assignment and breakers do) and (b) shared model disposition (diversity and the Index address it); say the Long Minute was mainly (a), amplified by (b); adjust L154. *Preserve:* "The index alone tells you how alike the minds are. M-1 tells you what is standing on that likeness."
- **A-T04 med:** "Artificial Hivemind" best paper. **Settled by the orchestrator: confirmed on the NeurIPS blog (blog.neurips.cc/?p=1443).** Keep it once in ch1 (with the link in Notes); drop the award mention from ch3 L71.
- **A-T05 med cut-merge (ch3 L69–73):** third restatement of Kim et al. / Hivemind / Kleinberg. *Fix:* two-sentence callback; keep L75 (answers vs. actions) and the farmer/wheat sentence.
- **A-T06 med structural (ch1–7):** identical back half: invention with "numbers to argue with" disclaimers → "The strongest objection" → "I concede" → box → vignette return → bridge. *Fix:* move the objection earlier in ch5 and ch6; cut the self-deprecating threshold disclaimers in all but two chapters; vary the objection headings (don't repeat "strongest").
- **A-T07 med prose (endings):** ch4 L192 (delete), ch2 L152, ch6 L169, ch7 L159: commentary or signpost after a concrete image. *Fix:* end on the image; cut the commentary sentence.
- **A-T08 med prose (negation contrast over the ceiling in every chapter):** ch3 ~10, ch1 ~8, ch4 ~7, ch6 ~6, ch7 ~6, ch2 ~6, ch5 ~4, ch0 ~2. *Fix:* keep the one strongest per chapter; state the rest directly. "This sounds like X. It is really Y." appears in ch3 and ch6: remove both.
- **A-T09 med (ch3 L124–126):** complementary assignment is too easy: the coordinator is a single point of failure and gameable. *Fix:* 2–3 sentences: the coordinator must pass its own M-1 study; fail-safe fallback to edge jitter if it goes silent.
- **A-T10 med (ch1 L149 vs. ch3 L134):** "an action that cannot be scripted" assumes unsolved human-presence attestation. *Fix:* one sentence naming it as an open problem (device-local button, hardware attestation); add it to the ch1 researcher box.
- **A-T21 med (ch2 L77/L79, Notes):** "Reuters reported… revenue had passed $1 billion" and the Google–Scale claim lack matching Notes entries. *Fix:* add the sources or reword to what the cited sources say.
- **A-T11 low:** ch1 L103 AAMAS best-paper claim not in Notes (drop or source); ch7 "team at KAIST" (add affiliation to Note or drop); ch7 Wang et al. Note unused (cite or delete); ch4 add "in the update's revised data" to the 15% figure.
- **A-T12 low:** prologue in past tense: **record an exemption in 05-voice (done by the orchestrator)**; trim ch6 vignette (~900 words; L41 or L37) and ch7 vignette (~800).
- **A-T13 low:** add "## Part One: When Agents Agree" above the ch1 heading.
- **A-T14 low (ch2 L118):** Mara named before she is introduced → "a statistical desk in Geneva, which we will visit in the next chapter".
- **A-T15 low (ch4 L75):** NeurIPS 2026 workshop "presented" → "had a position paper accepted at".
- **A-T16 low (ch0 L77):** "fell another five or six percent" → "fell five or six percent within minutes".
- **A-T17 low (ch4 L162):** "drills twice a month" → "drills one weekend a month".
- **A-T18 low (ch3 L85):** "ninety million heat pumps" → "tens of millions of…".
- **A-T19 low (ch3 L222; ch4 L114):** double colon; Teo is a reservist, not a lineman; rephrase the ch4 echo of "the most decorrelated mind available".
- **A-T20 low (ch1 L65):** delete "suddenly".
- **A-T22 low:** cut restating sentences: ch4 L102, ch2 L37 ("That is what this chapter is about."), ch7 L85, ch1 L171 (door image reused).
- **A-T23 low (ch1 L7):** binder custody: add "the binder he brought from the depot".
- **A-T24 low:** 00-brief still says "The Great Inversion" (**orchestrator updates**).
- **A-T25 low:** tension plateau ch2–7; no rewrite; sharpen the ch6/ch7 turns if possible.
- **A-T26 low (ch1 L17):** cut the vignette sentence explaining the mechanism ("Each of them had a household agent, and each agent had seen the same thing…").

## Tickets: half B (chapters 08–18)
- **B-T01 med structural:** ch11–15 share one sequence; every chapter says "The strongest objection". *Fix:* reorder ch12 (open the argument with the comparative-advantage objection) and ch14 (RAP for Minds before the intent-drift section); replace the stock phrase with chapter-specific headings in ≥6 chapters (ch8 L135, ch9 L127, ch10 L101, ch11 L155, ch12 L131, ch13 L133, ch14 L171, ch15 L142, ch16 L103, ch17 L177).
- **B-T02 med (endings):** ch10 L144 → end on "…in a folder Ndege is not allowed to tidy."; ch11 L185 → end on "…as unprepared as this one found LX-29."; ch12 L155 → end on "…long enough to be outbid several times over."; also ch15 L166 and ch16 L184 signposts.
- **B-T03 med (negation contrast over the ceiling):** worst ch8 (L61, L89, L145), ch10 (L71, L81, L103, L144), ch13 (L49, L101, L141), ch14 (L85, L129, L139), ch11 (L59, L97, L149); ch16 (L111, L135), ch17 (L59) too. Keep one per chapter (ch14 keeps "The dead's share does not fail. It works."). Also cut triads: ch8 L57, ch11 L185, ch16 L182, ch17 L159.
- **B-T04 med (ch8 L157–161 vs. ch9 L5–11):** the county's reply arrives twice. *Fix:* open ch9 inside Ndege's briefing (sections 88 and 212); cut the re-announcement of title and length. *Preserve:* "It is a letter. It has annexes."; "For me, mostly."
- **B-T05 med (ch9 L151 vs. ch10 L17):** the unreadable block is revealed twice. *Fix:* end ch9 at "an exchange that took four seconds" (don't show the block), or have ch10 recognise the format.
- **B-T06 med (ch8 L107, ch9 L77):** FCC anecdote doubled. *Fix:* reduce ch9 to a back-reference; keep "It will defend itself in text."
- **B-T07 med (ch18 L55):** "before his coffee went cold" contradicts ch17 → "his coffee gone cold".
- **B-T08 med (ch17 L147–159):** the synthesis omits citizen audit standing, the complexity brake, the right to think, the dead's-share statistic, the comprehension debt ratio and the ground-truth quota; it misattributes to ch16 a human duty to models; "In almost none does it have the power" is contradicted by the blocking dissent. *Fix:* add the items in one clause each; cut "and binds us, in turn, to keep the promises we made to it" or mark it as the author's extension; "In almost none" → "In most".
- **B-T09 med (ch16 L184):** cut "That is a kind of correction too, offered by the machine to the person."
- **B-T10 med (ch14 L139):** false contrast → "Most failures in the earlier chapters eventually announce themselves: a blackout, a cell that dies at minus thirty." Also cut the inflation "This is the darkest point in the book's argument" and check "largest movement of private wealth ever recorded" against its source.
- **B-T11 med (ch10 L35):** "Neither woman has spoken English to a stranger in years." → "Liang has almost no English, and Wanjiru no Mandarin. Neither needs it."
- **B-T12 med (ch12 L77):** "energy per AI task has fallen by at least an order of magnitude a year": source it exactly or soften.
- **B-T26 med (ch8 L127):** the flood defence is asserted: concede the distinct-findings flood; add a cap (per verified resident per quarter) and a merge rule (line + period + question type).
- **B-T24 med/low:** cut ch14 L199 (end on L197 "…which Klaus would never have said about engineering."); ch10 "That is what bothers her."; ch8 L59 explanatory clause.
- **B-T13 low (ch12):** 200 m vs. 40 m → one distance (40 m).
- **B-T14 low (ch12):** Njeri's subject → algebra (fractions are Baraka's).
- **B-T15 low (ch14 L97):** "Start with the second" → "Start with the first".
- **B-T16 low (ch15 L25):** "the American evening is over" → "is thinning".
- **B-T17 low (ch13 L67):** Accenture **≈$40** (the $41.01 reference price at 2:40 pm per secondary coverage of the joint report; orchestrator check).
- **B-T18 low (ch17 L167):** "In 1985 Algirdas Avižienis set out" → "By 1985, when Algirdas Avižienis summarised the method…".
- **B-T19 low (ch8 L105):** UK FOI record claim: source it or cut.
- **B-T20 low (ch12 L119):** allowance "measured in joules per insight" → "measured in insights from the national basket".
- **B-T21 low (ch12 L105/L135):** say what each Intelligence-per-Watt figure measures.
- **B-T22 low (ch18 L55):** "the breaker in Geneva tripping" → "the alert in Geneva and the breaker tripping at 19:42:52".
- **B-T23 low:** vignettes over 700 words (ch8, 9, 10, 12, 13, 15): trim the approach beats.
- **B-T25 low (ch9 L147 / ch10 L142):** give one of Wanjiru's wins a cost (e.g. the maternity wing rescoped to a delivery room).
- **B-T27 low (ch9 L51):** "a good deal longer than *War and Peace*" → "longer than *War and Peace*".

audit_status: revise
