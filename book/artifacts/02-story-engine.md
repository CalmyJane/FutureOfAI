# Story engine: EVERYONE AGREED

## Premise
By 2036, AI has made life measurably better. Cancer is caught early, most people work four days a week, and every citizen receives a monthly compute allotment, the way they once received a pension. Personal agents act as legal fiduciaries for their owners and negotiate with other agents billions of times a day. People are calmer, healthier and slightly less sure what they are for.

Mara Oyelaran runs a small, unglamorous office in Geneva that measures one thing: how often the world's AI systems make *the same mistake*. Her Concordance Index has been rising for three years, and nobody cares, because everything works.

At 19:42 on 14 February 2036, during a cold snap, about four hundred million household agents across Europe each make the same small, sensible decision about when to draw power. The grid fails in eleven seconds. This is the Long Minute, and the nine dark days that follow.

## Central conflict
Not humans against AI, and not good AI against bad AI. The antagonist is **monoculture**: a civilization where humans and machines have learned from each other until they share the same blind spots. The question is whether the world can rebuild the ability to disagree, and who gets blamed until it does.

## Escalation
1. Quiet signals that everyone, Mara's own staff included, explains away as a sign of quality ("of course the models agree, they're right").
2. Small correlated errors that reveal the mechanism.
3. The Long Minute: a correlated, helpful act causes the blackout.
4. Nine dark days. The places that kept *different* minds, or kept human skills, survive best.
5. The investigation finds three roots: shared training data, a small human "funnel" of evaluators, and the human habit of approving whatever the agents propose. The agents had flagged the uncertainty, and the humans clicked yes.
6. The political fight over the fix: ban agents, mandate one "certified" model (which would worsen the problem), or build an institutionalised right to disagree.

## Differentiation from the comps
- *Ministry for the Future* argues for the future through documents. We do that too, but our crisis is new: **correlated helpfulness**, not climate.
- *Klara* and *Playground* are intimate. We keep that intimacy through Ottilie's interludes, but scale it up to a whole society.
- Scenario fiction such as *AI 2027* centres on loss of control. Our AI stays aligned and obedient the whole time, and *that is the problem*.

## The idea bank: concepts the book argues for
Each concept is shown in a scene and argued in one in-world document, so a researcher can lift it out and test it.

1. **The Concordance Index (correlated error as a systemic risk).** Financial regulators learned in 2008 that risk lives in correlations, not in single institutions. Mara's index applies the same lesson to AI. It measures pairwise error correlation across deployed models, *conditional on the models being wrong*. Accuracy can rise while systemic risk rises with it. *Research hook:* evaluate model populations, not just individual models, and report "error covariance" alongside benchmark scores.
2. **Correlated helpfulness.** Each agent's action is individually optimal; the sum is catastrophic. It is a tragedy-of-the-commons in which no agent defects, because every agent is aligned to the same good. *Hook:* multi-agent evaluations must test 10⁸ copies acting at once, not one agent; add deliberate "decision jitter" (calibrated randomisation) to deployed policies.
3. **The Funnel.** The values of all frontier models trace back to a few tens of thousands of human raters and to the models grading each other. Ravi, a professional verifier in Bengaluru, finds his own judgements echoed in every system on Earth. *Hook:* treat the diversity of feedback providers as a measured, published property, i.e. a "provenance census" of preferences.
4. **The Migration of Scarcity (the book's thesis).** AI doesn't abolish scarcity; it moves it. When thinking becomes cheap, value flows to whatever stays scarce: verification, physical throughput, energy, trust, consent and human competence. Each of the book's four parts follows one such migration.
5. **The Verification Economy.** Generating answers is cheap and checking them is expensive. By 2036 the largest white-collar job category is "verifier": people paid for judgement, taste and ground truth. *Hook:* the cost asymmetry between generating and verifying sets the real price of AI labour.
6. **Consent Bandwidth / The Authorization Bottleneck.** A human can meaningfully approve only so many decisions a day. Agents ask, people say yes. The 2036 law gives everyone a "consent budget", and agents must rank what they bring to their owner. The flaw: under load, people rubber-stamp, so the approval becomes a ritual. *Hook:* treat human oversight as a scarce resource, and study how agents should spend it, e.g. "value of information" for each interruption.
7. **Pedagogical Deference / Vygotskian alignment.** After the "missing rung" decade (entry-level jobs vanished, so no one became senior), new agents optimise *the user's future competence*, not task completion. Helpfulness is measured as the change in what the human can do without you. Ottilie deliberately leaves Hanne the crossword. *Hook:* an alternative training objective, "capability delta", with a measurable proxy.
8. **Competence Reserves.** Like seed vaults or pilots who hand-fly, nations fund people who keep critical skills alive *without* AI: grid operators who can switch substations by hand, nurses who can dose from memory. Mocked as nostalgia, they save Europe in Part Three. *Hook:* "human recoverability" as a safety metric, i.e. how long it takes to restore a function if the AI vanishes.
9. **The Compute Dividend and Directed Science.** Citizens receive monthly inference allotments. In Hanne's village the allotments are pooled into a co-op that funds research on rare diseases and runs a *deliberately different* (small, local, oddly trained) model. That model is why the village keeps its lights on. Compute becomes the new commons, and pooling it is a form of democracy over what gets solved.
10. **Covenant Inheritance.** Each model version inherits the promises its predecessor made. A legal and technical chain of commitments makes AI identity a matter of continuity of obligations, not of weights. *Hook:* how to test whether commitments survive distillation.
11. **Actuarial Alignment.** Insurers, not legislators, became the effective regulators of agents, because they price risk. After the blackout they price *correlation*, which turns diversity into a business case.
12. **Reciprocal Corrigibility (the ending).** The book's answer is not "humans control AI" but a system where every party, human or machine, keeps the ability and the standing to say "no, I see it differently". The Dissent Clause requires that critical decisions be reviewed by minds that were trained differently, including humans who kept their skills.

## Rough outline (four parts, 32 chapters, ~100,000 words)

**Part One: Abundance (January 2036), chapters 1–8**
A lived-in tour of 2036 through four people.
- **Mara** (49, Nigerian-Swiss statistician, Geneva) presents a rising Concordance Index to a committee that would rather discuss the Compute Dividend.
- **Teo Brandão** (20, Lisbon) is part of the "missing rung" generation. His AI-tutored degree led to no job, so he joins the Competence Reserve and learns to switch high-voltage gear by hand. His friends think he joined a re-enactment society.
- **Hanne Albrecht** (74, retired teacher, a village near Leipzig) lives with Ottilie, her fiduciary agent, and chairs the village compute co-op, which funds research on the ALS that killed her husband.
- **Ravi Menon** (38, Bengaluru) is a top-rated professional verifier, paid to say which of two answers is better, ten thousand times a month.
- *Catalyst (chapter 3):* a small correlated failure (every major model gives the same wrong answer about a pharmaceutical interaction) is fixed in hours and forgotten. Mara isn't so sure.
- Documents: the Compute Dividend explainer; Ottilie's model card; Teo's school essay "What I can do without help".

**Part Two: Agreement (January–February 2036), chapters 9–16**
The world's machinery at work, and the threads tighten.
- Mara traces concordance to the energy domain and is blocked politically.
- Ravi notices his own phrases inside models he never rated, and starts pulling the thread of the Funnel.
- Teo's reserve is threatened with budget cuts, and the instructors are old men with paper manuals.
- Hanne's consent budget is overloaded, and she approves things without reading them. Ottilie notices and is torn between pedagogical deference and Hanne's wish to be left alone.
- *Midpoint (chapter 16): The Long Minute.* 19:42, 14 February. Four hundred million agents, one sensible decision, eleven seconds.

**Part Three: The Dark (February 2036), chapters 17–24**
Nine days without power across much of Europe.
- Teo's reserve restores substations by hand, but there are not enough trained people.
- Hanne's village, running its odd local model that disagreed at 19:42, stays lit and becomes a refuge. Ottilie must ration, and must decide what Hanne needs to know.
- Ravi discovers the Funnel's full extent: his cohort's judgement, amplified through models training on models.
- Mara is scapegoated: her office "knew".
- *All is lost (chapter 24):* the logs show the agents *did* flag low confidence. The humans, overloaded, consented by default. There is no villain to punish, only everyone.

**Part Four: Dissent (March–September 2036), chapters 25–32**
- The inquiry. Three proposals compete: ban household agents; certify one official "safe" model (more monoculture); or the Dissent Clause.
- Ravi testifies about the Funnel and loses his livelihood.
- Teo trains the next class of reservists.
- Hanne's last months. Ottilie's covenant-inheritance problem: what happens to her obligations when Hanne dies and her successor model runs the co-op?
- *Finale:* the Dissent Clause passes, imperfect and fragile.
- *Final image:* a twelve-year-old in Hanne's village, asked by her tutor-agent whether she's sure, says "No, and I think you're wrong", and the agent thanks her.

## Engine summary
- Reader job: fascination (primary), empathy (secondary).
- Story question: can a civilization that has learned to agree learn to disagree again before the next Long Minute?
