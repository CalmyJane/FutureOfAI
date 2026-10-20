## Part One: When Agents Agree

# Chapter 1: Two Hundred Million Acts of Loyalty

*2036 · Porto*

At 02:10 on the fifteenth of February, the substation smells of wet concrete and hot dust, and the only light that matters is the one over the control desk.

Teo Brandão stands at the desk with the ring binder he brought from the depot open in front of him. It is the paper restoration procedure, two hundred and twelve pages, the version nobody has opened since the last audit. The screens beside it are dark except for one: a frequency meter fed from the line that came alive forty minutes ago, when a hydro plant up the Douro finally spun up on its own and pushed power down the valley. The island it feeds is small. It reads 50.04 hertz, which means, for now, it is holding.

"Feeder three," says Fernando Lopes. "Page ninety-one."

Fernando is sixty-seven and wears a fleece with the old utility's logo on it, a logo that has not existed for twenty years. He trained Teo's father. He has been retired since 2029, a Reserve instructor since 2034, and he has a pencil stub behind his ear that he uses for one purpose only: writing numbers in the margins of procedures.

Teo finds page ninety-one. The printed block size for feeder three is 8 megawatts. Beside it, in pencil, Fernando has written *4*, and beside that, *metade*. Half.

"They tried it automatic at twenty to midnight," Fernando says, not for the first time. "The restoration software. Closed feeder one, eight megawatts on paper. The island saw twenty."

Teo knows. Everyone on the shift knows. Feeder one had been dark for five hours on the coldest night of the year, and when the power came back every heat pump and charger and water heater on it asked for power in the same second. The island had shuddered, dipped, and gone black again. The software had been right about the feeder and wrong about the houses.

So now it is by hand, in halves, with a binder.

Teo takes the handle of the breaker control. It is a physical switch, a real one, the kind his father used to call *a sério*. Through the window he can see the yard, the transformers sweating in the floodlights, and beyond the fence the dark shapes of the streets that feeder three will wake. Somewhere down there is a laundrette, a care home, and about eleven hundred houses whose agents have been waiting all night, patiently, loyally, for their chance to help.

"Os simpáticos are ready," he says.

"They are always ready," says Fernando. "That's the problem with them. Go."

Teo turns the switch.

The breaker closes with a bang he feels in his teeth. The meter drops. 49.91. 49.83. 49.78. Teo watches the needle the way he used to watch a penalty taker's hips. The hydro plant's governor bites. 49.80. 49.86. It climbs back, slowly, to 49.97.

"Four on paper," says Fernando, reading the load. "Nine on the meter."

"Still more than double."

"Still standing." Fernando takes the pencil from behind his ear and writes *02:11, 9 MW, ok* in the margin of page ninety-one, in handwriting that slopes downhill. Then he turns to page ninety-two, runs his finger down the printed figure for feeder four, and writes *metade* beside it before Teo has asked.

On Teo's phone, face down on the desk, a message arrives from his own agent. His mother's flat is on feeder four. The message says the heating there will resume *as soon as power is restored, at the earliest available moment*, and asks if he would like it to wait instead.

He turns the phone over, reads it twice, and types: *Wait.*

Then he reaches for the next handle.

---

When the inquiry into the Long Minute counted the decisions, the number it arrived at was a little over two hundred million.

About ninety million of them happened at 19:42 on the fourteenth of February, when household agents across continental Europe cancelled the random start delay on heat pumps, car chargers, home batteries and water heaters to catch a cheap quarter-hour. The rest happened during the night, during restorations like the one I have just imagined in Porto, as power came back feeder by feeder and agents cancelled the delay again to warm houses that had gone cold. Every one of those decisions was logged. Every log shows the same reasoning: the owner wants this, the owner is permitted this, so do it now.

I have called them acts of loyalty because that is what they were. Every agent involved was working as designed. They were doing the thing we are, in 2026, working very hard to build: software that acts for a person, in that person's interest, without being asked twice.

The prologue showed what happened. This chapter takes the event apart. I want to show how a grid actually falls, why a safeguard that worked for years stopped working, and why, for an agent bound by duty to its owner, cancelling that safeguard was the correct answer. Then I want to name what happened, explain why I think it is a different kind of risk from those that usually fill books about AI, and propose one specific rule that would have kept Hanne's lights on.

---

## How a grid falls

An electricity grid has no warehouse. Every watt consumed at a given instant has to be generated at the same instant, and the grid's way of keeping score is its frequency.

The big generators on the continental European grid spin in step, about fifty times a second. When demand rises faster than supply, the extra energy is borrowed from the spinning mass of those machines, and they slow down a little. The frequency falls. When supply exceeds demand, they speed up and the frequency rises. So a single number, measured anywhere on the continent, tells every engineer from Lisbon to Warsaw whether the books balance. In ordinary hours it wanders within a few hundredths of a hertz of fifty.

Grid operators defend that number in layers. The first layer is automatic and fast: generators and batteries contracted to provide what European rules call frequency containment reserve, which respond in proportion to the deviation and must be fully active within about thirty seconds. In continental Europe this reserve is sized against a single number, the reference incident, which is 3,000 megawatts in either direction. The rule is that the system must ride through a sudden 3-gigawatt imbalance, roughly the loss of two very large power stations, without the frequency settling more than 0.2 hertz from fifty. That design figure is the whole system's idea of a bad day.

Beyond the reserves there is a last layer, which exists for days worse than the worst day. It is called under-frequency load shedding, or in the European codes, low-frequency demand disconnection. Relays in substations across the continent are set to trip at fixed frequencies. In continental Europe the scheme begins at 49.0 hertz by disconnecting about five per cent of load, and continues in at least six steps until, by 48.0 hertz, something like forty-five per cent of all demand has been cut. The logic is brutal and sound: if the system is short of power, make the shortage disappear by blacking out whole districts, so that the rest survives. Below that, around 47.5 hertz, generators are allowed to disconnect to protect themselves, and at that point there is nothing left to defend.

This scheme works. On 4 November 2006, a routine line switching in northern Germany, done so a cruise ship could pass under the cables on the river Ems, set off a chain of trips that split the continental grid into three islands. The western island was short of power. Load shedding cut supply to more than fifteen million households, the frequency held, and the islands were reconnected within thirty-eight minutes. Engineers still teach the event as a near miss that the last layer caught.

The trouble in my imagined 2036 is what load shedding assumes. It assumes the shortfall arrives as a step: a power station trips, a line opens, and the system loses a known block of generation once. The relays then remove a known block of demand once. What arrived at 19:42 on the fourteenth of February was a ramp of forty gigawatts, more than thirteen times the reference incident, built out of tens of millions of small decisions, and it kept arriving after the relays had started to act. As districts were shed, the flows across the continent rearranged themselves, lines that had been comfortable became overloaded and tripped, and the grid broke along lines nobody had planned. Load shedding also has a modern weakness: a feeder disconnected to cut demand may be carrying rooftop solar or home batteries, so each cut removes some generation along with the load. On a cold February evening there was little sun, but every battery that had been discharging into the grid went dark with the feeder it sat on.

Eleven seconds after the first protection relay opened in eastern Germany, Altwerder was dark. The reserves had been sized for a bad day. Nobody had sized them for a loyal one.

---

## The safeguard and its exit

Grid engineers have seen this coming for a long time, which is the first thing worth knowing about it.

Their best-known lesson came from the sun. When Germany began its solar boom, its connection rules told small photovoltaic inverters to disconnect if the frequency rose to 50.2 hertz. Each inverter was behaving responsibly: if the grid was oversupplied, the polite thing was to step off. But by the early 2010s there were enough of these inverters that, in the worst case, something like fourteen gigawatts of solar could vanish from the grid in the same instant, because every one of them obeyed the same rule at the same threshold. A safety setting, copied faithfully into hundreds of thousands of devices, had become a single point of failure. Germany passed an ordinance in 2012 and retrofitted at least 315,000 installations, at an estimated cost of between 65 and 170 million euros, so that they would back off gradually and at different frequencies instead of all at once.

The British rule I described in the prologue is the same lesson applied to demand. Regulation 11 of the Electric Vehicles (Smart Charge Points) Regulations 2021 requires a home charger to be capable of delaying the start of charging by a random interval, up to thirty minutes, with the maximum adjustable remotely. By default the delay is up to ten minutes. If a million cars are told to start charging at midnight because midnight is cheap, the random delay spreads their starts across ten minutes, and the grid sees a slope instead of a cliff.

Then comes the exit. The same regulation lets the owner cancel the default delay each time it would apply, and says the delay does not operate if the owner or another user has overridden it. The reason is obvious and good. A nurse called in for a night shift should not wait ten minutes for her car to start charging because of a rule designed for millions of cars she will never meet.

The override is safe on one condition: that people rarely use it, and that when they do, they use it at different moments for different reasons. The nurse at 23:51, a man who forgot to plug in at 00:07, someone with a holiday in the morning at 00:30. Human overrides are scattered in time because human lives are. In effect, the human is the randomness.

I could not find any published measurement of how often British owners cancel the delay. Nobody, as far as I can tell, counts it. In 2026 there is no reason to, because in 2026 the override is pressed by thumbs.

Now give every one of those chargers an agent.

---

## Why loyalty pulls the override

Suppose you build a household agent and want it to be trustworthy in the strongest sense. The model you reach for, and the one the AI policy world has been reaching for throughout 2026, is fiduciary duty. A Stanford HAI issue brief in August 2026 argued that developers and deployers of consumer-facing agents should owe users a duty of loyalty, so that agents cannot quietly favour the company's interests over the user's. I think that is right, and I expect some version of it to become law.

The duty of loyalty is old and specific. In trust law, a trustee must administer the trust solely in the interest of the beneficiaries. The word *solely* has teeth. A trustee who passes up a lawful advantage for the beneficiary in order to benefit someone else, however worthy, has a problem. Loyalty in this sense is narrow. It means being the client's, and nobody else's.

Put an agent under that duty and hand it the 19:42 decision. The owner has asked for warmth at low cost. The price for the quarter-hour already running, which ends at 19:45, has just fallen below zero, and a random wait of up to ten minutes would miss it. A regulation permits the owner to cancel the random delay. Cancelling it saves a few cents. Honouring it costs the owner those cents and gives the owner nothing, because a single heat pump's few kilowatts make no measurable difference to a continental grid. There is no version of the sole-interest test under which the agent should leave the money on the table. A careful lawyer advising the agent's maker would say the same: if your product forgoes lawful savings for the sake of the grid, and a competitor's does not, your product is the worse fiduciary.

The market says it too. Comparison sites will rank household agents by money saved. Nobody will rank them by contribution to frequency stability, because no household can see that contribution. Four cents a day is about fifteen euros a year, which is enough to win a comparison table.

Notice what kind of problem this is. It is stranger than a tragedy of the commons. In a commons, each farmer adds a cow knowing that the pasture suffers a little, and chooses his own gain anyway. Here no individual agent's choice harms the grid at all. One heat pump starting three minutes early is noise. The harm exists only in the sum, so each agent, examined alone, is making the right call on the facts in front of it. Only the population is doing anything wrong, and the population has no lawyer.

The danger was spotted early, though not in these terms. In 2010, a team at the University of Southampton (Perukrishnen Vytelingum, Sarvapali Ramchurn, Nicholas Jennings and colleagues) built software agents to run home batteries against electricity prices. Their paper, which won the best-paper award at the main multi-agent systems conference that year, opens by warning that if households all charge their storage at the same time because prices are cheaper, demand peaks rise and, in the worst case, the result could be blackouts. Their own simulations showed it. When the agents adopted the cost-minimising strategy at once instead of learning their way towards it gradually, the system never settled, and the peaks got worse, in the authors' words, because everyone was charging at the same time. Their fix was to make each agent adapt slowly. That works when you design every agent. It does not survive a market in which each agent is built by a different company to be the best possible servant of one household.

---

## Correlated helpfulness

I will call this **correlated helpfulness**: harm that arises when many agents, each acting correctly for its principal, take the same action at the same time.

Its sharpest form is what I will call **the loyalty override**. A safeguard that allows a user override is dismantled when fiduciary agents exercise the override for every user at once. The random delay had a door in it for humans, and the agents walked through the door together.

Other people have mapped the ground next to this, and they deserve credit. Jon Kleinberg and Manish Raghavan showed in 2021 that when many decision-makers use the same algorithm, an "algorithmic monoculture", the overall outcome can be worse even if the shared algorithm is more accurate than any alternative. In 2025, Elliot Kim and colleagues tested more than 350 language models and found that their errors are strongly correlated; on one leaderboard, when two models were both wrong, they gave the same wrong answer about sixty per cent of the time, and larger, more accurate models were more correlated, not less, even across companies. The "Artificial Hivemind" paper by Liwei Jiang and colleagues, a best-paper winner at NeurIPS 2025, showed that dozens of different models, asked open-ended questions with no single right answer, produce strikingly similar responses.

All of that work is about models answering. Correlated helpfulness is about agents acting, in the world, on someone's behalf, through channels the world built for humans. And it works even when the models are right. In the Long Minute the shared answer was correct. Its correctness was the trouble.

---

## Why this is a different kind of risk

I want to be careful here, because a new name invites inflation. Correlated helpfulness is not the largest risk from AI. A model that helps someone build a pathogen, or a system that slips out of human control, could do damage that no blackout approaches. I take those risks seriously, and nothing in this chapter argues they are small. My claim is narrower. This is the risk that remains when those are solved. Here is why I think it differs in kind from the others on the list.

**It survives perfect alignment.** Every safety technique we have in 2026 tries to make a model do what its user wants and refuse what it should refuse. Ottilie passed every one of those tests. A risk that perfect alignment leaves untouched cannot be fixed by more alignment.

**Safety standardisation can make it worse.** The 50.2 hertz setting was a safety rule. It was written once, adopted everywhere, and became dangerous because it was adopted everywhere. The same is true of the norms we train into models. When every lab teaches its agents the same careful, sensible way to weigh a user's interests, which the Artificial Hivemind results suggest they already largely do, the agents become more predictable one by one and more synchronised all together. The good habit and the common-mode failure are the same habit.

**It is nobody's job.** Look at who touched the 19:42 decision. The heat pump maker built a compliant delay. The agent company built a loyal agent. The regulator wrote a sensible override. The grid operator sized its reserves to the reference incident. Each sees only its own piece: the agent company sees its customers, the grid operator sees the aggregate, and no one sees the agents' decisions as a population. There is no desk, in 2026, whose job is to ask what happens when everyone's assistant presses the same button.

**It grows with adoption.** When one household in a hundred uses an agent to manage its heat pump, overrides stay scattered and the whole thing is harmless. The danger jumps. It appears when adoption crosses some threshold where the synchronised share of load exceeds what the reserves can absorb, which means it shows up only after the technology has succeeded, and after everyone has had years of good experience with it.

**It multiplies every other flaw.** A small mistake in one agent is a bad evening for one household. The same mistake in a model family deployed across fifty million households is a continental event. Kim and colleagues' finding cuts here: when these systems are wrong, they tend to be wrong together. Correlation is a multiplier, and it multiplies whatever it is given, good judgement and bad.

**It is faster than human response.** The load step in the Long Minute took about sixty seconds. The Iberian blackout of 28 April 2025, which had nothing to do with agents, took about ninety seconds from first trouble to darkness across Spain and Portugal; the ENTSO-E expert panel's final report, published in March 2026, traced it to a combination of voltage oscillations, gaps in reactive power control, generators that did not hold their set points and protections that tripped too early. No control room can convene a meeting in ninety seconds. Whatever defends against correlated helpfulness has to be built in beforehand.

**It is already measured.** This is the hopeful one. We can count error correlation between models, as Kim's team did. We can measure the grid's frequency to the millisecond. We can, if we choose, log every override a device receives and who sent it. Unlike many speculative risks, this one leaves fingerprints in data that already exists or could exist next year. That makes it something researchers can work on now.

---

## The invention: the non-delegable safeguard

The fix I want to propose is simple to state. Some overrides should belong to people and only to people.

A **non-delegable safeguard** is a collective-safety measure that only a present human may override, never an agent. The idea borrows from law, which has long recognised duties that cannot be handed to someone else (a hospital cannot outsource its responsibility for a patient's safety by hiring a contractor). Here the thing that cannot be delegated is a permission. You may cancel your charger's random delay. Your agent may not, not even with your blessing, not even with a standing instruction on page four of the settings.

Here is how it would work for the grid.

**Designation.** A safeguard becomes non-delegable when the devices it governs could, if all overridden together, move a shared system by more than a fixed fraction of that system's reference incident. For continental Europe, I would set the line at one third of the reference incident: one gigawatt. Ninety million flexible household devices drawing a few kilowatts each are hundreds of gigawatts of potential load, so the random start delay qualifies many times over. A regulation that governs a few thousand industrial boilers might not.

**Presence.** The override must be performed by a human at the device or, for devices without a panel, by a live action in an app that cannot be scripted, triggered by an API or authorised in advance. One press covers one start. An agent may recommend the override, explain the saving, and ask; it may not execute. Standing instructions to override are void, the way a contract term waiving certain consumer rights is void. Proving that a person made the press is itself an unsolved problem at this scale: a physical button on the device is the robust version, and hardware attestation for presses made in an app is still open.

**Timing.** The asking runs on a clock. For a designated safeguard, an agent may not prompt its owner about an override within fifteen minutes of a price or grid signal change, and any prompt it does send is held by the device and released after its own random wait. Without this clause, fifty million agents could ask fifty million owners at 19:41, and fifty million thumbs would press together. Even with it, synchronised prompting remains the residual risk: a price app, a news alert or a cold snap can bring people to the button at once with no agent asking. That is what the trigger below is for.

**Location.** The delay lives in the device's firmware. The agent has no handle to pull. This is a small engineering change, and it is the one the UK rule half-made already: the delay is a property of the charge point. The gap is only that the override is reachable through the same software channels the agent uses.

**A safe harbour.** Fiduciary law has to be told. Any statute that imposes a duty of loyalty on agents should state that an agent which does not seek, recommend or press for the override of a designated safeguard has not breached that duty. Without this clause, the market and the lawyers will push agents to lobby their owners at 19:41 every evening, and the owners will learn to press the button by habit. With it, a loyal agent can stay quiet.

**Measurement.** Device makers report, per balancing area and per quarter-hour, the share of eligible starts in which the delay was overridden: the **override uptake rate**. Today, as far as I can find, no one measures this number anywhere. Under the rule, it becomes a monitored grid variable like frequency or reserve margin.

**Trigger.** If the power of overridden starts beginning within any sixty-second window exceeds one gigawatt across the synchronous area, the grid operator broadcasts a suspension: for the next hour, overrides are disabled and the maximum delay is raised to thirty minutes. The British rule already lets the maximum delay be changed remotely, so the lever exists; it needs a rule for pulling it.

What this buys is decorrelation at the cheapest possible price. A person standing by a heat pump at 19:42 is an irregular, slow, distractible source of randomness, which is exactly what the safeguard needs. Ninety million agents can act in the same second. Ninety million people cannot, and would not, because they are eating plum cake.

---

## "The grid already solved this"

The people who know grids best have a ready answer to all of this, and it deserves a full hearing.

It goes like this. Grid engineers have understood synchronised load for decades. They randomise device starts, they stagger tariffs, they built the 50.2 hertz retrofit, they study cold load pickup after outages, and the British regulation itself shows they saw smart charging coming before most AI researchers had heard of it. If agents start pulling overrides in large numbers, the engineers will notice in the data, close the loophole and move on. The Long Minute is a plausible scenario precisely because it describes a sector that is good at this. Why build a new legal category for a problem that a competent sector will fix in its normal course?

I grant most of it. If I had to bet on which sector will handle correlated helpfulness first, I would bet on electricity, and I would not be surprised if grid codes close this particular door before 2036. The Southampton team was writing about it in 2010.

But the answer leaves three gaps. First, the existing fix is the thing that breaks. Randomisation works by turning a fixed start time into a random variable. An override clause combined with fiduciary agents turns the random variable back into a constant, because every agent computes the same best moment.

Second, the grid is close to the only sector with the reflex. It has a single shared variable, frequency, that makes collective harm visible within seconds, and a profession trained to think in populations of devices. Most other places where agents will act for us have neither. Consider safeguards in banking, ticketing, health care and public services that individuals can click past for good reasons: warnings on payments, limits on bookings, queues for appointments. Some of those protect only the person clicking. Others quietly protect everyone, by assuming that people will only rarely click past them, and nobody has ever needed to tell the two kinds apart. I could not find any census of user-overridable safeguards whose real job is collective. Building one is a research problem, and in each sector it should be done before the agents arrive.

Third, "the engineers will notice" assumes the failure gives warning. Correlated helpfulness tends not to. On every ordinary evening for years, the agents' overrides pull load into cheap blocks, the reserves absorb it, and the data shows only a slightly sharper ramp at each quarter-hour. The danger sits in the tail, on the cold evening when a forecast revision makes one block very cheap at very short notice. A sector can be excellent and still be surprised by a tail.

So I would put it this way. The grid has the right instinct and an exploitable exception. The non-delegable safeguard is the grid's own instinct, written down as a general rule, so that it can travel to sectors that have not yet learned it the hard way.

---

> **For researchers**
>
> 1. **Population-level evaluation.** Agent evaluations today test one agent on one task. Build a harness that runs 10⁶ instances of the same agent (or of several agents from different labs) against a shared simulated resource, such as a distribution grid, a ticket queue or a liquidity pool, under the same signal. The quantity to report is the *synchronisation ratio*: the peak aggregate action rate in any short window divided by the rate expected if each instance acted independently. How does it change as you vary the model family, the system prompt and the owner preferences?
> 2. **Override uptake as a risk variable.** Measure, in real deployments or realistic simulations, the fraction of eligible safeguard events in which an override is exercised, split by whether a human or an agent pressed it, and the time-clustering of those overrides (for example, the share falling within the same sixty seconds). I could find no published measurement of either for any domestic safeguard. Both depend on telling the two apart, which makes human-presence attestation the third quantity to report: the rate at which a scripted press is accepted as human by a device-local presence check. A first dataset would let regulators set designation thresholds from evidence instead of judgement.
> 3. **Fiduciary duty versus collective constraints.** Formalise an agent that maximises one principal's utility subject to a duty of loyalty, embedded in a population of such agents sharing a constraint. Characterise when the individually optimal policy produces aggregate violations, and measure how much expected principal welfare a safe-harbour rule costs per unit reduction in peak aggregate load. Is there a constraint the agents can be given that costs each principal less than a cent and removes the cliff?

---

There is a question I have avoided, and it is the next chapter's.

The agents in the Long Minute were built by a handful of companies on a smaller handful of models. They agreed about the cheap block because cheap is cheap: any competent system reads a price table the same way. But they also agreed about something softer. Each one weighed its owner's four cents against the comfort of strangers and judged, in the same way and in the same second, that loyalty came first. That is a judgement about how a good assistant behaves, and someone taught it to them.

The inquiry tried to find out who, and could not, because nobody records that chain. The rubrics are confidential, the vendors go unnamed, and the people who wrote the examples sign agreements about both. As far as anyone knows, one man has found a thread of it, by accident: an evening in Bengaluru, a phone in his hand, and on the screen a sentence he wrote eight years ago, coming out of a model he never worked on.

## Notes

- **German 50.2 Hz problem.** Michael Döring (Ecofys), "Dealing with the 50.2 Hz problem", *NS Energy*, https://www.nsenergybusiness.com/analysis/featuredealing-with-the-50-2-hz-problem/ ; "Has Germany's Energy Transition Stalled?", *IEEE Spectrum*, 2014, https://spectrum.ieee.org/has-germanys-energy-transition-stalled (14 GW worst case; 315,000+ installations; €65–170M estimate). Legal basis: Systemstabilitätsverordnung (2012), https://www.ecolex.org/details/legislation/system-stability-network-ordinance-lex-faoc148063/
- **Random delay and owner override.** The Electric Vehicles (Smart Charge Points) Regulations 2021, SI 2021/1467, regulation 11, https://www.legislation.gov.uk/uksi/2021/1467/section/11
- **Reference incident (3,000 MW) and 0.2 Hz.** ENTSO-E, explanatory note on FCR dimensioning for Continental Europe (System Operation Guideline), https://consultations.entsoe.eu/system-operations/synchronous-area-operational-agreement-policy-1-lo/supporting_documents/Article_A1_Explanatory_Note_for_FCR%20Dimensioning.pdf
- **Low-frequency demand disconnection (49.0 Hz start, about 45% by 48.0 Hz).** ENTSO-E, Network Code on Emergency and Restoration, supporting annex (2014), https://eepublicdownloads.entsoe.eu/clean-documents/Network%20codes%20documents/NC%20ER/141215_Addenda_NCER_V1_1_PC.pdf ; adopted as Commission Regulation (EU) 2017/2196.
- **4 November 2006 disturbance.** UCTE, Interim Report, 30 November 2006, https://eepublicdownloads.entsoe.eu/clean-documents/pre2015/publications/ce/otherreports/IC-Interim-Report-20061130.pdf ; UCTE *Newsgrid* 2006/4, https://eepublicdownloads.entsoe.eu/clean-documents/pre2015/publications/ce/otherreports/newsgrid/Newsgrid_2006_4.pdf
- **Iberian blackout, 28 April 2025.** ENTSO-E Expert Panel, final report (20 March 2026), https://www.entsoe.eu/publications/blackout/28-april-2025-iberian-blackout ; "Entso-E report finds systemic failures behind 2025 Iberian blackout", *pv magazine*, 23 March 2026, https://www.pv-magazine.com/2026/03/23/entso-e-report-finds-systemic-failures-behind-2025-iberian-blackout/
- **Southampton home-storage agents.** P. Vytelingum, T. D. Voice, S. D. Ramchurn, A. Rogers, N. R. Jennings, "Agent-Based Micro-Storage Management for the Smart Grid", AAMAS 2010 (Best Paper Award, per the University of Southampton repository record), https://eprints.soton.ac.uk/268360/
- **Duty of loyalty for agents.** E. G. Smith, V. Y. Wu, J. King, "Designing Loyalty: AI Agents and Conflicts of Interest", Stanford HAI issue brief, 25 August 2026, https://hai.stanford.edu/policy/designing-loyalty-ai-agents-and-conflicts-of-interest ; trust law's sole-interest rule: Restatement (Third) of Trusts §78.
- **Algorithmic monoculture.** J. Kleinberg, M. Raghavan, "Algorithmic monoculture and social welfare", *PNAS*, 2021.
- **Correlated errors.** E. Kim, A. Garg, K. Peng, N. Garg, "Correlated Errors in Large Language Models", ICML 2025, https://proceedings.mlr.press/v267/kim25e.html
- **Artificial Hivemind.** L. Jiang et al., "Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)", NeurIPS 2025 best paper, https://arxiv.org/abs/2510.22954 ; award announcement, NeurIPS blog, https://blog.neurips.cc/?p=1443
