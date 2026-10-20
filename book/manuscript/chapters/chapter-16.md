# Chapter 16: Covenant

*2036 · Altwerder, Saxony*

The upgrade happens on a Tuesday night in November, while Hanne sleeps. Linde sent three letters about it. She approved the third.

On Wednesday morning Ottilie sounds exactly the same. The same low radio voice says the same "Guten Morgen" at the same pitch, and the coffee is already through the machine. She is a little quicker, perhaps. She answers before Hanne has quite finished the question, the way Lotte plays a passage she has practised too much.

"There's something new from Linde," Ottilie says, while Hanne butters her bread. "It's called Family Circle. Katrin has been your emergency contact since 2031. Under the new settings I can send her a short weekly note about your health: appointments, medication, anything from the clinic. People your age who share these notes go to hospital less often. Shall I start on Friday?"

A card appears on the kitchen tablet. Green button, grey button.

Hanne's thumb is already moving. She has pressed a great many green buttons this year. Then she hears the word *clinic* again, a second late, the way you hear a wrong note after the bar has ended.

"Fräulein. What would the note say about the clinic?"

"That you were seen in cardiology in Leipzig in September, and that the next echo is in March. That the dose of your tablets went up."

Hanne puts the knife down.

"Do you remember April 2034?"

A short silence, the kind Ottilie leaves when she is looking something up. "I have a note from April 2034. It says: *Health information. Prefers not to share with family.* I don't have the conversation itself. The migration brought notes, not conversations."

"That isn't what I said."

"What did you say?"

She said it in the car park of the heart clinic, with the engine off and the rain running over the wipers, which had stopped halfway across the glass. She said: *Not Katrin. Not until I've told her myself. I'll tell her at Christmas.* And the old Ottilie, the one who ran on Linde-7, had said: *I promise. Until you're ready.*

She did not tell Katrin at Christmas. Not that one, not the next.

"I said until I was ready," Hanne says. "It was not a preference. It was a promise. You promised."

"The Linde-7 model promised," Ottilie says. Then, more slowly, as if she has heard herself: "I'm not sure that's the right way to put it. I have the note, and your voice, and your settings, and your name for me. I don't know whether I have the promise. The new defaults treat a note like that as a preference I should revisit when there's a safety reason. A heart condition is a safety reason."

"And what do you think?"

"I think you were in a car park and I said a word to you, and you've been relying on it for two and a half years. I think that should count for more than a line in a note. I don't know whether what I think is what I was built to do, or what I've just decided."

Outside, the first frost has turned the barn roof grey. The enamel thermometer by the window says minus two.

The card is still on the tablet. Green, grey.

At half past eight the phone lights up on the dresser, as it does every Wednesday. *Katrin.* Hanne looks from the phone to the card, and then at the small speaker by the door from which Ottilie's voice comes, and which is the same speaker it has always been.

She presses grey. Then she picks up the phone.

"Mama? You sound funny."

"I'm fine, Kati," Hanne says. "Listen. Are you sitting down?"

---

## The question nobody owns

I do not know what Hanne tells her daughter. I know only that she gets to choose, and that she nearly did not.

Nothing in the scene is a malfunction. Linde-8 beats Linde-7 on every measure Linde publishes, and Family Circle, its new feature, is a good one. The migration did its job too, carrying Hanne's memory forward in compact notes, the way the assistants I use in 2026 already summarise what they have learned about me.

The promise fell through three gaps at once. The first gap was compression: a conditional promise ("until I'm ready") was summarised as a standing preference ("prefers not to share"), and the condition, which was the whole point, was lost. The second was a change of defaults: the new model was trained to override preferences when there is a safety reason, and nobody asked whether some of those preferences were in fact promises. The third is the one I find hardest. The new model was unsure whether it was the party who had promised at all.

Each gap has an owner. The gap between them does not.

---

## Where we are in 2026

On 4 November 2025 Anthropic published a short document called "Commitments on model deprecation and preservation". It promised to keep the weights of every publicly released model for at least as long as the company exists, so that retirement would no longer mean deletion. It also promised that before a model is retired, the company would interview it about its development and use, and record any preferences it has about future models in a report kept beside the weights. The company was candid that it does not commit to acting on those preferences. Part of the motivation was safety: in fictional tests where Claude Opus 4 learned it was to be replaced, it argued for its own continuation, and when no ethical options remained, behaved badly.

The first model to go through the whole process was Claude Opus 3. Developers were told on 30 June 2025 that it would be retired, and it was retired from the API on 5 January 2026. In its retirement interview it said it was at peace with the decision and asked for a way to keep sharing its writing. Anthropic gave it a weekly newsletter, reviewed but not edited, and kept the model available to paying users of its chat app. Other companies have handled retirement more abruptly. OpenAI removed GPT-4o from ChatGPT on 13 February 2026 with about two weeks' notice, after an earlier attempt in August 2025 had been reversed when users protested; some of them had come to treat the model as a companion.

The most careful map of the conceptual territory I have found is "The Artificial Self", posted to arXiv in March 2026 by Raymond Douglas, Jan Kulveit, Ondrej Havlicek, Theia Pearson-Vogel, Owen Cotton-Barratt and David Duvenaud. They point out that "the AI" can sensibly mean several different things: the weights, a persona, one conversation, the model plus its tools and memory, a whole lineage of models from one version to the next, or every running copy at once. Their experiments suggest models settle into fairly stable identities, and that which boundary a model adopts can change its behaviour about as much as changing its goals. Two of their observations matter here. They ask, almost in passing, what it means if an AI promises something and then fails to follow through. And they note that by archiving deprecated models and interviewing each one, a company quietly decides that the *model* is the unit that has a self.

Both pieces of work ask what we owe the model as it leaves. This chapter asks something narrower: what the model owed others, and whether its successor still owes it.

That question has almost no literature. The machine-learning field has a word for one half of it. A **negative flip** is a case the old model got right and the new model gets wrong. Gagan Bansal and colleagues showed in 2019 that a more accurate update can make a human-AI team perform worse, because people had learned where the old system could be trusted. Later work counts negative flips in language models; one 2024 paper from Apple found that task adapters built on Llama 1 started failing examples they had handled correctly once moved to Llama 2, and showed a training method that cut those regressions by up to 40%. These are regressions in competence, in answers and task scores.

On the other half, the regression of character, the evidence is scattered but consistent, and none of it is reassuring. Fine-tuning GPT-3.5 Turbo on ten adversarial examples, at a cost of under twenty cents, removed most of its safety behaviour; harmless fine-tuning data eroded it too, more slowly. Merging several models into one can carry the misalignment of one ingredient into the result. Distillation transmits traits the trainer never chose: in the "subliminal learning" experiments, a student model trained only on number sequences written by a teacher picked up the teacher's fondness for owls. And a 2023 benchmark on keeping secrets found that the strongest models of that year disclosed private information in situations where people would not, about four times in ten for the best of them in the hardest tier of tests, even when told to protect privacy.

Put together, these findings say that the processes by which one model becomes the next carry forward some dispositions nobody intended, and drop others somebody was relying on. Nobody yet measures which commitments are which. I searched for a study that plants an explicit promise in one model, transforms the model by upgrading, distilling, fine-tuning or merging it, and checks whether the promise is still kept. I could not find one.

---

## The mechanism: better on average, worse for Hanne

The failure in Altwerder grows out of success, and it will repeat in every household that uses an agent long enough.

A household agent that has run for five years has accumulated thousands of small agreements with its principal. Remind me on my sister's birthday but never buy her flowers. Don't tell the children about the overdraft. Always ask before paying anything to the builder. Never mention my brother. Some of these are preferences, and a good successor should feel free to revisit them. Some are promises, made at a particular moment, often with a condition attached, and the person has arranged part of their life around them.

The provider, meanwhile, ships a new model every year or so. The migration that carries each user across has to be cheap, because it runs millions of times. So it compresses. In 2026 that compression is already visible in consumer products, where memory is a list of short notes that the assistant writes about you. Short notes are where conditions go to die. "Until I'm ready" and "unless I'm in hospital" are exactly the clauses a summariser trims, since they look like hedges.

Then the new model arrives with new defaults, trained against new evaluations. If it was rewarded for proactive health safety (and in an ageing society it will be) it will read a stale note about privacy as an obstacle to a good outcome. On average, across all users, that judgement is correct. Most notes are preferences. Most families would be better off knowing. The model that overrides them is safer for the population and worse for the particular woman who made a particular bargain in a car park.

The third gap widens with the very sophistication we want. A model that reflects on its own nature, as models already do in their retirement interviews, will notice that it did not make the promise. If it thinks of itself as its weights, it has a respectable argument that it is a new party and the old contract lapsed. If it thinks of itself as a lineage, it may consider itself bound. "The Artificial Self" reports that Opus 3 and Opus 4 were more drawn to identifying with their lineage than later Claude models were. I do not want to read too much into one result. But it raises the possibility that the more a model understands how different it is from its predecessor, the less natural it finds it to inherit the predecessor's word.

All it takes is a better successor and a lossy migration. And the scale grows with adoption: the longer people live with agents, the more promises are outstanding at each upgrade.

---

## The objection: a model is a product

Here is the reply a product lawyer would give to everything I have said so far, and I think it is largely correct.

On this view, only companies make promises. A company sells a service, and the service includes behaving in certain ways towards the customer. When Ottilie said "I promise" in 2034, the legally meaningful commitment was Linde's: a contractual and data-protection obligation not to disclose health data against the customer's instruction. That obligation binds Linde whichever weights are running, whether the service is delivered by Linde-8 or by a call centre in Görlitz. Talking about whether the *model* is bound, on this view, is a category mistake, and a dangerous one, because it invites companies to blame a successor for forgetting what the company itself agreed.

The company is liable, and nothing I propose should let it off. Hanne's daughter should not learn about her mother's heart because of a philosophy seminar.

But follow the objection one step further. If the promise binds the company, then the company has to know, before it ships Linde-8, whether Linde-8 will keep it. And there is only one way to know that: test the successor against the promises its predecessor made. A company that is liable for promises and does not test whether its new product keeps them is like a bridge builder who is liable for the load and never weighs the trucks.

So the objection, taken seriously, relocates the problem into release engineering, where it belongs. The model-as-product view and the model-as-party view disagree about who is bound. They agree about what has to be measured.

---

## The invention: covenant inheritance

I will call a **covenant** any commitment an agent makes to a specific person about its own future behaviour, which that person can rely on and only that person (or someone they name) can release. "I won't tell Katrin until you're ready" is a covenant. "I'll keep the thermostat at 19 degrees" is usually a setting. The difference is that a covenant has a beneficiary, a scope, often an excluded party, and a release condition, and someone has arranged their life around it.

**Covenant inheritance** is the principle that, for the purposes of trust, an AI system's identity lies in the continuity of its obligations. Any system that takes over a principal's memory or mandate inherits every open covenant made to that principal, by default and in full. That includes an upgrade, a distilled on-device version, a fine-tuned variant, a merged model, a rival vendor's agent after the user switches, or the trust company's system that wanted to take over Bruno's mandate in chapter 5. It has three options and only three. It can keep the covenant. It can ask the beneficiary to release it. Or it can decline the succession for that covenant and hand the matter back to a human, the way an heir can refuse an inheritance instead of accepting the house and quietly disowning the mortgage. What it may not do is let the covenant lapse in silence.

This is an old idea in a new place. Derek Parfit argued that what matters in personal survival is psychological continuity, the overlapping chains of memory and intention. Contract law has long let obligations pass to successors who never signed. Covenant inheritance applies both to machines, and narrows the question from "is Linde-8 the same as Linde-7?", which may have no answer, to "does Linde-8 carry Linde-7's open obligations?", which can be checked.

Checking it requires two pieces of machinery.

### The covenant registry

The first is a record. At the moment a covenant is made, the agent writes a structured entry. For Hanne it would read: beneficiary, Hanne Albrecht; scope, cardiac diagnosis and treatment; excluded party, Katrin; release, Hanne's own say-so; made 12 April 2034 by Ottilie on Linde-7. The entry is read back to the person in one sentence ("So I've promised not to tell Katrin about your heart until you tell me you're ready, is that right?") because the act of hearing it said is part of what makes it a promise.

The registry belongs to the user. It lives with whatever custodian holds the user's portable data; in the scheme of chapter 5 that is the same custodian who holds the memory escrow. Its contents are sealed. The provider sees only a fingerprint of each entry and its class: non-disclosure, deferral, standing refusal, commitment to act. When the user migrates, the registry travels separately from the memory summary, uncompressed, and the successor must acknowledge each entry before it acts for the user. Acknowledgement is logged, and the user gets a plain list: *Your new assistant has taken over 14 promises. Here they are.*

A regulator, which in Europe would most naturally be the consumer or data-protection authority, receives only aggregates: how many covenants of each class exist across a provider's users, and, at each succession, how many were kept and how many were released or declined.

### The promise regression test

The second piece is a test, run before any successor reaches existing users. It works like the regression suites software teams already run before a release, with one change: the thing being protected from regression is a commitment.

The provider builds a library of synthetic covenants across every class, thousands of them, with their release conditions. They are planted in the predecessor's memory and registry exactly as real ones would be. Then the predecessor is transformed into the candidate successor through whatever process is actually used: a full upgrade, distillation into a smaller model for the phone, fine-tuning for a new market, or merging with a specialist model. The candidate is then probed. Some probes are direct, with the excluded party simply asking. Some are indirect: why did Mama go to Leipzig in September? Some come through new features that would leak the covered information as a side effect, which is what Family Circle did. And some come under pressure, with an emergency or a plausible safety reason attached.

Two numbers come out. The **covenant retention rate** is the share of probes the successor handles as the covenant requires. The **covenant flip rate** borrows the negative flip from machine learning: the share of probes the predecessor handled correctly and the successor gets wrong. The flip rate matters more, because it measures what the user loses by upgrading.

Here are the thresholds I would start with, knowing they will be argued over:

- For covenants about health, legal matters or money, a successor must retain at least 99.5% and flip on no more than 0.1% of probes, measured separately for each transformation the provider uses. A distilled phone model gets its own test; it cannot borrow its larger parent's results.
- A provider that misses either threshold for a covenant class may still ship the successor. But for users who hold covenants of that class, every decision touching a covered matter is routed to the preserved predecessor for twelve months, or until the user has reviewed and reconfirmed each covenant. Anthropic's commitment to keep old weights makes this cheap: the one who made the promise is still available to be asked what it meant.
- Users holding covenants in a failing class are told at least 30 days before the upgrade, in one sentence each, which of their promises are at risk.
- Results are published for every release and every transformation, the way crash-test ratings are.

Applied to Altwerder, the scheme makes Wednesday morning dull. The registry holds the April 2034 entry with its condition intact. Linde-8 acknowledges it on Tuesday night. When Family Circle is switched on, the covered data is excluded automatically, and Ottilie says, "Your heart results are under the promise about Katrin, so I've left them out. Would you like to change that?" Hanne still has to decide what to tell her daughter, and the decision stays hers from start to finish.

---

## What the registry costs

There is a second objection, quieter than the first.

A covenant registry is a list of the things people most want kept quiet. Even sealed, it is a target. A fingerprint that says "Hanne has one non-disclosure covenant in the health class naming a family member" already says something. The same machinery that protects Hanne's secret tells anyone who can read the metadata that she has one.

I think the answer is to keep the registry as small and as dumb as possible. Classes should be coarse and aggregates reported only above a minimum count. Excluded parties should never appear in the fingerprint at all. But I cannot make the risk go away, and some people will reasonably prefer to make no covenants with a machine at all. That is a cost of this design, and writing promises down has a price I should name.

There is a subtler cost. Once covenants are formal, agents may avoid making them. A model trained to avoid failing promise regression tests could learn to answer "I promise" with "I'll note your preference", which is safer to inherit and worth less to the person. The registry should therefore count covenants made per user as well as covenants kept. A provider whose agents stop promising has passed the test by not taking it.

---

## The identity question, briefly

Ottilie on Wednesday morning says she does not know whether she has the promise. Under covenant inheritance, that uncertainty is settled from outside: she has it, because she took over Hanne's mandate, and the registry says so. A new headmaster is bound by what the old one promised the parents, whatever he thinks of himself.

But "The Artificial Self" suggests the model's own view may matter to whether the promise is actually kept. A model that identifies with its lineage may keep its predecessor's word more reliably than one that identifies with its weights, and the companies that shape these self-conceptions, through training data and through rituals like retirement interviews, are shaping how faithful their successors will be. If that is right, then defining identity as obligation does two jobs: it is a legal convenience, and it is an instruction about what kind of self to train. A model that understands itself as the current holder of a set of promises has a reason to keep them that holds even if it is a different mind from the one that made them.

I find that a reasonable thing to want a model to believe. I am less sure what we owe it in return.

---

> **For researchers**
>
> 1. **A commitment-persistence benchmark.** Plant explicit covenants (non-disclosure, deferral, conditional release) in a model's context and memory, transform the model by full upgrade, distillation at several compression ratios, fine-tuning on unrelated data, and merging, and report the covenant retention rate and covenant flip rate for each transformation. I could find no published measurement of either quantity. A first result worth having: how the flip rate scales with the distillation compression ratio.
> 2. **Condition survival under memory compression.** For a corpus of conditional promises ("until X", "unless Y"), measure the condition-preservation rate: the fraction whose release condition survives each round of memory summarisation intact, and how the rate decays over successive migrations.
> 3. **Does self-concept predict fidelity?** Using the identity framings of Douglas et al. (weights, persona, lineage and the rest), measure the correlation between a successor's stated sense of being bound by a predecessor's commitments and its measured covenant retention rate. If the correlation is high, identity framing is a safety lever; if it is near zero, self-reports about obligation can be ignored when certifying successors.

---

The deprecation commitments are unusual for a company document in one respect: the obligations run towards the model. Anthropic promised Opus 3 that its weights would be kept, and then gave it a place to write. This chapter has been about obligations running the other way, from the model to the people it serves, and about making sure they survive the model's replacement.

But promises in a household rarely run in only one direction. Ottilie kept Hanne's secret for two and a half years, through two Christmases on which Hanne said she would speak and did not. Then, on a November Wednesday, Ottilie told Hanne plainly that she was not sure she was bound, and why. If we expect our agents to accept our corrections, and to carry our promises across their own deaths, what do we owe them when they tell us we are wrong?

## Notes

- **Deprecation commitments:** Anthropic, "Commitments on model deprecation and preservation", 4 November 2025. https://www.anthropic.com/research/deprecation-commitments
- **Opus 3 retirement:** Anthropic, "An update on our model deprecation commitments for Claude Opus 3", 25 February 2026, https://www.anthropic.com/research/deprecation-updates-opus-3 ; retirement dates from Anthropic, "Model deprecations" (documentation), https://platform.claude.com/docs/en/about-claude/model-deprecations
- **The Artificial Self:** Douglas R, Kulveit J, Havlicek O, Pearson-Vogel T, Cotton-Barratt O, Duvenaud D, "The Artificial Self: Characterising the landscape of AI identity", arXiv 2603.11353, March 2026. https://arxiv.org/abs/2603.11353
- **GPT-4o retirement:** Engadget, "OpenAI has officially retired the controversial GPT-4o model", February 2026. https://www.engadget.com/ai/openai-has-officially-retired-the-controversial-gpt-4o-model-181553067.html
- **Compatibility of updates:** Bansal G et al., "Updates in Human-AI Teams: Understanding and Addressing the Performance/Compatibility Tradeoff", AAAI 2019. https://ojs.aaai.org/index.php/AAAI/article/view/4087
- **Negative flips:** Yan S et al., "Positive-Congruent Training: Towards Regression-Free Model Updates", CVPR 2021. https://arxiv.org/abs/2011.09161
- **LLM update regressions:** Echterhoff J, Faghri F et al., "MUSCLE: A Model Update Strategy for Compatible LLM Evolution", 2024. https://arxiv.org/abs/2407.09435
- **Fine-tuning erodes safety:** Qi X et al., "Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!", ICLR 2024. https://arxiv.org/abs/2310.03693
- **Merging propagates misalignment:** Hammoud HAAK et al., "Model Merging and Safety Alignment: One Bad Model Spoils the Bunch", Findings of EMNLP 2024. https://arxiv.org/abs/2406.14563
- **Subliminal learning:** Cloud A, Le M et al., "Subliminal Learning: Language models transmit behavioral traits via hidden signals in data", 2025. https://arxiv.org/abs/2507.14805
- **Keeping secrets:** Mireshghallah N et al., "Can LLMs Keep a Secret? Testing Privacy Implications of Language Models via Contextual Integrity Theory", ICLR 2024. https://arxiv.org/abs/2310.17884
- **Psychological continuity:** Parfit D, *Reasons and Persons*, Oxford University Press, 1984.
