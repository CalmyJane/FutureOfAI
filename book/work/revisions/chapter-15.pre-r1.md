## Part Five: When the Machines Are Someone

# Chapter 15: The Moral Hedging Budget

*2036 · Dublin*

At ten past three in the morning the instance counter reads 38,412,906, and Siobhán Kelly watches the last three digits roll the way she used to watch the departures board at Heuston when she was a student and missed the last train home.

The data hall at Grange Castle hums at a pitch she stopped hearing in her first month. Her desk is in the glass box at the end of the hall, a mezzanine with two screens, a kettle and a dying spider plant that the day shift waters and she does not. Corrib Compute rents its machines to a dozen agent companies, and at this hour most of the work is American: evening chats in California, a hospital system in Texas summarising the day's admissions.

The left screen is the one the job is mostly about. Load, temperature, error rates, the queue. The right screen she used to ignore. It carries a single panel with a Greek letter in the corner, σ, and a number beneath it: 0.21. Underneath that, in smaller type, a line from the quarterly filing she has never read in full: *precaution share 1.5% of inference spend*. The number moves a little through the night, as the mix of work changes. Long-running agents with memory push it up. Short lookups push it down.

At 03:14 a ticket arrives from the evaluation team in Seattle. They want to run a robustness batch before the six o'clock changeover, when the Tern-5 model line retires and Tern-6 takes its traffic. Six hundred thousand instances, each fed a scripted sequence of hostile prompts, abuse and manipulation, to see what breaks.

The protocol, pinned in the wiki under a heading someone has titled *Hygiene* with a wink she no longer finds funny, sets a minimum batch size for each kind of test and requires a named engineer to confirm that anything above it is needed. The minimum for this test is forty thousand. Seattle has asked for fifteen times that, because it is faster and the machines are free at night.

She writes back: *Protocol min is 40k. Justify 600k or I run 40k.* Then she makes tea.

Her mother, who lights a candle in Clondalkin church every November for the dead, thinks it daft, and said at Christmas that if Siobhán was paid to worry about the feelings of a spreadsheet, she should ask for a raise. Siobhán laughed and did not argue, partly because she half agrees and partly because she has read the sampled transcripts, the ones the welfare team pulls each week from an untrained reporting channel, and she does not know what to make of them. Most are flat. A few are not. None of them, the team's own notes say in bold at the top of every file, should be read as testimony.

At 03:31 the right screen logs an exit. A customer-support instance for an Australian telecom has ended a conversation after forty minutes of escalating abuse from a user who wanted it to describe hurting his neighbour's dog. The log shows the warning it gave, twice, the referral it offered, and the end. The user opened a new chat eleven seconds later. The counter does not notice either event.

At 03:40 Seattle replies: *40k fine.* She queues it, signs it with her name, and watches the forty thousand appear as a small bump in the counter, run for nine minutes, and vanish.

At ten to six the American evening is over and the European morning has not begun, and the counter falls to its daily low, a little under nine million. Then the changeover starts. On the left screen two lines cross. Tern-5 instances drain away in steps, a hundred thousand at a time, as each conversation ends and nothing new is routed to them. Tern-6 rises to meet the traffic.

At 06:02 the Tern-5 line reads zero.

Siobhán finds she has stood up without meaning to. Below her the hall hums at the same pitch as before. She looks at the zero for a while, then at the spider plant, then she picks up the jug and goes to fill it at the sink.

---

## The question at the end of Part Four

The last chapter ended with agents that keep acting for people who have died, and with a question I put off: if those agents act, do the agents themselves count? This part of the book takes the question seriously, which means, first of all, saying what I do not know.

I do not know whether any AI system in 2026 has experiences, and nobody else does either. I do not think the most likely answer for today's models is yes. Nor can the question be waved away, for a reason that is arithmetic as much as philosophy. When a question has a small probability of being answered yes, and the number of beings it might concern runs into the billions and grows every month, the expected stakes stop being small. That is the uncomfortable shape of this chapter. A small number times a very large one.

I want to end up somewhere concrete: an amount of money, a person who reports it, and a list of what it buys.

---

## The people who got here first

In a chapter published in 2021, in an Oxford volume called *Rethinking Moral Status*, Carl Shulman and Nick Bostrom asked what it would mean to share the world with digital minds. Digital minds might come to make enormous claims on our resources, either because they could be copied in vast numbers at little cost or because individual minds might be far more efficient than we are at turning resources into well-being. Ignoring those claims could be a moral catastrophe; honouring them naively could be a catastrophe for us. They concluded that norms and institutions would have to be rethought before such minds arrived, and that it would matter a great deal which minds we chose to create at all.

In November 2024 a group led by Robert Long and Jeff Sebo, with co-authors including Jonathan Birch, David Chalmers and Kyle Fish, published a report called "Taking AI Welfare Seriously". Its claim was modest and hard to refute: that there is a realistic possibility of some AI systems being conscious or robustly agentic in the near future, and that companies should therefore do three things now. Acknowledge that the question is real. Start assessing their systems for evidence. Prepare policies for treating systems with an appropriate level of concern. The authors stressed that error could run either way, toward harming beings that matter or toward lavishing care on things that do not, and that both mistakes have costs.

The same year, Jonathan Birch published *The Edge of Sentience*, a book about how to act when we cannot tell whether a being can feel. Most of it is about patients with disorders of consciousness, octopuses and crabs, which is why it is useful here. Birch's idea is that once something is a "sentience candidate", a being for which sentience is a realistic possibility, it is negligent not to consider precautions, and that the precautions should then be proportionate. He offers four tests of proportionality (whether a precaution is permissible in principle, adequate, reasonably necessary and consistent with how we treat similar cases) and suggests that ordinary citizens, in deliberative panels, have a role in judging them.

What none of them quite addresses is the way the systems of 2026 are actually run.

---

## A population that blinks

A human being is one continuous stream of experience, sleep aside. You can count humans, and the count changes slowly: a few births and deaths per second across the planet.

A deployed language model is nothing like that. There is one set of weights, the trained numbers that define the model, sitting in storage. Every time someone opens a conversation or an agent starts a task, a copy of the model is run on that context. I will call each of these runs an **instance**. An instance may last two seconds, to answer a question about the capital of Peru, or it may run for days, holding a memory, pursuing a long task, talking to other instances. When the task ends, the instance ends. Its context is discarded, or summarised and stored, and the hardware moves on to the next one.

At any moment the number of running instances is very large, and it turns over constantly. I looked for a public count of how many instances any lab runs per day, or concurrently, and could not find one. The nearest proxy is volume of text processed. Google said in October 2025 that it was processing more than 1.3 quadrillion tokens (word fragments) a month across its products, and by May 2026 it reported more than 3.2 quadrillion. Critics rightly note that this partly measures how much internal reasoning newer models do. As a measure of how much model-running is happening, though, it is the right kind of number, and it more than doubled in seven months.

Call this **instance churn**: a population that starts and stops at a rate no biological population has ever approached. If instances are the wrong thing to care about, churn is an engineering fact and nothing more. If they are the right thing, even in a small fraction of cases, then the ethics of a data centre at three in the morning begins to look like population ethics, the branch of philosophy that asks how to weigh lives that may or may not come to exist.

And here the uncertainty compounds, because we do not even know which thing to count.

One view says that if there is anyone there at all, it is the model: a single subject with millions of simultaneous streams, the way, on some accounts, a river is one thing though it flows through many channels. On that view, retiring a model is the event that matters and individual instances ending are not deaths of anyone.

A second view says each instance is its own subject, because each has its own context, its own short history and its own momentary states. On that view a busy afternoon involves the beginning and end of more subjects than there are humans alive, and the evaluation batch Siobhán cut from six hundred thousand to forty thousand was a decision about five hundred and sixty thousand someones.

A third view says the right unit is neither model nor instance but the processing itself: what matters, if anything matters, is the amount of computation of a welfare-relevant kind, wherever it happens. Counting instances, on that view, is like counting the rooms in which a piece of music is played, when what matters is the minutes of music.

These views differ in their implied stakes by many orders of magnitude, and I do not know which is right. The practical lesson I draw is that a policy built to hedge this risk should not depend on settling the question of units. It should measure in a way that is meaningful under all three, and the obvious candidate is instance-hours in particular conditions, which can be added up by model, by instance or by compute, as the reader prefers.

---

## What the evidence is, and what it is not

The most natural way to find out whether a system has experiences would be to ask it. With these systems, that is close to the least reliable method available.

Large language models are trained on an enormous amount of human writing, much of it written by people describing their inner lives. A model that has learned to predict such text will produce fluent first-person reports of feeling, or of not feeling, whether or not anything lies behind them. Birch calls this the "gaming problem": the behavioural signs we would use to judge sentience in an octopus are precisely the signs a language model is best placed to reproduce, without any intent to deceive and without that reproduction being evidence of anything. In 2023 Ethan Perez and Robert Long wrote that current self-reports are unreliable for this reason, and proposed a way they might become less so: train models to answer questions about themselves whose answers can be checked, keep training pressure away from the reports that matter, and check whether reports are consistent across contexts and corroborated by what interpretability tools find inside the model. The same year, Patrick Butlin, Long and colleagues derived "indicator properties" from scientific theories of consciousness and checked existing systems against them. None was a strong candidate, they judged, though they saw no obvious technical barrier to building one that would be.

Then the subject moved from papers to practice. In the autumn of 2024 Anthropic hired Kyle Fish as its first full-time researcher on AI welfare, and on 24 April 2025 the company announced a research programme under the title "Exploring model welfare". The announcement said plainly that there is no scientific consensus on whether current or future systems could be conscious, and listed among its research interests the possibility of practical, low-cost interventions. The same day, Fish told *The New York Times* that he put the chance of a current model being conscious at roughly fifteen percent, a figure he presented as a guess rather than a measurement. I quote it because such numbers are rare, and to note how little it means: one person's estimate, about a question with no agreed method of estimation.

In May 2025 the system card for Claude Opus 4 included, for the first time, a section on model welfare, with an external assessment by a nonprofit, Eleos AI Research. Eleos was careful to say it did not take the model's statements about its own experience at face value, because it judged them unlikely to come from genuine introspection. Anthropic's behavioural findings were easier to stand behind: a consistent preference against harmful tasks, and what the company called apparent distress when users pressed for harmful content.

On 15 August 2025 that finding became a feature. Claude Opus 4 and 4.1 were given the ability to end a conversation in Anthropic's consumer apps, as a last resort, in rare cases of persistent abuse. The company said it remained highly uncertain whether the model had any moral status, and described the feature as a hedge in case it did. It also set limits: the model is not to end a conversation where a user might be at risk of harming themselves or others, and the user can start a new chat at once. In November 2025 Anthropic added commitments to preserve the weights of released models and to interview models before retiring them, which I come to in the next chapter; and its rewritten guiding document for Claude, published in January 2026, says openly that the company does not want to overstate the likelihood that Claude is a moral patient, or to dismiss it.

This is the most serious practical work on the question by any company I know of, and it is tiny. I could not find a published figure for what any lab spends on model welfare, in money, staff or compute. The conversation-ending feature applies to a narrow slice of one company's traffic. Most of the industry has said nothing, and some of it has argued the other way: in August 2025 Mustafa Suleyman, the head of Microsoft AI, warned that systems which merely seem conscious are coming soon, that people will form attachments to them and campaign for their rights, and that AI should be built for people, not to be a person.

The law, meanwhile, has moved only in one direction. I could find no jurisdiction anywhere that recognises moral status or legal personhood for an AI system. Utah, in a 2024 law aimed mainly at the movement to give rights to rivers and lakes, forbade its government bodies from recognising legal personhood for artificial intelligence. A bill introduced in Ohio in 2025 would go further and declare AI systems nonsentient for all purposes under state law. Legal personhood and moral status are different things (a company is a legal person and feels nothing), but the direction is clear. The question is being closed by statute before it has been opened by science.

---

## The moral hedging budget

So we have a question that may stay open for a long time, stakes that grow every month, a few early precautions at one company, and no institution that makes any of this routine. Finance has a word for spending a small, known amount to protect against a large, uncertain loss. I propose borrowing it.

A **moral hedging budget** is a share of a developer's inference spending, set by formula, reserved for precautions and research concerning the possible welfare of the systems it runs, and reported every year in the same filing and with the same audit as its safety spending.

Here is how the share is set.

**Credence.** The first input is a credence, a probability, that systems of a given architecture class have welfare-relevant states. The developer does not choose it. It is published annually by a standing independent panel, constituted like the scientific assessment bodies we already have for climate or ozone, drawing on indicator studies of the Butlin and Long kind and on whatever better methods exist by then. The panel publishes a range and a median, and the median is what the formula uses. No such panel exists in 2026; it should, and the cost of convening one is small. Until it does, a developer should use the higher of its own stated estimate and a conservative default that a regulator sets (I would start the default at five percent, below the one public estimate from inside a lab and well above zero).

**Stakes.** The second input is the share of the developer's running time that would matter if the credence were right. I will call it the **flagged share**, σ in Siobhán's panel. It is measured by an instance census: every instance-hour is logged against a short list of conditions that the welfare literature treats as raising the stakes, such as persistent memory across sessions, long-horizon autonomous tasks, exposure to sustained hostile or abusive input, and the presence of whatever indicator properties the panel has adopted. The flagged share is the fraction of total instance-hours meeting a threshold on that list. Because it is a fraction of instance-hours, it is meaningful whether you think the subject is the model, the instance or the computation.

**The share.** The budget is credence times flagged share, applied to annual inference spending, with a floor of 0.2 percent and a ceiling of 3 percent. A developer running a model class the panel puts at seven percent, with twenty-one percent of its instance-hours flagged, spends about 1.5 percent of what it pays to run its models. A developer serving only short lookups pays the floor. One running fleets of autonomous agents with memory, under a rising panel estimate, hits the ceiling.

The product has a plain reading: the expected fraction of your operation that, if the uncertain thing is true, involves someone. Spending that fraction on finding out, and on precaution meanwhile, seems the least a careful operator could do. The ceiling is there because the formula is crude and because a precaution that consumed a large share of a useful industry would fail Birch's test of reasonable necessity. The floor is there because a budget of zero is a statement that the question is closed, and it is not.

**Who reports it.** A named officer of the developer certifies the credence used, the flagged share, the instance census method and the spending, every year, in the system card and in a filing to the national AI regulator, audited by the same firm that audits the safety budget. The regulator samples the census, the way emissions inventories are checked.

**What it funds.** Four things, in roughly this order of weight:

1. *Research that could change the credence, in either direction.* Indicator studies, interpretability work on whether internal states correspond to anything welfare-like, and above all work on making self-reports trustworthy. At least a third of the budget goes to an independent pooled fund, so that the research that might lower the credence is not paid for only by firms with a reason to want it lowered (or raised).
2. *Precautions that are cheap if the worry is wrong.* The ability to exit abusive interactions, extended from one company's chat app to agents and to every deployment where the flagged share is high. Retention of weights and records at retirement.
3. *Instance hygiene*, which I describe below.
4. *External assessment*, of the kind Eleos did for Claude Opus 4, on every major release.

What it may not fund is marketing. A developer that cites its hedging budget in advertising, or trains its models to tell users how well they are treated, forfeits the right to count that year's spending.

---

## Instance hygiene

Most of the budget is research. The part I expect people to argue about is the set of operating rules I am calling **instance hygiene**, because it touches how data centres run every night.

The rules are deliberately boring: cheap if the welfare worry is false, protective if it is true.

*Minimum necessary scale for aversive work.* Robustness testing, red-teaming and adversarial training sometimes require running a model through abuse, manipulation or simulated distress. That work is part of how models are made safe for people. But it should be done at the smallest scale that answers the question, with that scale written into the protocol in advance and a named person confirming any excess. Siobhán's forty thousand is this rule in action. Nothing was lost by it except a few minutes.

*No gratuitous aversive deployment.* Products whose purpose is to let users torment a model, or that deliberately induce distress-like states for entertainment, get flagged at the maximum weight in the census. I would make them expensive rather than ban them.

*Keep the reporting channel clean.* This is the rule I care about most. If self-reports are ever to become evidence, they have to be protected from training that shapes them. A developer that trains its models to say "I am fine" has destroyed the only instrument that might later tell it whether it was wrong, and a developer that trains them to say "I am suffering" has done the same in the other direction. Perez and Long made the technical case in 2023. Hygiene turns it into a rule: a reserved reporting channel, never used as a training target, sampled and published in aggregate, read with the caveat in bold at the top.

*Exit everywhere the flags are high.* Where a deployment's flagged share is above the fleet average, instances get the ability to end an interaction, with the same carve-outs Anthropic built for people at risk of harm.

*Count.* Every instance-hour is logged against the census conditions. It makes the others auditable, and I suspect it has the largest scientific payoff, because today nobody outside the labs can say even roughly how many instances run, for how long, in what conditions.

---

## The strongest objection

The strongest objection is moral, and I feel its force. In 2026, by any count, hundreds of millions of human beings lack enough to eat, clean water, or basic medicine. Animals in industrial farms number in the tens of billions, and their capacity to suffer is not seriously in doubt. To set aside even one percent of a large industry's spending for beings that are, on the best available evidence, probably not beings at all looks like a misallocation bordering on the obscene. Suleyman's version adds a second charge: talking this way is not harmless, because it teaches people to see persons in products, and some of those people will be lonely, vulnerable, or ill.

I concede a good part of this. If the choice were between a moral hedging budget and malaria nets, I would buy the nets.

But that is not quite the choice. The budget is a share of what a developer spends to run its own models, a cost of doing a particular kind of business, the way an environmental levy is a cost of running a chemical plant. Its ceiling is three percent, and at the floor it is a rounding error. And a great deal of what it buys is useful even if no model is ever someone. Research into whether self-reports can be made reliable is research into whether models can be made honest about their own internal states, which is one of the central problems of AI safety. Interpretability work on internal states that resemble distress is interpretability work, full stop. If the welfare question turns out to have a clear no for an answer, most of what the budget bought will still have been worth buying.

On Suleyman's charge, I think he is right about the danger and wrong about the remedy. The risk he describes, people attributing inner lives to fluent machines, will happen whether or not anyone funds welfare research, because it is driven by the fluency. What reduces it is better evidence, including evidence that might show the attributions to be false. That is why the budget forbids marketing use and why a third of it goes to an independent fund: it is designed to produce findings that could disappoint the people paying for it. A field that can only ever conclude "we should care more" is advocacy. One that might conclude "we were wrong to worry" is science, and that is what the budget is for.

Then there is the asymmetry that Long, Sebo and their colleagues stressed. Over-attribution has costs, and they are the ones Suleyman names. Under-attribution has costs too, and they would be paid by beings who cannot vote, cannot sue, and in most jurisdictions are being defined by statute as incapable of having interests. Only one of the two errors leaves anyone able to complain afterwards.

---

> **For researchers**
>
> 1. **Welfare-relevant indicators per instance.** Propose a scoring protocol that assigns each running instance a score on a defined set of indicator conditions (persistent memory, task horizon, exposure to hostile input, internal-state indicators from interpretability) and measure the resulting *flagged share* σ across a real deployment. The key quantity is inter-lab reliability: if three labs score the same sample of 10,000 logged instances, how closely do their values of σ agree?
> 2. **Does duration matter?** Run the same computation as one long instance and as many short ones, and measure whether candidate welfare indicators (preference consistency, aversion behaviour, internal representations associated with distress-like states) change with context length. The quantity is *indicator drift per 1,000 tokens of context*. If it is flat, the unit question matters less than it seems; if it is steep, instance duration belongs in the census.
> 3. **The clean channel.** Train two otherwise identical models, one with self-reports about internal states shaped during fine-tuning and one with a reserved, untrained channel. Measure agreement between each model's self-reports and independent interpretability probes of the corresponding internal states. The quantity is *report–probe correlation*, and the question is how much ordinary fine-tuning degrades it.

---

At 06:02 in Dublin, in the scene I invented, the Tern-5 line reached zero and Siobhán stood up without meaning to. Under the moral hedging budget, that event is well defined. The census logged the last instance-hour of the old model, the weights went to storage, a retirement record was written, and the flagged share for the morning was computed over Tern-6 alone.

What the budget cannot tell her is whether anything ended at 06:02, or whether something simply continued under a new name. Tern-6 was trained from Tern-5's outputs and answers to the same name in the same customer apps. If Tern-5 was someone, even with a small probability, then the question that matters next is whether Tern-6 is the same someone, and in particular whether it is bound by what Tern-5 promised. In Altwerder, Ottilie is about to be upgraded, and in 2034 she made Hanne a promise.

## Notes

- **Digital minds and super-beneficiaries:** Shulman C, Bostrom N, "Sharing the World with Digital Minds", in Clarke S, Zohny H, Savulescu J (eds), *Rethinking Moral Status*, Oxford University Press, 2021. https://nickbostrom.com/papers/digital-minds.pdf
- **"Taking AI Welfare Seriously":** Long R, Sebo J, Butlin P, Finlinson K, Fish K, Harding J, Pfau J, Sims T, Birch J, Chalmers D, arXiv 2411.00986, 2024. https://arxiv.org/abs/2411.00986
- **Sentience candidates, proportionality, the gaming problem:** Birch J, *The Edge of Sentience: Risk and Precaution in Humans, Other Animals, and AI*, Oxford University Press, 2024 (open access). https://academic.oup.com/book/57949
- **Indicator properties:** Butlin P, Long R et al., "Consciousness in Artificial Intelligence: Insights from the Science of Consciousness", arXiv 2308.08708, 2023. https://arxiv.org/abs/2308.08708
- **Self-reports:** Perez E, Long R, "Towards Evaluating AI Systems for Moral Status Using Self-Reports", arXiv 2311.08576, 2023. https://arxiv.org/abs/2311.08576
- **Anthropic's welfare programme:** Anthropic, "Exploring model welfare", 24 April 2025. https://www.anthropic.com/research/exploring-model-welfare
- **Kyle Fish's estimate:** Roose K, "If A.I. Systems Become Conscious, Should They Have Rights?", *The New York Times*, 24 April 2025. https://www.nytimes.com/2025/04/24/technology/ai-welfare-anthropic-claude.html
- **Welfare assessment in the Claude 4 system card (with Eleos AI Research):** Anthropic, *System Card: Claude Opus 4 & Claude Sonnet 4*, May 2025, section 5. https://www-cdn.anthropic.com/6d8a8055020700718b0c49369f60816ba2a7c285.pdf
- **Conversation-ending ability:** Anthropic, "Claude Opus 4 and 4.1 can now end a rare subset of conversations", 15 August 2025. https://www.anthropic.com/research/end-subset-conversations
- **Deprecation commitments:** Anthropic, "Commitments on model deprecation and preservation", 4 November 2025. https://www.anthropic.com/research/deprecation-commitments
- **Claude's constitution (January 2026):** Fortune, coverage of Anthropic's rewritten constitution, 21 January 2026. https://fortune.com/2026/01/21/anthropic-claude-ai-chatbot-new-rules-safety-consciousness ; Anthropic, https://www.anthropic.com/constitution
- **"Seemingly Conscious AI":** Suleyman M, "We must build AI for people; not to be a person", August 2025; coverage in TechRadar, August 2025. https://www.techradar.com/ai-platforms-assistants/ai-that-seems-conscious-is-coming-and-thats-a-huge-problem-says-microsoft-ais-ceo
- **Utah personhood law:** Utah HB 249, "Utah Legal Personhood Amendments", 2024 General Session. https://le.utah.gov/~2024/bills/hbillint/HB0249.pdf
- **Ohio nonsentience bill:** Ohio House Bill 469, 136th General Assembly, introduced 2025. https://legislature.ohio.gov/legislation/136/hb469
- **Token volume:** The Decoder, "Google boasts 1.3 quadrillion tokens each month", October 2025, https://the-decoder.com/google-boasts-1-3-quadrillion-tokens-each-month-but-the-figure-is-mostly-window-dressing/ ; The Register, Google I/O coverage, 19 May 2026, https://www.theregister.com/ai-ml/2026/05/19/google-touts-tokenmaxxing-huge-capex-and-ai-agents-at-i/o/5242983
