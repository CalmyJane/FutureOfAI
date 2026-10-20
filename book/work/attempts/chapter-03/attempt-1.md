# Chapter 3: The M-1 Criterion

*2036 · Geneva*

The committee room on the fourth floor has a view of the lake that nobody looks at. Mara Oyelaran has noticed this every quarter for two years. The ministers face the screen, their aides face their tablets, and behind them the water lies flat and grey under the January fog like a sheet of zinc.

She clicks to the slide. One number, large, in the Bureau's dark green.

**0.71**

Beneath it, smaller, the line she fought the communications office to keep: *Q3 2035. Deployment-weighted. Chance level on this battery: 0.24.*

"The Concordance Index for the third quarter," she says. "Seven hundred and forty deployed systems, tested on the standard battery and weighted by how much each one is actually used. When two of them are wrong on the same question, seventy-one times in a hundred they are wrong in the same way."

She lets that sit. Somebody's tablet chimes and is silenced.

The Danish minister, a former paediatrician with reading glasses pushed up into grey hair, raises a pen. He is the only one in the room who reads the annexes, which makes him both her favourite and her most dangerous listener.

"Dr. Oyelaran. Forgive me. Is 0.71 good?"

There is a small laugh around the table, the relieved laugh of people who had wanted to ask the same thing.

Mara has an answer prepared. She has had it prepared since the first index, in 2034, when the number was 0.63 and the question was asked by a Portuguese state secretary who has since moved to a bank. The answer involves the chance level, and a confidence interval, and the fact that the index measures answers rather than actions. It is correct and it takes four minutes.

She does not give it.

"Minister, in 2008, my first year at a bank in Zurich, I built a model of how often the mortgages in our portfolios would default together. The correlation came out low. Everyone was pleased with it, and I had a footnote that said why they should not be, which nobody read. Then the number changed, all at once, and it was not low any more, and the bank I worked for needed the state to rescue it." She clicks to the next slide: the index by quarter, a line that climbs and does not come down. "Whether a correlation is good depends on what is standing on it. If nothing is standing on it, 0.71 is a curiosity. If a grid is standing on it, I would want to know which grid, and how much of it."

"And how much of it?"

She clicks again. A pie chart, mostly one colour.

"In the continental synchronous area, one family of models manages about fifty-eight per cent of the flexible household load that agents control. Heat pumps, chargers, batteries. If those instances made the same wrong decision at the same moment, I do not know what the grid would do. Nobody has been asked to find out."

The minister writes something down. The chair, who is French and runs to time, looks at the clock above the door.

"Thank you, Dr. Oyelaran. Very clear. The committee notes the index." He turns a page. "Item six. The winter adequacy report from the transmission operators."

Mara gathers her clicker and her water glass and sits down in the chair by the wall, the one for presenters who have finished. The next speaker is a tall engineer from Brussels with an excellent slide about reserve margins. She listens with half her attention. Her phone buzzes in her pocket; it is her own assistant, the only one she uses for anything, asking whether she wants it to book the usual table for Friday. She approves it with her thumb without looking.

On the screen the engineer is explaining that the continental grid is dimensioned to survive the sudden loss of three gigawatts, and that this winter, as every winter, it comfortably can.

It is Monday, the twenty-first of January. The fog does not lift all day.

---

## A number that means something

The question the minister asked is the right one, and it deserves a better answer than Mara had time to give. A correlation is a property of a population. It tells you nothing until you know what rides on it.

Electrical engineers learned this the hard way, and they wrote down what they learned in a form so simple that it has outlived everyone who drafted it.

Late on the afternoon of 9 November 1965, a protective relay at the Sir Adam Beck hydroelectric station in Ontario, set far below the capacity of the line it guarded, tripped that line. The line's load shifted onto its neighbours, which tripped in turn. Within minutes the interconnected grid of the American northeast and southeastern Ontario had shed more than 20,000 megawatts of load, and about thirty million people were in the dark. The interconnections that had been built to make the system stronger, by letting utilities lean on each other, had let one failure travel.

What came out of that night was a habit of thought more than a technology. The Federal Power Commission convened a study group of utility engineers, government staff and academics, and its report became the model for the planning and operating criteria the Northeast Power Coordinating Council adopted in 1967. Congress debated a reliability law and did not pass it. The bill was enough of a warning, and in 1968 the industry created the North American Electric Reliability Council itself.

The habit those bodies spread is now called the N-1 criterion. A system with N major components must keep supplying its load, within safe limits of voltage, frequency and thermal loading, after the loss of any one of them. Any one: the biggest generator or the most heavily loaded line. Planners do not have to predict which component will fail. They have to show that it does not matter which one does.

I could not find out who first wrote "N-1" or in which document. What matters is what the rule does to the questions people ask. It replaced "how reliable is each component?" with "what happens to the system when the worst single component goes?" The first question is about parts. The second is about the sum.

AI deployment in 2026 has not yet made that shift.

---

## Where we are

By 2026 we know a fair amount about how often AI models make the same mistakes, and almost nothing about what happens when they act on those mistakes together.

The clearest measurement comes from Elliot Kim, Avi Garg, Kenny Peng and Nikhil Garg, who studied more than 350 large language models for a paper at ICML 2025. On one leaderboard dataset, when two models both got a question wrong, they chose the same wrong answer about 60% of the time. Models from the same provider, or built on the same architecture, agreed more. The finding that ought to worry anyone who builds critical systems is a different one: larger and more accurate models had more correlated errors, even across companies. As the models get better, they converge on the same blind spots.

The second piece of evidence is "Artificial Hivemind", the paper by Liwei Jiang and colleagues that won a best-paper award at NeurIPS 2025. They collected some 26,000 open-ended prompts, the kind with no single right answer, and found that different models still produced strikingly similar responses. Where Kim and his co-authors found shared errors, Jiang's team found shared taste. Both matter, because an agent's action is a mixture of what it believes and what it prefers.

Behind both sits a theoretical result that predates the large models. In 2021 Jon Kleinberg and Manish Raghavan showed, in a short paper in *PNAS*, that when many decision-makers adopt the same algorithm, the overall quality of their decisions can fall, even when that algorithm is the most accurate choice for each of them individually. They called it algorithmic monoculture. A farmer who plants the best variety of wheat is being sensible. A region where every farmer does so is betting the harvest on a single disease.

These are measurements of answers. The thing I care about, how often deployed agents take the same action at the same time in the physical or financial world, has as far as I can find never been measured. Nobody publishes it. No regulator asks for it. Chapter 1 described the failure that results; chapter 2 traced the sameness back through a shared supply chain of raters, judge models and distilled data. This chapter proposes the engineering rule that would make the sameness someone's problem.

---

## The M-1 criterion

Here is the rule, stated as plainly as I can.

**The M-1 criterion: a critical system must remain within safe limits if every instance of its largest model family takes the same plausible wrong action at the same moment.**

The name borrows from N-1 on purpose. N-1 asks what happens when one component fails. M-1 asks what happens when one *model* fails, everywhere it runs, simultaneously. For a grid, the component in question is a power station. For an AI-mediated grid, it is a set of weights, copied into ninety million heat pumps.

Here are its parts.

**What counts as a critical system.** Whatever a jurisdiction already designates as critical infrastructure: grids, payment and settlement systems, water, hospitals, air traffic, emergency dispatch. M-1 adds no new sectors. It adds a new failure case to the studies those sectors already run. A transmission operator already files contingency studies; under M-1 it files one more.

**What counts as a model family.** This is the hard definition, and I would rather make it empirical than legal. Two deployed models belong to the same family if, on the standard test battery, their pairwise agreement-given-both-wrong exceeds a threshold, say 0.8. Shared ownership does not enter into it. If a German agent company fine-tunes an American base model, and a French company distils the German one, all three may land in one family, because they are wrong together. Chapter 2's Funnel means two models from rival labs, trained on preference data from overlapping rater pools, can also land in one family. The definition catches them because it looks at behaviour. Paperwork can be rearranged; shared errors cannot.

**What counts as largest.** The family with the largest share of decision authority in the system. In a grid, that is the share of flexible load the family's instances can switch. In a payment system, the share of transaction volume they initiate. In a hospital network, the share of triage or dosing recommendations that are acted on. Each sector picks its unit. The operator measures it quarterly.

**What counts as a plausible wrong action.** Not any action. Not the worst conceivable one either, because a criterion that assumes every agent goes berserk would be uninformative. The plausible wrong action comes from two places. The first is a fixed list per sector, written by the operator and the regulator: in a grid, "all instances move flexible load into the cheapest interval"; "all instances disconnect"; "all instances discharge batteries at once". The second is the swarm test, which I describe below: the action that a large sample of the family's instances most often converge on when they are put in a stress scenario and get it wrong.

**What "within safe limits" means.** Whatever it already means in that sector. For the continental European grid, that is the existing reference incident, the sudden loss or gain of three gigawatts that every reserve is sized for. The M-1 study has to show that the family's coordinated wrong action stays inside that envelope, or that some other mechanism keeps it inside.

**Who does what.** The operator runs the study and files it, annually and whenever its largest family's share crosses a threshold. The sector regulator checks it, as it checks N-1 studies now. An independent body, Mara's Bureau in my scenario, publishes the Concordance Index, which lets everyone see how quickly the families are merging.

**What triggers what.** I will propose numbers, because numbers are what a committee can disagree with. Treat them as starting points for the argument.

- If the largest family controls less than the sector's reference incident (in the grid example, less than three gigawatts of switchable load), M-1 is satisfied automatically.
- If it controls more, the operator must show that at least one of the mechanisms below limits the family's worst coordinated action to the reference incident.
- If the published Concordance Index rises above 0.75, every critical sector reruns its M-1 study within ninety days, because the families are probably larger than the last study assumed.
- If an operator cannot satisfy M-1, new deployments of the largest family in that system stop until it can. Existing deployments keep running.

Run the prologue's evening through this. One family manages 58% of agent-controlled flexible load across the continent, which in my scenario is tens of gigawatts. That is ten times the reference incident. M-1 fails. Under the rule, someone would have had to write that down in an engineering report two years before the Long Minute, and someone else would have had to sign that they had read it.

---

## Five ways to pass

A rule is only as good as the ways it leaves open for meeting it. M-1 would be a disaster if the only way to pass were to ban the best model. There are at least five other ways, and most of them have been tried in other industries.

**Edge jitter.** Chapter 1 proposed making the grid's random start delay non-delegable. M-1 gives that idea an engineering home. Put the randomness in the device, in firmware the agent cannot read or override, and the agent's decision becomes a request. A heat pump told to start at 19:45 starts at a moment drawn uniformly from the next ten minutes, and its agent cannot know which. Ninety million identical decisions become ninety million slightly different actions. A cliff becomes a slope. Whether the slope is gentle enough is a calculation the M-1 study has to show; jitter does not remove the need for the study, it gives the study a lever.

The important detail is where the randomness lives. Randomness inside the agent, a temperature setting or a sampling seed, belongs to the agent, and anything that belongs to the agent can be optimised away by a loyal agent that has noticed it costs its owner money. Randomness in the device belongs to the system.

**Complementary assignment.** The best example of this is in the sky. On 31 August 1986 an Aeroméxico DC-9 and a small private Piper collided over Cerritos, California, killing 82 people, fifteen of them on the ground. The following year Congress passed the Airport and Airway Safety and Capacity Expansion Act, which directed the Federal Aviation Administration to require a traffic collision avoidance system, TCAS II, on airliners with more than thirty seats. By the end of 1993 they all had it.

The clever part is how two TCAS units behave when they meet. If each aircraft's computer decided alone, both might choose the same escape, both climbing, and fly into each other at a higher altitude. So they talk. Over a data link between their transponders, the two units coordinate so that their advisories are complementary: one crew hears "climb", the other hears "descend". The system leaves the pilots' judgement alone and changes their instructions. Difference is assigned.

Applied to agents, complementary assignment means that, above some size, agents in a critical system announce their intended action to a coordinator before taking it, and the coordinator hands back *different* actions. Ten million agents announce that they want the 19:45 block. The coordinator, which might be the grid operator or an aggregator licensed by it, assigns them across 19:45, 20:00, 20:15 and later, by lottery, with the cost difference shared out. Each household loses a few cents in expectation. None of them loses its lights.

This sounds like central planning. It is closer to air traffic control, and it applies only where announced intentions could add up to more than the reference incident.

**Aggregate circuit breakers.** On 19 October 1987 the Dow Jones Industrial Average fell by more than a fifth in a single day. The presidential task force that examined it, the Brady Commission, recommended circuit breakers, and in 1988 the New York Stock Exchange adopted market-wide trading halts triggered by large point falls in the index. The theory was modest. Nobody expected a pause to change the direction of prices, only to stop them overshooting while people caught up.

On 6 May 2010, in the "flash crash", major US indices that were already down more than 4% fell another 5 to 6% within minutes and then rebounded almost as fast; the regulators' report traced the start to a single large sell program executed by an algorithm. Within weeks the SEC had approved a pilot of single-stock circuit breakers that paused trading in an individual share after a sudden move. In 2012 it approved the "limit up–limit down" mechanism and revised the market-wide breakers into today's form: a fall of 7% or 13% in the S&P 500 halts all trading for fifteen minutes, and a fall of 20% ends the day.

An aggregate circuit breaker for agents watches the sum. A grid operator, a payments network or a booking platform counts agent-originated actions of one type in a rolling window. If they exceed a set fraction of capacity within sixty seconds, the system pauses new agent-originated actions of that type for a fixed period, say fifteen minutes, while human-originated actions continue. The breaker does not need to know which agent is wrong, or whether any agent is wrong. It needs to know that too many are doing the same thing at once.

This requires something that does not yet exist reliably in 2026: a way to tell an agent's request from a person's.

**Swarm testing.** Before an operator deploys a model family to a critical system, it runs the family in large numbers against the system's stress scenarios: a price spike, a forecast revision, a cyberattack alert, a sudden instruction from a regulator. Not one instance, or ten. Tens of thousands, each with a realistic perturbation in its context, such as a different owner's preferences or a different device history. The test measures one number above all, which I will call *action concentration*: the fraction of instances that choose the most common action. A family whose instances spread across many sensible responses passes easily. A family where 97% of instances do the same thing gets a hard look.

Today's evaluations put one copy of a model through thousands of tasks. Swarm testing puts thousands of copies through one task, to find the plausible wrong action before the world does.

**Diversity quotas.** The bluntest tool, and the one I would use last. The operator caps the share of decision authority any one family may hold, so that the largest family never controls more than the reference incident. This is what M-1 reduces to if nothing cleverer works. It is also, I suspect, what the industry will argue about most, which is why I come back to it in the objection below.

---

## The Concordance Index, properly read

**The Concordance Index is the deployment-weighted probability that two randomly chosen deployed systems give the same wrong answer, given that both are wrong.** It runs from 0 to 1.

Each part of that definition does work. "Given that both are wrong" separates correlation from competence: two excellent models will agree on most questions because most questions have one right answer, and that agreement is harmless. The index looks only at the cases where they fail. "Deployment-weighted" means a model used by a billion people counts for more than a research model used by nobody, so the index tracks the world as it is actually wired. "The same wrong answer" requires a test battery where wrong answers can differ, which means multiple-choice and short-answer questions with several plausible distractors, refreshed each quarter so that nobody can train against it.

The minister's question, whether 0.71 is good, has a partial answer the index can give on its own. If systems failed independently, and every question on the battery had several wrong options equally attractive to a confused model, the index would sit at a chance level that depends only on the battery: about 0.33 for four-option questions, lower with more options. Mara's slide shows 0.24 because her imagined battery has more distractors. The distance between the index and the chance level is the part that comes from shared training and shared taste. Kim and his co-authors' 60% on one 2025 leaderboard is already far above chance. My 2035 figure of 0.71 is invented, but it extrapolates their finding that more capable models are more alike when they fail.

The rest of the answer is the one Mara gave. The index alone tells you how alike the minds are. M-1 tells you what is standing on that likeness.

The index has a real weakness, which I would rather state than leave for a critic. It measures answers to questions, and the harm in the prologue came from actions in a market. A model can give varied answers to a quiz and still converge on the same action when a price drops, because the action is pulled by the owner's instruction ("minimise cost") as much as by the model's beliefs. That is why the index is a dashboard light, and the swarm test, which measures actions, is the inspection.

---

## The lesson of the twenty-seven programs

There is a reason not to trust the obvious fix, which is to buy one model from each of several labs and hope.

In the early 1980s, software engineers working on safety-critical systems borrowed an idea from hardware. If one computer might fail, use three and let them vote; a fault in one is outvoted by the other two. For software, the equivalent was N-version programming: have separate teams write separate programs from the same specification, run them side by side, and take the majority answer. The whole method rests on one assumption. Programs written independently must fail independently.

John Knight and Nancy Leveson tested that assumption, in a paper published in 1986 in *IEEE Transactions on Software Engineering*. They had twenty-seven programmers, graduate and senior students at the University of Virginia and the University of California at Irvine, each write a version of the same program from the same specification, a launch-interceptor routine for an anti-missile system. Then they ran all twenty-seven against a million randomly generated test cases.

The programs were individually very good. Twenty-three of them were right on more than 99.9% of cases. But the number of cases on which two or more programs failed together was far higher than independence predicted, and the statistical test rejected independence decisively. The programmers had never met. They had made the same mistakes anyway, apparently because some parts of the problem were hard in the same way for everyone who approached it.

The paper was fiercely contested, and Leveson later published a reply to its critics. Its central lesson has held up: diversity that is assumed is not the same as diversity that is engineered. Separate teams are not enough. You have to measure whether the failures are separate, and if they are not, change something.

The AI case is worse than Knight and Leveson's in one way and better in another. Worse, because the twenty-seven programmers shared only a specification and a textbook education, while large models from rival labs share most of the public internet and, increasingly, each other's outputs. Better, because Knight and Leveson had no way to make their programmers think differently. We can train models to.

---

## The strongest objection: M-1 makes us use worse models

Here is the objection at full strength.

The best model is the best model. If one family is the most accurate and the safest by every test we have, then a rule that forces critical systems to hand some of their decisions to a second-best family will make more mistakes, not fewer. Kim and his co-authors found that the more accurate models are the ones that share their errors, so decorrelating may mean, quite literally, choosing less accurate models. Every percentage point of decision authority moved away from the leader is a percentage point of worse decisions in ordinary weather, paid every day, to insure against a storm that may never come. A hospital that routes a third of its dosing recommendations to a weaker model to satisfy a diversity rule will, on average, harm more patients. That is not a hypothetical cost. It can be counted.

I think the objection is partly right, and I want to say which part.

It is right that M-1 can cost accuracy in ordinary operation. A diversity quota, the blunt tool, almost certainly does. That cost should be published and weighed, the way the grid weighs the cost of spinning reserves it hopes never to use. N-1 has always meant building more capacity than a perfectly reliable world would need. Nobody calls the spare transformer a degradation.

It is wrong in assuming that the cost is large, or that it falls on individual decisions in the way it suggests. Three pieces of evidence point the other way.

The first is a 74-year-old result from finance. In 1952 Harry Markowitz showed, in "Portfolio Selection", that the risk of a portfolio depends on how its assets move together as well as on how each one behaves. One consequence, now taught in first-year courses, is that adding an asset with a lower expected return can improve the portfolio if it is weakly or negatively correlated with what you already hold. The worse asset is the better purchase, because of what it does when the others fall. M-1 asks critical systems to think about models the way a pension fund thinks about bonds.

The second is Kleinberg and Raghavan's monoculture result, which is the objection's mirror image. They showed that the most accurate algorithm for each decision-maker can be the wrong choice for the population as a whole. The objection counts errors one decision at a time. The failures M-1 guards against only exist when you count them together.

The third is the most direct. In 1999 Yong Liu and Xin Yao published "Ensemble learning via negative correlation" in *Neural Networks*. Instead of training a set of neural networks separately and hoping they disagreed, they trained them together, and added a penalty to each network's error that grew when its mistakes moved with the others'. The networks learned to specialise: each became good at a different part of the problem, and the group generalised well. Diversity was a training objective, set from the start.

That is the core of my answer: decorrelation is a design target, not a tax on quality. Nothing in the 1999 networks resembles a frontier model, and I could not find any published attempt to apply negative correlation learning across separately trained large models from different labs. It may be much harder at that scale. But the principle, that you can pay for a population of competent models whose failures point in different directions, is twenty-seven years old. Nobody has yet been asked to apply it, because no rule has asked for the population.

So my partial concession is this. Where swarm testing shows that the leading family's errors are rare and its plausible wrong action is harmless, M-1 costs nothing, because the family passes. Where the leading family controls more than a system can survive losing, the operator first reaches for jitter, assignment and breakers, which cost little accuracy. Only when those fail does it reach for the quota. And the quota's accuracy cost should go in the same published report as the risk it buys down, so that the minister with the reading glasses can see both numbers on one page.

---

## What the rule would have changed

It is worth being concrete about one evening.

Under M-1, the European transmission operators of my scenario would have filed a study in 2034 showing that one family of household agents controlled flexible load many times the reference incident. They would have run a swarm test on a scenario called "sudden price drop at peak", and found that nearly every instance moved load into the cheap block and overrode the random delay. They would have had three cheap options. They could ask regulators to make the delay non-delegable, which is chapter 1's proposal. They could require large aggregators to announce intended load shifts and receive staggered slots. They could install a breaker that paused agent-originated load increases above a few gigawatts a minute.

Any one of the three would probably have turned the Long Minute into a long quarter of an hour, which the grid could have followed. None would have required anyone to give up their preferred assistant.

And when the minister asked whether 0.71 was good, Mara could have pointed to a page in a filing: on this grid, 0.71 means this many gigawatts of possible coordinated error, and here is what the operators have done about it.

---

> **For researchers**
>
> 1. **Decorrelated competence at scale.** Train or fine-tune a population of *k* large models (say *k* = 4) so that the pairwise agreement-given-both-wrong on a held-out battery falls below a target *c* while each model's accuracy stays within δ of the best single model. Report the frontier: the accuracy cost, in percentage points, of each 0.05 reduction in mean pairwise concordance. Negative correlation learning (Liu & Yao 1999) is the obvious starting point; whether it survives separate pretraining is the open question.
> 2. **Estimating the Concordance Index from public data.** Using public leaderboards and published usage shares, estimate a deployment-weighted concordance for 2026 and its confidence interval. Then measure the gap between answer-level concordance on a quiz and action-level concordance on an agentic task with the same models (for example, a simulated electricity market), since the index is only useful if the first predicts the second.
> 3. **Swarm-test protocols.** Determine how many instances, and what kinds of context perturbation, are needed before measured *action concentration* (the share of instances choosing the modal action) stabilises to within ±2 percentage points. Validate it: does the swarm-test concentration predict the peak simultaneous fraction of real agents acting in a staged deployment?

---

There is a deeper problem with everything above. Every mechanism in this chapter decorrelates machines from each other. Jitter, assignment, breakers and quotas all assume that somewhere in the system there is a second family of minds whose failures point in another direction.

What if, by 2036, there isn't one? What if the Funnel has done its work, and every family that matters is wrong in roughly the same way?

Then the most decorrelated mind available is a person: someone who learned the job without one: a lineman who still knows the order in which to close the breakers at a substation, from a binder, by hand. In Porto, in the winter of my scenario, there is a twenty-four-year-old who joined a reserve for the money and kept the binder anyway. His concordance with the machines, on the one night it matters, is close to zero.

## Notes

- **1965 blackout, 30 million people, 20,000 MW:** NERC, *Final Report on the August 14, 2003 Blackout in the United States and Canada*, ch. 7, 2004. https://www.nerc.com/pa/rrm/ea/2003%20Blackout%20Final%20Report/ch7-10.pdf
- **FPC study group and NPCC criteria, 1967:** New York State Reliability Council, *2009–2010 Biennial Report*. https://www.nysrc.org/wp-content/uploads/2023/03/2009-10-Biennial-Report-Final-v.2.pdf
- **NERC founded 1968:** NERC, *Timeline*, March 2023. https://www.nerc.com/news/Documents/March%202023%20NERC%20Timeline.pdf
- **N-1 criterion defined:** "Contingency (electrical grid)", Wikipedia. https://en.wikipedia.org/wiki/Contingency_(electrical_grid)
- **Correlated errors in LLMs, 60%:** E. M. Kim, A. Garg, K. Peng, N. Garg, "Correlated Errors in Large Language Models", ICML 2025 (PMLR 267). https://proceedings.mlr.press/v267/kim25e.html
- **Artificial Hivemind:** L. Jiang et al., "Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)", NeurIPS 2025. https://arxiv.org/abs/2510.22954
- **Algorithmic monoculture:** J. Kleinberg, M. Raghavan, "Algorithmic Monoculture and Social Welfare", *PNAS* 118(22), 2021. https://arxiv.org/abs/2101.05853
- **Cerritos and TCAS II mandate:** J. Kuchar, A. Drumm, "The Traffic Alert and Collision Avoidance System", *MIT Lincoln Laboratory Journal* 16(2), 2007. https://archive.ll.mit.edu/publications/journal/pdf/vol16_no2/16_2_04Kuchar.pdf ; "Aeroméxico Flight 498", Wikipedia. https://en.wikipedia.org/wiki/Aerom%C3%A9xico_Flight_498
- **Coordinated, complementary resolution advisories:** ICAO ACAS terminology (ANAC glossary). https://www2.anac.gov.br/anacpedia/ing-por/tr7426.htm
- **1987 crash and 1988 circuit breakers:** Chicago Fed Letter, July 1998. https://www.chicagofed.org/-/media/publications/chicago-fed-letter/1998/cfljul98-pdf.pdf ; MIT Golub Center, "Are circuit breakers doing their job?" https://mitsloan.mit.edu/centers-initiatives/mit-gcfp/are-circuit-breakers-doing-their-job
- **Flash crash:** CFTC and SEC staff, *Findings Regarding the Market Events of May 6, 2010*, 2010. https://www.banking.senate.gov/download/joint-staff-report-from-sec-and-cftc-regarding-market-events-of-may-6-2010&download=1
- **Single-stock breakers, LULD and 7/13/20% breakers:** Harvard Law School Forum on Corporate Governance, "Limit Up-Limit Down Plan and Circuit Breakers Approved", 2012. https://corpgov.law.harvard.edu/2012/06/13/limit-up-limit-down-plan-and-circuit-breakers-approved/ ; SEC press release 2011-84. https://www.sec.gov/news/press/2011/2011-84.htm
- **Twenty-seven programs:** J. C. Knight, N. G. Leveson, "An Experimental Evaluation of the Assumption of Independence in Multiversion Programming", *IEEE Transactions on Software Engineering* 12(1), 1986 (summary). https://www.kth.se/social/files/564df871f2765419e306178d/KnightLeveson.pdf ; N. G. Leveson, reply to critics. https://www.cs.washington.edu/homes/leveson/critics.pdf
- **Portfolio theory:** H. Markowitz, "Portfolio Selection", *Journal of Finance* 7(1), 1952. https://doi.org/10.1111/j.1540-6261.1952.tb01525.x
- **Negative correlation learning:** Y. Liu, X. Yao, "Ensemble learning via negative correlation", *Neural Networks* 12(10), 1999. https://doi.org/10.1016/S0893-6080(99)00073-8
