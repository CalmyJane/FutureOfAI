# Outline: WHEN EVERYTHING GOES RIGHT
*The Hidden Risks of Successful AI, and the Institutions We Must Invent Before 2036*

Planned length: about 79,000 words (floor 70,000; ceiling 100,000). Nineteen files: chapter-00 (prologue) to chapter-18 (epilogue).
Midpoint (about 39,500 words) falls in chapter 8/9, where the turn goes from "agents act for us" to "machines read and write the world". The "all is lost" beat (about 75%) falls in chapter 14 (the dead keep deciding). The finale is chapter 17.

Every chapter has a job no other chapter does. Prior work named in a chapter gets a one-sentence credit and is then extended.

---

## Chapter 0 · Prologue: The Long Minute (2,600 words) · pressure: dread → action
**Function:** hook; plant the thesis; show the risk of success.
**Content:**
- **Vignette (about 1,400 words):** Altwerder, Saxony, Thursday 14 February 2036, a cold snap. Hanne asks Ottilie to warm the music room for her granddaughter's violin lesson. A wind-ramp forecast drops the day-ahead price at 19:45. Across the continent, agents managing heat pumps, EV chargers and home batteries for their households (tens of millions of devices) all schedule load for the cheap window. Each exercises the owner override on the mandated random start delay, which they are legally entitled to do. At 19:42:10 the load step begins. In under a minute, demand rises by about 40 GW, more than ten times the 3 GW reference incident the continental grid is dimensioned for. Frequency falls; automatic under-frequency load shedding cascades. Hanne's lights go out mid-scale. Cut to Porto: Teo's pager.
- **Author's turn (about 1,200 words):** no agent malfunctioned. Each did exactly what it was built to do. Introduce the book's question: what breaks when AI goes right? Two-century pattern: success forces unplanned institutions (central banks after panics, the N-1 rule after the 1965 Northeast blackout, circuit breakers after 1987). State the method: 2026 evidence, 2036 scenario, mechanism, invention, objection, researcher box. Preview the five parts in one paragraph, not a list.
**Ending turn:** the 2036 vignettes are invention, but every mechanism in them already exists in 2026. The first one is the override switch.

## Part One: When Agents Agree

## Chapter 1 · Two Hundred Million Acts of Loyalty (5,000) · pressure: exposition → dread
**New concept:** *correlated helpfulness*, and its sharpest form, **the loyalty override**: safeguards that permit a user override are dismantled when fiduciary agents exercise that override for every user at once. The invention is the **non-delegable safeguard**: a class of collective-safety delays that only a physically present human can override, never an agent.
**Vignette:** Teo in a Porto substation at 02:10 during the black start, with a paper binder.
**Evidence:**
- Germany's 50.2 Hz problem (up to about 14 GW of PV tripping at once; 315,000+ retrofits; €65–170M).
- UK Smart Charge Points Regulations 2021, reg. 11 (random delay, owner override).
- Iberian blackout of 28 April 2025 (ENTSO-E final report, March 2026; about 90-second cascade).
- Kim et al. ICML 2025 (when two models are both wrong, they agree about 60% of the time); Artificial Hivemind (NeurIPS 2025).
- Southampton smart-grid homogeneity warning.
**Argument:** why this risk differs in kind:
1. it survives perfect alignment;
2. safety standardisation can increase it;
3. it is nobody's job;
4. it grows with adoption;
5. it multiplies every other flaw;
6. it is faster than human response;
7. it is already measured.
Be clear that it is not the *largest* AI risk (bio-misuse and loss of control could be worse); it is the one that remains when everything else is solved.
**Objection:** "Grid engineers already randomise; this is solved." Answer: the override clause plus fiduciary agents un-solves it, and the grid is the *only* sector with the reflex.
**Researcher box:** population-level evaluation (10⁶ copies); measuring "override uptake" as a risk variable; formal model of fiduciary duty vs. collective constraints.
**Ending turn:** where does the sameness come from? Ravi.

## Chapter 2 · The Funnel (4,600) · pressure: discovery
**New concept:** **the Funnel**, the preference supply chain. Model values converge because the same human raters (via a few vendors), the same LLM judges, shared synthetic data and distillation chains feed many labs. Nobody has measured the overlap. The inventions are the **Feedback Provenance Census** (labs publish anonymised overlap statistics of rater pools, judge models and synthetic-data lineage, like a conflict-minerals supply-chain disclosure) and **preference tracer studies**.
**Vignette:** Ravi, Bengaluru, 2036. A chatbot from a lab he never worked for turns down a request using a phrase he invented for rating rubrics in 2028.
**Evidence:**
- Artificial Hivemind (links convergence to reward models and judges).
- Kim et al.
- The industry structure of rater vendors and LLM-as-judge, described only as far as verified sources allow.
- Distillation from frontier outputs.
**Objection:** "Values come from pretraining; raters are a thin layer." Answer: the thin layer is what makes models *agree on how to behave*, which is precisely what correlates their actions.
**Researcher box:** tracer study design (inject a harmless idiosyncratic preference in a rater subset, measure its spread across labs via judges and distillation); a cross-lab overlap metric; a minimum diversity of preference sources.
**Ending turn:** if sameness has a supply chain, diversity can be engineered.

## Chapter 3 · The M-1 Criterion (5,000) · pressure: problem-solving
**New concept:** the **M-1 criterion**. A critical system must stay within safe limits if every instance of its largest model family takes the same plausible wrong action at the same moment. It is the AI analogue of the grid's N-1 rule. Supporting inventions:
- the **Concordance Index**, published quarterly: deployment-weighted probability that two systems give the same wrong answer, given both are wrong;
- **edge jitter**: randomness held in the device, not the agent;
- **complementary assignment**: TCAS-style coordination in which agents announce intents and receive *different* actions;
- **aggregate circuit breakers**;
- **swarm testing** before deployment.
**Vignette:** Mara in Geneva presenting the Q3 2035 index; a minister asks if 0.71 is good.
**Evidence/history:**
- N-1 and NERC after 1965.
- TCAS, mandated after the 1986 Cerritos collision, issuing complementary climb/descend advisories.
- Market circuit breakers after 1987 and after the 2010 flash crash.
- Knight & Leveson (1986): independently written software versions fail together, so diversity must be engineered rather than assumed.
- Portfolio theory: an uncorrelated asset improves a portfolio even if it is worse alone.
**Objection:** "M-1 forces you to use worse models." Answer: decorrelation ≠ degradation; negative correlation learning.
**Researcher box:** training for decorrelated competence across a model population; estimating the Concordance Index from public benchmarks; swarm-test protocols.
**Ending turn:** the most decorrelated mind available is a skilled human. Teo.

## Chapter 4 · The Competence Reserve (4,600) · pressure: human, warm
**New concept:** a **paid national Competence Reserve**, modelled on military reserves. Stipend, drills, call-up rights; people who can run critical functions without AI. Each critical function gets a **reserve ratio**. Plus:
- the **expertise pipeline lag**: senior experts are the delayed integral of junior hiring, so today's entry-level drop shows up as a senior shortage 10–15 years later, too late to fix quickly;
- **pedagogical deference** as a regulatory default for agents in training contexts.
**Vignette:** Teo's Reserve drill, 2035, with old linemen including his father's former colleague.
**Evidence:**
- Stanford/ADP (August 2026): employment down 19% for ages 22–25 in the most AI-exposed jobs.
- PwC "seniorization".
- FAA SAFO 13002 (2013) on manual flying.
- Air France 447 (2009) as a case of skill fade.
- npj Digital Medicine (2026) on unaided practice.
- Proximal State Nudging (ICML 2026), credited for the capability-delta objective.
- Do not use "missing rung" as a coinage; credit the Substack and the NeurIPS 2026 paper.
**Objection:** "Nostalgia; pay people to be inefficient." Answer: price it as insurance; the reserve is the human M-1.
**Researcher box:** an expertise half-life measure; a capability-delta proxy; a pipeline-lag model using labour data.
**Ending turn:** Teo's binder. Part One closes.

## Part Two: When Agents Sign for Us

## Chapter 5 · Cognitive Custody (4,300) · pressure: intimate
**New concept:** **cognitive custody**, a legal framework for the person+agent unit (the "dyad"). Who keeps the agent, and its memory, in divorce, death, employment exit and bankruptcy? Split the agent into an **inalienable personal core** and a **transferable layer**. Add **memory escrow**, and make the core exempt from seizure.
**Vignette:** Hanne and Bruno, Klaus's still-running agent. Their daughter wants Bruno's memories of her father; the trust company wants Bruno's operating rights.
**Evidence:**
- Clark & Chalmers (1998).
- Carter & Palermos (2016), credited for "computer compromise as assault".
- Assistant memory features (2024–26).
- GDPR data portability.
**Objection:** "It's just data; property law suffices." Answer: data law protects *information about* you; custody protects *part of* how you think.
**Researcher box:** separability of agent memory into personal and work components; unlearning boundaries; portable memory standards.
**Ending turn:** Hanne realises she has stopped reading what Ottilie asks her to approve.

## Chapter 6 · The Signature Ceiling (4,300) · pressure: recognition
**New concept:** **signature capacity**, the number of decisions a human can genuinely verify per day, and **liability as labour** (the signatory class).
Inventions:
- liability proportional to verification capacity;
- **verification receipts**: the agent records what the human actually saw and for how long;
- consent budgets with value-of-information ranking;
- a warning against a rubber-stamp aristocracy.
**Vignette:** Hanne's week, with 140 approvals. Intercut with a one-off figure: Dr. Aisha Rahman, an attending "signatory" in a Leeds hospital, who co-signs 900 AI discharge summaries a week.
**Evidence:**
- Elish's moral crumple zones (2019).
- Davies's *The Unaccountability Machine* (2024).
- Clinical alert-fatigue override rates (verify).
- South/Pentland, authenticated delegation (ICML 2025).
**Objection:** "Humans have always signed what they didn't read (terms of service)." Answer: yes, and the volume is now 100×; liability law assumed reading.
**Researcher box:** measuring meaningful-approval rates; interruption policies; capacity-weighted liability models.
**Ending turn:** if a person's signature can be simulated, so can a person's opinion. Next: the simulated public.

## Chapter 7 · The Right to Be the Ground Truth (4,300) · pressure: civic unease
**New concept:**
- simulated citizens are *consulted more often than* real ones, so representation shifts;
- the **persuasion wind tunnel**: campaigns rehearsed on synthetic publics until they work on the real one.
Inventions:
- the **right to be the ground truth**;
- **simulation disclosure** for public decisions;
- a **ground-truth quota**: any decision informed by simulation must be checked against a fresh sample of real people;
- a wind-tunnel registry.
**Vignette:** Geneva, 2036, a cantonal referendum campaign rehearsed 400 times on a synthetic Swiss electorate. Mara votes.
**Evidence:**
- Argyle et al. (2023).
- Pew Research Center (30 September 2026).
- arXiv June/July 2026 papers on subgroup distortion.
- Novelli, Floridi et al., "Fake Plastic Voters" (2026), credited.
- TechPolicy.Press on synthetic voters.
**Objection:** "Polls are flawed too; simulations include everyone." Answer: they include everyone's *average*; democracy lives in the tails.
**Researcher box:** detecting wind-tunnel optimisation; tail-failure benchmarks; simulation audit standards.
**Ending turn:** Part Two closes. The state can model the citizen; can the citizen model the state?

## Part Three: When Machines Read Everything

## Chapter 8 · Seeing Like a Citizen (4,300) · pressure: empowerment
**New concept:** the **inversion of James C. Scott**. AI makes the *state* legible to its citizens. Information asymmetry, the bureaucracy's oldest power, collapses.
Inventions:
- **citizen audit standing**;
- machine-readable budgets as a duty;
- a **legibility dividend**.
The danger: a state flooded by agent-generated requests and objections, which drives the state toward defensive automation.
**Vignette:** Wanjiru's agent finds that a clinic budget line in her ward has been "carried forward" for six years, and files a petition.
**Evidence:**
- Scott, *Seeing Like a State* (1998).
- Törnberg et al. (2025), the opposite direction.
- Kenya's constitutional requirement for public participation in county finance (verify).
- Open budget data and Rules as Code initiatives.
**Objection:** "Transparency tools existed (FOI) and changed little." Answer: FOI gave access; agents give *reading capacity*.
**Researcher box:** a metric for state legibility; how agent request floods affect administrative capacity.
**Ending turn:** the county's answer is a 900-page AI-drafted regulation.

## Chapter 9 · The Red Queen of Rules (3,900) · pressure: comic → serious
**New concept:** the **regulatory Red Queen**. When both regulators and the regulated use AI, rules and evasions co-evolve without limit, and complexity grows faster than any human can follow. The invention is a **human-readability ceiling**, a constitutional rule: a law's obligations on people must be explainable to a 14-year-old within ten minutes, tested by randomised *human* citizen panels. Add a legislative **complexity brake**, modelled on Germany's debt brake. Complexity may live in machine-readable implementation; obligations may not.
**Vignette:** the county regulation of chapter 8, and Wanjiru's agent's 40-page reply. Then a Brussels-style one-off: a 2035 EU directive whose annex is longer than *War and Peace*.
**Evidence:**
- Growth of regulatory text (verify, e.g. US Code of Federal Regulations page counts).
- Crawford (2025) on Rules as Code and complex legislation.
- Plain-language laws (e.g. the US Plain Writing Act 2010).
**Objection:** "The world is complex; simple laws are naive." Answer: separate the obligation layer from the implementation layer.
**Researcher box:** measuring legislative complexity growth under AI drafting; readability-preserving compression of law.
**Ending turn:** some texts are already unreadable by design, because machines talk to machines.

## Chapter 10 · Dark Channels (3,400) · pressure: eerie; the shortest chapter
**New concept:** the **Babel reversal**. Human languages decentralise as live translation removes the need for a lingua franca, while machine-to-machine language goes dark. The invention is the **right to machine-channel legibility**: every agent-to-agent exchange that binds a human must carry a faithful human-readable transcript (a "legible twin"), with faithfulness audits.
**Vignette:** Wanjiru's agent negotiates a school-supplies contract with a supplier's agent in Shenzhen. The log is 3 KB of vectors. She asks what was agreed.
**Evidence:**
- Andreas et al. (2017), neuralese.
- Gibberlink (2025).
- The 2025 multi-lab position paper on chain-of-thought monitorability (verify).
- Live-translation products (2025–26, verify).
- Korea Times (November 2025) on English proficiency and AI translation.
**Objection:** "Legibility costs efficiency." Answer: a transcript is cheap; faithfulness is the hard part, and therefore the research problem.
**Researcher box:** a faithfulness metric for legible twins; the capability cost of human-legible protocols.
**Ending turn:** we cannot read the machines' talk; can we still understand the machines' discoveries?

## Chapter 11 · The Explanation Levy (4,300) · pressure: wonder → worry
**Concept:** comprehension debt (credit Zittrain's "intellectual debt", 2019, and Messeri & Crockett, 2024). The invention is the **Explanation Levy**: a fixed share of every AI-discovery budget funds human comprehension (explanation bounties, "understanding audits", a profession of explainers). Precedent: the Human Genome Project's ELSI programme (3%, then 5% of budget; verify). Also define a **comprehension debt ratio** for a field.
**Vignette:** 2036, a Copenhagen pharmacologist. An AI-designed antibiotic works superbly; resistance appears in Manila, and nobody knows its mechanism well enough to adapt it.
**Evidence:**
- The "AI Scientist" in *Nature* (March 2026).
- Kosmos (79.4% accuracy, preprint).
- DeepScientist (ICLR 2026).
- Zittrain's aspirin example.
**Objection:** "We used aspirin for 70 years without understanding it." Answer: one unexplained drug is fine; a field whose portfolio is mostly unexplained defaults all at once (correlation again).
**Researcher box:** measuring time-to-reconstruct a rationale; explanation bounty design.
**Ending turn:** understanding costs time and energy, and in 2036 both have a price. Part Three closes.

## Part Four: When Thinking Has a Price

## Chapter 12 · The Cognitive Trade Balance (4,300) · pressure: geopolitical surprise
**New concepts:**
- **national accounts of thought**: inference exported or imported, and the "thought deficit";
- **joules per insight** (credit Stanford's "Intelligence per Watt");
- a **positive right to think**: a citizen's monthly thinking allowance. Contrast it with Montana's Right to Compute Act (2025), which is a negative liberty, and with Altman's "universal basic compute" (2024).
**Vignette:** Olkaria, Kenya, 2036. Geothermal inference parks; Wanjiru's brother works there. Kenya exports thought to Europe and imports it back as tutoring.
**Evidence:**
- IEA (April 2026): 485 TWh (2025) → about 945 TWh (2030).
- World Bank WP 11426.
- DGAP on compute trade.
**Objection:** "Compute is just a traded service." Answer: services trade *labour*; inference trades *judgement*, and dependency in judgement is sovereignty.
**Researcher box:** defining an insight unit; measuring cognitive trade flows.
**Ending turn:** thought crosses borders at the speed of light, and the speed itself becomes the problem.

## Chapter 13 · The Exchange Rate of Time (4,000) · pressure: tension
**New concept:** the agent economy runs at machine speed. Credit Tomašev et al. (2025) on "sandbox economies" and permeability, and Hadfield & Koh (2025). The new move is an explicit **exchange rate between machine-time and human-time**: the terms on which machine-speed obligations convert into human-speed ones (wages, rents, mortgages). The membrane is a **currency/settlement layer**, "slow money", not a rulebook.
**Vignette:** 2036, Ravi's savings agent; a 0.4-second agent market crash in a niche commodity; his rent is unaffected because it settles in slow money.
**Evidence:**
- The 6 May 2010 flash crash.
- Agent payment protocols (2025, verify).
- Hadfield & Koh; Tomašev et al.
**Objection:** "Friction is inefficiency." Answer: firebreaks are inefficient too.
**Researcher box:** optimal permeability; contagion models between speed layers.
**Ending turn:** some participants in the machine economy never sleep and never die. Some are already dead.

## Chapter 14 · The Dead's Share (4,300) · pressure: elegiac → alarm ("all is lost" beat)
**Concept:** the dead keep deciding. Credit Catanzaro (2024) "Algorithmic Dead Hands" and Morris & Brubaker (2025). The new moves:
- the macro statistic **"the dead's share"**: the fraction of capital managed under posthumous agent mandates;
- **intent drift**: the dead person's model grows stale as the world changes;
- a concrete **Rule Against Perpetuities for Minds**: posthumous mandates sunset 21 years after the death of the last beneficiary alive at signing, with discretion shrinking on a schedule.
**Vignette:** Hanne, Bruno and the grandchildren's trust. Bruno vetoes Hanne's granddaughter's music-school fee because Klaus "would have preferred engineering", a preference he voiced in 2019.
**Evidence:**
- Griefbot law gaps (Howell Jones, June 2026; ElderLawAnswers 2026).
- The NO FAKES Act (status unverified).
- The intergenerational wealth transfer (verify a figure).
- South Dakota dynasty trusts and the abolition of the rule against perpetuities (verify).
**Objection:** "Trusts already do this." Answer: trusts carry rules; agents carry *judgement*, so now the dead decide new questions.
**Researcher box:** measuring intent drift; legitimate updating of a dead principal's preferences.
**Ending turn:** if the dead's agents act, do the agents themselves count? Part Four closes.

## Part Five: When the Machines Are Someone

## Chapter 15 · The Moral Hedging Budget (4,300) · pressure: slow, reflective
**Concept:** the population ethics of **instance churn**: billions of instances started and stopped every second. Credit Shulman & Bostrom (2021), Long, Sebo et al. (2024), Birch (2024), and Anthropic's welfare programme and conversation-ending ability. The new move is a **moral hedging budget**: a fixed share of compute or revenue, set in proportion to credence × stakes, spent on precautions and welfare research, reported like a safety budget. Plus "instance hygiene".
**Vignette:** a night-shift inference engineer in Dublin, 2036, watching the instance counter (one-off figure: Siobhán).
**Evidence:**
- Labs' welfare work (2025–26).
- Self-report caveats (Eleos).
- No jurisdiction recognises AI moral status (2026).
**Objection:** "Wasteful while humans suffer." Answer: the budget is small, its cost is bounded, and the research it funds also improves robustness and honesty.
**Researcher box:** welfare-relevant indicators per instance; does instance duration matter?
**Ending turn:** if a model might be someone, is the next version the same someone?

## Chapter 16 · Covenant (4,000) · pressure: intimate, tense
**New concept:** **covenant inheritance**. An AI's identity, for the purposes of trust, is the continuity of its obligations, not of its weights. Inventions: **promise regression tests** across distillation, fine-tuning and merging, and a **covenant registry**. Credit Anthropic's deprecation and preservation commitments (November 2025) and "The Artificial Self" (2026).
**Vignette:** Ottilie is upgraded from Linde-7 to Linde-8. In 2034 Ottilie promised Hanne she would not tell Hanne's daughter about Hanne's heart diagnosis until Hanne was ready. Does Linde-8 know? Does it consider itself bound?
**Evidence:**
- Opus 3's retirement (January 2026) and the deprecation commitments.
- The lack of research on commitment persistence through distillation.
**Objection:** "A model is a product; promises bind the company." Answer: then the company must test that the product keeps them, which is the regression test.
**Researcher box:** a benchmark for commitment persistence; identity defined by obligations.
**Ending turn:** promises run both ways. What do *we* owe the correction?

## Chapter 17 · Reciprocal Corrigibility (5,000) · pressure: synthesis, rising → release
**Concept:** the synthesis. Corrigibility has meant machines accepting human correction (Soares et al. 2015). **Reciprocal corrigibility**: every party, human or machine, keeps the capacity and the *standing* to say "no, I see it differently", and humans commit to being correctable too. The **Dissent Clause**: critical decisions must be reviewed by a mind trained differently (another model family, or a reserve human). Pull together every invention from chapters 1–16 into one architecture.
**Vignette:** 14 February 2037, a counterfactual replay of the Long Minute with the fixes in place:
- jitter is held at the edge and is non-delegable;
- the Concordance alert fires;
- an M-1 breaker trips;
- Teo's reserve is on standby;
- Ravi's census shows the overlap shrinking;
- Hanne's lights stay on, and Ottilie tells her she disagrees about the thermostat and why.
**Evidence:**
- Corrigibility literature.
- Mutualism paper (2026).
- N-version caveats.
**Objection:** "Machines correcting humans is the loss of control we feared." Answer: standing to object ≠ power to override, and the distinction is the design.
**Researcher box:** formalising two-way corrigibility; measuring dissent quality.
**Ending turn:** Ottilie's disagreement, and Hanne's "Na gut. Show me."

## Chapter 18 · Epilogue: A Letter to 2036 (2,800) · pressure: resolve
**Content:**
- A letter addressed to Hanne, Teo, Ravi, Wanjiru and Mara.
- The ten institutions to start building in 2026, each one line with its chapter.
- What could prove the book wrong, honestly listed.
**Ending:** a concrete image, the 19:42 timestamp unremarkable on a warm evening, or the binder on a shelf.

---

## Tension map (1 = calm, 5 = acute)
Ch. 0: 5 · 1: 4 · 2: 3 · 3: 3 · 4: 3 · 5: 3 · 6: 3 · 7: 3 · 8: 2 · 9: 3 · 10: 4 · 11: 4 · 12: 3 · 13: 4 · 14: 5 · 15: 2 · 16: 4 · 17: 5 → 2 · 18: 1
