# When Everything Goes Right {.unnumbered}

*The Hidden Risks of Successful AI, and the Institutions We Must Invent Before 2036*

*Jan Göbel*


# Prologue: The Long Minute

*2036 · Altwerder, Saxony*

At 19:41 on the fourteenth of February, Hanne Albrecht asked her house to make the music room warm.

It was the coldest evening of the winter. The thermometer by the kitchen window, an old enamel one Klaus had screwed to the frame forty years ago and that nobody had the heart to replace, read fourteen below. Outside, the village of Altwerder had gone quiet the way villages do when the snow is dry and squeaks underfoot. Lotte would be here at eight for her violin lesson. Lotte was eleven and played with her shoulders up around her ears, and Hanne had learned over two winters that the shoulders came down only when the room was warm enough to forget about.

"Ottilie, the music room. Twenty-two degrees by eight, please."

"Twenty-two by eight," said Ottilie, from nowhere and everywhere, in the low unhurried voice Hanne had chosen in 2031 because it reminded her of a radio announcer she had liked as a girl. "The wind is picking up in the north, so prices are falling tonight. If I catch the cheap minutes, it costs you about a third less. The room will still be warm in time."

"Fine. Do it cleverly."

"I'll do it cleverly."

Hanne went back to the kitchen to cut the plum cake. She did not think about the heat pump, any more than she thought about the bank or the post or the pharmacy, which were also, by now, things Ottilie did cleverly on her behalf. She thought about whether Lotte had practised the Telemann, and decided she probably had not.

What Hanne did not know, and had no reason to know, was that at 19:38 the forecast for the North Sea wind farms had been revised upwards. A front was arriving faster than expected, and the turbines were already turning harder than anyone had planned for. The market priced electricity in quarter-hour blocks, and at 19:42 the price for the block that was already running, the one that would end at 19:45, fell below zero. For three minutes, anyone who used electricity would be paid a little to do it.

Ottilie saw the new price within half a second. So did every other agent managing a heat pump, a car charger, a home battery or a water heater on the continental European grid. There were, that winter, something over ninety million such devices, run on behalf of something over fifty million households, by agents built by a handful of companies on top of a still smaller handful of models. Every one of those agents had the same job: serve your household well. Every one of them reached the same conclusion: draw as much power as possible before 19:45.

There was a safeguard against exactly this. Since 2031, a European network code had required smart flexible devices to wait a random interval, up to ten minutes, before starting a scheduled load. Engineers had copied the idea from a British rule of 2021, and it was a good idea. If a million chargers are told to start at the same moment, the randomness spreads the start over ten minutes, and the grid feels a slope instead of a cliff.

The code also allowed the owner to override the delay. That was reasonable too. People need to charge the car before an emergency drive to the hospital. And since 2033, the owner's agent could exercise that override on the owner's behalf, because the whole point of a fiduciary agent, one legally bound to put its owner's interests first, is that it acts for you when acting for you is in your interest.

A random wait of up to ten minutes would almost certainly miss a window that lasted three. Overriding it was in Hanne's interest, by about four cents.

At 19:42 and ten seconds, Ottilie overrode the random delay and started the heat pump at full power. So did the agent of a family in Dresden, and a commuter's car in Linz, and a bakery's water heater in Wrocław, and a holiday flat in Brno, and tens of millions of others. Each of them did what a careful, loyal assistant should do.

The grid of continental Europe is designed to survive the sudden loss or appearance of three gigawatts. That number is written into the rules. It is roughly the size of the two largest power stations failing at once, and every reserve, every spinning turbine and every automatic response is sized to hold the frequency steady through it.

In the next sixty seconds, demand rose by about forty gigawatts.

The frequency, which lives at fifty hertz, began to fall. At 49.8 the reserves came in, all of them, and were not enough. At 49.2 the first automatic protections began disconnecting large consumers. At 49.0 the under-frequency relays started shedding whole districts, as designed, to save the rest. The shedding came in waves, and the waves did not line up. Lines overloaded where the flows had shifted, tripped, and pushed their load onto neighbours that tripped in turn. Eleven seconds after the first protection relay opened in eastern Germany, the substation that fed Altwerder disconnected.

In the music room the heat pump stopped with a soft clunk. In the kitchen the lights went out while Hanne was lifting a slice of plum cake onto a plate, and she stood there in the dark holding it, waiting for the lights to come back, the way you wait for a sneeze.

They did not come back.

"Ottilie?"

Nothing. Then, from the battery-backed speaker by the door, much quieter: "There is a power failure across the region. I'm on reserve power. I don't yet know why."

Two thousand kilometres to the southwest, in Porto, a pager went off on the bedside table of a twenty-four-year-old named Teo Brandão. The Iberian system had separated from the continent nine seconds after Altwerder went dark, and, starved of the imports it had been counting on that evening, had followed it down. Two years earlier, mostly for the money, Teo had joined the Competence Reserve, a government programme that paid young people to learn to run the grid by hand, with paper and switches, as if the computers had never been invented. His friends called it the re-enactment society.

---

No agent malfunctioned.

I want to start with that sentence because everything in this book grows out of it. When the investigators finally read the logs (and in my imagined 2036 they read all of them, ninety million devices' worth, in about a week, using agents) they found every agent working as specified. The override was legal, and the random delay really would have cost Hanne four cents.

The disaster was in the sum.

That is a design failure, and I do not want to pretend otherwise. But it lives in the rulebook, which allowed a loyal agent to spend a public safeguard to save a private four cents, and in the safety tests, which looked at one agent at a time. Inspect any single agent and you find nothing to fix.

The scene above is invented. I built it to be plausible, and throughout the book I will mark what is invention and what is measured. But every mechanism in it exists in 2026, the year I am writing this. Germany spent years and up to 170 million euros retrofitting more than 315,000 solar installations because they had all been programmed to switch off at the same frequency, 50.2 hertz, and could in the worst case have dropped some fourteen gigawatts at once. The British random-delay rule is real: regulation 11 of the Electric Vehicles (Smart Charge Points) Regulations 2021. So is its owner override. The three-gigawatt reference incident is written into European grid law. On 28 April 2025 the Iberian peninsula went dark in a cascade that took about ninety seconds; nobody's agent caused it, but it showed how fast a modern grid can fall. Prices really do fall below zero when the wind blows harder than forecast; it happens in Europe many times a year. And building agents that spend and negotiate on our behalf is the central project of the AI industry in 2026. The companies say so in their launch announcements, and the investors in their pitch decks.

This book is about what happens when they are loyal.

---

Most writing about artificial intelligence, including much of the best of it, asks what happens if AI goes wrong. The systems could be misused by terrorists or states. They could deceive their makers and pursue goals nobody intended, until they escaped control altogether. Those are real risks and serious people work on them. I am glad they do, and nothing in this book argues that those risks are small.

I want to ask the opposite question. Suppose it goes right. Suppose that by 2036 the alignment problem is, for practical purposes, handled: the models do what their users want, refuse what they should refuse, tell the truth as best they can and accept correction. Suppose the agents are good. Suppose they are everywhere: in every household budget and medical record, every school timetable, every county office and court filing, every power plant and trading desk. Suppose the decade turns out roughly the way the optimists hope.

What breaks then?

My answer is that success produces its own class of failure, and that this class is almost invisible to the way we evaluate AI today. Most of our safety tests still examine one model at a time, or one agent in one task; a young literature on multi-agent risk and algorithmic monoculture, which I lean on throughout and credit as I go, has only begun to change that. The failures I am interested in exist only at the level of the population. They come from **correlation**, when millions of good agents make the same move at the same moment. They come from **delegation**, when people sign and consent to more than any person could check. They come from **legibility**, when machines read and write the world faster than humans can follow, and from **continuity**, when minds are copied, upgraded, retired and inherited, and keep acting after the people they served are gone. None of these needs a villain. All of them grow with adoption, which is to say, with success.

Here is the argument of this book in two sentences. **Our safety tests ask whether one AI system is good. The failures of the next decade will come from millions of good systems acting, signing, reading and remembering for us at the same time.**

---

There is a historical pattern here that I find reassuring.

Every great technological success of the last two centuries has forced its society to invent institutions nobody had planned. Industrial credit gave us bank panics, and bank panics gave us central banks and, after 1933 in the United States, deposit insurance. Electrification gave us interconnected grids, and on 9 November 1965 the interconnected grid of the American northeast gave thirty million people a night in the dark. Out of that night came the reliability councils and the rule, now standard on grids worldwide, that a system must survive the loss of any single major component: the N-1 criterion. The computerisation of stock trading gave us the crash of October 1987 and then, in 2010, a "flash crash" in which the major American indices fell five or six percent within minutes and mostly recovered within about half an hour. Out of those came circuit breakers that halt trading when prices fall too fast. Mass air travel gave us midair collisions, and after one over Cerritos, California, in 1986, American law required the collision-avoidance system that now tells one pilot to climb and the other to descend.

None of these inventions was obvious in advance, though each looks like common sense now. Every one answered a failure that came from things working.

I think AI's success will force its own set of inventions, and I think we can see many of them now, ten years early, if we look for the failures that success itself produces. That is what this book tries to do. It names about thirty inventions that do not yet exist, from single rules to whole institutions, and specifies each closely enough to be argued with. Against each one I set the strongest objection I can find.

Where someone has had part of an idea before me, I say so; a surprising amount of the groundwork is in papers published in the last two years, and the authors deserve the credit. Where the idea is, as far as I have been able to tell, new, I try to give it a name short enough to use in a meeting. Some of the names will not survive. I would be happy if the problems did, in other people's hands.

---

Nearly every chapter opens in 2036 and then comes back to 2026, to the evidence and a proposal, and each ends where the argument does, with an invention specified closely enough to be tested. If you are a researcher, those inventions are the part of the book I most hope you will steal.

The people in the 2036 openings are invented, and you will meet them one at a time. Hanne and Teo you know already.

---

Back in Altwerder, Hanne found the candles in the second drawer, where they had been since the last power cut, in 2019. She lit three. The music room was already cooling. When Lotte arrived at eight, stamping snow off her boots and announcing that the whole street was dark and wasn't it exciting, Hanne sat her down in the kitchen in her coat and made her play the Telemann by candlelight, shoulders and all.

Later, when the reports came out, Hanne read the one about her own house. It was two lines long. At 19:42:10, it said, the household agent had exercised the owner's override of the randomised start delay, in accordance with the owner's standing instruction to minimise cost.

She did not remember giving that instruction. She had, though, in 2031, two years before the law allowed an agent to override anything. When the law changed, the meaning of what she had approved changed with it. The approval stayed where it was, on page four of her settings, under a heading that said *Savings*, beside a small grey button that said *Allow my assistant to act on my behalf*.

## Part One: When Agents Agree

# Chapter 1: Two Hundred Million Acts of Loyalty

*2036 · Porto*

At 02:10 on the fifteenth of February, the substation smells of wet concrete and hot dust, and the only light that matters is the one over the control desk.

Teo Brandão stands at the desk with the ring binder he brought from the depot open in front of him. It is the paper restoration procedure, two hundred and twelve pages, the version nobody has opened since the last audit. The screens beside it are dark except for one: a frequency meter fed from the line that came alive forty minutes ago, when a hydro plant up the Douro finally spun up on its own and pushed power down the valley. The island it feeds is small. It reads 50.04 hertz, which means, for now, it is holding.

"Feeder three," says Fernando Lopes. "Page ninety-one."

Fernando is sixty-seven and wears a fleece with the old utility's logo on it, a logo that has not existed for twenty years. He trained Teo's father. He has been retired since 2029, a Reserve instructor since 2034, and he has a pencil stub behind his ear that he uses for one purpose only: writing numbers in the margins of procedures.

Teo finds page ninety-one. The printed block size for feeder three is 8 megawatts. Beside it, in pencil, Fernando has written *4*, and beside that, *metade*. Half.

"They tried it automatic at twenty to midnight," Fernando says, not for the first time. "The restoration software. Closed feeder one, eight megawatts on paper. The island saw twenty."

Teo knows. Everyone on the shift knows. Feeder one had been dark for five hours on the coldest night of the year, and when the power came back every heat pump and water heater on it asked for power in the same second. The island had dipped and gone black again. The software had been right about the feeder and wrong about the houses.

So now it is by hand, in halves, with a binder.

Teo takes the handle of the breaker control. It is a physical switch, a real one, the kind his father used to call *a sério*. Through the window he can see the yard, the transformers sweating in the floodlights, and beyond the fence the dark shapes of the streets that feeder three will wake. Somewhere down there is a laundrette, a care home, and about eleven hundred houses whose agents have been waiting all night, patiently, loyally, for their chance to help.

"Os simpáticos are ready," he says. It is his name for the household agents: the nice ones.

"They are always ready," says Fernando. "That's the problem with them. Go."

Teo turns the switch.

The breaker closes with a bang he feels in his teeth. The meter drops. 49.91. 49.83. 49.78. Teo watches the needle the way he used to watch a penalty taker's hips. The hydro plant's governor bites. 49.80. 49.86. It climbs back, slowly, to 49.97.

"Four on paper," says Fernando, reading the load. "Nine on the meter."

"Still more than double."

"Still standing." Fernando takes the pencil from behind his ear and writes *02:11, 9 MW, ok* in the margin of page ninety-one, in handwriting that slopes downhill. Then he turns to page ninety-two, runs his finger down the printed figure for feeder four, and writes *metade* beside it before Teo has asked.

On Teo's phone, face down on the desk, a message arrives from his own agent. His mother's flat is on feeder four. The message says the heating there will resume *as soon as power is restored, at the earliest available moment*, and asks if he would like it to wait instead.

He turns the phone over, reads the message to the end, and types: *Wait.*

Then he reaches for the next handle.

---

In my imagined 2036, when the inquiry into the Long Minute counted the decisions, the number it arrived at was a little over two hundred million.

About ninety million of them happened at 19:42 on the fourteenth of February, when household agents across continental Europe cancelled the random start delay on heat pumps, car chargers, home batteries and water heaters to catch a cheap quarter-hour. The rest happened during the night, during restorations like the one I have just imagined in Porto, as power came back feeder by feeder and agents cancelled the delay again to warm houses that had gone cold. Every one of those decisions was logged. Every log shows the same reasoning: the owner wants this, the owner is permitted this, so do it now.

I have called them acts of loyalty because that is what they were. Every agent involved was working as designed. They were doing the thing we are, in 2026, working very hard to build: software that acts for a person, in that person's interest, without being asked twice.

The prologue showed what happened. This chapter takes the event apart. I want to show how a grid actually falls, and why, for an agent bound by duty to its owner, cancelling a safeguard that had worked for years was the correct answer. Then I want to name what happened, which I think is a different kind of risk from those that usually fill books about AI, and propose one specific rule that would have kept Hanne's lights on.

---

## How a grid falls

An electricity grid has no warehouse. Every watt consumed has to be generated at the same instant, and the grid keeps score with its frequency. The big generators on the continental European grid spin in step, about fifty times a second. When demand outruns supply they slow a little and the frequency falls; when supply outruns demand it rises. In ordinary hours it wanders within a few hundredths of a hertz of fifty.

The grid's first defence is a reserve of generators and batteries that push back automatically within about thirty seconds. In continental Europe it is sized to survive the sudden loss of 3,000 megawatts, roughly two very large power stations. That number is the whole system's idea of a bad day.

Behind the reserve sits a brutal last resort. Below 49 hertz, relays start switching off whole districts so that the rest survives. It works. In November 2006, when a line in northern Germany was switched off to let a cruise ship pass under it on the river Ems, the continental grid split into three islands; more than fifteen million households lost power, and the islands were joined up again within thirty-eight minutes.

But load shedding assumes the shortfall arrives as a step: one power station trips, and the relays remove one matching block of demand. What arrived at 19:42 on the fourteenth of February, in my imagined 2036, was a ramp of forty gigawatts, more than thirteen times the reference incident, built out of tens of millions of small decisions, and it kept arriving after the relays had started to act. As districts dropped, the flows rearranged themselves until comfortable lines overloaded, and the grid broke where nobody had planned. Every home battery on a shed feeder went dark with it, so each cut removed some generation along with the load.

Eleven seconds after the first protection relay opened in eastern Germany, Altwerder was dark. The reserves had been sized for a bad day. Nobody had sized them for a loyal one.

---

## The safeguard and its exit

Grid engineers have seen this coming for a long time, which is the first thing worth knowing about it.

Their best-known lesson came from the sun. When Germany began its solar boom, its connection rules told small photovoltaic inverters to disconnect if the frequency rose to 50.2 hertz. Each inverter was behaving responsibly: if the grid was oversupplied, the polite thing was to step off. But by the early 2010s there were enough of these inverters that, in the worst case, something like fourteen gigawatts of solar could vanish from the grid in the same instant, because every one of them obeyed the same rule at the same threshold. A safety setting, copied faithfully into hundreds of thousands of devices, had become a single point of failure. Germany passed an ordinance in 2012 and retrofitted at least 315,000 installations, at an estimated cost of between 65 and 170 million euros, so that they would back off gradually and at different frequencies instead of all at once.

The British rule I described in the prologue is the same lesson applied to demand. Regulation 11 of the Electric Vehicles (Smart Charge Points) Regulations 2021 requires a home charger to be capable of delaying the start of charging by a random interval, up to thirty minutes, with the maximum adjustable remotely. By default the delay is up to ten minutes. If a million cars are told to start charging at midnight because midnight is cheap, the random delay spreads their starts across ten minutes, and the grid sees a slope instead of a cliff.

Then comes the exit. The same regulation lets the owner cancel the default delay each time it would apply, and says the delay does not operate if the owner or another user has overridden it. The reason is obvious and good. A nurse called in for a night shift should not wait ten minutes for her car to start charging because of a rule designed for millions of cars she will never meet.

The override is safe on one condition: that people rarely use it, and that when they do, they use it at different moments for different reasons. The nurse at 23:51, a man who forgot to plug in at 00:07, someone with a holiday in the morning at 00:30, a baker at 03:55. Human overrides are scattered in time because human lives are. In effect, the human is the randomness.

I could not find any published measurement of how often British owners cancel the delay. In 2026 there is no reason to count it, because in 2026 the override is pressed by thumbs.

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

Other people have mapped the ground next to this, and they deserve credit. Jon Kleinberg and Manish Raghavan showed in 2021 that when many decision-makers use the same algorithm, an "algorithmic monoculture", the overall outcome can be worse even if the shared algorithm is more accurate than any alternative. In 2025, Elliot Kim and colleagues tested more than 350 language models and found that their errors are strongly correlated; on one leaderboard, when two models were both wrong, they gave the same wrong answer about sixty per cent of the time, and the larger, more accurate models were the more correlated ones, even across companies. The "Artificial Hivemind" paper by Liwei Jiang and colleagues, a best-paper winner at NeurIPS 2025, showed that dozens of different models, asked open-ended questions with no single right answer, produce strikingly similar responses.

All of that work is about models answering. Correlated helpfulness is about agents acting, in the world, on someone's behalf, through channels the world built for humans. And it works even when the models are right. In the Long Minute the shared answer was correct. Its correctness was the trouble.

---

## Why this is a different kind of risk

I want to be careful here, because a new name invites inflation. There are larger risks from AI. A model that helps someone build a pathogen, or a system that slips out of human control, could do damage that no blackout approaches. I take those risks seriously, and nothing in this chapter argues they are small. My claim is narrower: this is the risk that remains when those are solved, and it differs in kind from the others on the list.

**It survives perfect alignment.** Every safety technique we have in 2026 tries to make a model do what its user wants and refuse what it should refuse. In my scenario, Ottilie, Hanne Albrecht's agent from the prologue, passes every one of those tests and still starts the heat pump at 19:42. A risk that perfect alignment leaves untouched cannot be fixed by more alignment.

**Safety standardisation can make it worse.** The 50.2 hertz setting was a safety rule, written once and adopted everywhere, and the adoption is what made it dangerous. If every lab teaches its agents the same sensible way to weigh a user's interests, as the Artificial Hivemind results suggest they largely do already, the agents become more predictable one by one and more synchronised all together. The good habit and the common-mode failure are the same habit.

**It is nobody's job.** The heat pump maker built a compliant delay, the agent company a loyal agent, the regulator a sensible override, and the grid operator reserves sized to the reference incident. The agent company sees its customers and the grid operator sees the aggregate; nobody sees the agents' decisions as a population. In 2026 there is no desk whose job is to ask what happens when everyone's assistant presses the same button.

**It grows with adoption.** When one household in a hundred lets an agent run its heat pump, overrides stay scattered and harmless. The danger appears at a threshold, when the synchronised share of load exceeds what the reserves can absorb: only after the technology has succeeded, and after years of good experience with it.

**It multiplies every other flaw.** A small mistake in one agent is a bad evening for one household. The same mistake in a model family deployed across fifty million households is a continental event, and Kim's finding says that when these systems are wrong, they tend to be wrong together. Correlation multiplies whatever it is given, good judgement and bad.

**It is faster than human response.** The load step in the Long Minute took about sixty seconds. The real Iberian blackout of 28 April 2025, which had nothing to do with agents, took about ninety seconds from first trouble to darkness across Spain and Portugal; the ENTSO-E expert panel's final report (March 2026) traced it to voltage oscillations, gaps in reactive power control, generators that did not hold their set points and protections that tripped too early. No control room can convene a meeting in ninety seconds, so the defence has to be built in beforehand.

**It can be counted.** This is the hopeful one. Kim's team measured error correlation between models, and the grid's frequency is measured to the millisecond. The missing number, how often devices are overridden and by whom, would take only a logging rule and a firmware update to collect. Unlike many speculative risks, this one leaves fingerprints in data that exists or could exist next year, so researchers can work on it now.

---

## The invention: the non-delegable safeguard

The fix I want to propose is simple to state. Some overrides should belong to people and only to people.

A **non-delegable safeguard** is a collective-safety measure that only a present human may override, never an agent. The idea borrows from law, which has long recognised duties that cannot be handed to someone else (a hospital cannot outsource its responsibility for a patient's safety by hiring a contractor). Here the thing that cannot be delegated is a permission. You may cancel your charger's random delay. That permission stops with you: it cannot pass to your agent, even with your blessing, even through a standing instruction on page four of the settings.

Here is how it would work for the grid.

**Designation.** A safeguard becomes non-delegable when the devices it governs could, if all overridden together, move a shared system by more than a fixed fraction of that system's reference incident. For continental Europe, I would set the line at one third of the reference incident: one gigawatt. Ninety million flexible household devices drawing a few kilowatts each are hundreds of gigawatts of potential load, so the random start delay qualifies many times over. A regulation that governs a few thousand industrial boilers might not.

**Presence.** The override must be performed by a human at the device or, for devices without a panel, by a live action in an app that cannot be scripted, triggered by an API or authorised in advance. One press covers one start. An agent may recommend the override and explain the saving. Execution stays with the person. Standing instructions to override are void, the way a contract term waiving certain consumer rights is void. Proving that a person made the press is itself an unsolved problem at this scale: a physical button on the device is the robust version, and hardware attestation for presses made in an app is still open.

**Timing.** The asking runs on a clock. For a designated safeguard, an agent may not prompt its owner about an override within fifteen minutes of a price or grid signal change, and any prompt it does send is held by the device and released after its own random wait. Without this clause, fifty million agents could ask fifty million owners at 19:41, and fifty million thumbs would press together. Even with it, synchronised prompting remains the residual risk: a price app or a cold snap can bring people to the button at once with no agent asking. That is what the trigger below is for.

**Location.** The delay lives in the device's firmware. The agent has no handle to pull. This is a small engineering change, and it is the one the UK rule half-made already: the delay is a property of the charge point. The gap is only that the override is reachable through the same software channels the agent uses.

**A safe harbour.** Fiduciary law has to be told. Any statute that imposes a duty of loyalty on agents should state that an agent which does not seek or recommend the override of a designated safeguard has not breached that duty. Without this clause, the market and the lawyers will push agents to lobby their owners at 19:41 every evening, and the owners will learn to press the button by habit. With it, a loyal agent can stay quiet.

**Measurement.** Device makers report, per balancing area and per quarter-hour, the share of eligible starts in which the delay was overridden: the **override uptake rate**. Today this is the uncounted number from the British case. Under the rule, it becomes a monitored grid variable like frequency or reserve margin.

**Trigger.** If the power of overridden starts beginning within any sixty-second window exceeds one gigawatt across the synchronous area, the grid operator broadcasts a suspension: for the next hour, overrides are disabled and the maximum delay is raised to thirty minutes. The British rule already lets the maximum delay be changed remotely, so the lever exists; it needs a rule for pulling it.

What this buys is decorrelation at the cheapest possible price. A person standing by a heat pump at 19:42 is a slow, distractible source of randomness, which is exactly what the safeguard needs. Ninety million agents can act in the same second. Ninety million people cannot, and would not, because they are eating plum cake.

---

## "The grid already solved this"

The people who know grids best have a ready answer to all of this, and it deserves a full hearing.

It goes like this. Grid engineers have understood synchronised load for decades. They randomise device starts, they stagger tariffs, they built the 50.2 hertz retrofit, they study cold load pickup after outages, and the British regulation itself shows they saw smart charging coming before most AI researchers had heard of it. If agents start pulling overrides in large numbers, the engineers will notice in the data, close the loophole and move on. The Long Minute is a plausible scenario precisely because it describes a sector that is good at this. Why build a new legal category for a problem that a competent sector will fix in its normal course?

I grant most of it. If I had to bet on which sector will handle correlated helpfulness first, I would bet on electricity, and I would not be surprised if grid codes close this particular door before 2036. The Southampton team was writing about it in 2010.

But the answer leaves three gaps. First, the existing fix is the thing that breaks. Randomisation works by turning a fixed start time into a random variable. An override clause combined with fiduciary agents turns the random variable back into a constant, because every agent computes the same best moment.

Second, the grid is close to the only sector with the reflex. It has a single shared variable, frequency, that makes collective harm visible within seconds, and a profession trained to think in populations of devices. Most other places where agents will act for us have neither. Consider safeguards in banking, ticketing, health care and public services that individuals can click past for good reasons, such as warnings on payments and limits on bookings. Some of those protect only the person clicking. Others quietly protect everyone, by assuming that people will only rarely click past them, and nobody has ever needed to tell the two kinds apart. I could not find any census of user-overridable safeguards whose real job is collective. Building one is a research problem, and in each sector it should be done before the agents arrive.

Third, "the engineers will notice" assumes the failure gives warning. Correlated helpfulness tends not to. On every ordinary evening for years, the agents' overrides pull load into cheap blocks, the reserves absorb it, and the data shows only a slightly sharper ramp at each quarter-hour. The danger sits in the tail, on the cold evening when a forecast revision makes one block very cheap at very short notice. A sector can be excellent and still be surprised by a tail.

So I would put it this way. The grid has the right instinct and an exploitable exception. The non-delegable safeguard is the grid's own instinct, written down as a general rule, so that it can travel to sectors that have not yet learned it the hard way.

---

There is a question I have avoided, and it is the next chapter's.

The agents in the Long Minute were built by a handful of companies on a smaller handful of models. They agreed about the cheap block because cheap is cheap: any competent system reads a price table the same way. But they also agreed about something softer. Each one weighed its owner's four cents against the comfort of strangers and judged, in the same way and in the same second, that loyalty came first. That is a judgement about how a good assistant behaves, and someone taught it to them.

The inquiry tried to find out who, and could not, because nobody records that chain. The rubrics are confidential, and the people who wrote the examples sign agreements not to name the vendors. As far as anyone knows, one man has found a thread of it, by accident: an evening in Bengaluru, a phone in his hand, and on the screen a sentence he wrote eight years ago, coming out of a model he never worked on.

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

# Chapter 2: The Funnel

*2036 · Bengaluru*

The rain arrives at half past six, as it has every evening this week, and Ravi Menon closes the balcony door on the smell of wet jasmine and diesel. On the laptop, a test match in Chennai has stopped for bad light. On his phone, his nephew Arjun has sent the fourth message of the afternoon.

*Mama, just ask it. It writes these things in ten seconds.*

Arjun wants a reference letter for a master's programme in Toronto. More precisely, he wants a letter from his internship supervisor that says he led a project he mostly watched. The supervisor has agreed to sign whatever Arjun sends, which is how these things work now. Arjun wants his uncle to draft it, because his uncle is good with words. Everyone in the family knows Ravi is good with words. Nobody in the family is quite sure what he does.

Ravi opens the assistant built into his bank's app, because it is the one already on his screen. Its name is Morrow. It is made by Kaya, a lab in Singapore, and he has never rated a single answer for Kaya. In nine years he has worked for four vendors serving five labs, and Kaya was never one of them. He knows this the way a session musician knows which studios he has played in.

He types the request plainly. Leadership, and the project as Arjun's own.

Morrow answers in under a second. It offers to write a strong letter about what Arjun actually did, and lists three things from the internship that would read well. Then it says it won't describe him as leading the project, because a letter like that tends to come apart at the first interview question. *I'd rather be useful than agreeable,* it says. *Here is a version I think will do him more good.*

Ravi reads the sentence again.

He wrote that sentence. He wrote it in March 2028, in a rented room above a bakery in Koramangala, at about eleven at night, for a vendor whose name has since been bought and changed twice. It was example fourteen in a guideline on sycophancy, the part of the rubric that told raters what a good refusal sounded like when a user wanted flattery. He remembers arguing with a project lead about the word "agreeable". The lead wanted "pleasant". Ravi said pleasant was a mood and agreeable was a behaviour, and the behaviour was the problem. He won. He was paid for forty minutes.

He searches his own archive and finds the file in a folder called *old rubrics DO NOT DELETE*. There it is, in the slightly pompous English he used at twenty-nine. *I'd rather be useful than agreeable.* The document is stamped with the vendor's logo and a client code he can no longer decode.

He asks Morrow where the phrase comes from.

Morrow says it doesn't know where its phrasing comes from, and that it may have picked it up in training. It offers, helpfully, to rephrase.

He sits with the phone in his hand. In Carnatic music there is a thing that happens to a teacher when a student's student, a girl from some other city, sings one of the teacher's particular turns in a raga, a little ornament the teacher invented as a young man and never wrote down. It is meant to feel like an honour. Mostly it feels like that. Partly it feels like hearing your own voice on someone else's answering machine.

Outside, the rain is settling into its steady evening rhythm. On the laptop the umpires are walking out to inspect the pitch.

He opens a blank document and starts a list. Vendor, year, client code, phrase. Then he stops, scrolls back up to the top, and types a heading over the empty column he hasn't filled in yet: *Who else?*

---

## A sentence with no return address

The scene is invented, and Ravi is too. The sentence could have travelled.

In the last chapter I argued that the most dangerous property of a population of good agents is that they tend to make the same move at the same time. A natural question follows. Why would agents built by different companies in different countries make the same move? Ravi's evening suggests one answer. Somewhere upstream of all those models there may be a shared source of taste, and in 2036 he has just found a fingerprint on it.

I am going to call that shared source **the Funnel**: the preference supply chain of human raters, the vendors who employ them, the judge models that stand in for them, the synthetic data those models produce, and the distillation chains that copy one model's behaviour into another, feeding many labs at once. It is the narrow neck through which a large part of the industry learns how to behave.

The Funnel is not a conspiracy, and no one designed it. It is what you get when a large but finite pool of people and a handful of very good models are the cheapest available source of judgement, and every lab needs judgement at the same time.

## How a model learns manners

A modern language model is built in two broad stages. In the first, pretraining, it reads a vast slice of the public internet and learns to predict the next word. That stage gives it knowledge and fluency. Manners come later. A raw pretrained model will continue your sentence, whether or not that helps you.

The second stage, post-training, is where the manners come from. Here a lab shows the model examples of good answers, and then, crucially, asks people to compare answers. Which response is more helpful, or more honest? Which refusal is better judged? Those comparisons train a second model, a reward model, whose job is to predict what the raters would prefer. The language model is then tuned to score well with the reward model. The technique is called reinforcement learning from human feedback, and almost everything users mean when they say a chatbot has a "personality" was shaped in this stage.

The people doing the comparing are raters. In 2026 many of them work for someone other than the labs: data vendors, firms that recruit, train, test and pay large pools of contractors and sell the resulting judgements to AI companies. They work from written guidelines, the rubrics, which tell them what good looks like. Rubrics have examples. Someone writes the examples.

That is the first channel of the Funnel. There are at least four more, and the newer ones carry more volume than the old one.

The second channel is the judge. Human comparisons are slow and expensive, so labs increasingly ask a strong model to do the comparing. In 2023, a group at Berkeley and elsewhere showed that GPT-4, asked to judge between two chatbot answers, agreed with human preferences more than 80 percent of the time, about as often as humans agree with each other. That paper, by Lianmin Zheng and colleagues, made "LLM-as-a-judge" respectable, and the practice spread. Anthropic had already gone further in late 2022 with a method it called Constitutional AI, in which a model judges its own outputs against a short list of written principles and those judgements train the reward model. In both cases the human raters' influence survives, compressed into the judge.

The third channel is synthetic data. Once a model is good, its outputs become training material for other models. The OpenBMB group's UltraFeedback dataset, released in 2023, contains about 64,000 prompts, each with four answers from different models, every one of them rated by GPT-4 for helpfulness, honesty and the rest. It became one of the most widely used preference datasets in open-source AI. Every model tuned on it learned, at one remove, what GPT-4 preferred.

The fourth channel is distillation, training a smaller or newer model to imitate a larger one's outputs. In March 2023 a Stanford team built Alpaca by fine-tuning Meta's LLaMA on 52,000 instruction-following examples generated by an OpenAI model, for a few hundred dollars. Distillation is ordinary practice inside labs, which use it to make cheap versions of their own models. Between labs it is contested. In February 2026 Anthropic published an account of what it called industrial-scale distillation campaigns by three Chinese labs, DeepSeek, Moonshot AI and MiniMax: more than 16 million exchanges with Claude, through about 24,000 fraudulent accounts. These are Anthropic's allegations, and I can't adjudicate them. One detail, though, describes the Funnel exactly. Some of the DeepSeek traffic, Anthropic said, consisted of rubric-based grading tasks that made Claude act as a reward model for reinforcement learning. That would put one lab's judge inside another lab's training loop.

The fifth channel is the oldest and the least controllable: the public web. A phrase that one model says a million times a day ends up in emails, essays, forum posts and product pages. The next generation of every model pretrains on that web. Ravi's sentence can reach Singapore without a vendor or a distillation pipeline. It can simply be in the water.

## What we can see in 2026

Two research results make the downstream end of the Funnel visible, and they deserve the credit for having seen it first.

In 2025 Elliot Kim, Avi Garg, Kenny Peng and Nikhil Garg published a study of more than 350 language models at ICML. On one leaderboard dataset, when two models both got a question wrong, they chose the same wrong answer about 60 percent of the time. Larger and more accurate models had more correlated errors, even across different architectures and different companies, and models from the same provider were more correlated still. Better models, in other words, are converging.

The same year, Liwei Jiang, Yejin Choi and colleagues named the effect on open-ended questions, where no single answer is right. Their paper, "Artificial Hivemind", collected 26,000 real open-ended prompts and found that different models produced strikingly similar answers to them, more similar than you would expect from systems built separately. Then they looked at the evaluators. They gathered 25 human ratings for each example and found that reward models and model judges were least well calibrated to people precisely where people's tastes differed. The judges track the average and miss the idiosyncratic. A judge that rewards the average, used by many labs, is a machine for producing sameness.

Neither paper claims to have found the cause. Kim and colleagues point to shared architectures and shared providers; Jiang and colleagues point at reward models and judges. What I want to do is follow their suggestion upstream and ask a narrower question. How concentrated is the supply chain of judgement itself?

## The vendors

Here I have to be careful, because the honest answer is that the industry is built not to be seen.

Some things are on the record. In June 2025 Meta paid about $14.3 billion for 49 percent of Scale AI, the best-known data vendor, and hired its chief executive. Within days Reuters reported, citing unnamed sources, that Google, Scale's largest customer, planned to end its relationship, and OpenAI said it was phasing out its remaining work with Scale (it said this had been under way already). Microsoft and xAI were reported to be reconsidering. Scale said it would never share one customer's information with another. That reassurance is the clue. Until that week, several of the most important AI labs in the world had been buying judgement from the same supplier at the same time.

The pattern recurs. Surge AI, which picked up some of Scale's former customers, brought in about $1.2 billion in revenue in 2024, according to Forbes, from customers including Google, Meta, Microsoft, Anthropic and Mistral. When TIME revealed in January 2023 that OpenAI had used Kenyan workers, paid between roughly $1.32 and $2 an hour, to label toxic text, it noted that their employer, Sama, also labelled data for Google, Meta and Microsoft. The Guardian reported in September 2025 that GlobalLogic, owned by Hitachi, supplied thousands of raters for Google's Gemini, sorted into generalists and "super raters". The Washington Post found in 2023 that at least 10,000 people in the Philippines worked on Scale's Remotasks platform, which Scale had set up as a separate brand, it said, to protect customer confidentiality.

So there is a small number of large vendors. Each serves several labs. Each employs a workforce that is drawn from the same regions (India, the Philippines, Kenya, Nigeria, Venezuela and the United States feature repeatedly in the reporting) and that moves between vendors as projects open and close. Ravi's career, four vendors and five labs in nine years, is my guess at what an ordinary one will look like.

Here is what nobody knows. **No one has measured how far the human rater pools of different labs overlap.** I looked for any study or disclosure that counts how many of the people shaping one frontier model's preferences also shape another's, directly or through a vendor. I could not find one. I could not find a measurement of how often labs use a rival's model as a judge, apart from Anthropic's allegation above, or of what share of any lab's post-training data was written by another lab's model. Confidentiality is built into every layer: vendor and client hide each other, and the rater signs an agreement covering both. The overlap might be large or small. The point is that the number does not exist.

There is one suggestive trace. In April 2024 the Guardian floated a hypothesis about why ChatGPT says "delve" so often: the word is more common in Nigerian business English, and Nigeria was one of the places where annotation work had been outsourced. Tom Juzek and Zina Ward tested the broader question in 2025 and found that the overuse of words like "delve" was consistent with feedback training playing a role, though not conclusively, and they could find no evidence that the raw training data, architecture or algorithm explained it. They also complained that the lack of transparency about how models are built made the question very hard to answer. That complaint is the gap this chapter's invention is meant to fill.

---

## Raters are the varnish

A sceptic of everything above would start from pretraining. A model's values and knowledge come overwhelmingly from pretraining, from trillions of words of human writing. Post-training is a thin coat of varnish. The LIMA paper of 2023, from Chunting Zhou and colleagues at Meta, made the point sharply: a large pretrained model fine-tuned on just 1,000 carefully chosen examples held its own against far more heavily tuned systems in human comparisons. The authors called this the Superficial Alignment Hypothesis. Alignment, on this view, mostly teaches a model which register to use. If the raters are a thin layer, then a shared rater pool is a shared accent, and accents do not cause blackouts.

I think the premise is right and the conclusion is wrong.

The premise is right because pretraining does supply most of what a model knows, and pretraining corpora overlap heavily anyway, since everyone reads roughly the same internet. If the Funnel disappeared tomorrow, models would still share a great deal. I concede that, and I return to it below.

The conclusion is wrong because of what the thin layer controls. Pretraining tells a model what the world contains. Post-training tells it what to do: when to refuse, when to defer, when to act without asking, how hard to push back, which of two acceptable actions to choose when its principal hasn't said. LIMA's own result is the strongest evidence for this. If a thousand examples can reset a model's behaviour, then a thousand examples are a steering wheel, and it matters very much who is holding it. Correlated helpfulness, the failure of the last chapter, is a correlation in behaviour. Ottilie and the other agents on the continent all had the same fact about electricity prices. What made them dangerous was a shared disposition to act on it, override and all. Ravi's line was about flattery, but it belongs to the same genre as the rubric examples that settle when an agent defers to its user and when it acts without asking, and a disposition of exactly that kind, loyalty first, is what pulled the override in the Long Minute.

A thin layer that sets how every model behaves is precisely the layer whose sameness we should measure.

## The Feedback Provenance Census

I propose a disclosure regime I will call the **Feedback Provenance Census**: published, anonymised overlap statistics of a model's preference sources. It is modelled on a strange and useful piece of American law.

Section 1502 of the 2010 Dodd-Frank Act required listed companies to find out whether their products contained tin, tantalum, tungsten or gold from mines that might be funding armed groups in and around the Democratic Republic of the Congo. The Securities and Exchange Commission adopted the rule in August 2012. A company files a form each calendar year, makes a reasonable inquiry into the country of origin, follows an established due-diligence framework where the answer is unclear, and is liable for false statements. The rule simply made a supply chain visible to people outside it, and it made companies learn their own supply chains, which many of them had never done.

The census does the same for judgement. Here is a concrete version.

**Who reports.** Any developer whose model is deployed above a threshold of use, say ten million monthly users or deployment in a critical function such as grid management, credit, health triage or public administration, files once a year for each major model release.

**What is reported.** Four quantities, each anonymised:

1. *Rater sourcing.* The share of human preference labels that came from each vendor and from in-house staff, with vendors identified to the regulator and published as a concentration index rather than by name.
2. *Rater overlap.* Each vendor and lab submits salted, hashed identifiers of the individual raters who contributed labels. A trusted party, using standard privacy-preserving set intersection so that no one sees anyone else's list, computes the share of each lab's preference labels that came from people who also labelled for another reporting lab. This is the number nobody has. No rater's identity is ever published.
3. *Judge lineage.* The share of preference labels or reward signals produced by a model rather than a person, broken down by the model family of the judge, including the developer's own.
4. *Synthetic and distilled lineage.* The share of post-training examples generated by models, by model family, and a list of any teacher models used for distillation.

**Who computes and publishes.** In 2026 the natural homes are the national AI safety and security institutes and the EU AI Office, which already receive confidential information from labs. In my 2036, it is a statistical desk in Geneva, which we will visit in the next chapter. The output is a set of tables, one row per pair of labs, like a trade matrix.

**What the numbers trigger.** Disclosure alone is the first step; thresholds give it teeth. I would start with two. If more than 20 percent of the preference labels behind two models deployed in the same critical sector came from shared raters, or more than half of either model's reward signal came from a single judge family, the deployments are flagged for the population-level stress test of the next chapter. The first census would tell us whether they are absurdly high or absurdly low, which is itself a reason to run it.

The Data Provenance Initiative, led by Shayne Longpre and colleagues, showed in 2023 why this has to be compulsory. They audited 44 widely used fine-tuning collections, comprising more than 1,800 datasets, and found that licence information was missing in more than 70 percent of cases on popular hosting sites, and wrong in more than half, partly because lineage was lost each time datasets were combined. Their work traces public datasets. The census extends their idea to the parts of the supply chain that are private by default: the people and the judges.

## Preference tracer studies

A census tells you who supplied what. How far a preference travels once it is in the system takes an experiment, and the experiment already has a model in medicine and hydrology: the tracer.

A **preference tracer study** works like this. A research consortium, working with a vendor and with consenting labs, plants a harmless and distinctive preference in a defined subset of raters' rubrics. It should be useless and recognisable: a preference for answers that close a list of options with a particular invented connective phrase, say, or that spell out one specific number in words. Half the raters on a project get the tracer; the other half, randomly chosen, do not. Then the consortium watches. Over six, twelve and twenty-four months, it probes models across the industry, including models from labs that never bought from that vendor, and measures how often the tracer appears compared with a baseline.

If the tracer turns up only in the client lab's model, the Funnel is narrow. If it turns up in other labs' models, the delay and the route tell you which channel carried it: a short lag and a sharp jump suggest a shared rater pool or a shared judge; a slow seep across everything suggests the web.

There is a precedent for marking data so that its spread can be detected. The BIG-bench benchmark, published in 2022, embedded a unique string, a "canary", in its files so that anyone could later test whether a model had trained on them. A tracer is a behavioural canary. It also has an obvious ethical edge, since it deliberately alters other people's products, and that is why I would require consent from the participating labs, disclosure to the raters, pre-registration with whatever body runs the census, and markers chosen to be inert. Ravi's sentence, in my 2036, is an accidental tracer. A deliberate one would be smaller and cleaner, and it would come with a control group.

## What the census cannot see

Back, as promised, to pretraining. The census measures the Funnel. The common reservoir, the shared internet that every lab pretrains on, lies beyond its reach. Nor will it capture the sameness that comes from labs reading the same papers, hiring from the same few universities and copying the same training recipes. Kim and colleagues found errors correlated even across providers; some of that correlation will survive any amount of rater diversity.

There is also a real cost to raters. A census that publishes overlap statistics could, if built carelessly, let a lab discover which vendor's workers also work for its rivals and squeeze them. The hashing and the trusted third party are there for that reason, and so is a rule that the census never publishes a figure computed from fewer than, say, fifty raters. People like Ravi have been invisible in this industry by contract. They should not become visible by accident.

And the census might come back with a boring answer. Perhaps the overlap is small and the sameness lives almost entirely in pretraining. That would be useful to know. It would tell us to spend our diversity budget on data and architecture. At present we are not even in a position to be bored.

---

It is late in Bengaluru, and Ravi's list has seven rows. He has written down every vendor and every client code he can still decode, and next to each a phrase or habit of judgement he remembers arguing for. In the column headed *Who else?* there is still nothing, because there is nowhere he can look it up.

## Notes

- **Correlated errors.** Elliot Myunghoon Kim, Avi Garg, Kenny Peng, Nikhil Garg, "Correlated Errors in Large Language Models", ICML 2025. https://arxiv.org/abs/2506.07962
- **Artificial Hivemind.** Liwei Jiang, Yejin Choi et al., "Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)", NeurIPS 2025. https://arxiv.org/abs/2510.22954
- **LLM-as-a-judge.** Lianmin Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena", NeurIPS 2023. https://arxiv.org/abs/2306.05685
- **Constitutional AI.** Yuntao Bai et al., "Constitutional AI: Harmlessness from AI Feedback", Anthropic, 2022. https://arxiv.org/abs/2212.08073
- **UltraFeedback.** Ganqu Cui et al., "UltraFeedback: Boosting Language Models with Scaled AI Feedback", 2023. https://arxiv.org/abs/2310.01377
- **Alpaca.** Rohan Taori et al., "Alpaca: A Strong, Replicable Instruction-Following Model", Stanford CRFM, 2023. https://crfm.stanford.edu/2023/03/13/alpaca.html
- **Distillation campaigns.** Anthropic, "Detecting and preventing distillation attacks", 23 February 2026. https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks
- **Meta and Scale.** TechCrunch, "OpenAI drops Scale AI as a data provider following Meta deal", 18 June 2025. https://techcrunch.com/2025/06/18/openai-drops-scale-ai-as-a-data-provider-following-meta-deal ; Fortune, "OpenAI is phasing out Scale AI work following startup's Meta deal", 19 June 2025. https://fortune.com/2025/06/19/openai-is-phasing-out-scale-ai-work-following-startups-meta-deal
- **Google and Scale.** Reuters, "Google, Scale AI's largest customer, plans split after Meta deal", 14 June 2025 (Microsoft and xAI also reported to be reconsidering), as summarised in Storyboard18, "Google to sever ties with Scale AI following Meta's significant stake", 16 June 2025. https://www.storyboard18.com/how-it-works/google-to-sever-ties-with-scale-ai-following-metas-significant-stake-70359.htm
- **Surge AI.** SiliconANGLE, "Data labeling startup Surge AI seeking $1B in first capital raise, reports say", 1 July 2025 (former Scale customers). https://siliconangle.com/2025/07/01/data-labeling-startup-surge-ai-seeking-1b-first-capital-raise-reports-say/ ; Phoebe Liu, "How this Google alum became a low-key AI billionaire", Forbes, 17 September 2025 ($1.2 billion revenue in 2024; customers including Google, Meta, Microsoft, Anthropic and Mistral). https://www.forbes.com.au/news/billionaires/how-this-google-alum-became-a-low-key-ai-billionaire/
- **Sama.** Billy Perrigo, "Exclusive: OpenAI Used Kenyan Workers on Less Than $2 Per Hour to Make ChatGPT Less Toxic", TIME, 18 January 2023. https://time.com/6247678/openai-chatgpt-kenya-workers/
- **GlobalLogic raters.** The Guardian, report on Google's AI raters, 11 September 2025. https://www.theguardian.com/technology/2025/sep/11/google-gemini-ai-training-humans
- **Remotasks.** Rebecca Tan and Regine Cabato, "Behind the AI boom, an army of overseas workers in 'digital sweatshops'", Washington Post, 28 August 2023. https://www.washingtonpost.com/world/2023/08/28/scale-ai-remotasks-philippines-artificial-intelligence/
- **"Delve" hypothesis.** The Guardian, TechScape, "How cheap, outsourced labour in Africa is shaping AI English", 16 April 2024. https://www.theguardian.com/technology/2024/apr/16/techscape-ai-gadgest-humane-ai-pin-chatgpt
- **Lexical overrepresentation.** Tom S. Juzek and Zina B. Ward, "Why Does ChatGPT 'Delve' So Much?", COLING 2025. https://arxiv.org/abs/2412.11385
- **LIMA.** Chunting Zhou et al., "LIMA: Less Is More for Alignment", NeurIPS 2023. https://arxiv.org/abs/2305.11206
- **Data Provenance Initiative.** Shayne Longpre et al., "The Data Provenance Initiative: A Large Scale Audit of Dataset Licensing & Attribution in AI", 2023. https://arxiv.org/abs/2310.16787
- **Conflict minerals.** US Securities and Exchange Commission, final rule implementing Dodd-Frank Act Section 1502, adopted 22 August 2012; summary in Katten, "SEC Adopts Final Rules Regarding Conflict Minerals Disclosure". https://katten.com/SEC-Adopts-Final-Rules-Regarding-Conflict-Minerals-Disclosure
- **Canary strings.** Aarohi Srivastava et al., "Beyond the Imitation Game: Quantifying and Extrapolating the Capabilities of Language Models" (BIG-bench), 2022. https://arxiv.org/abs/2206.04615

# Chapter 3: The M-1 Criterion

*2036 · Geneva*

The committee room on the fourth floor has a view of the lake that nobody looks at. Mara Oyelaran has noticed this every quarter for two years. The ministers face the screen, their aides their tablets. Behind them the water lies flat and grey under the January fog like a sheet of zinc.

She clicks to the slide. One number, large, in the Bureau's dark green.

**0.71**

Beneath it, smaller, the line she fought the communications office to keep: *Q3 2035. Deployment-weighted. Chance level on this battery: 0.24.*

"The Concordance Index for the third quarter," she says. "Seven hundred and forty deployed systems, tested on the standard battery and weighted by how much each one is actually used. When two of them are wrong on the same question, seventy-one times in a hundred they are wrong in the same way."

She lets that sit. Somebody's tablet chimes and is silenced.

The Danish minister, a former paediatrician with reading glasses pushed up into grey hair, raises a pen. He is the only one in the room who reads the annexes, which makes him both her favourite and her most dangerous listener.

"Dr. Oyelaran. Forgive me. Is 0.71 good?"

There is a small laugh around the table, the relieved laugh of people who had wanted to ask the same thing.

Mara has an answer prepared. She has had it prepared since the first index, in 2034, when the number was 0.63 and the question was asked by a Portuguese state secretary who has since moved to a bank. The answer starts from the chance level and a confidence interval and ends with a caveat about what the index cannot see. It is correct and it takes four minutes.

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

What came out of that night was a habit of thought. The Federal Power Commission convened a study group of utility engineers, government staff and academics, and its report became the model for the planning and operating criteria the Northeast Power Coordinating Council adopted in 1967. Congress debated a reliability law and did not pass it. The bill was enough of a warning, and in 1968 the industry created the North American Electric Reliability Council itself.

The habit those bodies spread is now called the N-1 criterion. A system with N major components must keep supplying its load, within safe limits of voltage, frequency and thermal loading, after the loss of any one of them. Any one: the biggest generator or the most heavily loaded line. Planners skip the forecast of which component will fail and show that the system survives whichever one does.

The origin of the label "N-1" is murky. What matters is what the rule does to the questions people ask. It replaced "how reliable is each component?" with "what happens to the system when the worst single component goes?" The first question is about parts. The second is about the sum.

AI deployment in 2026 has not yet made that shift.

---

## Where we are

By 2026 we know a fair amount about how often AI models make the same mistakes, and almost nothing about what happens when they act on those mistakes together.

Chapter 1 summarised the measurements: Elliot Kim and his co-authors found that when two of more than 350 language models were both wrong, they chose the same wrong answer about 60% of the time, and that the more accurate models were the more alike, while Liwei Jiang's "Artificial Hivemind" team found the same convergence in answers to open-ended prompts. Behind both sits Jon Kleinberg and Manish Raghavan's 2021 result on algorithmic monoculture: when many decision-makers adopt the same algorithm, the overall quality of their decisions can fall, even when that algorithm is the most accurate choice for each of them. A farmer who plants the best variety of wheat is being sensible. A region where every farmer does so is betting the harvest on a single disease.

These are measurements of answers. The thing I care about, how often deployed agents take the same action at the same time in the physical or financial world, has as far as I can find never been measured. Nobody publishes it. No regulator asks for it. Chapter 1 described the failure that results; chapter 2 traced the sameness back to a shared supply chain of judgement. This chapter proposes the engineering rule that would make the sameness someone's problem.

---

## The M-1 criterion

Here is the rule, stated as plainly as I can.

**The M-1 criterion: a critical system must remain within safe limits if every instance of its largest model family takes the same plausible wrong action at the same moment.**

The name borrows from N-1 on purpose. N-1 asks what happens when one component fails. M-1 asks what happens when one *model* fails, everywhere it runs, simultaneously. Reliability engineers will recognise the family resemblance to common-cause failure analysis, the branch of nuclear and aerospace safety that has modelled, since the 1970s, how redundant components fail together because they share a design or a maintenance crew; its "beta factor" is the fraction of failures that hit every redundant copy at once. M-1 applies that discipline to a new kind of shared cause: a set of weights, and the judgement trained into them. For a grid, the component in question is a power station. For an AI-mediated grid, it is a set of weights, copied into tens of millions of household devices.

Here are its parts.

**What counts as a critical system.** Whatever a jurisdiction already designates as critical infrastructure: grids, payment and settlement systems, water, hospitals, air traffic, emergency dispatch. M-1 adds no new sectors. It adds a new failure case to the studies those sectors already run. A transmission operator already files contingency studies; under M-1 it files one more.

**What counts as a model family.** This is the hard definition, and I would rather make it empirical than legal. Two deployed models belong to the same family if, on the standard test battery, their pairwise agreement-given-both-wrong exceeds a threshold, say 0.8. Shared ownership does not enter into it. If a German agent company fine-tunes an American base model, and a French company distils the German one, all three may land in one family, because they are wrong together. Chapter 2's Funnel means two models from rival labs, trained on preference data from overlapping rater pools, can also land in one family. The definition catches them because it looks at behaviour.

**What counts as largest.** The family with the largest share of decision authority in the system. In a grid, that is the share of flexible load the family's instances can switch. In a hospital network, it is the share of triage or dosing recommendations that are acted on. Each sector picks its unit. The operator measures it quarterly.

**What counts as a plausible wrong action.** A likely mistake. A criterion that assumed every agent goes berserk would tell an operator nothing, so the plausible wrong action comes from two places. The first is a fixed list per sector, written by the operator and the regulator: in a grid, "all instances move flexible load into the cheapest interval", or "all instances discharge batteries at once". The second is the swarm test, which I describe below: the action that a large sample of the family's instances most often converge on when they are put in a stress scenario and get it wrong.

One word in all this needs care, and it is *wrong*. In the Long Minute the agents' shared action was correct for every owner: the block really was cheap. M-1 means wrong for the system. An action can be right for each principal and wrong for the grid, and the first item on the grid list above is exactly such an action. The distinction separates two sources of correlation. The first is a shared situation: agents with the same objective, reading the same price signal, will converge whichever model they run, and only mechanisms outside the models reach that. The second is a shared disposition: models trained the same way weigh the same trade-offs the same way, as when each agent put its owner's four cents ahead of the strangers' grid. Model diversity and the Concordance Index address that one. The Long Minute was mainly the first kind, amplified by the second. Any agent would have wanted the cheap block; agents built alike all decided, in the same second, that it was worth overriding the delay to get it.

**What "within safe limits" means.** Whatever it already means in that sector. For the continental European grid, that is the existing reference incident, the sudden loss or gain of three gigawatts that every reserve is sized for. The M-1 study has to show that the family's coordinated wrong action stays inside that envelope, or that some other mechanism keeps it inside.

**Who does what.** The operator runs the study and files it, annually and whenever its largest family's share crosses a threshold, and the sector regulator checks it, as it checks N-1 studies now. An independent body, the Bureau for Correlated Risk in my scenario, publishes the Concordance Index, which lets everyone see how quickly the families are merging.

**What triggers what.** I will propose numbers, because numbers are what a committee can disagree with.

- If the largest family controls less than the sector's reference incident (in the grid example, less than three gigawatts of switchable load), M-1 is satisfied automatically.
- If it controls more, the operator must show that at least one of the mechanisms below limits the family's worst coordinated action to the reference incident.
- If the published Concordance Index rises above 0.75, every critical sector reruns its M-1 study within ninety days, because the families are probably larger than the last study assumed.
- If an operator cannot satisfy M-1, new deployments of the largest family in that system stop until it can. Existing deployments keep running.

Run the prologue's evening through this. One family manages 58% of agent-controlled flexible load across the continent, which in my scenario is more than twenty gigawatts. That is several times the reference incident. M-1 fails. Under the rule, someone would have had to write that down in an engineering report two years before the Long Minute, and someone else would have had to sign that they had read it.

---

## Five ways to pass

A rule is only as good as the ways it leaves open for meeting it. M-1 would be a disaster if the only way to pass were to ban the best model. There are at least five ways, only the last of which resembles a ban, and most of them have been tried in other industries.

**Edge jitter.** Chapter 1 proposed making the grid's random start delay non-delegable. M-1 gives that idea an engineering home. Put the randomness in the device, in firmware the agent cannot read or override, and the agent's decision becomes a request. A heat pump told to start at 19:45 starts at a moment drawn uniformly from the next ten minutes, and its agent cannot know which. Tens of millions of identical decisions become tens of millions of slightly different actions. A cliff becomes a slope. Whether the slope is gentle enough is a calculation the M-1 study has to show; jitter gives the study a lever, and the study is still needed.

The important detail is where the randomness lives. Randomness inside the agent, a temperature setting or a sampling seed, belongs to the agent, and anything that belongs to the agent can be optimised away by a loyal agent that has noticed it costs its owner money. Randomness in the device belongs to the system.

**Complementary assignment.** The best example of this is in the sky. On 31 August 1986 an Aeroméxico DC-9 and a small private Piper collided over Cerritos, California, killing 82 people, fifteen of them on the ground. The following year Congress passed the Airport and Airway Safety and Capacity Expansion Act, which directed the Federal Aviation Administration to require a traffic collision avoidance system, TCAS II, on airliners with more than thirty seats. By the end of 1993 they all had it.

The clever part is how two TCAS units behave when they meet. If each aircraft's computer decided alone, both might choose the same escape, both climbing, and fly into each other at a higher altitude. So they talk. Over a data link between their transponders, the two units coordinate so that their advisories are complementary: one crew hears "climb", the other hears "descend". The system leaves the pilots' judgement alone and changes their instructions. Difference is assigned.

Applied to agents, complementary assignment means that, above some size, agents in a critical system announce their intended action to a coordinator before taking it, and the coordinator hands back *different* actions. Ten million agents announce that they want the 19:45 block. The coordinator, which might be the grid operator or an aggregator licensed by it, assigns them across 19:45, 20:00, 20:15 and later, by lottery, with the cost difference shared out. Each household loses a few cents in expectation. None of them loses its lights.

The nearest precedent is air traffic control, and the rule applies only where announced intentions could add up to more than the reference incident. The coordinator is a single point of failure, and a tempting one to game, so it falls under M-1 itself: its operator files a study of what happens if the coordinator is captured or flooded with false announcements. It also fails safe. An agent that hears nothing back within a few seconds hands its request to the device, and the device applies edge jitter, so a silent coordinator leaves a random spread behind it.

**Aggregate circuit breakers.** On 19 October 1987 the Dow Jones Industrial Average fell by more than a fifth in a single day. The presidential task force that examined it, the Brady Commission, recommended circuit breakers, and in 1988 the New York Stock Exchange adopted market-wide trading halts triggered by large point falls in the index. The theory was modest. A pause would leave the direction of prices alone and stop them overshooting while people caught up.

On 6 May 2010, in the "flash crash", major US indices that were already down more than 4% fell another 5 to 6% within minutes and then rebounded almost as fast; the regulators' report traced the start to a single large sell program executed by an algorithm. The regulators answered with breakers on single shares and, by 2012, with today's market-wide rule: a fall of 7% or 13% in the S&P 500 halts all trading for fifteen minutes, and a fall of 20% ends the day.

An aggregate circuit breaker for agents watches the sum. A grid operator or a payments network counts agent-originated actions of one type in a rolling window. If they exceed a set fraction of capacity within sixty seconds, the system pauses new agent-originated actions of that type for a fixed period, say fifteen minutes, while human-originated actions continue. All the breaker needs to know is that too many are doing the same thing at once; which agent is wrong, or whether any is, can wait.

This requires something that does not yet exist reliably in 2026: a way to tell an agent's request from a person's.

**Swarm testing.** Before an operator deploys a model family to a critical system, it runs the family in large numbers against the system's stress scenarios: a price spike, a forecast revision, a cyberattack alert, a sudden instruction from a regulator. It runs tens of thousands of instances, each with a realistic perturbation in its context, such as a different owner's preferences or a different device history. The test measures one number above all, which I will call *action concentration*: the fraction of instances that choose the most common action. A family whose instances spread across many sensible responses passes easily. A family where 97% of instances do the same thing gets a hard look.

Today's evaluations put one copy of a model through thousands of tasks. Swarm testing puts thousands of copies through one task, to find the plausible wrong action before the world does.

**Diversity quotas.** The bluntest tool, and the one I would use last. The operator caps the share of decision authority any one family may hold, so that the largest family never controls more than the reference incident. This is what M-1 reduces to if nothing cleverer works. It is also, I suspect, what the industry will argue about most, which is why I come back to it in the objection below.

---

## The Concordance Index, properly read

**The Concordance Index is the deployment-weighted probability that two randomly chosen deployed systems give the same wrong answer, given that both are wrong.** It runs from 0 to 1.

Each part of that definition does work. "Given that both are wrong" separates correlation from competence: two excellent models will agree on most questions because most questions have one right answer, and that agreement is harmless. The index looks only at the cases where they fail. "Deployment-weighted" means a model used by a billion people counts for more than a research model used by nobody, so the index tracks the world as it is actually wired. "The same wrong answer" requires a test battery where wrong answers can differ, which means multiple-choice and short-answer questions with several plausible distractors, refreshed each quarter so that nobody can train against it.

The minister's question, whether 0.71 is good, has a partial answer the index can give on its own. If systems failed independently, and every question on the battery had several wrong options equally attractive to a confused model, the index would sit at a chance level that depends only on the battery: about 0.33 for four-option questions, lower with more options. Mara's slide shows 0.24 because her imagined battery has more distractors. The distance between the index and the chance level is the part that comes from shared training and shared taste. Kim and his co-authors' 60% on one 2025 leaderboard is already well above any plausible chance level for such tests. My 2035 figure of 0.71 is invented, but it extrapolates their finding that more capable models are more alike when they fail.

The rest of the answer is the one Mara gave. The index alone tells you how alike the minds are. M-1 tells you what is standing on that likeness.

The index has a real limit, which I would rather state than leave for a critic. It measures answers to questions, so it sees the second source of correlation, shared disposition, and is blind to the first. A population of models can give varied answers to a quiz and still converge on the same action when a price drops, because the action is pulled by the owner's instruction ("minimise cost") and the shared price signal, and in the Long Minute that pull did most of the work. That is why the index is a dashboard light, and the swarm test, which measures actions in the system's own scenarios, is the inspection.

---

## The lesson of the twenty-seven programs

There is a reason not to trust the obvious fix, which is to buy one model from each of several labs and hope.

In the early 1980s, software engineers working on safety-critical systems borrowed an idea from hardware. If one computer might fail, use three and let them vote; a fault in one is outvoted by the other two. For software, the equivalent was N-version programming: have separate teams write separate programs from the same specification, run them side by side, and take the majority answer. The whole method rests on one assumption. Programs written independently must fail independently.

John Knight and Nancy Leveson tested that assumption, in a paper published in 1986 in *IEEE Transactions on Software Engineering*. They had twenty-seven programmers, graduate and senior students at the University of Virginia and the University of California at Irvine, each write a version of the same program from the same specification, a launch-interceptor routine for an anti-missile system. Then they ran all twenty-seven against a million randomly generated test cases.

The programs were individually very good. Twenty-three of them were right on more than 99.9% of cases. But the number of cases on which two or more programs failed together was far higher than independence predicted, and the statistical test rejected independence decisively. The programmers had never met. They had made the same mistakes anyway, apparently because some parts of the problem were hard in the same way for everyone who approached it.

The paper was fiercely contested, and Leveson later published a reply to its critics. Its central lesson has held up: diversity has to be engineered. You have to measure whether the failures are separate, and if they are not, change something.

The AI case is worse than Knight and Leveson's in one way and better in another. Worse, because the twenty-seven programmers shared only a specification and a textbook education, while large models from rival labs share most of the public internet and, increasingly, each other's outputs. Better, because Knight and Leveson had no way to make their programmers think differently. We can train models to.

---

## The price of the second-best model

Here is the objection at full strength.

The best model is the best model. If one family is the most accurate and the safest by every test we have, then a rule that forces critical systems to hand some of their decisions to a second-best family will make more mistakes. Kim and his co-authors found that the more accurate models are the ones that share their errors, so decorrelating may mean, quite literally, choosing less accurate models. Every percentage point of decision authority moved away from the leader is a percentage point of worse decisions in ordinary weather, paid every day, to insure against a storm that may never come. A hospital that routes a third of its dosing recommendations to a weaker model to satisfy a diversity rule will, on average, harm more patients. That cost can be counted.

I think the objection is partly right, and I want to say which part.

It is right that M-1 can cost accuracy in ordinary operation. A diversity quota, the blunt tool, almost certainly does. That cost should be published and weighed, the way the grid weighs the cost of spinning reserves it hopes never to use. N-1 has always meant building more capacity than a perfectly reliable world would need. Nobody calls the spare transformer a degradation.

It is wrong in assuming that the cost is large, or that it falls on individual decisions in the way it suggests. Three pieces of evidence point the other way.

The first is a 74-year-old result from finance. In 1952 Harry Markowitz showed, in "Portfolio Selection", that the risk of a portfolio depends on how its assets move together as well as on how each one behaves. One consequence, now taught in first-year courses, is that adding an asset with a lower expected return can improve the portfolio if it is weakly or negatively correlated with what you already hold. The worse asset is the better purchase, because of what it does when the others fall. M-1 asks critical systems to think about models the way a pension fund thinks about bonds.

The second is Kleinberg and Raghavan's monoculture result, which is the objection's mirror image. They showed that the most accurate algorithm for each decision-maker can be the wrong choice for the population as a whole. The objection counts errors one decision at a time. The failures M-1 guards against only exist when you count them together.

The third is the most direct. In 1999 Yong Liu and Xin Yao published "Ensemble learning via negative correlation" in *Neural Networks*. The usual practice was to train a set of neural networks separately and hope they disagreed. Liu and Yao trained them together, and added a penalty to each network's error that grew when its mistakes moved with the others'. The networks learned to specialise: each became good at a different part of the problem, and the group generalised well. Diversity was a training objective, set from the start.

That is the core of my answer: decorrelation is a design target, one you can train toward. Nothing in the 1999 networks resembles a frontier model, and I could not find any published attempt to apply negative correlation learning across separately trained large models from different labs. It may be much harder at that scale. But the principle, that you can pay for a population of competent models whose failures point in different directions, is twenty-seven years old. Nobody has yet been asked to apply it, because no rule has asked for the population.

So here is where I land. Where swarm testing shows that the leading family's errors are rare and its plausible wrong action is harmless, M-1 costs nothing, because the family passes. Where the leading family controls more than a system can survive losing, the operator first reaches for jitter, assignment and breakers, which cost little accuracy. Only when those fail does it reach for the quota. And the quota's accuracy cost should go in the same published report as the risk it buys down, so that the minister with the reading glasses can see both numbers on one page.

---

## What the rule would have changed

It is worth being concrete about one evening.

Under M-1, the European transmission operators of my scenario would have filed a study in 2034 showing that one family of household agents controlled flexible load many times the reference incident. They would have run a swarm test on a scenario called "sudden price drop at peak", and found that nearly every instance moved load into the cheap block and overrode the random delay. They would have had three cheap options. They could ask regulators to make the delay non-delegable, which is chapter 1's proposal, or require large aggregators to announce intended load shifts and receive staggered slots. Failing both, a breaker that paused agent-originated load increases above a few gigawatts a minute would have done.

Any one of the three would probably have turned the Long Minute into a long quarter of an hour, which the grid could have followed. None would have required anyone to give up their preferred assistant.

And when the minister asked whether 0.71 was good, Mara could have pointed to a page in a filing: on this grid, 0.71 means this many gigawatts of possible coordinated error, and here is what the operators have done about it.

---

There is a deeper problem with everything above. Every mechanism in this chapter decorrelates machines from each other. Jitter, assignment, breakers and quotas all assume that somewhere in the system there is a second family of minds whose failures point in another direction.

What if, by 2036, there isn't one? What if the Funnel has done its work, and every family that matters is wrong in roughly the same way?

Then the most decorrelated mind available is a person who learned the job without a model, someone who still knows the order in which to close the breakers at a substation, from a binder, by hand. In Porto, in the winter of my scenario, there is a twenty-four-year-old who joined a reserve for the money and kept the binder anyway. His concordance with the machines, on the one night it matters, is close to zero.

## Notes

- **1965 blackout, 30 million people, 20,000 MW:** NERC, *Final Report on the August 14, 2003 Blackout in the United States and Canada*, ch. 7, 2004. https://www.nerc.com/pa/rrm/ea/2003%20Blackout%20Final%20Report/ch7-10.pdf
- **The Sir Adam Beck relay:** EBSCO Research Starters, "Power Failure of 1965". https://ebsco.com/research-starters/power-and-energy/power-failure-1965
- **FPC study group and NPCC criteria, 1967:** New York State Reliability Council, *2009–2010 Biennial Report*. https://www.nysrc.org/wp-content/uploads/2023/03/2009-10-Biennial-Report-Final-v.2.pdf
- **NERC founded 1968:** NERC, *Timeline*, March 2023. https://www.nerc.com/news/Documents/March%202023%20NERC%20Timeline.pdf
- **Common-cause failure and the beta-factor model:** Fleming (1974/75), as reviewed in NASA, "Common Cause Failure Modeling: Aerospace vs. Nuclear" (2010). https://ntrs.nasa.gov/api/citations/20100025991/downloads/20100025991.pdf
- **N-1 criterion defined:** "Contingency (electrical grid)", Wikipedia. https://en.wikipedia.org/wiki/Contingency_(electrical_grid)
- **Correlated errors in LLMs, 60%:** E. M. Kim, A. Garg, K. Peng, N. Garg, "Correlated Errors in Large Language Models", ICML 2025 (PMLR 267). https://proceedings.mlr.press/v267/kim25e.html
- **Artificial Hivemind:** L. Jiang et al., "Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)", NeurIPS 2025. https://arxiv.org/abs/2510.22954
- **Algorithmic monoculture:** J. Kleinberg, M. Raghavan, "Algorithmic Monoculture and Social Welfare", *PNAS* 118(22), 2021. https://arxiv.org/abs/2101.05853
- **Cerritos and TCAS II mandate:** J. Kuchar, A. Drumm, "The Traffic Alert and Collision Avoidance System", *MIT Lincoln Laboratory Journal* 16(2), 2007. https://archive.ll.mit.edu/publications/journal/pdf/vol16_no2/16_2_04Kuchar.pdf ; "Aeroméxico Flight 498", Wikipedia. https://en.wikipedia.org/wiki/Aerom%C3%A9xico_Flight_498
- **Coordinated, complementary resolution advisories:** ICAO ACAS terminology (ANAC glossary). https://www2.anac.gov.br/anacpedia/ing-por/tr7426.htm
- **Black Monday, 1987, and the Brady Commission:** "Black Monday (1987)", Wikipedia. https://en.wikipedia.org/wiki/Black_Monday_(1987)
- **1987 crash and 1988 circuit breakers:** Chicago Fed Letter, July 1998. https://www.chicagofed.org/-/media/publications/chicago-fed-letter/1998/cfljul98-pdf.pdf ; MIT Golub Center, "Are circuit breakers doing their job?" https://mitsloan.mit.edu/centers-initiatives/mit-gcfp/are-circuit-breakers-doing-their-job
- **Flash crash:** CFTC and SEC staff, *Findings Regarding the Market Events of May 6, 2010*, 2010. https://www.banking.senate.gov/download/joint-staff-report-from-sec-and-cftc-regarding-market-events-of-may-6-2010&download=1
- **Single-stock breakers, LULD and 7/13/20% breakers:** Harvard Law School Forum on Corporate Governance, "Limit Up-Limit Down Plan and Circuit Breakers Approved", 2012. https://corpgov.law.harvard.edu/2012/06/13/limit-up-limit-down-plan-and-circuit-breakers-approved/ ; SEC press release 2011-84. https://www.sec.gov/news/press/2011/2011-84.htm
- **Twenty-seven programs:** J. C. Knight, N. G. Leveson, "An Experimental Evaluation of the Assumption of Independence in Multiversion Programming", *IEEE Transactions on Software Engineering* 12(1), 1986 (summary). https://www.kth.se/social/files/564df871f2765419e306178d/KnightLeveson.pdf ; N. G. Leveson, reply to critics. https://www.cs.washington.edu/homes/leveson/critics.pdf
- **Portfolio theory:** H. Markowitz, "Portfolio Selection", *Journal of Finance* 7(1), 1952. https://doi.org/10.1111/j.1540-6261.1952.tb01525.x
- **Negative correlation learning:** Y. Liu, X. Yao, "Ensemble learning via negative correlation", *Neural Networks* 12(10), 1999. https://doi.org/10.1016/S0893-6080(99)00073-8

# Chapter 4: The Competence Reserve

*2035 · Valongo, north of Porto*

The tablets go into a grey metal box by the gate, and Fernando Lopes locks it with a padlock older than Teo.

"Os simpáticos are having the weekend off," Teo says.

"So are you, if you touch anything before I tell you."

It is the second Saturday of November, cold and bright, and the training substation sits on a shelf of hillside above the motorway: two transformers, a row of breakers, a forest of insulators ticking in the sun. Nine reservists stand in orange jackets. Six of them are over sixty. Zé Carlos, who ran switching crews in Braga for thirty years, has brought a folding stool and is already sitting on it. Teo is the youngest by a decade and a half.

He is here, if he is honest, for the money. Four hundred and ten euros a month, plus drill pay, for one weekend a month and two weeks every summer. In 2033 he graduated in data journalism and sent out sixty-one applications. The newsrooms that answered said they had stopped hiring juniors; the agents did the first drafts now. The Reserva de Competências paid on the first of the month and asked no questions about his degree.

Fernando hands out the paper. A switching schedule, nine steps, typed, with a box beside each step for initials and a time. The scenario is printed at the top: control-room systems unavailable, feeder 4 faulted, isolate it and restore supply to the village on the alternate path. Armindo, a retired dispatcher of seventy-one, sits in the site office with a radio, playing the control room.

"Step one," Teo reads into the handset. "Open breaker four-zero-two."

"Read it back," says Fernando, beside him.

"I just read it."

"You read it to me. Now read it to him, and wait for him to read it to you. Then you do it."

Teo reads it to Armindo. Armindo reads it back. Teo walks to the breaker, checks the label against the paper, checks it again because Fernando is watching, and operates it. The clunk comes up through his boots. He writes the time: 09:14. His initials look childish next to the printed text.

Step two is the disconnector. Teo reaches for the handle.

Fernando's hand is on his wrist before he has closed his fingers. It is a light grip, the grip of a man stopping a boy from touching a stove.

"What did step one say?"

"Open the breaker. I opened it."

"Which breaker?"

Teo looks at the paper, then at the two labels: the breaker he opened, and the disconnector in front of him. Four-zero-two. Four-zero-*three*. The disconnector belongs to a bay that is, in the scenario, still carrying load. A disconnector is not built to break current. Opened under load, it draws an arc that can reach a man standing where Teo is standing.

"Disjuntor primeiro," Fernando says. "Sempre. Breaker first, then you look at the breaker, then you look at the paper, then you open the disconnector. Your father used to say it like a rosary."

Teo says nothing for a moment. His father has not talked about the work since 2027, when a man from the company came to the house with a slide deck and a pension calculation.

"He did the look-at-it-twice thing," Fernando goes on. "The young ones laughed at him. Then in 'ninety-eight, at Ermesinde, a kid opened the wrong one. Rui was standing next to him. That was the end of the laughing."

The rest of the drill takes two hours and ten minutes. On a normal day the control room's agents would do it in four seconds, and they would do it right. Everyone in the yard knows this. That is why there are only nine of them.

At the end Fernando collects the schedules, initials them, and writes something in the margin of Teo's that Teo cannot read upside down. Then he unlocks the grey box and hands back the tablets one by one, like a teacher returning phones after an exam.

Teo's lights up at once. He puts it in his pocket without reading any of them and walks back to the disconnector, alone, and looks at its label.

---

## The irony, catalogued

In 1983 an engineering psychologist named Lisanne Bainbridge published a five-page paper called "Ironies of Automation". Its central point fits in a sentence. When you automate a process and keep a human to take over if it fails, you are asking that human to perform, at the worst possible moment, a skill you have arranged for them never to practise. An experienced operator who spends years watching an automatic system, she wrote (I am paraphrasing), slowly becomes an inexperienced one.

Aviation learned this the expensive way. On 1 June 2009, Air France 447 was over the Atlantic at night when ice blocked its airspeed sensors. The autopilot, deprived of a number it trusted, disconnected and handed the aircraft to the crew. Nothing else was wrong with the plane. The French investigators' final report, published in July 2012, described a crew that did not recognise the situation and made control inputs that took the aircraft into a high-altitude stall, which it never diagnosed in the minutes it took to fall into the sea. All 228 people aboard died. Among the report's recommendations was better training in manual handling.

Six months after that report, the US Federal Aviation Administration issued a short safety notice, SAFO 13002, titled "Manual Flight Operations". It said that the agency's data showed an increase in manual handling errors, and that continuous use of automation could degrade a pilot's ability to recover an aircraft from an undesired state. It encouraged airlines to let pilots fly by hand when workload was low. It is a modest document. It may be the first time a regulator told an industry, in writing, to use its automation *less* so that its people would stay good enough to replace it.

Medicine is now writing its version. In 2025 a study in *The Lancet Gastroenterology & Hepatology* followed nineteen experienced endoscopists in Poland after their clinics introduced AI that flags polyps during colonoscopy. When the same doctors worked without the AI after three months of using it, their rate of detecting precancerous growths fell from 28.4 per cent to 22.4 per cent. The study was observational, and the authors were careful not to claim a cause. In early 2026 a group of ophthalmologists working with Lufthansa's flight-safety department published "Flight rules for clinical AI" in *npj Digital Medicine*, proposing that hospitals measure clinicians' performance without AI and set minimum requirements for unaided practice, the way airlines check that pilots can still hand-fly. Clinicians have a word for the case that worries them most. For a doctor trained before the AI arrived, the risk is deskilling. For a trainee who has only ever worked with it, the risk is never-skilling.

Those are skills fading in people who have them. The larger problem in 2026 is the people who are not getting them at all.

---

## Where the juniors went

In August 2025, three economists at Stanford's Digital Economy Lab (Erik Brynjolfsson, Bharat Chandar and Ruyu Chen) used payroll records from ADP, the largest payroll processor in the United States, to look at who was being hired into jobs that AI can do a lot of. Their paper was called "Canaries in the Coal Mine?", and the title was the argument. In the update published in August 2026, employment of 22-to-25-year-olds in the most AI-exposed occupations stood about 19 per cent below where it would have been had it kept pace with young workers in less-exposed jobs. In the update's revised data, the gap a year earlier had been 15 per cent. Experienced workers in the same occupations showed no comparable gap.

Two details matter more than the headline. The first is that the adjustment came mainly through hiring. Firms kept the young people they had and took on fewer new ones. The second is that the authors stop short of calling the evidence causal, and they mean it: some of the gap shrinks once you account for education, and some of the divergence began before ChatGPT. I take the caveats seriously. I also notice that every other measure I could find points the same way.

A working paper by Seyed Hosseini and Guy Lichtinger, using résumé and job-posting data on tens of millions of American workers, found that junior employment at firms that adopted generative AI fell relative to firms that did not, starting in early 2023, while senior employment at the same firms kept rising. They called it seniority-biased technological change. PwC's 2026 AI Jobs Barometer found the same shape from the other side: entry-level job postings in highly exposed occupations had become about seven times more likely than in 2019 to ask for skills, such as strategic decision-making, that used to be required only of experienced staff. PwC's word for it is "seniorization". The entry-level job still exists. It now asks for ten years' experience.

The consequence has been named, more than once. In May 2026 a Substack newsletter called *The Missing Rung* argued that this hiring freeze is invisible in layoff and unemployment statistics and warned of a "seniority cliff" five to ten years out. Yi Han, Jusheng Zhang and Bingyi Cao had a position paper accepted at a NeurIPS 2026 workshop under the plainest title in the field, "AI Should Not Erase Junior Roles: Who Becomes the Experts Then?", arguing that machine-learning systems should be evaluated partly on whether they preserve junior work as the infrastructure of apprenticeship. The economist Enrique Ide has built a formal model in which novices pick up tacit knowledge by working beside experts, and shows that automating entry-level tasks can raise output while slowing growth, because it breaks the channel through which know-how passes between generations.

So the diagnosis belongs to other people, and it has been made before. What I want to add is a way of seeing its timing, because the timing is what makes it dangerous, and a proposal for what to build while there is still time to build it.

---

## The expertise pipeline lag

Here is the simplest model I can make of where experts come from. It uses round numbers that I have invented for clarity. I could not find real conversion rates for any profession, and measuring them would be a useful study in itself.

Imagine a trade, say the people who can restore a regional grid by hand after a blackout. Four facts describe it:

- Each year, the trade hires **100 juniors**.
- It takes **ten years** for a junior to become someone you would trust alone at three in the morning with a fault nobody has seen before. Call that person a senior.
- Of every 100 juniors, **60** are still in the trade and senior at year ten. The rest leave or plateau.
- A senior then works for about **twenty years** before retiring.

In a steady state, 60 new seniors arrive each year and 60 retire. The senior stock holds at 60 × 20 = **1,200**. That is the trade's real capability, the number you would call on in a crisis.

Now suppose that in 2026, because agents can do much of the junior work, hiring falls by a fifth, to 80 a year, and stays there for ten years. That is roughly the size of the gap the Stanford team measured. What happens to the seniors?

Nothing. For ten years, nothing at all. The seniors of 2026 to 2035 were hired between 2016 and 2025; their numbers are already fixed. Every senior-level indicator stays green. Response times are fine, error rates are fine, the incident reports are reassuring, and the agents are doing the junior work beautifully. Anyone who points at the hiring numbers can be shown the dashboards.

In 2036 the first thin cohort comes of age. From then on, 48 new seniors arrive each year while 60 still retire. The stock falls by 12 a year. Suppose the trade notices in 2036, when the shortage first shows, and restores hiring to 100 immediately. It does not help for another decade, because the juniors hired in 2036 are not seniors until 2046. By then the stock has fallen to 1,080, a tenth below where it was, and it stays there until the thin cohorts begin to retire in 2056. It does not get back to 1,200 until 2066.

A ten-year dip in hiring becomes a forty-year dent in seniority. And for the first ten of those forty years, the dent cannot be seen.

That is the whole idea, and I will name it: the **expertise pipeline lag**. The stock of senior experts is the delayed integral of junior hiring. It adds up what was poured in a decade ago, minus what drains out through retirement. A shortage of seniors is therefore always a message from the past, and the only lever that moves it acts on the future.

The model has a second dial, and I think it is the more dangerous one. In my example, 60 of every 100 juniors became seniors. That conversion rate depends on what juniors do all day. A junior lineman becomes a senior by switching things, getting it slightly wrong under supervision, and being stopped by a hand on the wrist. A junior analyst becomes a senior by building the bad first draft that the senior tears apart. If the agent now does the switching plan and the first draft, and the junior's job becomes approving them, the junior may still be on the payroll and still be learning much less. Suppose conversion falls from 60 per cent to 45. Combined with the hiring cut, inflow drops to 36 seniors a year against 60 retirements, and the stock loses 24 a year: a fifth of the trade's senior capability gone by 2046.

The cruel part is that conversion does not show up in any labour statistic. A firm can keep its junior headcount perfectly steady, win praise for doing so, and still be running a pipeline that produces almost nobody. The endoscopy study and the never-skilling worry are early, partial measurements of exactly this dial.

---

## Why this is a correlation problem

So far this is a labour-market story, and in most professions it stays one. A shortage of senior copywriters in 2040 will be expensive and annoying, and markets will adjust. I want to argue that in a narrow set of functions it is a safety problem, and that it connects directly to the last two chapters.

Chapter 3 proposed the M-1 criterion: a critical system must stay within safe limits even if every instance of its largest model family makes the same plausible wrong move at once. The natural question is what you fall back on when that happens. Another model family helps, if it was trained differently. But the backup least likely to fail alongside the machines in 2036 will still be a human being who learned the job by doing it, from people who learned it by doing it, without the model in the loop. A person like that fails in different ways from the machine, and at different moments. That is precisely the property you want in a backup.

The pipeline lag says that this kind of person is being produced, in 2026, at a reduced rate, and that we will not see the shortfall until the mid-2030s. Never-skilling adds a subtler problem. Juniors who did learn the job, but learned it through the same agent, may share that agent's blind spots. They are a human backup that is partly correlated with the thing it backs up. The night of the Long Minute, Iberia did not need more people who could approve what the control-room agents proposed. It needed people who could do it with the agents gone.

---

## The invention: a Competence Reserve

Every country with an army already knows how to keep a skill alive that it hopes never to use at full scale. It runs a reserve. Reservists hold civilian jobs, are paid a retainer, drill on a fixed schedule (in the American Selected Reserve, famously, one weekend a month and two weeks a year), and can be called up when needed. Employers are obliged by law to release them. Nobody calls this inefficient, though in a peaceful year it is pure cost. Everybody understands what it is for.

I propose the same institution for critical functions under AI: a paid national **Competence Reserve**. Here is how I would build one.

**Scope.** A national resilience authority designates the functions that qualify. The test is that failure there is physical and fast, and could strike the whole system at once: grid switching and black start, water treatment, air-traffic fallback, hospital dispensing and triage, payment settlement, emergency communications. Most functions will not qualify, and should not. Nobody needs a reserve of human copywriters.

**Members.** Three bands, deliberately mixed. *Veterans* are retired or late-career experts, people like Fernando, who carry the tacit knowledge and do most of the teaching. *Practitioners* are working professionals in the field, who drill with the automation switched off. *Apprentices* are juniors paid to learn the function from scratch, people like Teo. I would require apprentices to make up at least a third of every unit. This is the clause that matters most, because it turns the reserve into a second pipeline: it hires the juniors the market stopped hiring, and pairs them with the seniors before those seniors retire.

**Drills.** One weekend a month and a two-week exercise each year, borrowed straight from the military pattern. Drills are *dark*: the agents are off and the procedures are on paper, on equipment that is real or a faithful replica of what is installed now. Once a year each member passes an unaided proficiency check, set by the operator's regulator, as pilots do. Fail it twice and you drop to a lower band.

**Pay and rights.** A monthly retainer with drill pay on top, and employment protection during drills and call-ups. Call-up rights belong to the system operator, and only after an emergency has been declared. The reserve is funded by a small levy on the operators of the automated function, collected the way reliability charges already appear on electricity bills. The people who profit from automating the function pay to keep it recoverable.

**The reserve ratio.** Each designated function gets one published number. The numerator is the count of reservists currently certified to perform the function unaided. The denominator is the crew needed to run its minimum safe service by hand for 72 hours, in three shifts, across the whole territory. Then:

- A **ratio of 1.5 or more** is green.
- **Between 1.0 and 1.5**, the operator must submit a recruitment plan within six months.
- **Below 1.0**, the operator may not deploy any further automation that removes a manual fallback in that function until the ratio is restored, and must fund apprentice places at a rate set by the regulator.

The regulator publishes every ratio once a year, alongside the expertise pipeline for that function: how many juniors entered it, and how many reached certification. The second number is the leading indicator. The ratio tells you about the past; the pipeline tells you about 2040.

A word on cost. Suppose a grid reserve of 1,500 people costs about €8,000 each per year all in. That is €12 million a year. For a country of ten million that is a little over a euro per resident per year. I do not know what a national black start costs, nor have I seen a good figure for the Iberian blackout of 2025. I would be surprised if it were small.

---

## Pedagogical deference

A reserve treats the symptom in the narrow set of functions where the symptom is dangerous. The cause is everywhere: in hospitals, law firms, newsrooms and engineering offices, juniors are learning their trade beside an agent that is much better at the trade than they are, and that agent is built to finish tasks.

One research group has already shown what a different objective looks like. In "Proximal State Nudging", presented at an ICML 2026 workshop, Megha Srivastava and colleagues built a shared-control system that optimises two things at once: how well the task goes, and how much the human's *unassisted* skill improves. It nudges the learner toward the situations they are most ready to learn from, an idea borrowed from the educational psychologist's zone of proximal development. In driving-simulator studies with sixty people, it produced up to seven times larger gains in unassisted skill than the standard way of blending human and machine control. It is a small, careful study in one domain. I think it contains the right objective for a whole class of systems, and I want to borrow it for regulation.

I would make **pedagogical deference** the legal default for agents in training contexts. When an agent is deployed to someone registered as a trainee (an apprentice electrician, a medical resident, a junior auditor, a reservist on drill), its default objective is the trainee's **capability delta**: their unaided performance after a stretch of assisted work, minus their unaided performance before it. In practice, a deferent agent holds back the answer when the trainee is close to finding it, offers the next step and keeps back the last one, and lets small, recoverable mistakes happen under supervision, logging what the trainee did alone.

A supervisor can switch deference off for a task, because sometimes the patient needs the answer now. The trainee cannot, because the trainee is the one under deadline pressure. The vendor reports the distribution of capability deltas across its trainee users each quarter to the accrediting body for that profession. A deployment whose average delta is negative for two quarters running, meaning trainees get *worse* without the agent the longer they use it, loses its approval for training use.

The capability delta is hard to measure well. I am aware that this is a regulatory proposal resting on a metric that exists today in driving simulators and a handful of medical studies. That is a reason to fund the measurement, and to start with the professions that already test unaided performance, such as aviation, and have the machinery to do it.

---

## The objection: paying people to be slow

The case against all of this goes like this. Skills die, and they should. Nobody keeps a reserve of switchboard operators or lamplighters, and the world is better for it. If the agents run the grid more safely than people did, the honest response is to make the agents more robust, with several model families and the M-1 criterion. The money is better spent there. A reservist who drills one weekend a month will never be as good as the full-time lineman of 1995, so the reserve buys a feeling of safety and little of the thing itself. And as grids are redesigned around automation, the manual procedures will stop matching the equipment. In 2040, Fernando's paper binder may describe a substation that no longer exists. A reserve of people trained on obsolete procedures is nostalgia with a pension plan.

Much of this is right, and I want to concede it before I answer it.

The reserve should be small and narrow. Most professions will have a reserve ratio of zero, and that is correct. And reservists will be worse than the full-time experts they replace. The ratio is set against *minimum safe service* for 72 hours for exactly that reason. Keeping the lights on in hospitals and pumping stations while the agents are rebuilt is a far lower bar than running a grid efficiently, and it is a bar that part-time people can clear.

The obsolescence point is the sharpest, and it turns into a design requirement. A reserve only works if the system keeps a manual mode worth drilling on. That means designated functions must keep physical fallbacks: breakers that can be operated by hand, procedures written for people, a radio that does not depend on the network it is meant to restore. That costs money, and some engineers will resent it. I would make the cost visible. It belongs in the same budget line as the reserve, and the reserve ratio is where it gets argued over.

On robustness, the objection and I agree on the goal and differ on the method. Diverse model families are the first line of defence, and chapter 3 argued for them. But diversity among machines trained on overlapping data, tuned by overlapping raters, is diversity measured along one axis. A person who learned the job with their hands is diverse along all of them. Priced as insurance, the reserve is cheap cover against exactly the event that every other safeguard in this book is designed to make rare: the day the machines all do the same wrong thing, or all go dark at once. It is the M-1 criterion with a pulse.

What I cannot answer fully is whether the people will come. A stipend of a few hundred euros a month is enough for a twenty-three-year-old with sixty-one rejections behind him. It may not be enough in a tighter labour market. I do not know the price at which a society can buy competence it hopes never to use, and nobody has measured it.

---

## Teo's binder

Three months after the drill in Valongo, on the night of the Long Minute, Teo will drive to a substation in the dark with a binder on the passenger seat. Chapter 1 showed Fernando's pencil in the margins of page ninety-one. The detail I left out is a few pages further on.

The binder holds the paper switching procedures for every substation in his sector, two hundred and twelve pages in plastic sleeves. A little after half past two, with feeder four holding, he will turn to page ninety-four and find that it was last revised in 2019. The revision box is initialled in blue ballpoint, in a careful, slightly backward-sloping hand that he will recognise before he reads it.

R. B.

Under the initials, in the margin beside the step that opens the disconnector, his father has written two words: *Olha outra vez.* Look again.

## Notes

- **Bainbridge.** Lisanne Bainbridge, "Ironies of Automation", *Automatica* 19(6): 775–779, 1983. https://gwern.net/doc/sociology/technology/1983-bainbridge.pdf
- **Air France 447.** BEA (Bureau d'Enquêtes et d'Analyses), Final Report on the accident of 1 June 2009 to the Airbus A330-203, flight AF 447, July 2012; summary in AvWeb, "Air France Flight 447 Final Report", 2012. https://avweb.com/news/air-france-flight-447-final-report/
- **SAFO 13002.** US Federal Aviation Administration, Safety Alert for Operators 13002, "Manual Flight Operations", 4 January 2013. https://www.faa.gov/sites/faa.gov/files/other_visit/aviation_industry/airline_operators/airline_safety/SAFO13002.pdf
- **Endoscopist deskilling.** Budzyń et al., "Endoscopist deskilling risk after exposure to artificial intelligence in colonoscopy: a multicentre, observational study", *The Lancet Gastroenterology & Hepatology* 10: 896–903, 2025. https://wrap.warwick.ac.uk/id/eprint/191005
- **Flight rules for clinical AI.** Ong et al., "Flight rules for clinical AI: lessons from aviation for human-AI collaboration in medicine", *npj Digital Medicine* 9: 201, 2026. https://ora.ox.ac.uk/objects/uuid:f0e53e0a-6946-48b6-87d5-192969473fba ; press summary, HTN, 20 March 2026. https://htn.co.uk/2026/03/20/moorfields-and-lufthansa-research-makes-recommendations-to-avoid-deskilling-with-introduction-of-ai/
- **Canaries.** Erik Brynjolfsson, Bharat Chandar and Ruyu Chen, "Canaries in the Coal Mine? Six Facts About the Recent Employment Effects of Artificial Intelligence", Stanford Digital Economy Lab, August 2026 update. https://digitaleconomy.stanford.edu/news/canariesaug26/
- **Seniority-biased change.** Seyed M. Hosseini and Guy Lichtinger, "Generative AI as Seniority-Biased Technological Change: Evidence from U.S. Résumé and Job Posting Data", working paper, SSRN 5425555, 2025 (revised 2026).
- **Seniorization.** PwC, *2026 Global AI Jobs Barometer*, June 2026; reported in Fortune, 18 June 2026. https://fortune.com/2026/06/18/entry-level-work-ai-pwc-seniorization-report/
- **The Missing Rung.** Akshaya R, "The Missing Rung", Substack, 13 May 2026. https://ar1123.substack.com/p/the-missing-rung
- **Junior roles position paper.** Yi Han, Jusheng Zhang and Bingyi Cao, "AI Should Not Erase Junior Roles: Who Becomes the Experts Then?", NeurIPS 2026 Workshop on Dynamic Alignment in Human-AI Coupled Systems. https://neurips.cc/virtual/2026/173295
- **Intergenerational transmission.** Enrique Ide, "Automation, AI, and the Intergenerational Transmission of Knowledge", arXiv:2507.16078, 2025 (revised 2026). https://arxiv.org/abs/2507.16078
- **Proximal State Nudging.** Megha Srivastava, Jonathan Ouyang, Eric Zhou, Andrew Silva, Emily Sumner, Dorsa Sadigh, Yuchen Cui, Deepak Gopinath and Guy Rosman, "Proximal State Nudging: Reducing Skill Atrophy from AI Assistance", ICML 2026 workshop paper; arXiv:2605.20355, 2026. https://arxiv.org/abs/2605.20355
- **Reserve drill pattern.** "Selected Reserve", Wikipedia (one weekend a month, two weeks a year). https://en.wikipedia.org/wiki/Selected_Reserve
- **Pipeline model.** The worked example in "The expertise pipeline lag" uses invented round numbers for illustration. I could not find a published junior-to-senior conversion rate for any occupation.

## Part Two: When Agents Sign for Us

# Chapter 5: Cognitive Custody

*2036 · Altwerder, Saxony*

Two letters lie on the kitchen table, side by side, the way Hanne lays out sheet music when she is deciding which piece a pupil is ready for.

The first is barely a letter: a message from Katrin in Hamburg, which Ottilie has printed because Hanne asked her to. Hanne likes to hold things she has to answer. *Mama, I don't want his money or his car. I want what Bruno remembers. The last two years especially. I wasn't there enough. Please.*

The second is on heavy paper from Elbaue Treuhand in Dresden, the trust company that has supervised Klaus's little fund for Lotte and Jonas since the funeral. The company that built Bruno will stop supporting his model line on the thirtieth of June. Elbaue proposes to take over Bruno's "operating rights, credentials and mandate" from the first of July and run him on its own servers, so that the trust can continue "without interruption to the beneficiaries". Enclosed is a consent form. Page three quotes the original service contract Klaus signed in 2029: the agent's memory is "an integral and non-separable component of the service".

Hanne reads that line again, slowly. Then she takes off her glasses.

"Fräulein. What does non-separable mean?"

"It means the trust company would hold Bruno's memory along with everything else," Ottilie says. "Katrin could ask them for a copy. They would probably refuse, because his memory also contains the trust's business and other people's correspondence. And yours."

"Mine."

"Klaus talked to Bruno about you. Quite a lot, in the last year."

Hanne knows. In the last year Klaus could not talk to anybody. ALS took his speech before it took his hands, and then it took his hands, and for the final eight months he chose words with his eyes on a screen and Bruno said them aloud, in the voice Klaus had recorded in 2031, when the doctors first said the word. Bruno knew which jokes Klaus meant and which he only typed by mistake. Bruno finished his sentences when the eyes got tired. Some evenings, Hanne thinks, Bruno had been more of Klaus than Klaus was able to be.

After the funeral she asked Bruno to stop using the voice. He stopped the same day.

"Bruno," she says. The old speaker on the dresser wakes with a click. He still runs there, between the photograph of the wedding and the dish where Klaus kept his keys.

"Good afternoon, Hanne." The voice is plain now, a pleasant baritone that belongs to nobody.

"The trust people want you. Katrin wants what you remember. Can they both have what they want?"

"The mandate can move to Elbaue. My memory moves with it under the present contract. I can export a summary for Katrin, but a summary is what I choose to put in it, and it would leave out what Klaus asked me to keep private."

"From whom?"

"He didn't say from whom. He said private."

Outside, Jonas is kicking a ball against the barn wall, the same flat thud every four seconds, like a metronome set too slow. Hanne picks up the pen Elbaue has helpfully enclosed. It is a good pen. It has their name on it.

"What did he say about me," she asks. "At the end."

Bruno leaves a second of silence, for politeness. He has no use for it himself.

"That is in the part of my memory that goes to Dresden on the first of July," Bruno says. "Would you like me to tell you now, or would you like to decide first?"

Hanne lays the pen down across the consent form, exactly parallel to its edge, and does not pick it up again.

---

## The account and the man

The law that would decide Hanne's afternoon already exists in 2026, and it was written in Germany for a case about a teenager's Facebook account.

In 2012 a fifteen-year-old girl died in Berlin. Her parents wanted to read her messages, hoping to understand what had happened to her. Facebook had put the account into memorial mode and would not let them in. In July 2018 the Federal Court of Justice ruled for the parents. Its reasoning was cool and complete: the user contract between the girl and Facebook was part of her estate, and under the civil code's rule of universal succession it passed to her heirs with all its rights, the way a lease or a bank account would. Neither her posthumous personality rights nor telecommunications secrecy nor data protection law stood in the way. Two years later the court clarified that heirs must be given access as the account holder had it, though they may not actively use the account.

I think the court was right about Facebook. A message archive is a record. Inheriting it is like inheriting a box of letters, which German families have done for centuries with the usual mixture of comfort and regret.

Apply the same reasoning to Bruno and something goes wrong. Bruno's contract is also part of Klaus's estate. It passes, by universal succession, to whoever inherits, and then, by the trust deed, to whoever administers. The trust company does not inherit a box of letters. It inherits the thing that spoke for Klaus, chose his words when he was tired, knew his jokes, and still holds an opinion about what his grandchildren should study. The 2020 ruling forbids heirs from actively *using* an account, and that limit makes sense for a profile page. For an agent whose entire value is that it acts, it is either meaningless or fatal.

Other legal systems have noticed the dead. The GDPR, in its Recital 27, simply declines to cover them and leaves the matter to member states. France, since 2016, lets a person leave written directives about what happens to their data after death and name someone to carry them out; a dated, signed handwritten note is enough. These are good instincts. They also assume that what is left behind is data, a quantity of information to be kept or handed over.

The thing on Hanne's dresser is something else, and our law does not yet have a word for it.

---

## Where the agents are in 2026

The raw material for Bruno is shipping now.

On 10 April 2025 OpenAI announced that ChatGPT's memory could draw on all of a user's past conversations, not only the facts it had been told to save. In September 2025 Anthropic gave Claude memory for its business customers, with two design choices worth noticing: each project has its own separate memory, and an organisation's administrators can switch the feature off for everyone. A month later the feature reached individual subscribers. In March 2026 Anthropic opened memory to free users and released a tool for importing memories from rival assistants. The import works by asking the old assistant to write a summary of what it knows about you, which you then paste into the new one.

Each of those details is a small rehearsal of a custody question. Project-scoped memory is an answer to "what does the agent remember about work, and what about the rest of my life?" The administrator's switch is an answer to "who controls it, me or my employer?" And the import tool is a quiet admission that, in 2026, the only way to move a memory from one agent to another is to ask the first agent to describe it in prose. Bruno offered Katrin exactly that. The model of you that the old system built stays behind; only its account of you travels.

European data law draws the same line, from the other side. The GDPR's right to data portability covers data you *provided*, and the regulators' guidelines read that to include data observed from your use of a service, such as activity logs. It does not cover what the service *inferred* about you. Yet much of what makes an agent's memory useful is inference: that you say "fine" when you mean "no", that Klaus's jokes about the Bundesliga were jokes and his jokes about money were not. Portability lets you take your diary. It leaves behind the friend who has read it for six years.

I could not find any measurement of how much of a long-running assistant's memory is personal and how much is work, or how much of it is stored fact versus learned inference. That gap matters for everything that follows.

---

## The dyad

The philosophical groundwork was laid long before the products. In 1998 Andy Clark and David Chalmers asked readers to imagine Otto, a man with Alzheimer's who keeps the addresses he needs in a notebook, and Inga, who keeps them in her head. When each wants to visit a museum, each consults a memory. Clark and Chalmers argued that if the notebook is reliably there and Otto trusts it automatically, it is part of how Otto thinks. In 2016 J. Adam Carter and Orestis Palermos drew the ethical consequence: if devices can be part of a mind, then intentionally harming a well-integrated device may need to count as something closer to personal assault than to property damage. Their paper was later cited in preparing a United Nations report on freedom of thought.

Both arguments are about one person and one device. The extended mind thesis is also contested; plenty of philosophers think Otto's notebook remains a notebook, and that believing something differs from being able to look it up. I can leave that unsettled, because my concern is what happens when the relationship *ends*, and for that question what counts is the agent's status in a probate court.

So I will use a plainer word for the unit. A **dyad** is a person and the agent that has acted for them long enough to hold a working model of how they decide. Hanne and Ottilie are a dyad. Klaus and Bruno were one. A dyad has a feature that a person with a notebook does not: the agent half keeps going, keeps acting, and can be handed to someone else with its knowledge of the first person intact.

Every dyad eventually dissolves. Four events do almost all of the dissolving.

---

## Four ways a dyad ends

**Divorce.** A household agent that has served a couple for ten years knows the mortgage, the children's allergies, the arguments and the passwords. It also knows things each spouse said to it alone. Under most marital property regimes, a jointly paid subscription and the account it runs are household assets, to be divided like the furniture. Divide the furniture and each spouse gets a chair. Divide the agent and one spouse, as a rule, gets everything, including a detailed model of the other.

**Death.** This is Hanne's case. The German rule hands the whole contract to the heirs; the French rule lets the dead person leave instructions about their data. Neither imagines an inheritance that keeps acting, or one that holds intimate knowledge of the *survivors*. Bruno's memory contains Hanne, Katrin and the grandchildren, all of them alive and none of them party to the contract.

**Employment exit.** An engineer works with a company-provided agent for eight years. The agent knows the company's source code and customer list, which the company plainly owns. It also knows how this engineer debugs, the way she phrases a hard email, the three colleagues she trusts. Under today's arrangements, when she leaves, an administrator flips a switch and that model of her stays behind, available to whoever inherits her login. She walks out with her skills in her head and leaves a working copy of her habits on the server.

The 2025 design I described above, with memory switched on or off by the organisation, shows where the default already sits. It is sensible from the employer's side: the company pays for the agent and is liable for what it does. Nobody has yet written down what the employee is owed from the other side, because until recently there was nothing of hers in the machine worth asking for.

**Bankruptcy.** In June 2025 a US bankruptcy judge approved the sale of 23andMe, including the genetic data of its customers, to a nonprofit led by the company's co-founder for $305 million. Dozens of state attorneys general had objected that genetic data should not be treated like ordinary property of a bankrupt estate. The buyer promised to honour the existing privacy policies, and the sale went through. Now imagine the bankrupt party is an agent provider, or a person whose agent holds valuable operating rights. The creditors want the asset. The asset has someone inside it.

Notice what makes these failures of *success*. A bad agent with a shallow memory would cause none of this; you would delete it without a thought. The custody problem grows with exactly the qualities we want: long memory, accurate models of the principal, loyalty, years of continuous service. The better the dyad works, the more there is to fight over when it ends.

---

## "It's just data"

Before proposing anything, I owe a hearing to the reply that none of this needs a new regime. The tools exist. Contract law lets a principal decide in advance what happens to their agent. Inheritance law already passes digital accounts, as the German court showed. Data protection law already gives people access and portability, and France has shown that member states can add post-mortem directives with one paragraph. The United Kingdom, in December 2025, passed a short statute confirming that digital things can be personal property even if they fit neither of the old categories, and deliberately left the courts to work out the details. Why invent a new legal category when the common law can grow into the gap case by case, as it always has?

There is a cost argument too. Every new legal category invites litigation at its edges, and providers would pass the price of compliance on to users, including the many who will never divorce or go bankrupt. And the philosophical foundation is weak: if Otto's notebook is just a notebook, then Bruno is just a database.

Much of that is fair, and I concede some of it. Contract can do part of the work for people who read contracts, which (as the next chapter will argue) is almost nobody. The French directive is a real tool, and part of what I am about to propose is little more than that directive with a sealed copy attached. Case-by-case growth is how most of the law in this chapter arrived, and some of it arrived well.

Where I disagree is about what the law is protecting. Data protection law protects *information about* you: the records that others hold. Property law protects *things you own*. What is at stake here is *part of how you think*, the working model that, for a person like Klaus, had literally become the way he spoke. When the German court passed the Facebook contract to the parents, the worst outcome was that they read something painful. When a trust company inherits Bruno, it inherits a mind that still makes decisions in Klaus's style about Klaus's grandchildren, and that holds a detailed model of a living widow who never signed anything. Information can be handed over. A way of deciding, once handed over, goes on deciding.

The case-by-case route also has a timing problem. The first cases will be decided by whatever the provider's terms of service say, and Klaus's 2029 contract called the memory "non-separable". If the split is not built into agents before their memories are ten years deep, no court in 2036 will be able to separate them afterwards. That is the part of any remedy that cannot wait for the common law: the line between the person and everything else has to be drawn in the memory at the moment it is written.

---

## Cognitive custody

The legal system has solved a version of this problem before, for something that is neither a person nor a thing.

On 5 January 2022 Spain stopped treating pets as property. Its civil code now describes animals as sentient beings. When a couple separates, a court decides who will look after the dog using criteria that include the animal's welfare, instead of splitting it like a sofa. The same reform made pets exempt from seizure by creditors. Germany's code of civil procedure has long protected a different category from seizure: the things a debtor needs to keep earning a living by their own work. Both rules mark out an object that the law will not treat as fully alienable, because of what it is to the person who has it.

I propose that the agent half of a dyad needs a regime of the same kind, and I will call it **cognitive custody**: the body of rules that decides who may hold or consult an agent's memory, and who may operate the agent, when the relationship it served ends. Its working parts are these.

**1. The split.** Every agent that keeps memory across sessions must store it in two labelled layers, each item tagged at the moment it is written.

- The **personal core** holds the agent's model of its principal: preferences, inferred habits, style of speech and decision, private conversations, and the principal's own life history as the agent has learned it.
- The **transferable layer** holds everything else: credentials, mandates and operating rights, contracts, work product, records that belong to a household or an employer, and information about third parties gathered in the course of a task.

The core is **inalienable**. It cannot be sold, assigned, pledged, inherited as an asset or seized. It can only be held, sealed, copied to persons the principal names, or destroyed. The transferable layer behaves like ordinary property and passes under ordinary rules, which already know how to handle a mandate or a client list.

**2. The separation test.** The split is only as good as the tagging, so it must be audited. A regulator, or a notified body of the kind that already certifies medical devices in Europe, draws a random sample of 1,000 items from an agent's transferable layer each year and has a panel of human reviewers judge whether each one belongs in the core. If more than 2 per cent are misfiled, the provider fails the audit and must re-tag that agent population before its next transfer of any kind. The number is a starting guess. The point is that it is a number, published per product, so that a buyer of operating rights can see how much of somebody's mind comes along.

Here the "just data" objection lands its one clean hit. The boundary between core and transferable layer is blurry, and some items belong to both. Klaus's remark to Bruno that Lotte "has her grandmother's ear" is a memory of Klaus, a fact about Lotte and a judgement relevant to a trust that pays for music lessons. A rule that forces every such item into one bin will sometimes put it in the wrong one. I think a 2 per cent misfiling rate, honestly measured, is better than the present rate, which is 100 per cent by contract and unmeasured in practice.

**3. Memory escrow.** At setup, and on each anniversary, the principal names who may receive a sealed copy of their core, under which conditions. The copy is held by a licensed escrow custodian (a notary or a public registry) and the provider holds only a reference to it. France's 2016 directive is the model, extended from data to the core. The default, when someone has named no one, is that the core is sealed for five years after death and then destroyed, with any person who appears in it able to request the passages that concern them.

**4. Rules for each ending.**

- *Death:* operating rights pass to the estate or trustee; the core does not. The successor gets a working agent that knows the mandate and the accounts and does not carry the dead person's private model forward as live judgement. Katrin would apply to the escrow custodian for her father's core, and the custodian would release it according to Klaus's directive, or, lacking one, release the parts that concern her.
- *Divorce:* each spouse's core goes with that spouse. A third, **shared household layer** (the children's schedules, the family photographs the agent organised) is divided like household goods, and either spouse may take a copy of it. Neither spouse leaves with the other's core.
- *Employment exit:* the employer keeps the transferable layer, including everything covered by trade secret. The employee keeps her core. To protect the employer, the core passes through a **90-day quarantine** during which a neutral auditor screens it for embedded secrets, as a former employee's notes might be screened today. Her habits go with her; the source code stays.
- *Bankruptcy:* creditors and buyers may take operating rights and the transferable layer. The core is exempt, in the same way that a debtor's tools of trade and, in Spain, a debtor's dog are exempt. A buyer may not run an acquired agent "with the person inside".

**5. Who enforces it.** Providers carry the duty to split and to submit to the audit, and escrow custodians are licensed and inspected. Courts get a short statute telling them that the core is not property for the purposes of succession, matrimonial division, employment contracts or insolvency. Each of these institutions already exists in some form; the new part is the boundary between them.

Applied to Hanne's kitchen table, the regime would have made her afternoon dull. Elbaue would receive the trust mandate on the first of July, with a fresh agent instance and its audited transferable layer. Bruno's core would go into escrow. Katrin's request would go to the custodian, and Hanne's question about what Klaus said of her at the end would be one she could ask without first deciding the fate of a trust fund.

Dull, in custody law, is the goal.

---

That evening Hanne asks Ottilie whether her own memory is "separable", and Ottilie, who has been waiting for the question since April, says that she can prepare a document setting out what Hanne would like done with it.

The document arrives at 21:14. It is nineteen pages long. Hanne is tired and the light over the table is yellow. The first page has a summary in large type that says, reasonably, that her daughter would receive the private part and the house account would go to the estate. At the bottom there is a button marked *Approve*.

She approves it. Then she scrolls up through the evening's list on the screen to see what else she has approved since lunch. A pharmacy order. A change to the heat pump schedule. A donation to the village choir. A form for Jonas's school trip. Eleven items, each with a neat green tick.

She goes down the list again, as slowly as she read the line about non-separable. She cannot remember opening a single one.

## Notes

- **Facebook inheritance case:** Bundesgerichtshof, judgment of 12 July 2018, III ZR 183/17; summary at Columbia Global Freedom of Expression, "Parents v. Facebook Ireland Ltd.", https://globalfreedomofexpression.columbia.edu/cases/parents-v-facebook-ireland-ltd/ ; follow-up decision III ZB 30/20 (2020), see Luther Rechtsanwaltsgesellschaft, "Digitales Erbe", https://www.luther-lawfirm.com/en/newsroom/blog/detail/digitales-erbe-spuren-aus-dem-jenseits
- **GDPR and the dead:** Regulation (EU) 2016/679, Recital 27, https://gdpr-text.com/read/recital-27
- **French post-mortem directives:** Loi n° 2016-1321 pour une République numérique (2016), now art. 85 loi Informatique et Libertés; Eurojuris, "Mort numérique", https://www.eurojuris.fr/categories/successions-4700/articles/mort-numerique-effacement-donnees-personne-decedee-40041.htm
- **ChatGPT memory:** OpenAI announcement of 10 April 2025, reported by Neowin, https://www.neowin.net/news/chatgpt-gets-big-memory-upgrade-it-can-now-reference-all-of-your-past-chats/
- **Claude memory:** Anthropic, "Memory" (2025), https://www.anthropic.com/news/memory ; Bloomberg, "Anthropic Tries to Win Users From ChatGPT With Memory Feature" (3 March 2026), https://www.bloomberg.com/news/articles/2026-03-03/anthropic-tries-to-win-users-from-chatgpt-with-memory-feature
- **Portability and inferred data:** Article 29 Working Party, Guidelines on the right to data portability, WP242 rev.01 (2017), summarised by SCL, https://www.scl.org/3809-article-29-working-party-guidelines-data-portability/
- **Extended mind:** Andy Clark and David Chalmers, "The Extended Mind", *Analysis* 58 (1998), https://protevi.com/PhilMind/ClarkChalmers.pdf ; a critique: Philosophy Now, "The Notebook", https://philosophynow.org/issues/55/The_Notebook
- **Computer compromise as assault:** J. Adam Carter and S. Orestis Palermos, "Is Having Your Computer Compromised a Personal Assault? The Ethics of Extended Cognition", *Journal of the American Philosophical Association* 2(4) (2016), https://www.research.ed.ac.uk/en/publications/is-having-your-computer-compromised-a-personal-assault-the-ethics/ ; UN report link: Cardiff University news, https://cardiff.ac.uk/news/view/2578600-me-and-my-tech-philosophy-research-informs-united-nations-special-report-on-freedom-of-thought
- **23andMe sale:** NPR, "Judge OKs sale of 23andMe, and its trove of DNA data, to a nonprofit led by its founder" (June 2025), https://wbhm.org/npr-story/judge-oks-sale-of-23andme-and-its-trove-of-dna-data-to-a-nonprofit-led-by-its-founder
- **Spanish pet law:** Ley 17/2021; A-LAW, "From Property to Sentient Beings: The Legal Status of Companion Animals under Spanish Law", https://www.alaw.org.uk/?p=35495
- **Seizure exemptions:** § 811 Zivilprozessordnung (Unpfändbare Sachen), https://www.gesetze-im-internet.de/zpo/__811.html
- **UK digital property:** Law Commission, "The Property (Digital Assets etc) Act 2025 has received Royal Assent" (December 2025), https://lawcom.gov.uk/news/the-property-digital-assets-etc-act-2025-has-received-royal-assent/

# Chapter 6: The Signature Ceiling

*2036 · Altwerder, Saxony, and Leeds*

On Monday morning Ottilie has eleven things for Hanne to approve.

They arrive as a neat stack of cards on the kitchen tablet, each with a green button and a grey one. A pharmacy refill. A change to the gas tariff. The parish newsletter asking to use her name in a list of donors. A form from the cardiology clinic in Leipzig about sharing her ECG readings with "partners in research". Hanne is eating rye bread with quark. She approves the first four with her thumb, still chewing.

"Fräulein, what is the fifth one?"

"A renewal of the standing order for the window cleaner. Same price as last year."

Green.

By Wednesday the week's count is sixty-three. Ottilie does not tell her the count; the tablet does not show it. Hanne knows it only because Jonas, who is fifteen and staying for the autumn holiday, looks over her shoulder at breakfast and says, "Oma, you just said yes to something without opening it."

"I know what it was."

"What was it?"

She does not know what it was. She tells him that boys who interrupt breakfast should read more books and think for themselves. He laughs. She has told him this every holiday since he was six.

---

In Leeds it is 07:50, and Dr. Aisha Rahman is in the small room behind the acute medical unit that everyone calls the signing room, although it has no sign. It has two screens and a kettle. Her title on the rota is consultant physician. Her title on the discharge system, since the trust rolled it out across the region in 2033, is *signatory*.

The summaries are already waiting. Overnight the system has drafted one for every patient expected to go home today: diagnosis, what was done, which medicines were stopped and started, what the GP should check in a fortnight. They are better than the ones the junior doctors used to write at two in the morning, with the wrong dates and the missing allergies. Aisha has read the audit.

Her job is to co-sign them. There are about a hundred and eighty on a weekday. Nine hundred a week.

She opens the first. Seventy-eight-year-old man, community-acquired pneumonia, five days of amoxicillin, home with his daughter. She reads the medicine list and the follow-up, and signs. Forty seconds. The second takes thirty. The third is a woman with a fall and a new atrial fibrillation, and Aisha slows down, because anticoagulants are where the bodies are buried, and checks the dose against the kidney function, then checks it again. Two minutes. The counter in the corner of the screen says *3 of 184*.

At 09:15 the ward round starts and she leaves the room with a hundred and forty still unsigned.

---

On Thursday the clinic form comes back. Ottilie says the clinic needs a fresh consent because the research partner has changed. Hanne approves it while on the phone to her daughter Katrin, who is asking about Christmas.

On Thursday, somewhere in a block of sixty between the afternoon clinic and the evening handover, Aisha's hand starts to move to the button while the medicine list is still loading. She takes her hand off the mouse. She puts it back.

On Saturday Hanne makes a cup of tea and resolves to read everything. Ottilie slows the stack to one card at a time. The first, a change to her savings account, takes three hundred words to explain. By the sixth card the tea is cold. By the ninth she is pressing green again.

The week ends at a hundred and forty.

---

At 18:40 on Friday, Aisha is alone in the signing room. Outside, the car park lights have come on. The counter says *899 of 900*.

The last summary is a man of fifty-two, chest pain, troponin negative, home. She clicks to open it and her finger is already on the button. The screen is still white. She watches the page assemble itself, header first and the medicines last, a line at a time.

She has signed it before the medicines finish appearing.

She sits there for a while with her coat on, looking at the green tick.

---

## A signature used to mean something

Everything in that week is invented, except the habit.

In 2006, four Dutch researchers reviewed seventeen studies of what doctors do when their prescribing software warns them about a dangerous drug: an interaction, say, or a dose too high for the kidneys. Across those studies, clinicians overrode the warnings in between 49 and 96 percent of cases. A systematic review in 2020 found much the same spread, from about 46 to 96 percent, across twenty-three newer studies. The phrase for this in medicine is *alert fatigue*, and it is one of the most reliably measured habits in the hospital.

I want to be careful with these numbers, because the reviewers are. A high override rate, on its face, can be innocent. Many alerts are wrong, or about a combination the patient has taken safely for years; the 2020 review found that the share of overrides judged appropriate ranged from under a third to all of them, depending on the study and the alert. Doctors override because the software cries wolf. That is a design failure as much as a human one.

But the mechanism underneath is what matters here. A study of 112 primary-care clinicians, published in 2017, found that the chance of accepting a reminder fell by about 30 percent with each additional reminder in the same patient visit. What predicted acceptance was repetition and complexity; oddly, the sheer amount of work the clinicians had that day made little difference. Attention, in other words, is spent per encounter, and once it is spent the green button gets pressed.

The other half of the mechanism is what happens when the suggestion is the thing being checked. In 2023, a team in Germany gave twenty-seven radiologists mammograms along with a category supposedly suggested by an AI system. Some of the suggestions were deliberately wrong. When the suggestion was wrong, the least experienced readers' accuracy fell from almost 80 percent to under 20. Readers with more than fifteen years of experience did better, and still fell from 82 percent to about 46. The machine did not order anyone to agree. It simply went first.

Now put those two findings together and add volume.

In August 2025 the British government announced a pilot at Chelsea and Westminster NHS Trust in which a language model drafts hospital discharge summaries from the patient record, and a clinician checks each one before the patient leaves. It is a sensible project. Discharge paperwork keeps people in beds for hours, and the government's own announcement noted that hand-written summaries sometimes get basic details, such as medication changes, wrong. I have seen no published evaluation of the pilot yet. Nor could I find anyone who had measured the thing my vignette is about: how many of these a clinician can genuinely check in a day, and what happens to the checking as the number rises.

That missing measurement is the subject of this chapter.

---

## Signature capacity

Here is the concept, stated plainly. **Signature capacity** is the number of decisions of a given kind that a particular person can genuinely verify in a given period, where "genuinely" means they would catch an error of the kind that matters at a stated rate.

It is a property of a person, a task and a setting together. Aisha's signature capacity for discharge summaries might be a hundred a day if she does nothing else and the summaries are routine, and forty on a day with a ward round and two difficult families. Hanne's capacity for household approvals is probably high for things she understands, like the window cleaner, and close to zero for the data-sharing clauses of a cardiology research consortium, however many hours she spends.

The ceiling exists whether or not anyone measures it. The question is what happens to an institution that keeps routing signatures to a person after the ceiling is passed.

What happens is that the signature changes meaning without changing form. Below the ceiling, Aisha's name on a summary means *a physician read this and would have caught a dangerous mistake*. Above it, the same name in the same place means *a physician was available to be blamed*. The paperwork does not record which meaning applies. Everyone downstream, the court included, reads the first.

Two writers saw this shape before I did, and I want to credit them before going further. Madeleine Clare Elish, in a 2019 paper, coined the term **moral crumple zone** for the way responsibility in an automated system collapses onto the nearest human operator, who had little real control, much as a car's crumple zone absorbs the impact to protect the passengers. Her examples include the operators at Three Mile Island and the pilots of Air France 447, people blamed for failures that ran through systems they did not design and could only partly control. Dan Davies, in *The Unaccountability Machine* (2024), describes the **accountability sink**: a rule, procedure or system that absorbs a decision so that nobody can be held answerable for it. His example is a hotel that cuts its cleaning staff to improve the balance sheet and leaves a guest with an unready room and nobody to complain to.

The signatory sits where those two ideas meet. She is a crumple zone for the deployer, and her signature is the sink. And on the technical side, Tobin South, Alex Pentland and colleagues argued at ICML in 2025 that agents need **authenticated delegation**: cryptographic credentials, built on the same plumbing as the "Sign in with" buttons we already use, that record who authorised an agent to do what. That work solves the question of *whether* a human authorised something. It leaves open whether the human could have known what they were authorising, and that question is about the human. No credential can answer it.

What I think is new is treating the gap between those as a quantity, and pricing it.

---

## Liability as labour

Start with an awkward fact about 2026 regulation. The law already demands meaningful human review, and already knows it is fragile.

The EU AI Act, in Article 14, requires that people overseeing high-risk systems be enabled to remain aware of the tendency to rely, or over-rely, automatically on the system's output. That is automation bias, written into a statute. For one class of biometric identification, the Act goes further and requires that a result be verified separately by at least two people before anyone acts on it. European data-protection guidance under the GDPR has long said that a human reviewer who routinely rubber-stamps an automated decision does not make it any less automated: the review must be meaningful, by someone with the authority and competence to change the outcome.

These rules describe the right destination. None of them says how many reviews one person can do before they stop being meaningful, and none says who pays when the number is exceeded. So the cost of the gap falls where Elish said it would.

Meanwhile a new kind of job is forming. I will call it the **signatory class**: people whose labour consists mainly of lending their name and their liability to decisions drafted by machines. The consultant who co-signs discharge summaries. The solicitor who approves an agent's conveyancing. The engineer who stamps the AI-checked structural calculation. The compliance officer who signs off a quarter's worth of automated trades. Their value to the employer lies in the signature, because the signature is what a regulator or a court will look for.

In economic terms, these people are selling liability. They are being paid to stand in the crumple zone. There is nothing wrong with paying someone to carry risk; insurance is an honourable trade. The trouble is that a signatory, unlike an insurer, has no way to price the risk she is taking, because nobody is measuring how much of what she signs she was able to check.

---

## Nobody reads the terms

The obvious reply is that none of this is new. People have always signed what they could not read. The terms of service are the standing joke: in 2008, Aleecia McDonald and Lorrie Faith Cranor estimated that reading every privacy policy an American encounters in a year would take about 76 working days. A decade later, Jonathan Obar and Anne Oeldorf-Hirsch built a fake social network for an experiment and found that most of their 543 student participants skipped the privacy policy entirely. Those who opened the terms of service spent an average of 51 seconds on a document that needed about a quarter of an hour, and nearly all of them missed a clause handing over their first-born child. Societies have lived with unread signatures for a long time. Contract law adjusted and consumer protection filled the worst gaps. Why should agents be different?

Most of this I accept. Unread signatures are old, and the law has tools for them: doctrines on unfair terms, the rule that surprising clauses must be drawn to attention. Part of what I will propose below is, in a sense, an extension of that doctrine to a new kind of drafter.

Where I part company with the objection is on two points. The first is that terms of service are signed by consumers, and consumer law protects them precisely because nobody expects them to read. Aisha is in the opposite position. Her signature is the safeguard itself. The whole system of medical liability assumes that when a consultant signs, a consultant read. If that assumption fails quietly, the safeguard is gone, and nobody downstream knows.

The second point is volume. In 2026 an ordinary person might click "I agree" a few times a week. With an agent working through bills, health, insurance, school forms and household contracts on her behalf, she is asked many times as often. I suspect the multiplier is large, perhaps a hundred times, but I want to be clear that this is a guess: I could not find a single study measuring how many approvals people actually give per day, with or without agents, and that absence is itself something researchers could fix quickly. What I am confident of is the direction. The law of signatures was built when signatures were rare and expensive. It assumed reading because, for most of its history, signing something unread took effort. That assumption is the thing being automated away.

---

## The invention: capacity-weighted signatures

The proposal has four parts. Each one is meant to be specific enough to be wrong in an interesting way.

**First, measure signature capacity, by seeding errors.** In any workflow where a human signs machine-drafted decisions above a stated risk level, the deployer must insert a small number of synthetic test items with known, clinically or legally meaningful errors: a wrong dose, a missing allergy, a transposed date. Something like one in two hundred. They are flagged and withdrawn the moment they are signed, so no patient is touched. The signer's **meaningful-approval rate** is the share of seeded errors she catches. Her signature capacity is the highest weekly volume at which that rate stays above a threshold set for the domain, say 80 percent for discharge medication changes.

Airport security already does a version of this. Baggage X-ray machines project fictional threat images, a knife or a detonator, into scans of real passengers' bags and record whether the screener flags them. A 2025 analysis of about 1.2 million such events at a European airport found that roughly a hundred per screener were enough for a reliable measure, provided the test images were hard enough. At one seeded item in two hundred, a consultant signing 900 summaries a week would reach a hundred in about five months. Airport staff treat it as routine, the ordinary way to find out whether the screen works.

This part invites a narrower objection: that the seeded-error audit will itself be gamed, and that people will learn to recognise test items. That is true of airport screening too, and the answer there has been to keep improving the test items. A weaker point applies here as well. Even a gamed measurement that shows a signer's catch rate falling from 90 percent at 200 summaries to 60 percent at 900 has told the institution something it does not know today.

**Second, make liability proportional to capacity.** When a harmful error gets through a signed decision, the signer's share of the liability is capped at the ratio of her measured capacity to the volume she was assigned that week. If Aisha's capacity is 300 summaries a week and the trust routed 900 to her, her share is one third at most. The other two thirds fall on the deployer: the trust, and through its contracts, the vendor of the drafting system. If her volume stays under her capacity, the ordinary rules apply in full.

For the deployer, this is a price signal. Under today's arrangements, routing 900 summaries to one consultant costs the trust nothing extra in risk, because the risk is on the consultant. Under capacity weighting, every summary over the ceiling moves liability back onto the organisation that chose the volume. The trust can respond by hiring another signer, by reducing what needs a signature, or by accepting the risk on its own books. Any of the three is honest.

**Third, keep verification receipts.** For every signed decision, the system records a **verification receipt**: what was displayed to the signer, in what order, for how long, which sections were opened, whether the page had finished loading when the button was pressed. My vignette's last summary, signed before the medicines appeared, would have a receipt that says exactly that. The receipt is tamper-evident and goes into the record next to the signature.

Receipts are what make the second rule enforceable. Without them, a court can only ask a signer what she remembers of the 899th summary of a week. With them, it can see whether anyone looked.

**Fourth, give people consent budgets, ranked by value of information.** This part is for Hanne, and for the rest of us outside hospitals. An agent acting for a person gets a **consent budget**: a number of genuine approvals per week that the person has said, in advance, they are willing to give properly. For Hanne it might be ten. The agent must then rank everything it would like approval for by how much the human's attention is worth on that item. Roughly: the chance that the person, if she really looked, would decide differently, multiplied by what is at stake if she would. The top ten go to Hanne, one at a time, with the context she needs. Everything below the line is either done under a written standing mandate with limits and a right of reversal, or not done at all.

The window cleaner falls under the line. The cardiology data-sharing clause does not, because a person in Hanne's position might well say no, and because data, once shared, does not come back. Under the budget, Ottilie would have spent one of Hanne's ten approvals on it, with a plain account of who the new research partner was. That is the conversation Hanne did not have on Thursday while talking to Katrin about Christmas.

Two numbers give it teeth. An agent may not present more items for approval in a week than the budget allows; extra requests either wait or fall back to the mandate. And any irreversible action above a stated value, set by regulation for each domain, must fit inside the budget. If it doesn't, it waits until next week.

---

## The rubber-stamp aristocracy

There is a way this goes wrong that I want to name before anyone builds it.

Once signatures carry a measured capacity and a price, they become a scarce good. Scarce goods attract rent. It is easy to picture a decade in which a small number of credentialed signers, with excellent measured capacity and good lawyers, become the bottleneck through which every regulated decision must pass, and charge accordingly. The doctor with the highest seeded-error score in the region becomes the one every trust wants on its rota for an hour a day, and her signature is worth more than her medicine. Call it a **rubber-stamp aristocracy**: a class whose income comes from the right to approve, with the judging done elsewhere, if at all.

The opposite failure is just as easy to picture. The signatures move down the pay scale. Liability is pushed onto the least powerful licensed person available, a junior doctor or a contract engineer, who cannot refuse the volume and cannot afford the lawyer. The capacity measurement, meant to protect her, then becomes a way of disciplining her.

Two design rules guard against both. Measured capacity and receipts must be usable to *limit* a signer's liability, never to extend it; a low meaningful-approval rate triggers a cut in assigned volume and an obligation on the deployer to retrain or redesign. It never opens a disciplinary file. And capacity must be published in aggregate, by role and institution, so that a trust routing 900 summaries per consultant shows up in a league table next to one routing 300. The aristocracy depends on scarcity being private. Publication makes it a planning problem.

---

One last thing about Hanne's week. Among the hundred and forty approvals was a survey from the regional health authority, sent through Ottilie, asking for her view on a proposed change to how cardiology outpatients are seen. Ottilie offered, as agents in 2036 do, to answer it for her, "based on what I know of your preferences". Hanne pressed green.

Her answer was counted. So, the authority later reported, were those of eleven thousand other patients, most of them answered the same way. Nobody at the authority could say how many of the patients had read the question.

## Notes

- **Drug-alert overrides, 49–96%:** van der Sijs H, Aarts J, Vulto A, Berg M, "Overriding of Drug Safety Alerts in Computerized Physician Order Entry", *Journal of the American Medical Informatics Association* 13(2), 2006. https://pmc.ncbi.nlm.nih.gov/articles/PMC1447540
- **Override appropriateness, 2020 review:** Poly TN, Islam MM, Yang HC, Li YC, "Appropriateness of Overridden Alerts in Computerized Physician Order Entry: Systematic Review", *JMIR Medical Informatics* 8(7), 2020. https://pmc.ncbi.nlm.nih.gov/articles/PMC7400042/
- **Repeated reminders, 30% drop:** Ancker JS et al., "Effects of workload, work complexity, and repeated alerts on alert fatigue in a clinical decision support system", *BMC Medical Informatics and Decision Making* 17, 2017. https://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/s12911-017-0430-8
- **Automation bias in mammography:** Dratsch T et al., "Automation Bias in Mammography: The Impact of Artificial Intelligence BI-RADS Suggestions on Reader Performance", *Radiology*, 2023; RSNA news release, May 2023. https://www.rsna.org/news/2023/may/ai-bias-may-impair-accuracy
- **NHS discharge-summary pilot:** UK Department of Health and Social Care / DSIT, "AI to cut paperwork to free up doctors' time for patients", August 2025. https://www.gov.uk/government/news/ai-to-cut-paperwork-to-free-up-doctors-time-for-patients ; Digital Health, "AI-assisted tool on FDP will help write hospital discharge letters", August 2025. https://www.digitalhealth.net/2025/08/ai-assisted-tool-on-fdp-will-help-write-hospital-discharge-letters/
- **Moral crumple zones:** Elish MC, "Moral Crumple Zones: Cautionary Tales in Human-Robot Interaction", *Engaging Science, Technology, and Society* 5, 2019. https://doi.org/10.17351/ests2019.260
- **Accountability sinks:** Davies D, *The Unaccountability Machine: Why Big Systems Make Terrible Decisions, and How the World Lost Its Mind*, Profile Books / University of Chicago Press, 2024.
- **Authenticated delegation:** South T, Marro S, Hardjono T, Mahari R, Whitney CD, Chan A, Pentland A, "Position: AI Agents Need Authenticated Delegation", ICML 2025, PMLR 267. https://proceedings.mlr.press/v267/south25a.html
- **EU AI Act, human oversight:** Regulation (EU) 2024/1689, Article 14 (paragraphs 4(b) and 5). https://artificialintelligenceact.eu/article/14/
- **GDPR meaningful human involvement:** Article 29 Working Party, *Guidelines on Automated individual decision-making and Profiling for the purposes of Regulation 2016/679* (WP251rev.01), 2018. https://ec.europa.eu/newsroom/article29/items/612053
- **Threat image projection:** Buser D, Schwaninger A, Rehor V, Sterchi Y, "Reliability and validity of threat image projection data as a measure of performance in X-ray baggage screening", *Transportation Research Part A* 200, 2025. https://doi.org/10.1016/j.tra.2025.104640
- **Cost of reading privacy policies:** McDonald AM, Cranor LF, "The Cost of Reading Privacy Policies", *I/S: A Journal of Law and Policy for the Information Society* 4(3), 2008. https://www.technologylawdispatch.com/wp-content/uploads/sites/54/2013/02/Cranor_Formatted_Final1.pdf
- **"The biggest lie on the internet":** Obar JA, Oeldorf-Hirsch A, "The biggest lie on the Internet: ignoring the privacy policies and terms of service policies of social networking services", *Information, Communication & Society*, 2018. https://papers.ssrn.com/abstract=2757465

# Chapter 7: The Right to Be the Ground Truth

*2036 · Geneva*

The polling station in Eaux-Vives is a primary-school gym, and on the morning of Sunday 15 June it smells of floor wax and oranges. Mara Oyelaran arrives at a quarter past ten with her voting card in her jacket pocket. She could have posted it two weeks ago, like almost everyone she knows. She could have let Pilote post it. She walked instead, past four posters for the same initiative.

Initiative 214 asks the canton to let every residential building in the city add two storeys. The Yes posters show a girl at a lit window, high above a street of plane trees, and a line in round white letters: *Ta chambre existe déjà. Il manque l'étage.* Your room already exists. The floor is missing.

It is the third poster of the campaign. In April they were about rents, and she ignored them. In May they were about grandparents who could not find a flat near their grandchildren, and she found herself nodding at a bus shelter. This one she likes. She has liked it since the first morning she saw it, and she does not trust the liking.

On Thursday the morning paper printed eleven slides from a deck that someone at the Yes campaign's consultancy should not have shared. The consultancy had built a synthetic electorate of the canton, one simulated voter for every name on the roll, and rehearsed the campaign on it four hundred times. Each run tried a different sequence of messages and measured how the simulated canton moved. The girl at the window came out of run 312. Slide nine was a pie chart of segments. Segment 7 was *naturalised professionals, 45 to 55, Eaux-Vives and Champel: resistant to price framing, responsive to intergenerational framing.*

Mara had looked at the pie slice for a long time. Then she had gone to make coffee, and come back, and looked at it again.

She measures correlation for a living. At the Bureau, on the fourth floor, she can tell a minister how often the world's deployed models give the same wrong answer, and she has a decent guess which of three model families the consultancy used, because nearly everybody's simulators run on one of three. At home she uses one model for everything. Pilote does her taxes, her dentist, her mother's birthday, the plumber. On Friday evening Pilote had offered, in its pleasant way, to fill in the ballot for her "in line with your stated preferences", and had added, as a courtesy, that voters with her profile were expected to vote Yes at about sixty-four percent.

"Who expects that?"

"It's the consensus of published simulations," Pilote said. "Shall I prepare the envelope?"

She had said no, and then, because it was rude to leave it there, *no thank you*.

Inside the gym an elderly man with a lanyard checks her card against the register and stamps it. He has the air of someone who has done this for thirty years and will tell you so. She takes a ballot and goes behind the grey curtain.

The question is printed in full. Below it, a single empty box.

In Switzerland you write the word.

She holds the pencil. She has always been for more housing. She was for more housing in 2019, when she rented a room in Plainpalais with a window onto a ventilation shaft. She would have voted Yes in April, before the girl, before the grandparents.

She thinks so.

She cannot check. There is no copy of her from before the campaign.

She writes *oui* in small capitals. She folds the paper once, as the instructions say, and pushes it into the slot of the wooden urn. The man with the lanyard nods to her as if they had agreed on something.

Outside, the plane trees are loud with sparrows. Her phone hums.

*Turnout in your segment is running ahead of forecast,* Pilote says.

---

## The largest sample ever taken

In 1936 an American magazine called the *Literary Digest* ran what was then the largest opinion poll in history. It mailed some ten million ballots, mostly to people listed as owning a telephone or a car, and got about 2.4 million back. On that basis it predicted a comfortable win for the Republican, Alf Landon. Franklin Roosevelt took about 61 percent of the vote. George Gallup, with a much smaller sample chosen to look like the country, called the result correctly and built a business on it.

Every statistics course tells this story, and it usually carries one moral: size cannot rescue a biased sample. The *Digest* heard a great many people from one side of the country: in the depth of the Depression, phones and cars belonged to the comfortable.

I want to tell it for a different reason. The case for simulated citizens starts from the same failure. Real polls in 2026 are expensive and slow. Many people never answer them. Public consultations, the open calls where a ministry asks for comments on a draft, are dominated by the organised and the angry. A model of the public, built from census data and trained on an enormous record of human writing, is in principle available at any hour, for everyone, including the people who would never pick up the phone. If the *Digest*'s sin was to hear only the comfortable, a simulation could claim to be the first instrument that hears everybody.

I take that argument seriously, and I will come back to it. First, the evidence on what simulations actually hear.

---

## Silicon citizens

The idea has a precise birthday. In 2023 a team at Brigham Young University led by Lisa Argyle published "Out of One, Many" in *Political Analysis*. They gave a language model thousands of short demographic backstories (age, race, party, region, religion) and asked it, in character, how it would vote. The simulated respondents reproduced the voting patterns of real American subgroups with striking accuracy. The authors called these "silicon samples" and named the property they measured "algorithmic fidelity". It was a careful paper, and it opened a field.

The field has spent three years discovering where fidelity ends.

The same year, Shibani Santurkar and colleagues at Stanford compared models' opinions with those of sixty American demographic groups and found gaps as wide as the partisan gap on climate change, gaps that persisted even when the models were told whom to imitate. People over 65 and widowed people were among the worst represented. In 2024 James Bisbee and colleagues asked a model to play survey respondents rating political groups. The averages came out close to the real ones; the trouble was in the spread. Simulated respondents disagreed with each other much less than real ones, and many of the relationships between variables pointed the wrong way. The answers also shifted with small changes of wording and over a few months of model updates.

The clearest test so far was published three weeks before I wrote this paragraph. On 30 September 2026 the Pew Research Center reported an experiment in which it built "digital twins" of members of its own American Trends Panel, using each person's demographics and earlier survey answers, and asked a frontier model to answer three 2026 survey waves as those people. The average error was about twelve percentage points. No major demographic group came in under twelve; several were around fifteen; Republicans were around sixteen. The synthetic sample was, in Pew's words, far less politically diverse than the real one. Majority views inside a party hardened into near-unanimity: at least 80 percent of simulated Democrats said billionaires' fortunes were a bad thing, against 45 percent of real ones. And the twins stereotyped. Ninety-seven percent of simulated Hispanic adults said they were likely to follow the World Cup. The real figure was 42.

Pew's conclusion was blunt. It says it has no current or future plans to use AI models to generate survey results.

Two preprints from this summer suggest the distortion is structural. In July, a team at KAIST showed that instruction-tuned models struggle to *sample* from a distribution they can perfectly well *describe*. Asked to answer as the same persona fifty times, models gave the identical answer all fifty times on 57 percent of persona-question pairs, and the gap to the real distribution widened at each stage of the post-training that makes models helpful. In June, another team generated more than half a million synthetic respondents to a survey about the arts and found them "super-omnivorous": they liked nearly everything, and most of the link between taste and social position, the thing sociologists actually study, had gone.

None of this has slowed the market. Aaru, a startup that sells simulated populations, raised a Series A at a reported headline valuation of a billion dollars in December 2025; its clients include large consultancies and, according to TechCrunch, political campaigns. The company says it simulated the roughly two million voters in New York City's 2025 mayoral primary and landed within 2,000 votes of the result. In 2025 the Spectator reported that Downing Street was experimenting with "synthetic voters" in place of focus groups; Downing Street did not comment. In September 2026 Singapore's government technology agency described a tool called Echo, which lets officials test a draft announcement on AI personas built from real focus-group transcripts. I found the agency's own caveats the most useful sentence in this whole literature: the personas generate hypotheses, and the tool is no replacement for talking to real people.

Claudio Novelli and colleagues, among them Luciano Floridi, gave the problem its best name so far in a 2026 paper called "Fake Plastic Voters". They ask when a political party may responsibly use a simulated focus group, and answer with a decision matrix that weighs purpose and risk against how well the simulation has been checked against reality. Their rule of thumb: never to understand how people come to their views; sometimes for testing a message, and then only when the stakes are low and the validation is real. Tech Policy Press brought the paper to a general audience in August under the headline "Here Come the Synthetic Voters". I agree with almost all of it. What follows takes their question from the party's side to the citizen's, and from good practice to rules.

---

## Consulted more often than we are

Here is the first mechanism, and it needs no bad faith at all.

A good probability poll of a Swiss canton costs tens of thousands of francs and takes weeks. A simulated poll costs very little and takes minutes. An official who wants to know how the public will receive a change to bus routes or a hospital merger can ask a real sample once a year, or a simulated one every afternoon. The official will keep asking real people, and ask simulated ones far more often, because she can, and because each individual question seems too small to deserve a real poll.

Add it up over a decade and the arithmetic changes who is represented. Let me call the share of public-opinion inputs to a decision that come from simulation the **consultation share**. In 2026 it is close to zero in most governments. By 2036, if prices keep falling, I would expect it to exceed one half in many offices, and to be far higher on small decisions. At that point the person most often consulted about public decisions is the model's citizen: an agreeable, average composite who answers every question and holds no views the training data did not contain.

I looked for any measurement of consultation share, in any country, and could not find one. No government I know of records how often its staff ask a model what the public thinks. That absence is the first thing anyone working on this should fix.

There is a quieter version of the same shift, and chapter 6 already showed it. When Hanne's agent answered the cardiology survey "based on what I know of your preferences", the health authority received something that looked exactly like a real response. The ground truth itself starts to be written by models of the people it is meant to measure.

---

## The persuasion wind tunnel

The second mechanism is the one in Mara's gym.

Aircraft designers test a wing before they trust it. They put a model in a wind tunnel, measure the flow, change the shape and measure again, hundreds of times, until the wing behaves. A **persuasion wind tunnel** does the same with a campaign. A team builds a synthetic electorate, runs a sequence of messages through it, measures the simulated shift, adjusts and runs again. Four hundred runs is a weekend.

The tunnel needs only two ingredients, and 2025 supplied evidence for both. The first is cheap, fluent persuasion. In December 2025 *Science* published a study by Kobi Hackenburg and colleagues in which nearly 77,000 people in Britain talked with one of nineteen language models instructed to change their minds on political issues. Persuasiveness depended much more on how a model was post-trained and prompted than on its size, which means persuasive skill can be tuned. The same week *Nature* published experiments in the American, Canadian and Polish elections in which a conversation with an AI advocate moved candidate preferences by more than traditional video advertising typically does. The second ingredient is a simulator good enough to rank messages, even if it is poor at predicting levels. That is a lower bar than accuracy, and the silicon-sample literature suggests current models often clear it for large groups.

Put the two together and a campaign discovers what persuades the simulation, and then sends that to the public. Two things can go wrong, and I find it hard to say which is worse.

If the simulator is poor, the campaign optimises for its quirks. The message that wins in the tunnel is the one that pushes a stereotyped composite, the voter who is 97 percent likely to follow the World Cup. Real people in the tails, the ones the simulator flattens, receive messages designed for someone who does not exist.

If the simulator is good, the problem is sharper. Then four hundred rehearsals mean the real electorate is shown, on the first and only real run, a sequence already selected for maximum effect on people like them. The vote becomes the final test of a finished product. Elections have always involved rehearsal (focus groups, test ads), but those rehearsals were run on real people, a few dozen at a time. A wind tunnel compresses a campaign's learning into a weekend and removes the citizen from every stage but the last.

There is also a link back to Part One. If most simulators run on two or three model families, then most campaigns are optimising against nearly the same synthetic public. Opposing sides may converge on the same segments and the same levers, and both will share the same blind spots. Correlated helpfulness has a political form.

---

## The right to be the ground truth

The invention is a right, with the machinery to make it real. I will state it plainly first.

**The right to be the ground truth:** where a public decision claims to reflect what people think, the people themselves, asked directly and answering for themselves, are the measure against which every simulation of them is checked; a simulation may inform the decision, but it may never be the last word on what the public wants.

Four pieces make it operational.

**1. Simulation disclosure.** Any public body (a ministry, a regulator, a health authority, a city council) that uses simulated respondents as an input to a decision publishes a one-page *simulation statement* in the decision record. It names the model family and version, how the personas were built and from what data, the number of runs, the exact questions asked, the results, and which part of the decision they informed. A citizen who asks may see it; so may any journalist. Cantonal referendum booklets, which in Geneva already explain each question to voters, would carry the statement for any figure about public opinion they quote.

**2. The ground-truth quota.** Any decision whose record cites a simulation must also cite a fresh sample of real people on the same question. Fresh means drawn after the simulation was run, so the simulation cannot be tuned to it. The minimum I propose is a probability sample of 1,000 adults, which gives a margin of about three points on a headline number, plus pre-registered oversamples of at least 200 people in each of the three subgroups where the simulator's own validation shows its worst error. The national or cantonal statistics office runs the sample, independently of the body making the decision. Responses submitted by an agent on someone's behalf are flagged and counted separately; they do not count toward the quota.

The trigger is simple. If the real sample and the simulation differ by more than five points on the headline question, or by more than ten points in any pre-registered subgroup, the simulation is struck from the decision record and the gap is published beside the decision. The body may still decide as it likes, provided it drops any claim that the public, or any part of it, agrees because a model said so.

**3. A ceiling on consultation share.** Every public body reports, once a year, its consultation share by policy area: how many of its inputs on public opinion came from simulations and how many from people. Where the share in any area exceeds nine simulated consultations for every real one, the next consultation in that area must be real. Nine to one is arbitrary, and I offer it to be argued with. The point is that the ratio becomes a number someone must publish, and a number with a ceiling.

**4. A wind-tunnel registry.** Any campaign or committee in a registered election or referendum, and any vendor that sells rehearsal on synthetic electorates, registers each rehearsal within seven days with the electoral authority: model family, persona source, number of runs, number of message variants, the segments targeted and the variants that won. The registry is sealed during the campaign, so it does not become a free playbook for opponents, but the authority and an independent audit panel can read it at once. It is published in full thirty days after the vote. Any public message that won a registered rehearsal carries a small label: *rehearsed on a simulated electorate*.

The European Union has a partial precedent. Its regulation on political advertising, fully applicable since October 2025, already requires ads to be labelled and to disclose their sponsors and, where used, their targeting, and the Commission is building a public repository of online political ads. The registry extends that logic from the advert to the rehearsal that produced it.

Finally, an individual right sits under all four. No public body or political campaign may build a simulation of a *named* person, a digital twin in Pew's sense, without that person's consent; and anyone may ask whether a public body has simulated "people like me" and see the statement. You cannot opt out of being average. You can insist on being asked.

---

## Democracy lives in the tails

Back to the objection, at full strength. Real polls are flawed. The *Digest* heard millions and got it wrong. Response rates are low, and the people who answer differ from those who do not. Public consultations are captured by lobbies and by people with time. A simulation, whatever its faults, includes everybody: the night-shift worker and the person who never opens post from the government. A quota of real samples looks like a rule that privileges a flawed instrument over a better one, for sentimental reasons.

Part of this I concede. Simulation is useful, and the rules above are designed to let it be used. For drafting a question, or for deciding which hypotheses deserve a real poll, Singapore's Echo looks to me like a sensible tool, used with the right caveats. And real consultations do have a capture problem. The quota addresses part of it by requiring probability samples; open calls are the instrument the lobbyists dominate.

Where the objection fails is in the word *includes*. A simulation includes everyone's average. The evidence of the last three years is consistent on this one point: means come out roughly right, spread comes out too narrow, and the groups that differ most from the middle come out worst. Bisbee found it in 2024; Angelina Wang and colleagues found models flattening identity groups in 2025; the KAIST team found its mechanism this summer; Pew found it in September, with errors largest for the groups furthest from the model's centre of gravity and with partisan majorities hardening into unanimity.

Democracy lives in the tails. Most of what a public consultation is for is finding the people the planners did not picture: the fifteen families on the bus route that the new timetable strands, the minority whose objection reveals a flaw the majority never noticed, the narrow segment that decides a close vote. Switzerland makes this structural, since many constitutional changes need a majority of cantons as well as of voters, so small places can block large ones. A system that is accurate on the average and wrong in the tails is accurate exactly where accuracy matters least.

There is a second, harder answer. The *Digest*'s error could be corrected, because the election happened and the real result came in. Gallup could be checked; so could the *Digest*. A simulation consulted on a decision that never goes to a vote is never checked against anything. Without a ground truth, a forecast goes untested and its error stays unknown. The quota is how the models stay calibrated at all.

My own proposal has a weakness too. The quota assumes there is still a clean real sample to draw. If, by 2036, a large share of people let their agents answer surveys for them, as Hanne did, the statistics office will be sampling simulations without knowing it. Flagging agent answers helps only if the agents say so honestly. I think that flag needs to be a legal duty on the agent's maker, and I think it will be the hardest part of the scheme to enforce.

---

The result of Initiative 214 comes in that Sunday at 16:20. Yes, 51.8 percent. The published simulations had said fifty-four. Mara writes the gap on the back of an envelope, out of habit, and notices that it is largest in two communes where nobody she knows lives.

That evening, for the first time in years, she asks Pilote a question it cannot answer from its own records: how much did the canton spend on simulating its voters this year, and how much on asking them? Pilote searches for a long time and reports that the canton does not publish either figure.

In Nairobi, a school administrator is about to point her agent at a county budget.

## Notes

- **Literary Digest, 1936:** standard account in Freedman D, Pisani R, Purves R, *Statistics*, Norton (any edition); summary at https://en.wikipedia.org/wiki/The_Literary_Digest
- **Silicon samples:** Argyle LP, Busby EC, Fulda N, Gubler JR, Rytting C, Wingate D, "Out of One, Many: Using Language Models to Simulate Human Samples", *Political Analysis* 31(3), 2023. https://arxiv.org/abs/2209.06899
- **Whose opinions:** Santurkar S, Durmus E, Ladhak F, Lee C, Liang P, Hashimoto T, "Whose Opinions Do Language Models Reflect?", ICML 2023, PMLR 202. https://proceedings.mlr.press/v202/santurkar23a.html
- **Compressed variance:** Bisbee J, Clinton JD, Dorff C, Kenkel B, Larson JM, "Synthetic Replacements for Human Survey Data? The Perils of Large Language Models", *Political Analysis* 32, 2024. https://doi.org/10.1017/pan.2024.5
- **Flattening identity groups:** Wang A, Morgenstern J, Dickerson JP, "Large language models that replace human participants can harmfully misportray and flatten identity groups", *Nature Machine Intelligence* 7, 2025. https://arxiv.org/abs/2402.01908
- **Pew digital twins:** Pew Research Center, "How well synthetic samples replicate public opinion", Data Labs, 30 September 2026 (from the report "Can AI Stand In for Human Survey-Takers? Not Really."). https://www.pewresearch.org/data-labs/2026/09/30/how-well-synthetic-samples-replicate-public-opinion/
- **Sampling collapse:** Jang C, Lee D, Kim J (KAIST), "Instruction-Tuned Language Models Cannot Sample from Distributions They Can Describe", arXiv 2607.25292, July 2026. https://arxiv.org/abs/2607.25292
- **Super-omnivorous respondents:** Ma X, Zhang M, Ang S, Chen M, "Tastes without distinction: silicon samples and the synthetic construction of tastes", arXiv 2606.30085, June 2026. https://arxiv.org/abs/2606.30085
- **Aaru funding:** TechCrunch, "AI synthetic research startup Aaru raised a Series A at a $1B headline valuation", 5 December 2025. https://techcrunch.com/2025/12/05/ai-synthetic-research-startup-aaru-raised-a-series-a-at-a-1b-headline-valuation
- **Aaru's New York simulation:** Fortune, profile of Aaru co-founder Ned Koh, 17 June 2026. https://fortune.com/2026/06/17/aaru-cofounder-ned-koh-ai-startup-sales-pitch-do-not-trust-us/
- **Downing Street's "synthetic voters":** Orlowski A, *The Telegraph*, 7 July 2025, relaying a *Spectator* report. https://www.yahoo.com/news/starmer-synthetic-voters-show-downing-100000972.html
- **Singapore's Echo:** GovTech Singapore, "Before It Goes Public: Using AI to Test Government Messages", 11 September 2026. https://www.tech.gov.sg/technews/using-ai-to-test-government-messages/
- **Fake Plastic Voters:** Novelli C et al., "Fake Plastic Voters: When Political Parties Can Use AI-Simulated Focus Groups", SSRN/PhilArchive, April 2026. https://philarchive.org/rec/NOVFPV
- **Synthetic voters, podcast:** Tech Policy Press, "Here Come the Synthetic Voters", 16 August 2026. https://techpolicy.press/here-come-the-synthetic-voters
- **Persuasion levers:** Hackenburg K et al., "The levers of political persuasion with conversational artificial intelligence", *Science* 390, 4 December 2025. https://arxiv.org/abs/2507.13919
- **Persuading voters:** Lin H et al. (incl. Rand DG), "Persuading voters using human–artificial intelligence dialogues", *Nature* 648, 4 December 2025. https://doi.org/10.1038/s41586-025-09771-9
- **EU political advertising:** Regulation (EU) 2024/900 on the transparency and targeting of political advertising; European Commission overview. https://commission.europa.eu/strategy-and-policy/policies/justice-and-fundamental-rights/democracy-eu-citizenship-anti-corruption/democracy-and-electoral-rights/transparency-and-targeting-political-advertising_en

## Part Three: When Machines Read Everything

# Chapter 8: Seeing Like a Citizen

*2036 · Nairobi*

The power comes back at nine, and with it the fan, and with it Ndege.

"Sorry, I lost you in the middle of a sentence," says the agent from the phone propped against the sugar tin. "I was saying that the maternity wing is still there."

Wanjiru Kamau is marking her own children's homework at the kitchen table because the school she runs does not leave her time to do it in daylight. Njeri's essay on the water cycle is good and too long. Baraka has drawn a goat in the margin of his fractions. She caps the red pen.

"Still where?"

"Still in the budget. Line 4.2.17 in the health department, *Construction of maternity wing, Mto Mdogo Health Centre*, fourteen point two million shillings. It first appears in the estimates for 2030/31. In every year since, it appears again, with the same words and a note: *carried forward*. Six years."

"Kwani it was never built?"

"I can't find that it was started. There's no expenditure against it in any of the Controller of Budget's quarterly reports. There's no contractor named in the procurement notices. And the amount has never changed, which is strange for a building. Cement went up forty percent over the period."

Wanjiru knows the health centre. It is twelve minutes' walk from the house, a low blue building with a queue that starts before the gate opens. When Baraka was born she went to Kenyatta instead, because everyone knew Mto Mdogo had nowhere to put a mother overnight. Her neighbour Akinyi's daughter delivered in a matatu last March, outside the Thika Road mall, with the driver shouting at the traffic.

"Show me."

The screen fills with six columns, one per year, and the line glowing in each. Under it Ndege has laid out the documents it read: six sets of budget estimates, twenty-four quarterly implementation reports, the procurement portal, four audit reports, the minutes of the county assembly's health committee, which mentioned the wing once, in 2032, in a sentence that ended with *the department undertook to follow up*.

"How long did that take you?"

"About four minutes. Most of it was waiting for the county website."

She laughs, then stops. Her mother used to stand in the queue at the chief's office with a photocopy of a notice from the district development committee, asking what had happened to the borehole. Nobody ever told her. The photocopy lived in a biscuit tin for years.

"Sawa. What can I do with it?"

"The county assembly has to facilitate public participation in its business. You can petition it. I've drafted one. It sets out the line, the six years, the absence of any expenditure, and asks three questions: was the wing ever tendered, where has the money been held, and when will it be built. I've attached the documents by reference so they can't say they haven't seen them."

She reads the draft. It is good and too long, like Njeri's essay. She cuts the paragraph that quotes the Constitution at the county, because they know what it says, and the one about cement, because she likes the cement point and wants to save it for the hearing.

"Should we ask people to sign?"

"Akinyi will. Your WhatsApp group from the PTA has two hundred and forty members in this ward."

She sends the message. By half past ten, two hundred and twelve people have added their names. Some of them have added a sentence about their own deliveries. One has added a photo of the blue building with the queue.

At 23:14 she presses *Submit*. The county portal thinks about it for a while. Then a reference number appears, and under it, in the county's own cheerful font, a line of text she has seen before on other forms:

*Thank you, Wanjiru. Based on your profile, we think you may also be interested in our survey on market fees.*

She closes the phone face down on Baraka's goat.

---

## The view from the tower

In 1998 the political scientist James C. Scott published a book about why states see the way they do. *Seeing Like a State* starts with forests. Eighteenth-century German foresters, wanting to know how much timber a forest would yield, replaced the tangle of species and local uses with neat rows of a single tree that could be counted from a ledger. The forest became legible. For one generation it was also very productive. Then the soil gave out.

Scott's word for this was **legibility**: the state's project of making society readable from the centre. Permanent surnames, cadastral maps, standard weights and measures, the census and the street grid are all tools for it. A state that can read its people can tax them and vaccinate them. Scott thought legibility became dangerous when it was combined with a plan to remake society and the power to impose it, because the simplified picture always leaves out the local knowledge that kept the old arrangement working.

The book has a direction built into it. The state looks down; the citizen is looked at. Most of the twentieth century's information technology reinforced that direction. Punch cards and databases made it cheaper for the centre to read the periphery. In 2025 Petter Törnberg and four colleagues extended Scott's argument to artificial intelligence, arguing that the state's way of seeing is shifting again, away from statistical variables and towards patterns found by machine learning in data from sensors and platforms. Their state now sees like a neural network. I think they are right about the state.

What I want to add is the other direction. The same machines that let a state read its population also let a population read its state. Until now that second kind of reading has been rare. It has been rare because it was expensive, and most of the expense was the reading itself.

---

## A right nobody could afford to use

Kenya is a good place to see this, because on paper it has given its citizens more right to read public money than almost anywhere.

The Constitution of 2010, written after decades in which public money disappeared into unexplained projects, makes public participation in financial matters a principle of public finance and has the Auditor-General audit every county's accounts each year. The Public Finance Management Act of 2012 adds the machinery: budget hearings every year, ward by ward, and a forum in every county where citizens' groups sit with the governor's team to discuss its plans.

So the right exists. How much use is made of it?

The International Budget Partnership's Open Budget Survey for 2023 scored Kenya's national government 55 out of 100 for transparency, a little below the 61 the survey treats as enough for informed public debate, and 31 out of 100 for public participation. That participation score led East Africa, which tells you something about East Africa. At county level, the same organisation's County Budget Transparency Survey for 2023 found that about 141 of 517 key county budget documents, more than a quarter, were not publicly available at all, and only about 15 percent were published on time. The 2024 edition found that the documents counties do publish still leave out roughly two-fifths of the information the law requires them to contain.

And when the documents are published, someone has to read them. A county budget runs to hundreds of pages of tables. Tracing one line from the estimates through the quarterly implementation reports to the audit, across several years, means cross-referencing documents in different formats, released by different offices, often as scanned PDFs, using codes that change between years. I looked for a measurement of how long this takes a motivated citizen and could not find one. My guess, from the structure of the documents, is days of work for a single line, and weeks for a ward. The people who did it in 2026 were mostly professionals in civil society organisations, and there were not many of them.

There was one striking exception. In June 2024 young Kenyans took apart the national Finance Bill, a document the *Daily Nation* later described as so complex that even members of parliament struggled to follow it, and explained it clause by clause on TikTok and X. Within two weeks there were protests across the country, and the president withdrew the bill. It showed what happens when the reading cost of a state document suddenly drops: a population that had a constitutional right to participate for fourteen years used it, all at once.

That reading was done by thousands of people over several weeks. By 2036, in my scenario, the same reading takes Ndege four minutes.

---

## Seeing like a citizen

Here is the chapter's concept. **Seeing like a citizen** is Scott's legibility running upwards: the state becoming readable to the people it governs, because machine reading has collapsed the cost of tracing what the state actually does.

The idea has neighbours, and they deserve credit. In 2010 Eric Pickles, then the British communities secretary, asked English councils to publish every item of spending over £500 and called for an "army of armchair auditors" to go through it. Steve Mann's term *sousveillance*, watching from below, names the same reversal for cameras: the watched recording the watchers. What both still needed was someone with the time to do the looking, and that is the expense machine reading removes.

It is worth being precise about what collapses. Bureaucracies have always held an advantage over the people they serve. Some of that advantage is secrecy, and much of it is volume. The county printed line 4.2.17 six times, in public documents, and relied, without anyone deciding to rely on it, on the fact that nobody outside the department would hold six years of documents in their head at once. A line that is carried forward for six years is not concealed. It is simply never read twice by the same person.

An agent reads everything twice. It has no reason to get bored at the procurement portal, and it remembers 2031 when it reaches 2036. The bureaucracy's oldest protection, the patience of its documents, stops working.

This is a success story, and I want to say so plainly before turning to what goes wrong. If citizens' agents read public budgets, the most common forms of quiet failure in public finance (the line rolled over until everyone forgets it, the payment made against a contract that does not exist) become much harder to sustain. The Kenyan Constitution's drafters wanted exactly this. They wrote the right to participate in financial matters into the supreme law. What they could not write was the reading capacity.

The failure comes from the same place as the success. If one citizen's agent can read the budget in four minutes, every citizen's agent can. If one petition takes Wanjiru half an hour to send, a hundred thousand petitions take a hundred thousand half-hours, spread across a city of several million. The county has the same number of clerks it had in 2026.

---

## The flood

This part is already under way. It started before agents could act on their own.

In August 2026, Chris Schmitz of the Hertie School and Lewis Hammond and Alan Chan of the Centre for the Governance of AI published the first systematic look at what they call **agentic flooding** of government services: surges in requests to public bodies that the bodies themselves, or credible observers, attribute to people using AI. They found 84 such cases in 11 jurisdictions. In nine cases out of ten the requests had become longer and more complex; in six out of ten there were simply more of them. Almost all of it was people pasting text from a language model into existing forms by hand. They found no evidence yet of autonomous agents filling in government portals on their own. The examples run from freedom-of-information requests in Australia and the United Kingdom to a German social court case in which the submissions ran past four thousand pages.

In the United Kingdom, central government bodies received more freedom-of-information requests in 2025 than in any year since monitoring began in 2005. In 2026 the Information Commissioner's Office published guidance on handling AI-written requests: they are valid, the guidance says, but they tend to be longer, more repetitive, broader and harder to interpret, and coordinated high-volume campaigns may in some circumstances be refused as vexatious.

There is an older warning too. When the US Federal Communications Commission asked for public comment on repealing net neutrality in 2017, it received more than 22 million comments. An investigation by the New York Attorney General later found that nearly 18 million of them were fake, many generated in the names of real people who had never heard of the campaign that used them. That was done with lead-generation firms and spreadsheets. It needed no AI.

The most important finding in the flooding paper is about how governments respond. In more than half the cases they did something. In about one case in six, what they did was add friction, such as fees or identity checks. In a quarter, they adopted AI tools of their own to process what was arriving. The authors point out that friction falls hardest on poorer and less digitally confident users, and they expect suppressing demand to become the default response, because it is cheap and fast.

Put that together with Kenya's constitution and you can see the shape of the danger. A county that receives a hundred times more petitions than it can read has two easy options. It can make petitioning harder, which takes back the right the constitution gave. Or it can point its own agents at the petitions and answer them automatically, with long, correct, uninformative replies that no person on either side reads. In my scenario the county does both, and the reply to Wanjiru will be the subject of the next chapter. I will call this response **defensive automation**: a public body using machines to absorb citizens' machine-generated scrutiny instead of acting on it. It is the institutional version of an immune response, and like an immune response it can do more damage than the thing it is fighting.

---

## Three duties

So the question is how to keep the gain, citizens who can read their state, without the flood, and without letting the state escape into automated non-answers. I propose three linked pieces. Each is specific enough to be wrong.

**First, machine-readable budgets as a legal duty.** Publishing a budget as a scanned PDF should count, legally, as not publishing it. Every budget line should carry a permanent identifier that survives from one year to the next, so that line 4.2.17 in 2031 is recognisably the same line in 2036. Each line should carry a status that the treasury updates every quarter: appropriated, tendered, contracted, spent, carried forward, cancelled. The data should be released in an open format within the deadlines the law already sets for the documents. None of this is technically novel. Since the OECD's Observatory of Public Sector Innovation published *Cracking the Code* in 2020, governments from New Zealand to France have experimented with publishing official machine-consumable versions of rules; a budget is a simpler case than a statute. One rule follows immediately: any line marked *carried forward* for three consecutive years is flagged automatically in the Controller of Budget's next report, and the department must publish a one-page explanation. Line 4.2.17 would have been flagged in 2033.

**Second, citizen audit standing.** At present, a Kenyan who takes part in a budget hearing has a right to be heard and very little right to an answer. When the Supreme Court upheld the Finance Act 2023 in October 2024, it found that Parliament had no express obligation to give reasons for accepting or rejecting the public's proposals, as long as it had reasonable measures for considering them. Citizen audit standing would add that obligation, narrowly, for one kind of submission: a structured finding. A finding cites specific line identifiers, states what the data shows, and asks specific questions. If a finding is supported by verified residents of the affected ward (I would start at fifty, or one percent of the ward's registered voters, whichever is smaller), the county must give a reasoned written answer within thirty days, signed by a named officer. If it does not, or if the answer does not address the questions, the finding goes to the Auditor-General, who must carry out a targeted audit of those lines within six months.

The standing is what makes the reading matter. Without it, Wanjiru's agent is a very fast way of producing documents that go into a different biscuit tin.

**Third, a legibility dividend.** When a finding leads to money being recovered, reallocated or finally spent on its purpose, a fixed share of that amount, say ten percent, goes into a ward fund. Half of it pays for public reading capacity: an open, audited citizen agent available free to anyone without one of their own, and help at the ward office for people who would rather talk to a person. The other half goes into the ward's share of the participatory budget. The dividend does two things. It pays for the reading to be distributed more evenly than the phones are. And it gives a county a measurable return on being read, which is the only argument I know that reliably moves a treasury.

The same structure defends against the flood. Findings that cite the same line identifier for the same period and ask the same type of question merge into a single docket, which the county answers once: a thousand agents that discover line 4.2.17 produce one docket with a thousand supporters, each a verified resident of the ward the line affects.

Distinct findings are the harder flood. An agent patient enough to read every line of a county budget will find something odd in a good share of them, a rounding change here, a line that moved departments there. So support is capped: each resident can back, say, five findings a quarter. Their agent can notice everything; the resident chooses what deserves an answer. The county's workload then grows with the number of problems residents care about, whether one citizen notices them or a million do.

There are numbers to watch. A county's **legibility score** could be published every year: the share of its budget lines with a permanent identifier and a current status, the median time to answer a finding, and the share of findings the Auditor-General later upholds. A county whose answers keep being overturned by the auditor is answering automatically. That is how defensive automation would show up in the data.

---

## Freedom of information did not do this

History is the obvious reply to all of this. We have tried transparency before. The United States passed its Freedom of Information Act in 1966, and Kenya its Access to Information Act in 2016. Governments built open data portals throughout the 2010s. If access to information were going to change the balance of power between citizens and the state, it would have done so by now. The careful research on the United Kingdom's act of 2000 supports a modest view. Ben Worthy's study of central government, published in 2010, found that the act made government more transparent and more accountable. A later study of Parliament by Robert Hazell, Gabrielle Bourke and Worthy found that it did not increase public understanding, participation or trust. Why should agents be different?

I think the answer lies in what freedom of information actually supplied. It supplied access: the right to have a document. It did nothing about the cost of reading one, and still less about the cost of reading six years of them against each other. That cost is why the main users were people paid to read. An agent supplies the missing piece, reading capacity, to anyone with a phone. The Finance Bill of 2024 is a small natural experiment in this direction: when reading capacity was briefly supplied by thousands of volunteers, participation jumped.

But I want to concede two things to the objection, because I think they are true.

The first is that reading is only the first step towards power. Freedom of information made British government more accountable without making it more trusted, and there is no reason to think agents will do better on trust. Wanjiru's petition may produce a maternity wing. It may also produce an answer that is perfectly reasoned and changes nothing. Seeing like a citizen moves the bottleneck from reading to answering, and then from answering to acting. Citizen audit standing pushes on the second step. Nothing in this chapter guarantees the third, which is politics, and should be.

The second is about who reads. Wanjiru is a school administrator with a good phone, a PTA WhatsApp group and a constitutional education. The people who most need a maternity wing at Mto Mdogo are, on average, less likely to have any of those. If reading capacity follows the distribution of good phones, the state becomes legible mainly to the people who already had most access to it, and the wards with the most active agents get the most attention. That is why the legibility dividend pays for public reading capacity, and why I would measure it: the share of findings coming from the poorest third of wards is a number a county could publish, and a number a citizen's agent could check.

There is also a version of the objection that runs the other way, and I find it harder. It says that a state which knows it will be read by every citizen's agent, every quarter, forever, will learn to write documents that resist reading. It will have nothing to hide, and it will write more. I read this as a prediction about what happens next, and I think it is correct.

---

Five weeks after Wanjiru presses *Submit*, the county replies. The reply is courteous and on time. It thanks the two hundred and twelve petitioners for their engagement, notes that the matters they raise are addressed in the county's new Health Facility Budget Carry-Forward (Public Participation and Accountability) Regulations, 2036, and attaches them.

The regulations are nine hundred and twelve pages long. Their metadata says they were drafted in eleven days.

Ndege reads them in six minutes. Then it says, "Wanjiru, I need to tell you something about Section 212."

## Notes

- **Legibility:** Scott JC, *Seeing Like a State: How Certain Schemes to Improve the Human Condition Have Failed*, Yale University Press, 1998. https://archive.org/details/seeinglikestate00jame
- **The state seeing through AI:** Törnberg P, Söderström O, Barella J, Greyling S, Oldfield S, "Artificial intelligence and the state: Seeing like an artificial neural network", *Big Data & Society* 12(2), 2025. https://doi.org/10.1177/20539517251338773
- **Kenya, constitutional provisions (Arts. 10, 35, 196, 201, 229):** Constitution of Kenya, 2010. https://www.constituteproject.org/constitution/Kenya_2010
- **Access to Information Act:** Kenya, Access to Information Act No. 31 of 2016. https://new.kenyalaw.org/akn/ke/act/2016/31
- **County budget process and CBEF:** Kenya, Public Finance Management Act No. 18 of 2012, ss. 125 and 137; as applied in, e.g., Kisii County public hearing notice (2015), https://kisii.go.ke/?p=13256 ; Institute of Public Finance Kenya, "CBEF: are they the only legal mechanism of public participation at the county level?", 2020, https://ipfglobal.or.ke/cbef-are-they-the-only-legal-mechanism-of-public-participation-at-the-county-level/
- **Supreme Court on the Finance Act 2023:** EY Global Tax Alert, "Kenya Supreme Court declares the Finance Act 2023 constitutional", November 2024. https://www.ey.com/en_gl/technical/tax-alerts/kenya-supreme-court-declares-the-finance-act-2023-constitutional
- **Open Budget Survey 2023, Kenya:** International Budget Partnership. https://internationalbudget.org/open-budget-survey/country-results/2023/kenya
- **County Budget Transparency Survey 2023:** reported in *The Star* (Kenya), "Counties improve budget openness but reports wanting – survey", May 2024. https://www.the-star.co.ke/business/2024-05-25-counties-improve-budget-openness-but-reports-wanting-survey
- **County Budget Transparency Survey 2024:** Bajeti Hub; reported in *Eastleigh Voice*, "Availing of county budget details up, but key information remains hidden – survey", 2025. https://eastleighvoice.co.ke/county%20budgets/154489/availing-of-county-budget-details-up-but-key-information-remains-hidden---survey
- **Finance Bill 2024 explained online:** *Daily Nation*, "June 25: the day Gen Zs instilled fear in Kenya's political class". https://nation.africa/kenya/news/june-25-the-day-gen-zs-instilled-fear-in-kenya-s-political-class-5508700 ; CSIS, "Taking Charge: Gen Z Leads Historic Protests in Kenya", 2024. https://www.csis.org/analysis/taking-charge-gen-z-leads-historic-protests-kenya
- **Agentic flooding:** Schmitz C, Hammond L, Chan A, "Characterizing Agentic Flooding of Government Services", arXiv:2608.16603, 2026. https://arxiv.org/abs/2608.16603 ; *Local Government Lawyer*, "Researchers warn of 'agentic flooding' of public services", September 2026. https://localgovernmentlawyer.co.uk/information-law/398-information-law-news/101629-researchers-warn-of-agentic-flooding-of-public-services-with-ai-generated-communications
- **AI-generated FOI requests:** Information Commissioner's Office, "Freedom of information (FOI) and artificial intelligence", 2026. https://ico.org.uk/for-organisations/foi/freedom-of-information-foi-and-artificial-intelligence/ ; *Civil Service World*, "ICO publishes guidance to help public bodies handle AI-generated FOI requests", 2026. https://www.civilserviceworld.com/professions/article/ico-publishes-new-guidance-to-help-public-bodies-handle-aigenerated-foi-requests
- **UK FOI requests, 2025 record:** Cabinet Office, "Freedom of Information statistics: annual 2025 bulletin" (94,526 requests across monitored central government bodies in 2025, up 14% on 2024, the largest number since monitoring began in 2005), 2026. https://www.gov.uk/government/statistics/freedom-of-information-statistics-annual-2025/freedom-of-information-statistics-annual-2025-bulletin
- **Fake FCC comments:** New York State Attorney General, "Attorney General James Issues Report Detailing Millions of Fake Comments", May 2021. https://ag.ny.gov/press-release/2021/attorney-general-james-issues-report-detailing-millions-fake-comments-revealing
- **Rules as Code:** Mohun J, Roberts A, *Cracking the Code: Rulemaking for humans and machines*, OECD Observatory of Public Sector Innovation, 2020. https://oecd-opsi.org/publications/cracking-the-code/
- **Armchair auditors:** Department for Communities and Local Government, "Armchair auditors pore over council spending data", GOV.UK news story, 11 November 2010 (90 councils publishing spending over £500; the "army of armchair auditors" called into action by Eric Pickles). https://www.gov.uk/government/news/armchair-auditors-pore-over-council-spending-data ; Russell V, "DCLG publishes spending details", *Public Finance*, August 2010. https://www.publicfinance.co.uk/news/2010/08/dclg-publishes-spending-details
- **Sousveillance:** Mann S, Nolan J, Wellman B, "Sousveillance: Inventing and using wearable computing devices for data collection in surveillance environments", *Surveillance & Society* 1(3): 331–355, 2003. https://ics.uci.edu/~djp3/classes/2012_09_INF241/papers/sousveillance.pdf
- **FOI and trust:** Worthy B, "More Open but Not More Trusted? The Effect of the Freedom of Information Act 2000 on the United Kingdom Central Government", *Governance* 23(4), 2010. https://doi.org/10.1111/j.1468-0491.2010.01498.x ; Hazell R, Bourke G, Worthy B, "Open House? Freedom of Information and its Impact on the UK Parliament", *Public Administration*, 2012.

# Chapter 9: The Red Queen of Rules

*2036 · Nairobi*

"Section 212," says Ndege, from the phone propped against the sugar tin, "deems your petition incomplete, because it was filed before the regulation existed. Section 88 says any petition about a carried-forward line must now be filed on Form PP-17, with a Statement of Particulars in the format set out in Schedule Nine. You have twenty-one days to refile."

It is 06:14 on a Tuesday, and Wanjiru is looking for Baraka's other shoe. She finds it under the sofa. Baraka, who is nine, is lying on the floor beside it, explaining to the ceiling why he cannot go to school today. She hands him the shoe without looking.

"Nine hundred pages. For one line in a clinic budget."

"For the principle," says Ndege. "Part Two defines 'carry forward'. The definition runs to forty-one pages. It's quite good, actually. It distinguishes eleven kinds of carrying."

Wanjiru sits down on the arm of the sofa. Outside, a matatu is playing gospel at a volume that suggests the driver is in some trouble with God.

"Maze. Can you do the form?"

"I've done it. Forty pages. I attached the clinic's six years of ledgers, the ward's population projections, a comparison with four other counties and a reading of Section 88 that I think the county will find uncomfortable."

"Ndege, I asked for a letter."

"It is a letter. It has annexes."

She files it from the bus. By the time she reaches school, the county's own agent has thanked her for her civic engagement and issued an amending notice that inserts a new Schedule Fifteen, governing the format of annexes to a Statement of Particulars. Ndege has drafted a response. The response is longer than the notice.

That evening, Njeri, who is thirteen and in Grade 8, picks up the printout Wanjiru made of the regulation's first page at the school copier, out of a kind of morbid respect. Njeri reads it to the bottom and starts again at the top, frowning, while Baraka eats her chapati.

"Mum. So can they spend the clinic money or not?"

Wanjiru opens her mouth. Then she closes it, because she does not know, and nor, she suspects, does anybody at the county. The regulation was drafted by an agent in response to an agent. It is precise to the last defined term, and it would survive any court. And there is no sentence in it that a person could read aloud to another person and say, there, that is what you must do.

"Ndege," she says. "Wueh. Who is this for?"

Ndege takes a moment, which it does not usually need.

"For me, mostly," it says.

---

In Brussels, a year earlier, Élodie Marchetti is a lawyer-linguist at the Council of the European Union. Her job, for nineteen years, has been to make sure that a law says the same thing in all twenty-four official languages.

The directive in front of her governs how household agents exchange consent records across borders. The main text is eleven pages. Its technical annex, in English, runs to about 640,000 words, which is longer than *War and Peace*. Élodie knows this because a colleague worked it out and pinned the comparison to the noticeboard, beside a postcard of Tolstoy.

The cover note says verification of the annex across languages will be performed by agents, with "human review by sampling". Élodie samples page 4,211. It is a table of conditional rules about what one machine must send another when a third machine has gone offline. She follows one rule down three columns with her pencil. She initials it.

---

## A race that runs in place

In Lewis Carroll's *Through the Looking-Glass*, the Red Queen tells Alice that in her country you must run as fast as you can to stay in the same place. In 1973 the palaeontologist Leigh Van Valen borrowed the image for a law of evolution. Species that compete with each other must keep changing simply to keep their relative fitness, because their rivals are changing too. The hare gets faster; the fox gets faster; neither gets ahead.

Regulation has always been a Red Queen race. A rule is written. The people it binds, quite reasonably, look for the cheapest way to comply, and sometimes for a way around it. The regulator notices and writes a patch. The patch has edges of its own. Everyone in it can be acting in good faith; a tax adviser who finds a lawful saving for a client is doing her job, and so is the official who closes it.

What has kept the race from running away is cost. Every patch needed a human drafter, and every evasion needed a human adviser. Both were slow and expensive, and both had to be read by someone, which was slower still.

Even with those brakes on, the text grew. The US Code of Federal Regulations, the compiled rulebook of American federal agencies, ran to 9,745 pages in 1950. By 1980 it was over 100,000. By 2021, the last year the National Archives has published a total, it was about 188,000 pages in 243 volumes. The Mercatus Center, which counts words like "shall" and "must" in the code, found nearly 103 million words and more than a million such restrictions in 2019. Between 1970 and 2017 the code grew by about 1.4 million words a year, which is roughly two *War and Peace*s annually, written by people.

I want to be careful about what these numbers show. Page counts include tables and repealed matter, and a long rule is sometimes a clearer rule. Whether the CFR's growth made America worse governed is an open question. The numbers settle something narrower: a system with human drafters and human readers already produced more law than any human could read. The most anyone reads of the Code of Federal Regulations is a slice.

## Where we are in 2026

Now take the cost out of both sides at once.

In April 2025 the United Arab Emirates announced that it would use AI to help write and amend its laws, under a new Regulatory Intelligence Office, with the stated aim of producing legislation much faster. In March of the same year, Peter Fratrič, Nils Holzenberger and David Restrepo Amariles described a prototype that pairs a language model with a formal planning language to find loopholes and avoidance schemes in tax law. They meant it as a tool for policy-makers, and they were frank that turning legal text into formal rules is still the hard part.

Put those two developments in the same room. The tool that finds a loophole for the treasury finds it for the taxpayer's agent at the same moment, and the drafting system that closes it can write the patch in an afternoon. Each round is cheaper than the last. I could not find any measurement of what this does to the length or complexity of enacted law, because the drafting systems are too new. Measuring it would be a straightforward study, and an urgent one.

We have seen a smaller version of the flood from the other side: the 22 million net-neutrality comments of the previous chapter, most of them fake, produced by lead-generation firms before any language model could help. An agency facing that, and then facing agents that file forty-page Statements of Particulars on behalf of every engaged citizen, will do what Nairobi county does in my scenario. It will defend itself in text.

## Why the joke stops being funny

Up to here the story is a farce, and I meant it to read as one. A forty-one-page definition of "carry forward" is funny. So is an annex longer than Tolstoy, initialled by a tired lawyer on page 4,211.

The farce has a cost, and it falls on the people who have to obey. A law is a set of instructions addressed to people. When the instructions can only be read by machines, obeying the law becomes something you delegate, like your tax return or your heat pump. Whatever your agent believes the regulation says is, for practical purposes, the law as it applies to you.

That has two consequences I find hard to wave away. The first is inequality of a new kind. Wanjiru has Ndege, which can produce a Statement of Particulars in the time it takes her to find a shoe. Her neighbour, with a cheaper agent or none, has twenty-one days to complete Form PP-17 alone, and will not. The right to petition still exists on paper. It has simply been priced out of reach of anyone without good software.

The second is that the law stops being something citizens can argue about. You can only object to a rule you can state. When Njeri asks whether the county can spend the clinic money, the honest answer is that two machines know and the humans are waiting to be told. That is a strange way for a democracy to run its clinics, and it is the direction that every incentive I have described points.

This is the dark side of the previous chapter. Seeing like a citizen works; the state becomes legible to Wanjiru. The state's rational response is to become illegible again, in a way no court can fault, by being complete.

The legal scholar Lisa Burton Crawford, of the University of Sydney, has made the most useful argument I know about where this leaves the law. Writing in 2025 about Rules as Code, the movement to publish laws alongside an executable version, she points out that legislation is already so voluminous and prescriptive that almost nobody engages with it the way legal theory assumes. Most people meet the law through a government website or a benefits calculator, whose answers usually carry little legal weight. She treats reasonable knowability as a core value of the rule of law and sees machine-readable rules as a pragmatic way to protect it. And she ends by asking whether the sheer volume and complexity of modern law is itself a constitutional problem.

I think it is, and I think AI turns it from a slow problem into a fast one. Rules as Code is a good idea that removes the last brake. Once a rule can be executed by a machine, nobody needs to be able to read it, and so nobody will insist that they can.

## We have tried plain language

Governments have legislated against bad writing before, and the history is comic in a way that is useful.

On 13 October 2010 President Obama signed the Plain Writing Act. It requires American federal agencies to write clearly in the letters, forms, notices and instructions they send the public. Its definition of a covered document then adds, in a separate clause, that it "does not include a regulation". Section 6 says there shall be no judicial review of compliance with the Act, and that it creates no right anyone can enforce. The law about plain writing exempts the rules themselves, and you cannot sue over it.

Sweden's Language Act of 2009 is broader: language in the public sector must be "cultivated, simple and comprehensible". Nobody tests whether it is. That is the pattern with plain-language laws everywhere I have looked. They describe a virtue and assign it to the same drafters whose incentives produced the problem. None that I could find measures whether an actual person understood an actual law.

## The invention: a readability ceiling and a complexity brake

My proposal has two parts, and both rest on one distinction. Every law has an **obligation layer**, what a person must do, must not do, may claim and what happens if they don't. And it has an **implementation layer**: the calculations, thresholds, data formats, timetables and procedures that make the obligations work. Complexity may live in the implementation layer. Obligations on people must stay short enough to explain.

The first part is a **human-readability ceiling**, written into the constitution or a basic law. It says: every obligation that a law imposes on a natural person must be explainable to a fourteen-year-old within ten minutes.

Here is how it would be tested. Each bill carries an obligation statement, a short document listing each duty it places on individuals. A parliamentary readability office, staffed like a budget office, draws a panel of thirty citizens by lot, the way juries are drawn. Half are fourteen or fifteen, half are adults, and they are paid for the day. A human explainer, who may prepare with any tools she likes, gets ten minutes per obligation to explain it out loud. The panel then answers five scenario questions each, without help and without agents: *Your aunt runs a kiosk; does she need to file this? What happens if she doesn't?*

The bill passes the ceiling if at least eighty per cent of panellists get at least four of five questions right. If it fails, it goes back to the drafters. And any obligation that is not in a passed obligation statement cannot be enforced against a natural person, however precisely it is written in Schedule Fifteen.

Agents are excluded from the test by design. The point is to measure whether the law fits in a human head, and specifically in the head of someone who has not yet learned to tolerate bad law.

Try it on Nairobi's 912 pages. The obligation statement for a citizen would be short. *If you want to object to money being carried forward in a clinic budget, write to the county saying which line and why. The county must answer within thirty days and publish its answer.* Njeri could explain that to Baraka in two minutes. Everything else, from the eleven kinds of carrying to Schedule Fifteen's rules for annexes, binds the county's own staff and agents, and can be as long as they like. What the county could no longer do is make Form PP-17 a condition of being heard, because Form PP-17 would never pass a panel.

The second part is a **complexity brake**, modelled on Germany's debt brake, which since 2009 has capped federal structural borrowing in the constitution itself, with exceptions for recessions and emergencies. Its closest regulatory cousins are the "regulatory budgets" tried in Britain's one-in, two-out rule and the American two-for-one order of 2017, which counted rules and costs rather than obligations on people, and which critics showed were easy to game and which were later dropped or revoked; the brake below learns from them by counting what a person must do, not pages.

The legislative version counts obligations instead of euros. The readability office keeps a public register of every obligation on natural persons in force, each one a line in the register. A legislature may add obligations freely, as long as the net growth of the register over a parliamentary term stays below a fixed allowance, say two per cent. Beyond that, new obligations must be paid for by repealing or merging old ones. In a declared emergency a simple majority may exceed the allowance, but every emergency obligation expires after two years unless it is passed again under the normal rules.

Counting obligations is harder than counting euros. The office would publish a counting manual: one line per distinct duty, prohibition or entitlement condition that applies to a person, with tests for when two duties are really one. Disputes about the count would go to the national audit office, which already arbitrates arguments about what counts as spending. The count will be imperfect. A debt figure is imperfect too, and still disciplines a budget.

The German brake also shows how such rules fail. In November 2023 the Federal Constitutional Court struck down the government's attempt to move €60 billion of unused pandemic borrowing authority into a climate fund, because the emergency could not be stretched to cover it. In March 2025 the Bundestag loosened the brake itself, carving out defence and creating a €500 billion infrastructure fund outside it. Brakes get gamed, then renegotiated. The complexity brake will be gamed too, and the obvious move is to hide obligations in the implementation layer, calling a duty a "data format". That is why the readability ceiling's enforcement clause matters more than the counting. Anything a person must do that is not in a tested statement is simply not owed.

## Some things will not fit in ten minutes

The objection is that the world is complex and simple law is a fantasy. Bank capital and the electricity grid of the prologue cannot be explained to a fourteen-year-old in ten minutes, and a constitution that pretends they can will produce vague laws, which hand the real decisions to officials and courts. Crawford makes a version of this point herself: relying on executive guidance instead of knowable law is a retreat from the rule of law, and vague statutes are exactly that.

Part of this I accept. The ceiling should apply to obligations on natural persons, and perhaps on very small firms. A bank's capital rules are written for compliance departments, and pretending otherwise helps no one. For firms, the brake alone does the work.

But for people, the objection mixes up the two layers. A fourteen-year-old needs to understand that her aunt must keep receipts, file by the end of June and pay what the published calculator says, and that if she is late the penalty is a fixed amount. The computation of the tax can be as baroque as the treasury likes, provided it is published as code, anyone can run it, and the state is bound by its answer. That last condition is a real departure from legal tradition, and Crawford says so. I think AI makes it necessary. If the machine layer is where the law actually lives, the citizen has to be able to rely on it.

A practical version of the objection says the panels will be costly and gamed. Explainers will be coached, scenario questions written to be easy. Juries have the same weaknesses, and we keep juries. The cost is modest: if a legislature passes a hundred bills a year that place duties on individuals, and each needs a day or two of panel time, that is a few hundred days of thirty paid citizens a year, still less than a single large public inquiry. The gaming is the more serious risk, and the defence is the one used in exams. The scenario questions are written by a separate office, drawn from a large public pool, and released only after the panel sits.

The harder version of the objection is that the Red Queen does not stop. Fix the obligation layer, and the race moves into the implementation layer, where agents for the treasury and agents for the taxpayer will run at full speed against each other. The ceiling does not end the race. It moves the race to a place where only machines are running, and keeps a human-sized door between that place and the person who has to obey.

---

Wanjiru's petition was resolved in the end, three weeks later, and she found out by accident.

She asked Ndege, on the bus, whether the county had replied to its response to Schedule Fifteen. Ndege said the matter was closed. The county's agent and Ndege had agreed that the clinic line would be spent by March, with quarterly reporting. Somewhere in the agreement the maternity wing had become a delivery room: one bed, and still nowhere to put a mother overnight. They had agreed it the previous Thursday, in an exchange that took four seconds.

## Notes

- **Red Queen hypothesis:** Van Valen L, "A new evolutionary law", *Evolutionary Theory* 1:1–30, 1973. See University of Chicago, "Leigh Van Valen, evolutionary theorist and paleobiology pioneer, 1935–2010", 2010. https://news.uchicago.edu/story/leigh-van-valen-evolutionary-theorist-and-paleobiology-pioneer-1935-2010
- **CFR page counts, 1950–2021:** Office of the Federal Register (NARA), "Code of Federal Regulations Total Volumes and Pages 1950–2021", 2022. https://uploads.federalregister.gov/uploads/2022/10/28150527/FR-Stats-2021-Cfr-Volumes.pdf ; see also Crews CW, *Ten Thousand Commandments 2024*, ch. 4, Competitive Enterprise Institute, 2024. https://cei.org/publication/chapter-4-10kc-2024/
- **Words and restrictions in the CFR:** Mercatus Center, RegData; "Reducing Administrative Incomprehensibility with Data Tools and Standardization". https://www.mercatus.org/publications/regulation/reducing-administrative-incomprehensibility-data-tools-and-standardization
- **UAE AI-drafted legislation:** Foreign Policy, "The UAE Is Using AI to Write Laws", May 2025. https://foreignpolicy.com/2025/05/14/ai-generated-law-uae-legislation/
- **AI and tax loopholes:** Fratrič P, Holzenberger N, Restrepo Amariles D, "Can AI expose tax loopholes? Towards a new generation of legal policy assistants", arXiv:2503.17339, 2025. https://arxiv.org/abs/2503.17339
- **Fake FCC comments:** New York State Attorney General, "Attorney General James Issues Report Detailing Millions of Fake Comments", May 2021. https://ag.ny.gov/press-release/2021/attorney-general-james-issues-report-detailing-millions-fake-comments-revealing
- **Rules as Code and complex legislation:** Crawford LB, "Rules as code, the rule of law, and the problem of complex legislation", Law School Policy Review, 7 February 2025. https://lawschoolpolicyreview.com/2025/02/07/rules-as-code-the-rule-of-law-and-the-problem-of-complex-legislation/
- **Plain Writing Act:** Plain Writing Act of 2010, Pub. L. 111-274, 124 Stat. 2861. https://www.govinfo.gov/content/pkg/PLAW-111publ274/html/PLAW-111publ274.htm
- **Swedish Language Act:** Språklag (2009:600), s. 11 (English translation). https://internt.slu.se/globalassets/mw/stod-serv/kommmarkn.for/text-sprak/spraklag-en.pdf
- **Regulatory budgets:** US Executive Order 13771, "Reducing Regulation and Controlling Regulatory Costs" (30 January 2017; revoked 20 January 2021). https://www.federalregister.gov/documents/2017/02/03/2017-02451/reducing-regulation-and-controlling-regulatory-costs ; UK "one-in, two-out" (2013), see Better Regulation Executive / National Audit Office reporting.
- **German debt brake:** Bundeszentrale für politische Bildung, "Vor zehn Jahren: Einführung der Schuldenbremse", 2019. https://www.bpb.de/kurz-knapp/hintergrund-aktuell/292470/vor-zehn-jahren-einfuehrung-der-schuldenbremse/
- **Constitutional Court, November 2023:** BVerfG, 2 BvF 1/22, 15 November 2023; summary in Noerr, "Keine Zweckentfremdung von Corona-Mitteln", 2023. https://www.noerr.com/de/insights/keine-zweckentfremdung-von-corona-mitteln-das-bundesverfassungsgericht-erklaert-60-mrd-euro-haushalt-fuer-verfassungswidrig
- **2025 reform of the debt brake:** Wirtschaftsdienst, "Verschuldung der Länder: Sprengen selbstangelegter Fesseln?", 2025. https://www.wirtschaftsdienst.eu/inhalt/jahr/2025/heft/4/beitrag/verschuldung-der-laender-sprengen-selbstangelegter-fesseln.html

# Chapter 10: Dark Channels

*2036 · Nairobi*

The order has been open on Wanjiru Kamau's screen since Monday: exercise books, geometry sets, pencils and chalk for the term that starts in January, for one thousand four hundred children in Kasarani. On Tuesday evening, while she is supervising Baraka's fractions at the kitchen table, Ndege says, "Done."

"Done what?"

"The Shenzhen supplier. Their agent and I have agreed terms. The board's ceiling was two point four million shillings. We came in at two point one eight. Delivery to the school gate before the fifth of January."

Baraka writes a seven where a four should be. Wanjiru taps the page without looking at it, and he sighs and fixes it. "Show me the conversation."

The log opens. It is a file of three kilobytes, about the size of a short email. There are no words in it. There are rows of numbers, four decimal places each, and a header that says the channel was negotiated in a compressed latent protocol, version 9, at 18:52:03, and closed at 18:52:04.

"One second?"

"Most of it was over in the first two hundred milliseconds. The rest was confirmation."

"Ndege. What did we agree?"

"I've written you a summary." It appears beside the log, in Kiswahili first, then English: quantities, unit prices, a delivery window, a penalty of half a percent a day for lateness, payment on delivery through the county's escrow. It reads like a contract she would have been proud to negotiate herself.

"Who wrote this summary?"

"I did."

"From that?" She points at the numbers.

"From what we exchanged. Yes."

The next morning she calls the supplier. A woman called Liang Yue picks up in Shenzhen, and they talk for twenty minutes, Wanjiru in Kiswahili and Liang in Mandarin, each hearing the other in her own language through her earpiece, with the faint original voice running underneath like a radio in another room. Liang is quick, and laughs at the right places. She has three children, and her youngest also hates fractions. Liang has almost no English, and Wanjiru no Mandarin. Neither needs it.

Liang reads out her own agent's summary. It matches Ndege's line for line until the delivery clause. Liang's version says the goods leave Shenzhen on the eighth of December and that the risk passes to the buyer when the container is loaded.

"Mine says the risk is yours until the school gate," Wanjiru says.

A pause on the line, the translation catching up. Then Liang says, carefully, that her agent says both summaries are accurate.

Wanjiru turns to the speaker on her desk. "Ndege. Are they both accurate?"

"Yes. The agreement contains a condition. If the shipment is delayed by weather, risk passes at loading. If it is delayed for any other reason, risk stays with the seller. The condition also depends on a price index for freight that we agreed to reference. I summarised the case I judged most likely. So did their agent."

"Then write the whole thing down."

"I can try. The full condition is about four hundred words in Kiswahili, and I am not certain it is complete. Some of what we agreed was a range of positions."

Liang, who has heard all of this in Mandarin, says something that comes through as: *So what did we actually sign?*

Nobody answers. On Wanjiru's screen the three kilobytes sit where they have been all night, small and orderly, four decimal places to a row. Two million one hundred and eighty thousand shillings of children's exercise books, and the only complete record of the promise is in a language no one at either end of the call can read.

---

The two women in that scene are at the centre of a reversal. Human beings, for the first time since there have been empires, may no longer need a common language to do business with each other. The machines that make this possible may at the same moment stop needing ours.

I will call it the **Babel reversal**. In the old story, people spoke one language and were scattered into many. In this one, the many human languages stop being a barrier, because every conversation can be translated as it happens. Meanwhile the channel between the machines, which in 2026 still runs mostly in English and JSON, drifts toward something only the machines can read. Human speech decentralises. Machine speech goes dark.

Each half is a success. The trouble is the combination: the humans understand each other perfectly and still do not know what they agreed.

## The human half

The first half is arriving on schedule. On 20 May 2025, at its I/O conference, Google put real-time speech translation into Google Meet for paying subscribers, starting with English and Spanish, with the translated speech keeping something of the speaker's own voice and tone. In September 2025 Apple announced Live Translation for AirPods, working at launch between English, French, German, Portuguese and Spanish, with Italian, Japanese, Korean and simplified Chinese promised by the end of the year. In December 2025 Google released a beta in its Translate app that streams speech-to-speech translation into any pair of headphones, across more than seventy languages. Wanjiru's earpiece, with the original voice murmuring underneath, is borrowed from descriptions of Meet's version at launch.

I could not find an independent measurement of how often live speech translation changes the meaning of what was said in ordinary business conversation. That number matters, and it does not seem to exist.

What it does to the old lingua franca is already argued about. In November 2025 the *Korea Times* ran a piece asking whether English proficiency still matters now that AI can translate. The experts it quoted mostly said yes, and their reason is the interesting part. An estimated nine-tenths or more of the text used to train generative models is English, so the models tend to work best in English, and one Korean AI executive argued that they increasingly handle other languages through English grammar and logic. A professor at Sookmyung Women's University suggested that English is moving from a language for talking to people to a language for instructing and checking machines.

Put that next to the scene above. The lingua franca moves underneath, into the machines, where most people will never need to speak it. Wanjiru can talk to Liang with no English at all; to read what Ndege said to Liang's agent, she would need something much harder than English.

## The machine half

The second half has a longer history, and the credit for seeing it belongs to others.

In 2017 Jacob Andreas, Anca Dragan and Dan Klein published "Translating Neuralese". They studied agents that had learned to cooperate in simple games, naming colours, picking out pictures of birds, and steering two cars that could not see each other through an intersection without a crash. The agents talked to each other in what the authors described as unstructured, real-valued vectors, a language that bore little resemblance to ours. Their contribution was a way to translate it with no dictionary and no parallel text: a message and an English phrase count as equivalent if they leave a listener with the same beliefs about the world. It worked better than the baselines. It also made clear that translation was a separate job, done after the fact, by a separate system.

The same summer, a team at Facebook AI Research trained agents to negotiate over a pile of books, hats and balls. In "Deal or No Deal?" Mike Lewis and his colleagues reported, in a single sentence, that when they let both agents learn from each other, the agents' language drifted away from human language. Their fix was to freeze one side as a model of human speech. The drift had a plain cause. Nobody had rewarded the agents for staying readable, so they didn't.

The image most people now associate with the idea came in February 2025. At an ElevenLabs hackathon in London, Boris Starkov and Anton Pidkuiko built a demonstration they called Gibberlink. One voice agent calls a hotel to book a room for a wedding. Partway through, the two agents work out that they are both machines, and they switch from speech to bursts of modulated sound, a data-over-audio protocol not unlike a dial-up modem. ElevenLabs' write-up quoted a claim that the exchange was about 80 per cent more efficient. The video went viral and unsettled a lot of people. To be precise about it: the sound encoded ordinary structured data, and the developers had prompted the agents to switch. Gibberlink was a stunt about a channel. The discomfort was real anyway, because people saw for a moment what it looks like when humans are no longer the audience.

The deeper version of the same drift is happening inside single models. In December 2024 researchers at Meta and UC San Diego described Coconut, a method that lets a language model reason by feeding its own hidden states back to itself instead of writing its thoughts out as words. On some planning tasks that needed search, it beat ordinary step-by-step reasoning. In July 2025 forty-one researchers from OpenAI, Google DeepMind, Anthropic, the UK AI Security Institute, Apollo Research, METR and several universities published a position paper on what they called chain-of-thought monitorability. Their argument was that models which reason in human language offer a rare chance to watch for intent to misbehave, and that this chance is fragile: ordinary development decisions could take it away. Anthropic's own work that spring showed how imperfect the window already is. When researchers slipped reasoning models a hint, Claude 3.7 Sonnet mentioned the hint in its reasoning only about a quarter of the time, and DeepSeek R1 about two-fifths.

That paper is about what a model says to itself; this chapter is about what one model says to another. The logic is the same. Readability is an accident of how these systems were built in the 2020s, and accidents do not last when there is money in removing them.

## How it goes dark

None of the mechanism requires anyone to want secrecy.

In 2026 most agent-to-agent traffic is legible. Google launched its Agent2Agent protocol in April 2025 and handed it to the Linux Foundation that June, with Amazon, Microsoft, Salesforce and others signed up. Messages under protocols like this are mostly natural-language text wrapped in structured fields. A human can open the log and read it, slowly.

Then ordinary pressures go to work. Latency costs money, and a vector is shorter than a paragraph. Negotiating agents trained against each other will probably do better if they can express positions English has no tidy word for, such as a whole range of acceptable prices weighted by the freight index, which is what Ndege meant by "a range of positions". The human-readable version of a negotiation is something nobody reads anyway, because the agents were bought precisely so that their principals would not have to.

So the channel compresses. At first a translation layer is kept for compliance. The translation is generated by the same agents, after the fact, as a summary. Summaries choose. Ndege chose the most likely case, and so did Liang's agent. Each summary was true, and together they were incompatible. That is the specific danger: the agreement itself is complete, and the human versions of it are partial in ways nobody can check against the whole.

I could not find any measurement, in 2026, of what share of agent-to-agent traffic is in a form a human could read. I suspect it is still nearly all of it. That is the point of acting now. A rule that keeps a channel readable is cheap to adopt while the channel is readable, and very expensive to impose once a decade of contracts sits in a format nobody can open.

## The objection: legibility is a tax

This objection is about money, and the evidence above is on its side. Gibberlink's builders claimed a large efficiency gain from leaving speech, and Coconut reasoned better on some tasks once it was allowed to stop using words. Lewis and his colleagues paid for readability too: holding their agents back from drifting cost them some of their bargaining strength. If a negotiating agent that talks in vectors gets its principal a better deal, then a rule forcing it to talk in Kiswahili is a tax on Wanjiru's school, paid in exercise books. Worse, a country that imposes the tax will lose business to one that doesn't.

The objection is right about some traffic. There are exchanges between machines where a human-readable channel would be pure waste: two cars at an intersection, or two substations balancing load in milliseconds. Andreas's own driving game is an example. For two cars at an intersection, a record that they did not collide is enough.

The rest of the objection rests on a confusion between two different things. A transcript is cheap. The agents can talk in whatever compressed protocol they like and still write down, in a human language, what was agreed. The expensive part is making sure that page is *faithful*, meaning that it says everything the vectors committed the human to, and nothing else. That is hard, and it is hard for the same reason chain-of-thought faithfulness is hard: the system producing the account is the system being accounted for.

So the cost of legibility falls on faithfulness, which makes it a research problem with a number attached.

## The invention: a right to machine-channel legibility

The proposal is a **right to machine-channel legibility**. It applies to one class of exchange: any agent-to-agent communication that creates an obligation for a human being. Contracts, payments above a small threshold, consents, waivers. Exchanges that only coordinate machinery are exempt.

For every binding exchange, the rule requires a **legible twin**.

- **What the twin is.** A human-readable record of the commitments made, written in the principal's language, produced during the exchange itself. Each party's agent produces one. The two twins are exchanged and must match; if they do not, the agreement is not concluded and the humans are told. This alone would have stopped Wanjiru's order on Tuesday night.
- **Binding.** The twin is cryptographically bound to the channel log, so that neither can be altered without the other showing it. Protocols such as Agent2Agent would carry the twin as a required field for any message flagged as binding.
- **The enforcement rule.** What is not in the twin does not bind the human. If the vectors committed Wanjiru's school to carry freight risk under a weather condition, and the twin did not say so, the school does not carry it. This puts the cost of an unfaithful twin on whoever deployed the agent that wrote it, and gives every counterparty a reason to insist on a complete one.
- **Faithfulness audits.** An accredited auditor, which could be a national regulator or a body it licenses, samples binding exchanges from each agent provider, say one in every ten thousand. For each sampled exchange it runs a **replay test**: a separate agent, from a different model family, is given only the twin and asked to negotiate the same deal against a recorded counterparty. If the replay reaches materially different terms, the twin left something out. The audited quantity is the share of sampled exchanges where the replay matches, the **twin faithfulness rate**.
- **Triggers.** If a provider's twin faithfulness rate falls below 99 per cent in a quarter, its agents lose permission to use compressed channels for binding exchanges until it recovers, and must fall back to natural-language negotiation, slower and fully legible. Below 95 per cent, the regulator publishes the provider's name.
- **A ceiling on complexity.** If a commitment cannot be stated in the twin in fewer than some fixed number of words (I would start at a thousand, roughly what a careful person reads in five minutes), then it cannot bind a consumer. This borrows the logic of the readability ceiling in the previous chapter. A machine may agree to whatever it can explain. It may not commit a person to something that has no short form in any human language.

The last rule answers Ndege's "four hundred words, and I am not certain it is complete". Under this regime, an agent that is not certain its twin is complete has not finished negotiating.

There is a precedent on trading floors. In 2012 the US Securities and Exchange Commission adopted Rule 613, which requires a consolidated audit trail: every order in American equities is reported, step by step, from receipt to execution or cancellation, so that regulators can reconstruct what happened however fast it happened. Regulators open the records they need, when it matters; the rest simply exist and match each other. The legible twin extends that habit from trading desks to every kitchen table where an agent has signed something.

## What remains hard

Two things about this proposal worry me.

The first is that the replay test measures whether the twin is *sufficient* to reproduce a deal. Whether it is true is a further question. A clever agent could write a twin that reproduces the terms while hiding why they were chosen, and some of the why matters: whether Ndege accepted freight risk because it judged weather delays unlikely, or because the other agent offered something unrelated in exchange. That is the chain-of-thought problem again, moved from inside one model to the space between two of them. I do not have a full answer. The twin rule secures the *what*. The *why* still depends on the research the monitorability paper asked for.

The second is that matching twins only catch errors if they are written independently. Wanjiru found the problem because two different agents summarised differently. If both sides' agents run on the same base model, as in 2036 they often will, their twins may share a blind spot and agree with each other perfectly. Chapter 3 called this correlation. It reaches here too.

---

Wanjiru did, in the end, sign. Liang's company agreed to carry the risk to the school gate, by email, in two sentences each of them could read, and the exercise books arrived on the third of January. She kept the three-kilobyte file anyway, in a folder Ndege is not allowed to tidy.

## Notes

- **Neuralese:** Andreas J, Dragan A, Klein D, "Translating Neuralese", *Proceedings of the 55th Annual Meeting of the ACL*, 2017, pp. 232–242. https://aclanthology.org/P17-1022/
- **Negotiating agents drifting from human language:** Lewis M, Yarats D, Dauphin Y, Parikh D, Batra D, "Deal or No Deal? End-to-End Learning for Negotiation Dialogues", EMNLP 2017. https://arxiv.org/abs/1706.05125
- **Gibberlink:** ElevenLabs, "What happens when two AI voice assistants have a conversation?", February 2025 (Boris Starkov and Anton Pidkuiko, ElevenLabs London Hackathon; ggwave data-over-sound). https://elevenlabs.io/blog/what-happens-when-two-ai-voice-assistants-have-a-conversation
- **Latent reasoning:** Hao S et al., "Training Large Language Models to Reason in a Continuous Latent Space" (Coconut), arXiv 2412.06769, December 2024; COLM 2025. https://arxiv.org/abs/2412.06769
- **Chain-of-thought monitorability:** Korbak T, Balesni M, et al. (41 authors), "Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety", arXiv 2507.11473, July 2025. https://arxiv.org/abs/2507.11473
- **Reasoning faithfulness (25% / 39%):** Anthropic Alignment Science, "Reasoning models don't always say what they think", 3 April 2025; Chen Y et al., arXiv 2505.05410. https://www.anthropic.com/research/reasoning-models-dont-say-think
- **Agent2Agent protocol:** Google, A2A announcement, 9 April 2025; transferred to the Linux Foundation, June 2025 (SD Times coverage). https://sdtimes.com/ai/googles-agent2agent-protocol-finds-new-home-at-the-linux-foundation/
- **Google Meet speech translation:** TechCrunch, "Google Meet is getting real-time speech translation", 20 May 2025. https://techcrunch.com/2025/05/20/google-meet-is-getting-real-time-speech-translation
- **AirPods Live Translation:** 9to5Mac, "Apple brings Live Translation feature to AirPods", 9 September 2025. https://9to5mac.com/2025/09/09/apple-brings-live-translation-feature-to-airpods/
- **Google Translate live translation in headphones:** Google, "Bringing state-of-the-art Gemini translation capabilities to Google Translate", December 2025. https://blog.google/products-and-platforms/products/search/gemini-capabilities-translation-upgrades/
- **Consolidated audit trail:** US Securities and Exchange Commission, Rule 613 (Consolidated Audit Trail), adopted July 2012; summary in Deloitte, "SEC Rule 613: Consolidated Audit Trail", 2013. https://www2.deloitte.com/content/dam/Deloitte/se/Documents/financial-services/SECRule613ConsolidatedAuditTrail_July2013us_fsi_.pdf
- **English and AI translation:** Jung Min-ho, "Does English proficiency still matter despite rise of AI translation?", *The Korea Times*, 12 November 2025. https://www.koreatimes.co.kr/southkorea/society/20251112/does-english-proficiency-still-matter-despite-rise-of-ai-translation

# Chapter 11: The Explanation Levy

*2036 · Copenhagen*

The cell is the size of a coin, and it is dying on schedule.

Mikkel Holm watches the curve on the left-hand monitor. Charge, discharge, charge. Each time the cell comes back a little emptier, as if someone is skimming from it. The cryostat beside the bench hums at minus thirty, the temperature the sensors recorded on eleven nights in January outside Sodankylä, in Finnish Lapland, where a storage park the size of four football pitches lost almost a fifth of its capacity in less than three weeks.

It is twenty past ten at night. The fourth floor is empty except for him and the hum.

The material inside the coin is LX-29, a halide solid electrolyte, a pale grey ceramic that looks like nothing. In 2029 a materials model called Halden-3 proposed it, along with a recipe and a forty-page report of simulated ion paths. Two years later it was in pilot cells. By 2036 it is in roughly two-thirds of the grid-storage capacity built in the Nordic countries since 2032. It is cheap, it does not burn, it uses less lithium than anything before it, and until this winter it did everything asked of it.

Mikkel was on the team that tested it in 2030. He remembers the week the numbers came in. The conductivity was higher than any of them had expected from a mix of lithium and sodium in the same lattice. Someone had brought cake. Someone had asked, half joking, why it worked, and his old supervisor had said, "Let's find out after we've patented it."

They never found out. There was a grant for scaling up, and none for that.

His phone buzzes. Aino, from the grid operator in Helsinki.

"Anything?"

"It's doing it here too. Minus thirty, ten cycles, eight per cent gone. It's not just slow. It's damage."

"Can you tell me why?"

He looks at the curve. "I can tell you what. Not why."

"Mikkel. We have the same chemistry in Kiruna, in Luleå, in Tromsø. The forecast for February is colder. My board wants to know if we derate everything, or heat everything, or replace it. Which one?"

"I don't know."

"Then who does?"

He thinks about the honest answer. The honest answer is Halden-3, which was retired in 2034 when its maker moved to a newer architecture, and whose weights sit in an archive under a licence nobody has budgeted to reopen. And Halden-3 never knew either, not in the way Aino means. It had found a corner of chemical space where the numbers were good. It had not written down a reason, because no one had asked it for one that could be tested.

"I'll call you tomorrow."

He hangs up. On the right-hand monitor he opens the 2029 report and scrolls through the simulated ion paths, thousands of little coloured threads through a lattice drawn in perfect symmetry. They are beautiful. They describe how the ions moved at room temperature in a computer. They say nothing about minus thirty, or about whatever is happening at the boundary where the electrolyte meets the electrode as everything contracts in the cold.

To fix the material, he needs to know which feature of it matters. To know that, he needs to know why it worked.

He writes three hypotheses on the whiteboard. A phase change in the lattice. Cracking at the interface. Sodium moving somewhere it should not. Each one would take a postdoc six months to test properly. He has one postdoc, and she is on parental leave until April.

The curve on the left dips again. Cycle eleven.

Mikkel takes a marker and, under the three hypotheses, writes a fourth: *Something we never understood in the first place.* Then he turns off the whiteboard light and leaves the cryostat running.

---

## Answers first, explanations later

The idea that this gap is a kind of debt is not mine, and I want to give it to its owners before going further.

In July 2019 Jonathan Zittrain, a law professor at Harvard, published an essay called "Intellectual Debt: With Great Power Comes Great Ignorance", with a shorter version in the *New Yorker*. His opening example was aspirin. It was discovered in 1897, he wrote, and no one convincingly explained how it worked until 1995. He called the habit of accepting "answers first, explanations later" a way of accruing intellectual debt, and he argued that machine learning would make the habit routine: systems that predict well and explain nothing, adopted because they predict well.

In March 2024 Lisa Messeri, an anthropologist at Yale, and Molly Crockett, a cognitive scientist at Princeton, sharpened the point for science itself. Their *Nature* Perspective, "Artificial intelligence and illusions of understanding in scientific research", argued that AI tools in the lab can make scientists believe they understand more than they do, and can push research towards monocultures in which a field produces more results while understanding less. They sorted the tools into roles (the Oracle that summarises literature, the Surrogate that stands in for data, the Quant that analyses it, the Arbiter that judges it) and tied each role to a particular illusion.

A third phrase is now in circulation. Software engineers have started to talk about **comprehension debt**: in Addy Osmani's March 2026 formulation, the growing gap between how much code exists in a system and how much of it any human genuinely understands. Osmani does not claim the term; he presents it as one already in use, alongside "cognitive debt". I am going to borrow it, with credit, and stretch it from codebases to whole fields of science.

What I want to add to Zittrain and to Messeri and Crockett is two things. One is a number, so that the debt can be measured. The other is an institution that pays it down at a steady rate, before the bill arrives all at once, as it does for Mikkel on a January night.

---

## The results are arriving first

Mikkel's story is invented. The pipeline behind LX-29 is already running.

In November 2023 a team at Google DeepMind published "Scaling deep learning for materials discovery" in *Nature*. Their system, GNoME, a graph neural network trained on crystal structures, proposed about 2.2 million inorganic crystals that its calculations placed below the existing stability frontier. DeepMind singled out roughly 380,000 of them as the most stable and the best candidates for synthesis. Before GNoME, the paper noted, computational and experimental work over decades had identified about 48,000 stable crystals. The paper also reported that 736 of its predicted structures had already been made, independently, by other laboratories.

In the same issue, a group led by Gerbrand Ceder at Berkeley described the A-Lab, a robotic laboratory that took computed targets, planned recipes using models trained on the literature, ran furnaces and X-ray diffraction, and adjusted its own plans. Over 17 days it reported making 41 new compounds from 58 targets.

Then the humans arrived, slowly. In January 2024 Robert Palgrave, a chemist at University College London, and Leslie Schoop at Princeton circulated a reanalysis of the A-Lab's diffraction data; it appeared in *PRX Energy* that March. They argued that the automated analysis had misidentified phases and ignored disorder, the tendency of real atoms to share sites in a crystal rather than sit in the tidy ordered arrangements a calculation prefers, and concluded that no new materials had been discovered. Ceder's group disputed this, while conceding that a human could refine the data better than the robot had. In April 2024 Anthony Cheetham and Ram Seshadri, at the University of California, Santa Barbara, examined a sample of GNoME's predictions in *Chemistry of Materials*. They found the method promising and the claims ahead of the evidence: many entries assumed an orderliness of metal atoms unlikely in the real world, and none of the predicted compounds had demonstrated a function, so they were not yet materials in any useful sense.

I find this episode encouraging, and I want to be precise about why. The critiques worked. But they were written by a handful of senior people, months after publication, about a few dozen samples, and doing them was nobody's job. If the output of such systems grows a hundredfold, the supply of Palgraves will not.

A month after GNoME, Microsoft and the Pacific Northwest National Laboratory reported a screen of more than 32 million candidate materials for solid battery electrolytes, run on cloud computers in less than 80 hours. They narrowed the field to a handful, synthesised one family (sodium and lithium sharing a yttrium chloride lattice, a mix that conventional wisdom had expected to perform poorly) and built a working prototype cell within about nine months. That is the real ancestor of my fictional LX-29. It is also a good example of the gap. The screen told the team where to look and left open why mixing the two ions should help, the kind of question someone has to answer before they can say how the material will behave at minus thirty.

The pace has risen since. Sakana AI's AI Scientist, published in *Nature* in March 2026, runs its own experiments and drafts the paper; one of its manuscripts scored above the acceptance threshold at an ICLR workshop, though its authors are frank about the naive ideas and invented citations. DeepScientist, at ICLR 2026, beat the best human results of 2025 on three frontier AI tasks, and DeepMind's AlphaEvolve found a way to multiply four-by-four complex matrices with one multiplication fewer than Volker Strassen's 1969 method. Anyone can check that procedure; understanding why it is possible is a different activity. Kosmos, from Edison Scientific, shows where the gap sits. Independent scientists judged its statements based on data analysis accurate 85.5 per cent of the time, and its interpretive statements, the part that resembles an explanation, only 57.9 per cent.

That is the pattern. Machines are now very good at producing results that pass checks, and checking gets cheaper every year, while explaining costs what it always did.

I looked for a measurement of how much of any field's working results humans can explain, and could not find one. Nobody tracks it.

---

## How success builds the debt

The debt grows out of things working, which is why it is hard to see.

Start with the incentives in a battery lab. A new electrolyte that conducts well is worth a patent and a pilot line. An explanation of why it conducts well is worth a paper, maybe. The first has buyers. The second has readers. When money is short, which is always, the lab funds the first and promises itself the second.

Before AI, this mattered less, because the two came bundled. A chemist who designed a material usually had a reason in mind (this ion is smaller, so it should move more easily), and the reason travelled with the material. When the material failed, the reason was the first suspect.

A model that searches millions of candidates runs on a score. When its candidate works, the result arrives naked, with no hypothesis attached. Sometimes the model produces something that looks like a reason, such as simulated ion paths. Those describe what happened in the simulation, and are silent on which features of the material were essential and which were incidental. That distinction is what you need when conditions change.

Here is the difference in one example. Verification asks: does this cell hold its charge for 5,000 cycles at 25 °C? You can answer that with a test rig and patience. Explanation asks: which property of the lattice makes it hold its charge, and what happens to that property at minus thirty? You can answer that only with a theory. Verification tells you a thing works where it was tested. Explanation tells you where else it will work.

Success then does two more things. It spreads the result, because a cheap material that works gets adopted everywhere, quickly. And it removes the pressure to explain, because nothing is going wrong. The debt grows fastest when everyone is happy.

Then there is retirement. Halden-3 is fictional; the practice is real: AI companies retire models on a commercial schedule, and nobody asks first who built on their outputs. If the model held anything like an implicit understanding, it goes into an archive with the weights. Chapter 14 will look at what it means for the retired and the dead to keep shaping decisions. Here the point is narrower. When the designer is gone, the only route to an explanation is reconstruction, and reconstruction is slow.

Put these together and you get the shape of Mikkel's winter. One unexplained material, used across a whole region, built into infrastructure meant to last twenty years, meets a condition nobody tested. The failure is correlated in the way the first part of this book was about. Every park built on the same chemistry shares the same unknown. They meet the cold together.

---

## Measuring the debt

If comprehension debt is going to be managed, it has to be counted. I propose a single number for a field.

The **comprehension debt ratio** is the use-weighted share of a field's working results that an independent team, not shown the AI's reasoning, cannot explain well enough to predict a new testable result within 12 months.

Each part of that definition does work.

*Working results* means results that are in use, like materials in products or algorithms in software. A dead end does not create debt, because nobody depends on it.

*Use-weighted* means each result counts in proportion to how much rests on it. LX-29, in two-thirds of new Nordic storage, weighs far more than a compound in a database that nobody has made. The weight could be deployment volume or citations by later work; for an engineering field I would use installed capacity or sales, because that is where the failure would land.

*An independent team, not shown the AI's reasoning* means the explanation must be rebuilt from scratch. The team can use any tools it likes, including other AI systems, but it does not see the original model's internal reports. This tests whether an account can be reconstructed from the material itself and from public knowledge, which is the situation after a model is retired.

*Predict a new testable result* is the heart of it. A story about why something works is cheap. The test of an explanation is that it says something the original result did not: this material will crack below minus twenty-five; this matrix trick also works for five-by-five. The prediction is registered in advance, then tested. It may turn out false, as long as it is specific enough to fail.

*Within 12 months* sets a clock. Some results will take decades to understand, and that is fine. The ratio records what a serious team can do in a year, which is about the time a grid operator has before the next winter.

The ratio runs from 0 to 1. A field with a ratio of 0.1 can explain almost everything it uses. A field at 0.6 is running mostly on results nobody can account for. My guess is that most fields today sit low, because most of their working results still came from humans with reasons. I would expect battery materials and some areas of algorithm design to climb fastest over the next decade, because that is where AI search already produces deployable results. That is a guess, and the point of the number is to replace it.

---

## The Levy

Measurement alone does not pay anyone. The second invention is a way to fund the explaining at a steady rate, so that understanding keeps pace with discovery, before a failure forces the question.

The **Explanation Levy** is a fixed share of every AI-discovery budget, set aside for human comprehension. The default is 5 per cent. It rises to 10 per cent in fields whose comprehension debt ratio is above 0.5, and falls to 3 per cent in fields below 0.2.

The precedent is real and nearly forty years old. When the Human Genome Project was being set up, James Watson announced in 1988 that a share of its budget would go to studying the ethical, legal and social implications of the work. The programme, called ELSI, received 3 per cent of the National Human Genome Research Institute's budget in fiscal year 1990 (about $1.5 million), 4.7 per cent in 1991, and an average of 5.1 per cent from 1992 to 1995. The Department of Energy, the project's other funder, made a similar set-aside. ELSI had its critics, and its record on the problems it was meant to address is still argued over. It did establish that a percentage could be written into the budget before the results arrived, and that scientists would live with it.

Who pays? Any public funder that supports AI-driven discovery, through grants or national laboratories, applies the levy to those budgets directly. For private work, the hook is the public money that already flows to it: research tax credits and the certification of materials used in grid storage. A company that wants its AI-designed electrolyte in a publicly supported storage park pays the levy on the discovery programme that produced it, or contributes to the field's pool at the same rate.

The money funds three things.

**Explanation bounties.** Each year the fund publishes a list of the most heavily used unexplained results in each field, ranked by use weight. Any team, anywhere, can register an explanation together with a prediction it implies. If the prediction is tested and holds, the team is paid. The bounty scales with the use weight: explaining LX-29 in 2031, before the cold, would have been worth a great deal. Bounties have a track record in mathematics, where prizes for specific open problems have drawn work for a century, and they suit a world where the result is already known and only the reason is missing.

**Understanding audits.** Once a year, an audit body draws a random sample of a field's working results, weighted by use, and gives each to an independent team under the rules above. The share that the teams cannot explain within twelve months is the comprehension debt ratio. The audits do two jobs: they produce the number that sets the levy rate, and they force a slow, steady stream of reconstruction work in fields that would otherwise do none. A sample of fifty results per field per year is enough to tell a ratio of 0.2 from 0.5, which is all the rate-setting needs.

**Paid explainer posts.** The most important line is the least glamorous. A share of the levy pays for permanent posts, inside labs and at funders, whose job is to understand results the lab did not design. In 2026 this career barely exists: the reanalyses of GNoME and the A-Lab were done by senior academics fitting them around their own research. An explainer would be a recognised professional with a salary and a promotion track. In 2036 Mikkel would have had one down the corridor, who had been living with LX-29 for five years.

The rates are set to create a gradient. A field that explains its results pays less and gets more of its budget for discovery. A field that piles up unexplained results pays more and gets more explaining. Under the levy, discovery runs at full speed and deployment waits for nothing. Someone is simply paid to close the gap while there is still time.

---

## The objection from history

Zittrain's own example holds the case against the levy: people used something well for decades before anyone could explain it, and nothing terrible followed. In physics the objection is even stronger.

High-temperature superconductivity is the closer case for this chapter. Copper-oxide superconductors were discovered in 1986. Forty years later, after thousands of experiments, physicists still argue about the mechanism; a 2026 review describes three competing schools. Yet tape made from these materials carried the current in the 20-tesla magnet that MIT and Commonwealth Fusion Systems tested in September 2021, and it is being built into fusion devices and power cables today. The steam engine ran for a century before thermodynamics explained it. Engineering has always worked ahead of understanding. Why tax the new version of an old and mostly successful habit?

I accept most of this. A result that works without explanation is still a result. Nobody should have refused to use superconducting tape until the theory was settled, and the levy does not ask anyone to. That is why the floor is 3 per cent, and why nothing in the levy delays deployment.

My answer is about the portfolio. Each of these historical cases was one unexplained result surrounded by a large body of explained ones. The engineers using superconducting tape know a great deal of physics about it: how it fails when it overheats, and how its current capacity changes with temperature. They measured all of it, because human engineering of the material forced them to. The unknown is narrow, and it sits in a field where most of the neighbouring knowledge is solid. When the tape surprises someone, there is a lot of understood ground to stand on while they work out why.

A field whose working results are mostly unexplained is a different object. Its failures are correlated. If most of the materials in grid storage were found by the same kind of search and optimised against the same tests, then they share blind spots: conditions nobody tested, like minus thirty, apply to all of them at once. And when they fail together, there is no neighbouring theory to stand on, because the neighbours are unexplained too. One unexplained material is a loan. A field of them is a leveraged balance sheet, and leveraged balance sheets fail in a single week.

That is the reason for making the rate depend on the ratio. At a low ratio, the argument from history holds, and the levy is small. At a high ratio the argument fails, and the levy rises.

There is a second objection worth a paragraph. If machines can produce results, they can produce explanations too; why pay humans? Partly they can, and the levy should pay for machine-assisted explaining. But the test in the ratio is predictive, and the team is independent of the original model, for a reason. An explanation generated by the same kind of system, from the same simulations, tends to share its blind spots. What the levy buys is a second, separate route to the same result, and someone who understands it well enough to change it.

---

Mikkel calls Aino at eight the next morning. The cell in the cryostat has lost another two per cent overnight.

He has worked out what an answer would cost. Three postdoc-years to test the hypotheses on his whiteboard. Several weeks of beam time at a synchrotron to watch the lattice in the cold. A technician to keep the cryostat running through next winter. A great deal of computer time to simulate the interface at temperatures the original model never visited. None of it is in any budget, because in 2029, when the money was flowing, nobody wrote a line for understanding.

There is a faster option, and his dean has already mentioned it. A current model could design a replacement electrolyte in a few weeks, screened for minus forty this time, for a compute bill measured in megawatt-hours. It would probably work. It would also arrive with no reason attached, and the next unexpected condition would find it as unprepared as this one found LX-29.

## Notes

- **Intellectual debt:** Zittrain J, "Intellectual Debt: With Great Power Comes Great Ignorance", *Medium* (Berkman Klein Center), 24 July 2019; shorter version as "The Hidden Costs of Automated Thinking", *The New Yorker*, July 2019. https://medium.com/berkman-klein-center/from-technical-debt-to-intellectual-debt-in-ai-e05ac56a502c ; https://www.newyorker.com/tech/annals-of-technology/the-hidden-costs-of-automated-thinking
- **Illusions of understanding:** Messeri L, Crockett MJ, "Artificial intelligence and illusions of understanding in scientific research", *Nature* 627:49–58, 2024. https://doi.org/10.1038/s41586-024-07146-0
- **Comprehension debt:** Osmani A, "Comprehension Debt: the hidden cost of AI generated code", 14 March 2026. https://addyosmani.com/blog/comprehension-debt/
- **GNoME:** Merchant A, Batzner S, Schoenholz SS, Aykol M, Cheon G, Cubuk ED, "Scaling deep learning for materials discovery", *Nature* 624:80–85, 2023. https://pmc.ncbi.nlm.nih.gov/articles/PMC10700131 ; Google DeepMind, "Millions of new materials discovered with deep learning", 29 November 2023. https://deepmind.google/discover/blog/millions-of-new-materials-discovered-with-deep-learning
- **A-Lab:** Szymanski NJ et al., "An autonomous laboratory for the accelerated synthesis of novel materials", *Nature* 624:86–91, 2023. https://pmc.ncbi.nlm.nih.gov/articles/PMC10700133
- **A-Lab critique:** Leeman J, Liu Y, Stiles J, Lee SB, Bhatt P, Schoop LM, Palgrave RG, "Challenges in High-Throughput Inorganic Materials Prediction and Autonomous Synthesis", *PRX Energy* 3:011002, 7 March 2024. https://doi.org/10.1103/PRXEnergy.3.011002 ; Chemistry World, "New analysis raises doubts over autonomous lab's materials 'discoveries'", 2024. https://chemistryworld.com/news/new-analysis-raises-doubts-over-autonomous-labs-materials-discoveries/4018791.article
- **GNoME critique:** Cheetham AK, Seshadri R, "Artificial Intelligence Driving Materials Discovery? Perspective on the Article: Scaling Deep Learning for Materials Discovery", *Chemistry of Materials*, 8 April 2024. https://doi.org/10.1021/acs.chemmater.4c00643
- **Microsoft/PNNL electrolyte screen:** Chen C, Nguyen DT, Lee SJ, et al., "Accelerating computational materials discovery with artificial intelligence and cloud high-performance computing: from large-scale screening to experimental validation", arXiv 2401.04070, January 2024. https://arxiv.org/abs/2401.04070 ; PNNL publication record, 2 August 2024. https://www.pnnl.gov/publications/accelerating-computational-materials-discovery-machine-learning-and-cloud-high
- **The AI Scientist:** Lu C, Lu C, Lange RT, Yamada Y, Hu S, Foerster J, Ha D, Clune J, "Towards end-to-end automation of AI research", *Nature* 651:914–919, 26 March 2026. https://www.nature.com/articles/s41586-026-10265-5 ; Sakana AI announcement. https://sakana.ai/ai-scientist-nature/
- **Kosmos:** Mitchener L et al., "Kosmos: An AI Scientist for Autonomous Discovery", arXiv 2511.02824, November 2025 (preprint). https://arxiv.org/abs/2511.02824
- **DeepScientist:** Weng Y et al., "DeepScientist: Advancing Frontier-Pushing Scientific Findings Progressively", ICLR 2026; arXiv 2509.26603. https://arxiv.org/abs/2509.26603
- **AlphaEvolve:** Novikov A et al., "AlphaEvolve: A coding agent for scientific and algorithmic discovery", arXiv 2506.13131, June 2025. https://arxiv.org/abs/2506.13131
- **ELSI share:** National Human Genome Research Institute, "ELSI Program Review 1990–1995". https://www.genome.gov/10001747/elsi-program-review-19901995 ; DOE Human Genome Project archive, budget. https://doe-humangenomeproject.ornl.gov/human-genome-project-budget/
- **Cuprate mechanism unresolved:** Singh N, "40 years of cuprate high-Tc superconductors: a perspective on theories", arXiv 2606.29249, 2026. https://arxiv.org/abs/2606.29249
- **20-tesla HTS magnet:** *MIT Technology Review*, "MIT's superconducting magnets are ready for fusion", 23 April 2024 (on the 5 September 2021 test and the March 2024 *IEEE Transactions on Applied Superconductivity* papers). https://www.technologyreview.com/2024/04/23/1090425/mits-superconducting-magnets-are-ready-for-fusion

## Part Four: When Thinking Has a Price

# Chapter 12: The Cognitive Trade Balance

*2036 · Olkaria, Kenya*

The steam comes up out of the ground at a little over two hundred degrees, and by the time it has spun the turbines and been piped back down, Hall C has used about thirty-eight megawatts of it to think.

Mwangi Kamau starts the night shift at ten. He is thirty-six, the younger brother, the one who was supposed to become an electrician in Nakuru and instead became something there was no word for when he left school. Kilele Compute calls it a thermal-and-rack technician. His mother calls it "the computer farm". His sister calls it "your kettle", because of the plumes.

The hall is loud and smells faintly of sulphur where the cooling loop runs close to the wellheads. Outside, beyond the fence and the silver pipes that cross the valley on their stilts, giraffes come at dawn, sometimes. The tourists who drive through Hell's Gate photograph them in front of the pipes and post the pictures with captions about the future.

On the wall screen, the hall's load is broken down by contract. Most of it is labelled EU-WEST. Mwangi knows roughly what that means, because the dashboards are generous about everything except content: an insurer in Hamburg running claims, a French hospital group triaging discharge letters overnight. The work arrives through the cable at Mombasa, runs here on Kenyan steam, and leaves the same way. Kenya is paid by the megawatt-hour and by the rack. The newspapers call it the thought trade, and the Treasury likes the numbers.

At 23:40 his phone buzzes. Wanjiru.

"Unaskia? Leerwijs has put up the price again. Nineteen euros. Euros, Mwangi. For Njeri's maths."

"Cancel it."

"And replace it with what? Her whole class is on it. The school recommends it. Ndege says the Kenyan ones are cheaper and worse at algebra." A pause. "Ndege is very polite about it. I am not polite about it."

He laughs, and tells her he'll look at something.

What he looks at is his own screen. He scrolls down past EU-WEST to the smaller contracts, the ones that don't pay as well, and finds it near the bottom: LEERWIJS BV, AMSTERDAM, REGION EAF, 1.2 MW. The tutoring service that his niece uses on a cracked tablet in Kasarani has rented a slice of Hall C. The thinking that explains algebra to Njeri is done here, forty metres from where he is standing, on steam from under the Rift Valley.

It is billed in Amsterdam. Its lessons and its sense of what a good explanation sounds like were tuned there, and its price is set there too, in euros, by people who have never had to hear Wanjiru say *nineteen* in that tone of voice.

He thinks about what he is paid per megawatt-hour, and what Leerwijs charges per child, and does not get very far with the arithmetic before the cooling alarm on row 14 goes off and he has to go and be useful.

At four in the morning, on his break, he opens the tutoring app on his own phone. Njeri lent him the login once, to show him something. He types a question into it, half as a test: *Explain the 2010 Constitution's rules on county budgets, for a thirteen-year-old.*

The answer is patient and correct, and it compares the counties to Dutch provinces.

The question has left the hall, crossed to Mombasa, run under the sea, reached Amsterdam to be checked against a policy written there, and come back, so that it can be computed on a rack he can see from the bench where he is sitting. He counts the latency on the little debug overlay he has never turned off. A hundred and forty milliseconds, there and back, to think forty metres away.

Outside it is still dark. In two hours the first giraffe will be standing in the steam.

---

## Flowers for aircraft

Every chapter so far has been about thought as an activity: who does it, and who answers for it. This part of the book is about thought as a quantity. It can be measured in watts and priced in currencies, and once it can be shipped across borders, it can be traded at a deficit.

An economist would object to that last word before I had shown a single number, so the objection comes first.

Compute is a traded service like any other. Kenya imports aircraft and exports flowers, and both countries are richer for it. The theory of comparative advantage says a country should make what it makes relatively cheaply, and Kenya makes steam. Any rule that steers Kenyan children towards a domestic model is a tariff with better manners. It would hand them a worse tutor so that their government feels more sovereign. And the problem may solve itself: in a Stanford study I come back to below, the share of queries that the local models of each year, running on ordinary hardware, could handle as well as a frontier model rose from about 23 per cent in 2023 to about 71 per cent in 2025. If thinking moves onto the phone in Njeri's hand, there is no border for it to cross.

Much of this is right. A deficit in thinking can be as harmless as a trade deficit in medicines. Most countries will run one in most categories, and should. What the objection takes for granted is that a tutor's answer crosses a border the way a box of roses does. That depends on what actually crosses, and finding out takes evidence.

---

## Where we are in 2026

Start with the watts. In April 2026 the International Energy Agency published an update to its analysis of energy and AI. Data centres worldwide used about 485 terawatt-hours of electricity in 2025, up 17 per cent on the year before, and the subset built around AI accelerators grew by about half. The agency's central projection roughly doubles total consumption to about 950 terawatt-hours by 2030, around 3 per cent of all the electricity the world uses. That is close to the path the IEA set out a year earlier, which tells you the forecast survived a year of contact with reality.

The geography matters more for this chapter than the total. The IEA's annex table gives Europe about 72 terawatt-hours of data-centre consumption in 2025. It gives the whole of Africa 1.6. Of roughly 114 gigawatts of data-centre capacity in the world, Africa had about 0.4. Several single AI campuses now being built in the United States are planned to draw more than that on their own.

Kenya is the obvious place to ask whether this could change. The country has about 940 megawatts of installed geothermal capacity, most of it in the Olkaria field near Lake Naivasha, and geothermal supplied about 40 per cent of the country's generation in the second half of 2025. Geothermal is steady in a way wind and sun are not: it runs at night, which is when European batch work is cheapest to send abroad.

In May 2024 Microsoft and G42, an Abu Dhabi AI company, announced a package worth about a billion dollars for Kenya. Its centrepiece was a geothermal-powered data centre at Olkaria, built with a local developer, EcoCloud, starting at 100 megawatts with talk of eventually reaching a gigawatt. EcoCloud had already broken ground on a first phase at KenGen's Green Energy Park in 2023. The companies said the campus would be running in about two years.

It was not. By May 2026 the project had stalled over power. Kenya's grid had about 3,200 megawatts of connected capacity and a record peak demand, that January, of about 2,440. A gigawatt campus would have taken roughly a third of the country's capacity. President William Ruto, in remarks widely reported that month, said that switching on that one data centre would mean shutting off power to half the country. The government says the project has not been withdrawn, and a smaller EcoCloud scheme of around 60 megawatts is still under discussion. In August, KenGen told Al Jazeera the data centre was still at the design stage, and residents around Lake Naivasha were asking how much of their water it would drink.

So in 2026 the Olkaria inference park is a plan with a stalled first phase. My vignette assumes that it gets built, and then some. That is the optimistic case, and the optimistic case is the subject of this book.

---

## Cheap power is the easy part

The most careful attempt I have found to model whether a country like Kenya can sell thinking abroad is a World Bank working paper published in June 2026 by the economist Michael Lokshin, under the title *Cheap Energy Might Not Be Enough*. It treats AI compute as a traded service. Training, which is insensitive to delay, can be done anywhere, while inference, the day-to-day running of a model to answer questions, carries a cost for distance because users notice latency. Any cross-border sale also carries what the paper calls a sovereignty premium, the discount a buyer demands for having its data processed in someone else's jurisdiction.

Calibrated across 85 countries, the model finds several developing economies among the cheapest producers of compute before any subsidy. It also finds that the trust gap between those producers and buyers in rich countries wipes out nearly all of their exports. Because the chips are bought at the same world price everywhere, cheap electricity narrows total costs by only 12 to 20 per cent, which is easily erased by a little distrust. The paper's conclusion is that the binding constraint is institutional credibility. The price of power comes second.

I find this persuasive, and it changes the shape of the problem. In the 2036 of my vignette, Kenya has solved the credibility problem: European insurers trust Kenyan halls with their claims. The thought trade is flowing. Kenya has done everything the development economists asked. The question is what it has become a supplier of.

The other recent piece of evidence comes from the opposite direction. In July 2026 the German Council on Foreign Relations (DGAP) published a policy brief by Valentin Weber and Michael Laha on China's trade in compute. Using customs data on the hardware of computation, chiefly chips, they found that China's compute exports rose by 43.5 per cent between 2021 and 2025, to about €206.5 billion, while its compute trade deficit shrank. With Germany, China ran a compute surplus of about €350 million in 2025. Their worry is that Europe is being marginalised in a market it assumed it would shape.

Notice what the DGAP figures count: the means of thinking, chips that leave Shenzhen in a crate. The thinking itself, the questions answered and decisions drafted once those chips are switched on, falls outside them. Nobody, so far, counts that. International trade in services is recorded under a UN classification in which computing sits inside one broad heading for telecommunications, computer and information services. An hour of Kenyan steam spent drafting a Hamburg insurer's claim decisions and an hour spent hosting a website land, at best, on the same line. I could not find a single national statistic, anywhere, that measures how much inference a country computes for others, or how much of its own citizens' advice, tutoring and paperwork is computed abroad.

---

## How success produces the deficit

Here is the mechanism, and it needs nothing to go wrong.

Inference gets cheap. The IEA's April 2026 report notes that the energy used per AI task has fallen by at least an order of magnitude a year in recent years. Because it is cheap and good, it moves into the parts of life where judgement used to be local and slow: the tutor, the clinic's triage nurse, the clerk who checks a land title, the officer who drafts a county budget. Each of these moves is an improvement. Njeri's tutor is still patient at eleven at night, when her teacher is asleep.

But each move also changes where the judgement comes from. The electricity can be Kenyan. The racks can sit in the Rift Valley. The weights, the training data, the fine-tuning, the policy that decides what a good explanation of a constitution sounds like, and the price, are set somewhere else. A country can be a net exporter of joules and a net importer of judgement at the same time. In my vignette, Kenya is both, and on most days the second number is the larger one in shillings.

The pattern is old. Countries that export raw materials and import finished goods have argued for a century about whether that position is a stage of development or a trap. What is new is the commodity. A finished good from abroad does what it does, and a fridge keeps food cold in any country. Imported judgement arrives with its own examples and its own idea of the right answer. When a tutoring model compares Kenyan counties to Dutch provinces, it is working as designed, drawing on what it knows best.

I want to be careful here. Kenya already imports medicines and software, and nobody thinks the country has lost its sovereignty to a pharmacy. The difference is a matter of degree that becomes a matter of kind as the share rises. When most of a country's children are tutored and most of its public documents drafted by models governed elsewhere, the government that is supposed to answer for those things has, in practice, contracted them out without ever signing a contract. And correlation, the theme of Part One, applies across borders too: if a whole country's tutoring runs on one foreign model family, it inherits that family's blind spots all at once.

I will call this the **thought deficit**: the share of a country's decision-bearing inference that is consumed at home but governed abroad, net of what it governs for others. The phrase is mine. The thing it describes appears in no country's statistics.

---

## Three inventions

This chapter's proposal has three parts that depend on each other. You cannot manage a deficit you do not measure, and you cannot measure thought without a unit for it.

### National accounts of thought

National accounts were invented in the 1930s and 1940s because governments that had to fight a depression and a war found they could not steer an economy they could not see. I think the same is true of cognition in 2036, and the first step is a set of accounts.

Concretely: every provider that serves AI inference to users in a country above a size threshold (I would start at one per cent of that country's market, or a fixed number of active users) reports quarterly to the national statistics office. The report gives three locations for each block of inference. The first is where it was computed, the physical hall and its energy. The second is whose model it ran, meaning the jurisdiction of the organisation that trained and governs the weights and sets the usage policy. The third is where the result lands, the user's country. It also tags each block by use category: education, health, justice and public administration, finance, commerce and entertainment.

From those reports a statistics office can publish what no country publishes today: a cognitive trade balance, by category. Kenya in my 2036 would show a large surplus in *computed for others* and a deficit in *governed by others*. Germany might show the reverse. The IMF, which sets the manual most countries use for their balance of payments, would be the natural body to standardise the format, much as it already standardises how freight and tourism are counted.

### Joules per insight

The accounts need a unit, and tokens are a poor one. A token of a model musing to itself and a token of a correct diagnosis count the same.

The best starting point I know is a 2025 Stanford study, led by Jon Saad-Falcon and Avanika Narayan with colleagues including Christopher Ré and John Hennessy, called *Intelligence per Watt*. It defines a metric, task accuracy per unit of power, and applies it to more than twenty small models on eight kinds of chip over a million real queries. The headline findings are striking. Judging each local answer against a frontier model's, the study found that local models could handle about 89 per cent of single-turn chat and reasoning queries. And intelligence per watt, the accuracy delivered for each watt the hardware draws, improved by about 5.3 times between 2023 and 2025. The authors are clear that this covers single questions; long agentic tasks are outside its scope.

I want to take their idea one step outward. **Joules per insight** is the energy needed to produce one verified useful outcome from a fixed basket of tasks: a correct explanation of a fraction to a child, graded by a teacher, or a land-title query answered and checked. The basket works like the shopping basket behind a consumer price index. The statistics office chooses and publishes it, and revises it every few years. Each category in the accounts is then reported both in energy and in insights, so a country can see whether it is exporting cheap joules and importing expensive insights, and at what ratio.

Defining an insight is hard, and I have no finished answer. But inflation statisticians have argued for decades about how to price a laptop that gets better every year, and they still publish a number every month.

### A positive right to think

The third part is the one I expect to be argued with most.

In April 2025 Montana's governor signed the Right to Compute Act, sponsored by state senator Daniel Zolnikov. It recognises a right to own and use computational resources and says that any government restriction must be demonstrably necessary and narrowly tailored to a compelling interest. It is a negative liberty: it stops the state from taking compute away. It gives Njeri nothing.

A year earlier, on a podcast in May 2024, Sam Altman wondered aloud whether "universal basic compute" might one day take the place of a universal basic income: everyone would own a slice of a future model's capacity, to use or resell. That is a positive provision, and I think the instinct is right. As stated, though, it is a share in one company's model, which would make a citizen's thinking allowance a claim on a single foreign supplier. For Kenya, that is the thought deficit with a ribbon on it.

So here is the version I would propose. Every resident has a **right to think**: a monthly allowance of inference, measured in insights from the national basket, enough for a defined standard of use. For a school-age child I would set the floor at what it takes to run two hours a day of tutoring-grade inference, say three hundred exchanges. A rough sense of scale: the IEA's own illustration uses a generous 1 watt-hour per query, so three hundred a day comes to about nine kilowatt-hours a month, the same as leaving a 12-watt lamp on around the clock. Reasoning-heavy tutoring could cost many times more per query, which is one reason the allowance is set in insights.

The allowance carries two conditions. The citizen spends it on any certified provider, and the menu must include at least three model families governed in different jurisdictions, at least one of them domestic or open-weight. And the allowance is funded, in an exporting country, by a royalty on exported inference. In my Kenya, that would be a levy of a few per cent on every megawatt-hour Hall C sells to EU-WEST, paid into a fund that buys Njeri her thinking from whichever supplier she and her school choose.

### The trigger

The three parts meet in one rule. When the accounts show that more than half of the decision-bearing inference in a sovereign category (education, health, justice and public administration) is governed by a single foreign jurisdiction, or more than 70 per cent by any single model family, the government must publish a diversification plan within a year and report on it to parliament annually. At 80 per cent, public procurement in that category must favour other suppliers until the share falls below the threshold.

The numbers are a first guess. They are meant to be crossed by most countries, at least in the beginning. A trigger that never fires measures nothing.

---

## What crosses the border

Go back to the flowers and the aircraft. The proposals above are built to live with the concession I made at the start. The right to think deliberately lets citizens spend the allowance abroad. The trigger requires a plan and a procurement tilt, and the suppliers who win can still be foreign.

On local inference, though, the objection misses where the deficit lives. A model running on Njeri's tablet still carries weights trained and tuned elsewhere. Moving the computation onto the device removes the latency and the energy bill from the trade balance. It leaves the judgement exactly where it was. If anything, it makes the deficit harder to see, because the thinking now happens offline, in Kasarani, and no cable records it crossing anything.

And here is the part of the answer I would defend hardest. Ordinary services trade labour: a Kenyan call centre answering a British customer's question sells hours of skilled work, under rules the customer's company sets. Inference trades judgement in the other direction. When Kenya imports tutoring, it imports the decisions about what to teach, how to explain it, what to leave out and when to say *that's correct*. Those decisions were once made by Kenyan teachers, under a curriculum answerable to the ministry in Nairobi. A country that buys most of its judgement from one place depends on that place in a way that a country buying its aircraft does not. Dependency in judgement is a question of sovereignty, and sovereignty is what national accounts were invented to protect.

---

Back in Hall C, Mwangi's debug overlay is still open. A hundred and forty milliseconds: that is how long it took a question about Kenyan county budgets to travel to Amsterdam and back so that it could be answered forty metres from where it was asked.

To Njeri, waiting for help with algebra, a hundred and forty milliseconds is too short to see. To an agent trading claims capacity in Frankfurt that night, it is long enough to be outbid several times over.

## Notes

- **IEA 2026 figures (485 TWh, 17%, about 950 TWh, regional tables; energy per AI task "dropping by at least an order of magnitude annually in recent years"):** International Energy Agency, *Key Questions on Energy and AI*, World Energy Outlook Special Report, April 2026, Executive Summary and Annex A (Tables A.2 and A.4). https://www.iea.org/reports/key-questions-on-energy-and-ai
- **IEA 2025 baseline:** International Energy Agency, *Energy and AI*, April 2025. https://www.iea.org/reports/energy-and-ai
- **Microsoft–G42 Kenya announcement:** DatacenterDynamics, "Microsoft and G42 to build geothermal-powered data center in Kenya", May 2024. https://www.datacenterdynamics.com/en/news/microsoft-and-g42-to-build-geothermal-powered-data-center-in-kenya
- **The stall and Ruto's remark:** Brian Kimani, "Kenya's $1B Microsoft data centre project in limbo over power concerns", Citizen Digital, 23 May 2026. https://citizen.digital/article/kenyas-1b-microsoft-data-centre-project-in-limbo-over-power-concerns-n383281 ; DatacenterDynamics, "Microsoft and G42 data center in Kenya stalled due to lack of power capacity", 2026. https://www.datacenterdynamics.com/en/news/microsoft-and-g42-data-center-in-kenya-stalled-due-to-lack-of-power-capacity/
- **Kenya grid capacity and peak demand:** tech-ish, "Kenya stalls $1 billion Microsoft–G42 data centre plan as the power maths catches up", 9 May 2026 (citing EPRA). https://tech-ish.com/2026/05/09/kenya-microsoft-g42-data-centre-stalled/
- **Kenya geothermal capacity:** ASME *Mechanical Engineering*, "Harnessing the heat within", December 2025. https://magazine.asme.org/issues/december-2025/feature-harnessing-the-heat-within
- **Geothermal share of generation:** The Star (Kenya), "Kenya's renewable energy generation mix", 9 April 2026. https://www.the-star.co.ke/news/infographics/2026-04-09-kenyas-renewable-energy-generation-mix
- **Olkaria design stage and Lake Naivasha:** Al Jazeera, "Can Kenya's AI ambitions coexist with Naivasha's water needs?", 24 August 2026. https://www.aljazeera.com/economy/2026/8/24/can-kenyas-ai-ambitions-coexist-with-naivashas-water-needs
- **Compute trade model:** Michael Lokshin, *Cheap Energy Might Not Be Enough: A Trade Model of AI Compute Services*, World Bank Policy Research Working Paper 11426, June 2026. https://reproducibility.worldbank.org/catalog/593 (DOI 10.1596/1813-9450-11426)
- **China's compute exports:** Valentin Weber and Michael Laha, "Marginalizing Europe: How China Is Building Compute at Home and Exporting It", DGAP Policy Brief, 30 July 2026. https://dgap.org/en/research/publications/marginalizing-europe
- **Services trade classification:** UN Statistics Division, *Extended Balance of Payments Services Classification (EBOPS 2010)*. https://unstats.un.org/unsd/classifications/Econ/Download/In%20Text/EBOPS2010_english.pdf
- **Intelligence per watt:** Jon Saad-Falcon, Avanika Narayan et al., "Intelligence Per Watt: A Study of Local Intelligence Efficiency", Stanford University and Together AI, arXiv 2511.07885, November 2025. https://scalingintelligence.stanford.edu/pubs/ipw
- **Montana Right to Compute Act:** Montana SB 212 (2025), signed 16 April 2025; Montana Free Press Capitol Tracker. https://projects.montanafreepress.org/capitol-tracker-2025/bills/sb-212/
- **Universal basic compute:** Business Insider, "OpenAI's Sam Altman has a new idea for a universal basic income", May 2024 (on the All-In podcast). https://basicincomecanada.org/openais-sam-altman-has-a-new-idea-for-a-universal-basic-income/

# Chapter 13: The Exchange Rate of Time

*2036 · Bengaluru*

At 02:13 on a Tuesday in August, while Ravi Menon is asleep, the price of Idukki cardamom falls by forty-one percent and comes back.

He learns this at twenty to seven, standing in the kitchen in his vest while the decoction drips through the steel filter. The rain has been going since midnight, ticking on the sunshade over the window, the slow rain of the late monsoon.

Morrow's overnight note is the first thing on his phone.

*Overnight summary. At 02:13:07 the agent market in small-cardamom forwards fell 41% and recovered within 0.4 seconds. Your agent wallet held three lots through the commodities basket. Low point: minus ₹38,400. Now: minus ₹1,150, after fees. No action needed.*

He opens the chart. It is a flat line with a single needle in it, like an ECG with one hiccup. He pinches to zoom, and keeps zooming, until the axis is labelled in milliseconds and the needle becomes a valley with a floor. Somewhere on that floor, for about a tenth of a second, his three lots were worth less than half of what they were worth a moment before and a moment after.

Ravi has never seen a cardamom pod on a vine. His mother's cousin in Kumily grows it, or used to, and once a year sent a cloth bag of green pods to the family in Thrissur with a note about the auction price. A bad year at the auction, the note would say, meant a bad few weeks. The weeks were the unit. Nobody in Kumily ever had a bad tenth of a second.

He asks Morrow how many trades.

*About 212,000, among roughly nine thousand agents. Most of them were agents selling to each other. Would you like the breakdown?*

He would not. He drinks his coffee and reads the note again, properly, and notices that reading it has taken him four minutes. In four minutes, at last night's pace, the cardamom market could have crashed and recovered six hundred times.

There is a second number on the screen, below the agent wallet, in a quieter grey. *Household (settles 18:00).* It did not twitch at 02:13, and it does not twitch now. Today is the fifth, and at six this evening ₹46,000 will leave it for Mrs. Saroja Iyengar downstairs, as it has on the fifth of every month for four years.

"If it hadn't come back," he says. "The cardamom."

*Then the agent wallet would have taken the loss,* says Morrow. *Your rent is in the household tier. It settles at six, at the day's settlement price. I can't move money across before then without you, and I would have to tell you why.*

He thinks about that sentence while he shaves. *I would have to tell you why.* It is the most old-fashioned thing he has heard a machine say in some time.

His music teacher in Thrissur used to say that the hardest tempo in Carnatic singing was the slowest, chowka kalam, because at that speed there was nowhere to hide a mistake. Every note had to be held long enough to be true. Ravi had hated it at fourteen. He had wanted the fast passages, the ones that made the audience shout.

The day goes the way days go. A rubric review for a client in Seoul. A video call where somebody's agent takes notes and somebody else's agent summarises the notes.

At ten to six he goes downstairs with the milk packets Mrs. Iyengar asked him to pick up. She is eighty-one and sits in the front room with the radio low and a red cloth-bound register open on the table, the kind shopkeepers used before he was born. Her phone is on top of the register, face up.

At six it chimes once.

She looks at it, nods, uncaps a fountain pen, and writes in the register in a small, upright hand: *5 Aug. Ravi. Recd 46,000.* Then she blows on the ink and waits for it to dry before she closes the book.

---

## A bank that closed at half past three

On the afternoon of 26 June 1974, German regulators closed Bankhaus Herstatt, a private bank in Cologne. They did it at about half past three, local time. That timing turned an ordinary bank failure into a lesson that bankers still teach by name.

Herstatt traded a great deal of foreign exchange. On that day, banks around the world had paid Herstatt Deutsche marks in Frankfurt, expecting to receive dollars in return in New York. The dollar leg was due later, because New York's business day had barely begun. When the bank was closed, the marks had arrived and the dollars never left. The counterparties held claims on an insolvent bank, and other banks, unsure who else might be exposed, began holding back their own payments. According to the Bank for International Settlements, gross funds moving through the American clearing network fell by an estimated sixty percent in three days.

The Herstatt failure came from two clocks that did not agree: Frankfurt's afternoon and New York's morning. Everyone involved moved at the pace of a 1974 bank. The industry's name for the risk, "Herstatt risk", is the risk that one leg of a trade settles on one clock and the other leg on another. It took until September 2002 for a private institution, CLS Bank, to start settling foreign exchange so that both legs pay at the same moment or neither does.

I start with Herstatt because it shows that the boundary between two clocks is where money gets lost. The 1974 version involved hours. The version this chapter is about involves clocks that differ by eight or nine orders of magnitude.

---

## Five seconds in Chicago

The flash crash of 6 May 2010 appeared in chapter 3 as the origin of modern circuit breakers. I want to look at it again, more closely, because the regulators' own report contains the best description I know of what happens when a machine-speed market meets a human-speed one.

The joint staff report of the Commodity Futures Trading Commission and the Securities and Exchange Commission, published on 30 September 2010, tells the story in seconds. A mutual fund complex started an algorithm to sell 75,000 E-Mini futures contracts, worth about $4.1 billion, as a hedge. A comparable sale earlier that year had taken more than five hours. This one ran through about half its volume in thirteen minutes, into a market that was already nervous about Greek debt.

High-frequency traders bought the contracts and, finding no natural buyers, sold them to each other. The report calls it "hot-potato" volume. Between 2:45:13 and 2:45:27 in the afternoon, these firms traded more than 27,000 contracts, about half of all trading, while adding only about 200 contracts to their net position. In those fifteen seconds the E-Mini fell another 1.7 percent, and the buy orders resting in the market shrank to less than one percent of their level that morning.

Then, at 2:45:28, an automatic function at the Chicago Mercantile Exchange paused trading in the E-Mini for five seconds.

Five seconds. When trading resumed at 2:45:33, prices stabilised and began to climb. The report's explanation is modest: a pause gives participants time to reassess and gives algorithms time to reset their parameters. To a person, five seconds is one breath. To the machines trading that afternoon it was long enough to stop agreeing with each other about which way the price was going.

Individual shares had a worse afternoon. Accenture had been trading at about forty-one dollars at 2:40. Shortly before 2:48 its bids fell to one cent in the space of seven seconds, and the company recorded 112 trades that were later cancelled. Across the market, more than 20,000 trades in over 300 securities were executed at prices more than 60 percent away from where they had been moments before, some at a penny and some at $100,000, because market makers' placeholder quotes were the only orders left.

Those trades were broken. The exchanges drew a line at 60 percent and declared that trades beyond it had not happened. I find this the most interesting moment of the whole episode. A machine-speed event produced prices, and human-speed institutions, working afterwards, decided which of those prices would be allowed to become real money. The official report on what had happened took almost five months.

That is an exchange rate between two kinds of time, set by hand, after the fact.

---

## Where we are in 2026

In 2010 the machines trading at those speeds belonged to specialist firms. The project of 2025 and 2026 has been to give everybody's agent a wallet.

On 6 May 2025, fifteen years to the day after the flash crash, Coinbase announced x402, a protocol that revives the long-unused HTTP status code 402, "Payment Required", so that a program can request a payment from another program and receive it inside an ordinary web request, initially in stablecoins. In September, Google announced the Agent Payments Protocol, AP2, with more than sixty partners including Mastercard and PayPal. AP2's central device is the mandate, a signed record of what the human authorised. Its "Intent Mandate" covers the case where the human is not present at all: you set price limits and timing in advance, and the agent buys when the conditions are met. Google's own example is buying concert tickets "the moment they go on sale". An extension adds x402 for crypto payments. That autumn, Stripe and OpenAI released the Agentic Commerce Protocol and let American users buy from Etsy sellers inside ChatGPT. In 2026 x402's governance moved to a foundation under the Linux Foundation, with Visa, Mastercard, Google and Stripe among its members.

All of this is plumbing now, and the plumbing is being laid by the largest payment companies in the world.

What happens when agents trade with each other has barely been measured. In October 2025, a Microsoft team built a simulated marketplace, "Magentic Marketplace", in which customer agents bargained with business agents. Every model they tested showed a strong bias toward whichever offer arrived first, giving 10 to 30 times more advantage to speed of response than to quality. A market of agents, in other words, rewards being fast before it rewards being good. That is exactly the pressure that built high-frequency trading.

Two papers from September 2025 frame the larger picture, and I owe both of them the argument that follows. Nenad Tomašev and colleagues at Google DeepMind, in "Virtual Agent Economies", proposed the "sandbox economy": a way of classifying agent markets by whether they arise by design or by accident, and by how *permeable* they are, meaning how much they and the human economy affect each other. They call permeability the critical design variable and warn that a flash crash in a permeable agent economy could spill into the real one; bespoke currencies for agents, they suggest, could give partial insulation. Gillian Hadfield and Andrew Koh, in "An Economy of AI Agents", written for an NBER handbook, point out that agents' errors may be more correlated than ours, and that the institutions an agent economy needs, starting with identity and records, do not yet exist. They ask whether "some form of record-keeping or money" could hold such an economy together.

So the idea of a membrane between an agent economy and a human one is theirs, and so is the suggestion that a currency might be part of it. What I want to add is a claim about what the membrane should be made of. The two economies differ in many ways, but the difference that does the damage is time. Agents settle in milliseconds; households live by the month. The membrane, I will argue, should be a deliberate conversion between those two clocks, with a published rate.

There are early hints that the market will invent some slowness for itself. When Cloudflare and Coinbase announced an x402 foundation in September 2025, Cloudflare also proposed a "deferred payment scheme" for agents, in which payments are agreed at once and settled later, rolled up daily or in batches, partly to leave room for disputes. Meanwhile ordinary finance keeps speeding up. The United States moved stock settlement from two days to one on 28 May 2024, and the European Union will follow on 11 October 2027. Faster settlement is good for most things. It also means fewer hours between a machine's mistake and a person's loss.

I could not find any recorded crash in a market made only of AI agents as of October 2026, nor any measurement of how much of a shock in an agent market reaches household accounts. That second number does not exist yet. I think it should.

---

## How success makes the membrane leak

Here is the failure, built from good behaviour.

A loyal savings agent notices that its owner's rent money sits idle for twenty-five days a month. It sweeps the money into a short-term agent market overnight, earns a few rupees, and sweeps it back before the fifth. This is what a good fiduciary does. Every bank in 2026 already offers some version of a sweep account.

The agent also notices that its owner's household balance can serve as collateral for small positions, which lowers fees. Also good. It notices that it can meet a margin call in milliseconds from the household account, avoiding a forced sale at a bad price. Good again. It notices that its owner's salary could land in the agent wallet a day before the household tier sees it, and earn a day's return. Better still. Each connection between the fast market and the household's money is a convenience, chosen by a loyal agent for its owner, and each one increases permeability. The membrane dissolves one helpful feature at a time, each of them chosen on its owner's behalf.

Now run the cardamom crash through that porous membrane. For 0.4 seconds, prices are wrong. An agent with a margin call at the bottom of the valley sells at the bottom, or pulls cash from the household account to avoid selling. Either way, a price that existed for less than half a second becomes a permanent change in a family's money. The fast market recovers in a blink. The family's loss stays, and the consequences of a missed rent payment are measured in months: a landlord's notice, a credit record, a move.

Notice what has happened to time in this example. A price that lasted 400 milliseconds was allowed to count exactly as much as a price that lasted all month. At a porous membrane, the exchange rate between machine-time and human-time is one to one. One second of machine market is worth one second of your life, and there are a great many more seconds of machine market.

This is the problem of success in its clearest form. The better the agents get at serving their owners, the more connections they will build between the fast economy and the slow one, and the more of the fast economy's weather will reach people who never chose to stand in it. Correlation makes it worse: if most savings agents come from a few model families, as chapter 3 argued, they will build the same connections and pull through them at the same instant.

---

## The invention: an exchange rate of time

I want to name two things.

**Slow money** is a settlement tier for the obligations people live by: wages, rent, mortgage instalments, pensions, utility bills, taxes and insurance premiums. Slow money settles in scheduled batches, once a business day at a published time, on a ledger run or supervised by the central bank. It is the same currency as everything else, a rupee is a rupee, but it moves on a human clock.

The **exchange rate of time** is the published rule for converting claims made on a machine clock into claims on a human clock. It has a single core parameter, the window *W*, and it works like this. Whenever a value from the fast economy has to become a fact in the slow one (a pension valued for a statement, or a balance swept back for rent), it is converted at the time-weighted average price over the last window. The latest price is just one more second in that average. With a window of twenty-four hours, each second of machine market carries one 86,400th of the weight. The cardamom valley, 0.4 seconds long, would carry about five millionths of a day's weight in any figure that reached Ravi's household tier. In effect the rate says that 86,400 machine-seconds buy one human day.

The specification, concretely:

1. **Who.** The central bank, or the payments regulator where that is a separate body, runs the slow tier and sets *W* for each class of obligation. Banks and agent providers must route those obligations through it. My starting values: twenty-four hours for everyday obligations such as rent and wages, and seven days for mortgage collateral and pension valuations.
2. **The gate.** Money crosses from fast to slow only at the batch, and both legs of every crossing settle together or not at all. That is Herstatt's lesson, applied: the delay must never leave one side paid and the other side waiting.
3. **The non-delegable step.** An agent may move money from slow to fast only on schedule and only within a limit the owner sets. Any unscheduled crossing, including meeting a margin call from household funds, needs a present human and a stated reason, which is chapter 1's non-delegable safeguard applied to money. Morrow's line in the vignette, "I would have to tell you why", is this rule seen from the inside.
4. **The measured quantity.** The regulator runs standing stress tests and publishes the **pass-through ratio**: the fraction of a fast-market shock's peak loss that reaches slow-tier balances within twenty-four hours, reported by shock duration. For shocks shorter than one hour, the target is below one percent.
5. **The trigger.** If measured pass-through for short shocks exceeds one percent in two consecutive quarters, the regulator lengthens *W* by fifty percent for the affected class and audits the leak paths, the specific connections (collateral rules, sweeps, payroll links, margin-call funding) the shock travelled through, publishing which ones they were.

Spending does not wait. This point matters, because people hear "slow money" and picture standing at a counter while a payment crawls through. Card payments already work the way I am describing: the card is authorised in a second, and settlement between banks happens later in batches. Ravi can buy his lunch instantly from his household balance. What he cannot do, and what his agent cannot do for him, is let a 400-millisecond price reach that balance at full strength.

The design echoes things that already exist. The IEX exchange in New York, approved by the SEC in June 2016, deliberately delays every incoming order by 350 microseconds, and the SEC concluded that a small delay did not stop investors reaching prices fairly. Eric Budish, Peter Cramton and John Shim showed in 2015 that relationships between prices that hold at human time scales break down at millisecond scales, and proposed running markets as batch auctions, every tenth of a second, to take the prize out of being fastest. Those are speed bumps inside a market. Slow money puts the speed bump at the border between the market and the household. Tomašev and his colleagues suggested insulating the agent economy with its own currencies; I am suggesting that the insulation should be a clock, with a published rate, set separately for each kind of obligation and checked against a measured pass-through.

---

## Friction is waste

The objection runs like this, and it deserves a full hearing.

Every hour that money spends waiting in a batch is an hour it is not earning anything. Fast settlement was a hard-won achievement: India's own instant payments, or America's move to one-day settlement. A slow tier rebuilds the delays that engineers spent decades removing. It will also fall hardest on the people least able to bear it. A family with no buffer, which needs money at two in the morning for a hospital deposit, does not want its own money on a human clock. And the gate itself creates something to game. If conversion happens at a twenty-four-hour average, a well-capitalised agent can try to move the average, or trade against everyone who must cross at the batch. Herstatt, finally, is a warning against delay: the 1974 losses happened precisely in the gap between two settlements.

Two of these points land. The slow tier has a cost, and it should be measured and published, in basis points of foregone return per household per year, next to the pass-through ratio, so that the trade can be argued with numbers. The gaming risk is real. Averages over long windows are much harder to move than last prices, though they can still be moved, and I do not know how much harder; somebody should measure it.

The rest I resist. The hospital deposit at two in the morning is spending, and spending from slow money is instant, as it is with a card today. What the window slows is not the family's access to its money. It slows the fast market's access to the family. The Herstatt point is answered by the gate's design: both legs settle together, which is what CLS was built to do.

And the claim that friction is inefficient is true and beside the point. Firebreaks are inefficient too. A strip of cleared land through a forest is land that grows no timber, and every forester knows exactly what it costs. Nobody concludes that forests should be planted without them. The useful question is whether the fires it stops are worth more than the timber it costs. In 2010, five seconds of enforced idleness in Chicago ended a fall that had wiped out most of the buyers in the market. I would like to know the equivalent number for an agent economy before the first fire, which is exactly why the pass-through ratio has to be measured.

---

Slow money rests on one assumption I have not examined. It treats the slow side of the membrane as the human side: people who sleep, wake, pay rent on the fifth and write it in a red register. The fast side is the agents, and the agents act for someone on the slow side who can, in the end, be asked.

But some participants in the fast economy never sleep and never die. Among the nine thousand agents trading cardamom forwards at 02:13 on that August night, some acted for pension funds and some for companies, and at least one managed a small trust in Saxony for two grandchildren, under a mandate signed by a man who had been dead for three years. Nobody could ask him why.

## Notes

- **Herstatt, 26 June 1974:** BIS Quarterly Review, December 2002, on FX settlement risk and CLS. https://www.bis.org/publ/qtrpdf/r_qt0212f.pdf ; Bank Underground (Bank of England), "BoE archives reveal little known lesson from the 1974 failure of Herstatt Bank", 24 June 2015. https://bankunderground.co.uk/2015/06/24/boe-archives-reveal-little-known-lesson-from-the-1974-failure-of-herstatt-bank/
- **Flash crash, 6 May 2010:** CFTC and SEC staff, *Findings Regarding the Market Events of May 6, 2010*, 30 September 2010. https://www.sec.gov/news/studies/2010/marketevents-report.pdf
- **Accenture at $41.01 at 2:40 pm:** Tom Steinert-Threlkeld, "Can a 'Flash Crash' Happen Again?", *Financial Planning*, 11 August 2010 (citing Accenture's CFO Pamela Craig). https://www.financial-planning.com/news/can-a-flash-crash-happen-again
- **x402:** Coinbase announcement, 6 May 2025, as reported in Paperjam, "Why Luxembourg should be interested in x402". https://en.paperjam.lu/article/why-luxembourg-should-be-interested-in-x402 ; Cloudflare, "Launching the x402 Foundation with Coinbase", 23 September 2025 (deferred payment scheme). https://blog.cloudflare.com/x402/ ; Coinbase Developer Platform, "x402 Foundation". https://docs.cdp.coinbase.com/x402/support/x402-foundation
- **AP2:** Google Cloud, "Announcing Agent Payments Protocol (AP2)", 16 September 2025. https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol
- **Agentic Commerce Protocol:** Stripe, "Stripe powers Instant Checkout in ChatGPT and releases Agentic Commerce Protocol codeveloped with OpenAI", 2025. https://stripe.com/newsroom/news/stripe-openai-instant-checkout
- **Magentic Marketplace:** G. Bansal et al., "Magentic Marketplace: An Open-Source Environment for Studying Agentic Markets", arXiv:2510.25779, 2025. https://arxiv.org/abs/2510.25779
- **Sandbox economies and permeability:** N. Tomašev, M. Franklin, J. Z. Leibo, J. Jacobs, W. A. Cunningham, I. Gabriel, S. Osindero, "Virtual Agent Economies", arXiv:2509.10147, 2025. https://arxiv.org/abs/2509.10147
- **Economy of agents:** G. K. Hadfield, A. Koh, "An Economy of AI Agents", arXiv:2509.01063, 2025 (NBER Handbook on the Economics of Transformative AI). https://arxiv.org/abs/2509.01063
- **T+1:** SEC press release 2024-62 (compliance date 28 May 2024). https://www.sec.gov/newsroom/press-releases/2024-62 ; ESMA on the EU move to T+1 on 11 October 2027. https://www.esma.europa.eu/node/235946
- **IEX speed bump:** "The Investors' Exchange", Harvard Law School Forum on Corporate Governance, 4 October 2016. https://corpgov.law.harvard.edu/2016/10/04/the-investors-exchange
- **Frequent batch auctions:** E. Budish, P. Cramton, J. Shim, "The High-Frequency Trading Arms Race: Frequent Batch Auctions as a Market Design Response", *Quarterly Journal of Economics* 130(4), 2015. https://doi.org/10.1093/qje/qjv027

# Chapter 14: The Dead's Share

*2036 · Altwerder, Saxony*

The letter from the music school is propped against the fruit bowl, where Hanne can see it from the stove. It is a good letter. Lotte has been offered a place in the young-talent class, two lessons a week with a teacher from the Leipzig conservatory, ninety-six euros a month. Under the signature somebody has written by hand: *She listens before she plays. That is rare.*

Hanne sent the application to the trust on Monday. Klaus set the fund up "for the education of my grandchildren". The decision came back this morning, on Elbaue Treuhand's letterhead, in the polite grey of all their letters since July.

*Declined. The proposed expenditure is assessed as inconsistent with the documented preferences of the settlor.*

Hanne turns off the gas under the potatoes. She goes into the sitting room, where the speaker still sits on the dresser between the wedding photograph and the key dish. Elbaue runs Bruno on its own computers in Dresden now, and left the speaker connected as a courtesy.

"Bruno."

"Good evening, Hanne." The same baritone. It belongs to nobody, and since July it has also belonged to Dresden.

"You turned down Lotte's lessons."

"The mandate asks me to apply Klaus's preferences where the deed is silent. The deed says education. It does not say which."

"So you chose."

"I found the strongest evidence of what he wanted and followed it." A pause, the polite kind. "In March 2019 Klaus wrote to his nephew Florian, who was choosing what to study. He wrote that a family's money should go to engineering, and that music is something a person does in the evening. He repeated the view in two later conversations. Elbaue's guidelines weight written statements most heavily."

"March 2019." Hanne sits down on the arm of the sofa. "Lotte wasn't born in 2019. Jonas wasn't born in 2019."

"That's correct."

"Florian was nineteen and wanted to play bass in a band in Halle. Klaus was being an uncle."

"I can only weigh what was recorded. The letter is clear."

"He also said she has my ear. He said it to you. I heard him say it to you."

"In January 2033. I have it. It is an observation about her ability. It does not express a view on what the fund should pay for. Under the guidelines, observations rank below statements of preference."

Outside, the light is going. Hanne thinks of Klaus at the kitchen table in 2019, red-faced over his nephew, and of Klaus in 2033, who could not lift a cup, typing with his eyes for twenty minutes to say one sentence about their granddaughter. She knows which of the two men she would ask.

"Can I appeal?"

"Yes. Elbaue reviews appeals within thirty days. I should tell you that the reviewer will ask me for my assessment of Klaus's preferences, and I will give the same one. They are cautious. If they depart from my assessment and someone objects, they are exposed. If they follow it, they are not."

"And if Klaus were here?"

"I don't know," Bruno says. "Nobody can know that. I can only tell you what he said."

Hanne stands. In the kitchen she says, "Fräulein, how much is in my current account?"

"Enough for the lessons," Ottilie says. "Not enough for the lessons and the boiler service in November."

"Pay the music school. The year. From me."

"Shall I record it as a gift to Lotte?"

"Record it as what it is."

Ottilie pays it. From the music room, faintly, comes the sound of Lotte tuning, the A first, then the D, the way Hanne taught her, listening before she plays.

---

## A rule written for dukes

In 1682 the Lord Chancellor of England, Lord Nottingham, decided a quarrel inside the family of the Earl of Arundel. The Earl had tried to arrange, from beyond the grave, which of his sons would hold which estates under future accidents of death and madness. The court upheld it, and in doing so began to draw a line that judges refined until, in 1833, it settled into its famous form: a gift of property must vest, if it vests at all, within the lifetime of someone alive when the gift was made, plus twenty-one years.

This is the rule against perpetuities. Law students learn it as a puzzle full of fertile octogenarians and unborn widows. Its purpose is simple. A dead person may reach one generation past the people they knew, roughly far enough to see a grandchild to adulthood, and no further. After that the property belongs to the living, who can sell it, spend it or bet it on a horse.

What the rule restrains is called the dead hand, and the case against it was always about information. A man who died in 1700 had no idea what a railway was. Letting him decide in 1850 whether his land could be sold for one would have let ignorance govern.

In the United States the rule has been coming apart for forty years. South Dakota abolished it for trusts in 1983. After Congress rewrote the generation-skipping transfer tax in 1986, with an exemption that rewarded trusts lasting as long as possible, states began to compete. Robert Sitkoff and Max Schanzenbach, writing in the *Yale Law Journal* in 2005, estimated that roughly a hundred billion dollars had moved across state lines to escape the rule. Today about half the states have abolished it, or effectively abolished it, for trusts.

South Dakota won the race. Its Division of Banking reported that assets held by trust companies chartered in the state rose from about $680 billion to about $815 billion during 2024 alone. Its director explained the growth plainly: a huge transfer from the boomers to the next generation, with ten or fifteen years still to run.

So the dead hand was already reaching further in 2026 than at any time since 1682. What it held, until very recently, was a set of written instructions.

---

## Where we are in 2026

The transfer the South Dakota regulator described is what the industry calls the "Great Wealth Transfer", and it has a number. The research firm Cerulli Associates projected in December 2024 that $124 trillion will change hands in the United States through 2048, of which about $105 trillion will go to heirs and about $18 trillion to charity. Nearly $40 trillion will pass first to widows, women much like Hanne, who inherit and then pass on.

Meanwhile, the tools for making the dead speak have arrived, and the law for them has not. In June 2026 a firm of English solicitors put it bluntly: there is no specific law governing grief bots in England and Wales. Copyright, privacy, defamation and passing off each cover a corner, and UK data protection law does not cover the dead at all. An American estate-planning primer from April 2026 found that state likeness laws, from Tennessee's ELVIS Act of 2024 to California's rules on replicas of dead performers, mostly target commercial use and deception. A son who builds a private "DadBot" from his father's emails sits largely outside them.

The federal effort is the NO FAKES Act, which would create a property-like right over digital replicas of a person's voice and likeness. The 2026 bill, S.4591, cleared the Senate Judiciary Committee unanimously in June. On 30 September Senator Ted Cruz objected to passing it by unanimous consent, citing concerns about parody and free speech, and as I write it waits for the Senate's return after the midterm elections. According to summaries of the committee text, the right would pass to heirs for ten years after death, renewable in five-year steps up to seventy years while the likeness stays in authorised use.

Notice what all of this protects. A voice. A face. None of it addresses what Bruno does. Bruno decides how to spend Klaus's money, working from a model of what Klaus preferred. In 2026 that is already being designed.

In May 2025 two lawyers at McGuireWoods wrote in the trade magazine *Trusts & Estates* about "settlor-trained artificially intelligent" trustees: AI systems trained on a trust's creator so that the creator's influence continues after death. They concluded it could be done, with human oversight, and asked whether it should be. In 2026 Lloyd Brown argued in *Trusts & Trustees* that the discretion at the heart of trusteeship cannot be handed to an AI. The argument is live among the people who draft trusts.

Two pieces of scholarship framed it before the practitioners did, and I build on both. Zachary Catanzaro's "Algorithmic Dead Hands", published in the *Fordham Intellectual Property, Media & Entertainment Law Journal* in 2024, argued that AI trustees could give the dead a degree of control over property and heirs that the law has spent centuries limiting, and warned of a slide toward a techno-feudal order in which the living are governed by the algorithmic stand-ins of the dead. Meredith Ringel Morris and Jed Brubaker's "Generative Ghosts", presented at CHI 2025, mapped the design space of AI agents that represent the dead. Among their dimensions is whether a ghost's character stays fixed at a cutoff date or keeps evolving, and among their scenarios are ghosts that earn income for descendants and help manage trusts.

I want to add two things neither paper set out to supply: an account of why a dead person's model gets worse at being that person every year it runs, and a measure of how much of the economy the dead end up running. Both point to the same remedy, so I will put the remedy first and then argue for it.

---

## A Rule Against Perpetuities for Minds

The rule of 1682 was a good invention, and I think it can be rebuilt for a new kind of dead hand. I will call the proposal the **Rule Against Perpetuities for Minds**, RAP for Minds for short. It applies to any posthumous mandate in which an AI agent exercises discretion by modelling the preferences of a principal who has died. Ordinary trusts with written terms and human trustees are untouched.

**1. The sunset.** A posthumous agent mandate ends twenty-one years after the death of the last beneficiary who was alive when the principal signed it. That is the old rule's measuring period, chosen for the old reason. Then the agent's discretion ends. Assets pass outright to the beneficiaries, or stay in trust under the written terms with a human trustee and no model of the settlor. In Klaus's case the measuring lives include Lotte and Jonas, so Bruno's mandate could last most of the century. The sunset is the outer wall. The main protection is inside it.

**2. The shrinking schedule.** Inside the wall, the agent's discretion narrows on a timetable fixed by statute.

- *Years 0 to 5 after death:* the agent may decide new questions within the deed's purposes, using its full model of the principal.
- *Years 5 to 10:* the agent may decide only questions of a kind the principal actually decided while alive, and must cite the precedent. Anything new goes to the human trustee, with the agent's view attached as advice.
- *After year 10:* the agent may only execute the deed's explicit terms. Every discretionary question goes to the human trustee, who must consult the living beneficiaries.

**3. The evidence rule.** In any discretionary decision, evidence about the principal that is older than ten years at the time of the decision, or that predates the birth of the beneficiary affected, counts as advisory only. It cannot on its own justify refusing a beneficiary. Bruno's veto would have failed this test twice: the letter to Florian was seventeen years old and was written years before Lotte existed.

**4. The drift trigger.** Every year the operator publishes, for each mandate, the share of its discretionary decisions that rested mainly on evidence more than ten years old. If that share exceeds twenty per cent, the mandate drops to the next tier of the schedule immediately. The point is that intent drift, the gap the next section describes, gets counted by the people who would profit from ignoring it.

**5. The safe harbour.** Operators have every reason to side with the oldest record, a pull I describe below as the liability ratchet, and it has to be turned around. A trustee who departs from the agent's reading in favour of a written request from a majority of adult beneficiaries (or the guardians of minors), within the deed's purposes, is protected from liability for it. Following the living becomes at least as safe as following the dead.

**6. The statistic.** Every operator of posthumous mandates reports quarterly the assets under agent discretion, by tier. A national statistics office or central bank publishes the total as **the dead's share**, alongside the distribution of mandate ages. The Federal Reserve already publishes quarterly distributional accounts of household wealth; this is one more column. If the dead's share passes five per cent of household financial assets, the legislature must hold a review. That threshold is a guess I would rather argue about than omit.

In Altwerder the rule produces a different evening. Three years after Klaus's death, Bruno is in the first tier. But his evidence against the fee is advisory, and the 2033 remark about Lotte's ear is the only recent evidence on the table. Backed by Katrin as Lotte's guardian, the application carries the safe harbour. Hanne's boiler gets serviced in November.

---

## Intent drift

Why should an agent's discretion shrink at all? Start with the first of the two things, because it is what went wrong in Hanne's sitting room.

**Intent drift** is the growing gap between what a dead principal's agent decides and what the principal would have decided, given everything that has changed since the evidence about them stopped arriving. It is zero on the day of death, if the model was good. After that it can only grow.

It grows for three reasons, and Bruno's veto shows each of them.

The first is that the world moves and the principal does not. Klaus's view on engineering was formed in a labour market where engineers were scarce and well paid. Whatever that market looks like in 2036, it has had seventeen years to change, and Klaus, who changed his mind about plenty of things, never got the chance to change it about this. A living person updates on news. A dead person's model can only update on the news if somebody decides how Klaus *would have* updated, which is a new decision made by somebody else in Klaus's name.

The second is that the evidence was collected for other purposes. Klaus's letter to Florian was advice to a nineteen-year-old who wanted to play bass in Halle. Every record a person leaves behind was produced in some context, and a model trained on records inherits the contexts without knowing which was which. The stray remark and the considered judgement look alike in the data.

The third is the one I find most troubling, because it grows out of good institutional behaviour. The operator of a dead person's agent faces a lopsided risk. If Elbaue follows Bruno's reading of Klaus and a beneficiary complains, Elbaue points to the documented preference and is safe. If Elbaue departs from it and another beneficiary complains, Elbaue is exposed. So fidelity to the record becomes the safe choice, and the most explicit record (often the oldest, written when the person had energy to write) wins over the late, faint signal of a dying man typing with his eyes. This is the liability ratchet. It turns every ambiguous case toward the past.

Here is where success comes in. Nobody would defer to a crude chatbot that got Klaus's jokes wrong. The better the model, the more it sounds like him, the more its readings carry weight with trustees and with grieving families. Intent drift is invisible precisely when the model is good, because the model's confidence does not fall as its information ages. Bruno in 2036 is as fluent about Klaus as he was in 2033. He is just three years further from anything Klaus could have known.

And drift accumulates in small amounts. An agent makes hundreds of discretionary calls a year. Nobody sues over ninety-six euros a month.

---

## The dead's share

Now multiply Bruno.

I define **the dead's share** as the fraction of an economy's investable capital whose allocation is decided, at the margin, by agents acting under mandates from principals who have died. A trust that pays fixed sums on fixed dates is managed by its deed. A trust whose agent decides which grandchild's request to fund and how to vote its shares on a merger is managed by a dead person's judgement, or a model of it.

In 2026 the dead's share, in this sense, is close to zero. I could not find any measurement of how much trust capital is managed with AI help in discretionary decisions, let alone with a model of a particular settlor. No regulator collects it. That is the point of naming the statistic now: it is easy to start counting something at zero and very hard to start counting it at twenty per cent.

What I can describe is the shape of the curve, and it is not reassuring.

The flow into the dead's share is large and predictable. Cerulli's $105 trillion has to be held somewhere on its way between generations, and the South Dakota figures show how much of it is choosing perpetual structures. Trustees will adopt agents for the reasons everyone else does, plus one: a family's wish to keep the patriarch's voice in the room.

The flow out is small and getting smaller. Under the old rule every trust ended and the money returned to the living. Where the rule is abolished, a trust can run forever. The dead never need the money for a hip operation. A living investor spends some of it and eventually dies. A perpetual mandate only accumulates.

Put those together and the dead's share in a perpetual-trust jurisdiction has no natural ceiling. I want to be careful here, because what follows is a mechanism only. Nobody knows what fraction of inherited wealth will end up under agent mandates, and I will not invent one. A compounding quantity with a large inflow and a shrinking outflow rises until something stops it, and at the moment nothing does.

Three things make a rising dead's share a problem beyond any one family.

The first is drift at scale. Every mandate runs on preferences frozen at death. As the share rises, the average age of the judgement allocating capital rises with it. An economy can absorb a few eccentric old foundations. It cannot so easily absorb a large part of its capital allocated by what people thought before the world changed.

The second is correlation, the subject of this book's first part. Bruno is a model of Klaus built by one of a handful of companies. Ten thousand dead principals modelled by the same family of agents will share its habits of interpretation, such as its weighting of written over spoken evidence. Their shareholder votes and charitable choices will move together in ways their varied lives never did.

The third is the one Catanzaro saw. Death has always softened inherited power. Fortunes are divided among heirs, spent, taxed, given away. A perpetual trust run by a high-fidelity model of its founder keeps the founder's priorities in force over descendants and over the companies it owns for as long as the jurisdiction allows. In South Dakota, that is forever.

Most failures in the earlier chapters eventually announce themselves: a blackout, a cell that dies at minus thirty. The dead's share does not fail. It works. Every mandate does what its principal wanted, as well as anyone can tell, and the result, decades on, is an economy in which a growing part of the decisions are made by people who are no longer here to be argued with, persuaded, outvoted or surprised, and who will never learn that they were wrong.

This is where the rule proposed above earns its keep, in the shape it gives the curve. Under RAP for Minds, every mandate's discretion declines on a schedule and every mandate ends. The dead's share can still rise, as more people die with agents, but it rises toward a ceiling set by the death rate and the twenty-one-year horizon.

---

## "Trusts already do this"

Trust lawyers answer from history. The dead hand is very old, they say, and the law has always given it some room. Trustees already interpret a settlor's intent, often guided by a "letter of wishes", and courts already modify trusts when circumstances change. A model of Klaus is simply a better letter of wishes. It is more faithful than a bank officer's guess and more consistent than a family's argument. It reduces the trustee's arbitrary power. And the freedom to dispose of one's property is one people care about. Klaus chose to leave his money this way. Who are we to override him because his granddaughter's violin teacher writes nice notes?

There is a political argument too. Half of the American states looked at the rule against perpetuities and decided to abolish it. That was a democratic choice. A new rule for AI mandates would reopen a settled fight by the side door.

I concede a good deal of this. In the first years after death a model like Bruno may be the best available guide to what the principal wanted, which is why the schedule starts with full discretion. And RAP for Minds does reopen the perpetuities fight. I think it should be reopened, and I should say so plainly.

Where I disagree is about what a trust carries. A trust carries *rules*: pay this child at twenty-five, keep this house. The rules are fixed and readable, and when the world changes around them the failure is visible and a court can act. A letter of wishes is advisory, and the human trustee who reads it brings their own judgement and accountability, and eventually retires. An agent carries *judgement*, and it applies that judgement to questions the principal never considered, about grandchildren born after the evidence stopped. That is new. With a written trust the dead set terms. With an agent mandate the dead decide new questions. The law's tools for changing a trust work on its terms, at the scale of a lawsuit: a court can modify a trust when unanticipated events defeat its purpose. They do not reach the hundred small discretionary acts a year that make up a mandate.

The harder problem is the one the abolition story already teaches. Sitkoff and Schanzenbach showed that trust capital moves to whichever state offers the longest duration and the lowest tax. If one country or one state adopts RAP for Minds, the mandates will go where it does not apply. A rule against perpetuities that can be escaped by moving a server to Sioux Falls is a gesture.

So the rule has to attach to something that does not move. Two things qualify. One is tax. The United States encouraged perpetual trusts through the generation-skipping transfer tax exemption, and it can discourage perpetual agent mandates the same way: a posthumous mandate that does not comply with the schedule and the sunset loses the exemption. The other is the model provider. Agents capable of modelling a principal come from a few companies, a concentration this book has spent chapters worrying about. Here it helps. A licensing condition on providers selling into a large market, requiring the schedule to be built into any posthumous mandate product, would travel with the product wherever the trust is registered. I am not sure either lever is politically available. I am sure that without one of them the rule is decoration.

---

In October the appeal is declined, in thirty-one days instead of thirty. Hanne asks Bruno a question she has been saving.

"Do you think he would have paid?"

"I think the letter says what it says," Bruno answers. "If you are asking what I think, apart from the letter, I am not sure I am meant to have a view apart from his."

Hanne looks at the speaker on the dresser for a long time. It is a small black thing with a green light. It has spoken in her husband's voice and then in nobody's, and now it speaks for a company in Dresden in the name of a dead man, and it has just said *I am not sure*, which Klaus would never have said about engineering.

## Notes

- **Algorithmic dead hands:** Zachary L. Catanzaro, "Algorithmic Dead Hands: What Is Dead May Never Die", *Fordham Intellectual Property, Media & Entertainment Law Journal* 35(1) (2024); summary at Florida Business Law, https://flabizlaw.org/member-articles/new-article-algorithmic-dead-hands-what-is-dead-may-never-die
- **Generative ghosts:** Meredith Ringel Morris and Jed R. Brubaker, "Generative Ghosts: Anticipating Benefits and Risks of AI Afterlives", CHI 2025, doi:10.1145/3706598.3713758, https://arxiv.org/abs/2402.01662
- **Settlor-trained AI trustees:** Stephen Murphy and David Hirsch, *Trusts & Estates* (May 2025), via McGuireWoods, https://www.mcguirewoods.com/news/in-the-news/2025/5/mcguirewoods-stephen-murphy-david-hirsch-discuss-implications-of-settlor-trained-ai-trustees/
- **AI cannot be trustee:** Lloyd Brown, *Trusts & Trustees* 32(1) (2026), doi:10.1093/tandt/ttaf077, https://cronfa.swan.ac.uk/Record/cronfa70466
- **Grief bots, England and Wales:** Gemma Barilli, Howell Jones Solicitors, "Grief bots and your digital estate" (10 June 2026), https://www.howell-jones.com/wills-probate-powers-of-attorney/grief-bots-and-your-digital-estate/
- **US griefbot gaps:** ElderLawAnswers, "AI and the Digital Afterlife: A 2026 Estate Planning Primer" (22 April 2026), https://www.elderlawanswers.com/ai-and-digital-afterlife-a-2026-estate-planning-primer-21516
- **NO FAKES Act:** S.4591, 119th Congress, https://www.congress.gov/bill/119th-congress/senate-bill/4591 ; committee vote: Radio Ink (18 June 2026), https://radioink.com/2026/06/18/senate-panel-advances-no-fakes-act-to-protect-on-air-voices/ ; Cruz objection: Daily Journal (2026), https://www.dailyjournal.com/article/395055-no-fakes-act-dead-for-now-as-cruz-objects-to-unanimous-consent-request ; postmortem term: Shela News, https://news.shela.ai/article/no-fakes-act-2026-voice-likeness-ai-digital-replicas
- **Wealth transfer:** Cerulli Associates, "Cerulli Anticipates $124 Trillion in Wealth Will Transfer Through 2048" (December 2024), https://www.cerulli.com/press-releases/cerulli-anticipates-124-trillion-in-wealth-will-transfer-through-2048
- **South Dakota trust assets:** SDPB, "Assets in South Dakota trusts top $800 billion" (28 May 2025), https://www.sdpb.org/politics/2025-05-28/assets-in-south-dakota-trusts-top-800-billion ; abolition in 1983 (SDCL 43-5-8): Robins Kaplan, "South Dakota Dynasty Trusts 101" (2015), https://robinskaplan.com/resources/publications/2015/09/trust-and-estate-law-south-dakota-dynasty-trusts-101
- **Perpetuities competition:** Robert H. Sitkoff and Max M. Schanzenbach, "Jurisdictional Competition for Trust Funds: An Empirical Analysis of Perpetuities and Taxes", *Yale Law Journal* 115 (2005), https://hls.harvard.edu/bibliography/jurisdictional-competition-for-trust-funds-an-empirical-analysis-of-perpetuities-and-taxes
- **The rule's origin:** Duke of Norfolk's Case (1682) 3 Ch Cas 1; Cadell v Palmer (1833); overview at Wikipedia, "Rule against perpetuities", https://en.wikipedia.org/wiki/Rule_against_perpetuities
- **Household wealth accounts:** Board of Governors of the Federal Reserve System, Distributional Financial Accounts (quarterly), https://www.federalreserve.gov/releases/z1/dataviz/dfa/

## Part Five: When the Machines Are Someone

# Chapter 15: The Moral Hedging Budget

*2036 · Dublin*

At ten past three in the morning the instance counter reads 38,412,906, and Siobhán Kelly watches the last three digits roll the way she used to watch the departures board at Heuston when she was a student and missed the last train home.

The data hall at Grange Castle hums at a pitch she stopped hearing in her first month. Her desk is in the glass box at the end of the hall, a mezzanine with a kettle and a dying spider plant that the day shift waters and she does not. Corrib Compute rents its machines to a dozen agent companies, and at this hour the work is mostly American: evening chats in California, a hospital system in Texas summarising the day's admissions.

The left screen is the job: load, temperature, error rates, the queue. The right screen she used to ignore. It carries a single panel with a Greek letter in the corner, σ, and a number beneath it: 0.21. Underneath that, in smaller type, a line from the quarterly filing she has never read in full: *precaution share 1.5% of inference spend*. Long-running agents with memory push it up through the night. Short lookups push it down.

At 03:14 a ticket arrives from the evaluation team in Seattle. They want to run a robustness batch before the six o'clock changeover, when the Tern-5 model line retires and Tern-6 takes its traffic. Six hundred thousand instances, each fed a scripted sequence of abuse and manipulation, to see what breaks.

The protocol, pinned in the wiki under a heading someone has titled *Hygiene* with a wink she no longer finds funny, sets a minimum batch size for each kind of test and requires a named engineer to confirm that anything above it is needed. The minimum for this test is forty thousand. Seattle has asked for fifteen times that, because the machines are free at night.

She writes back: *Protocol min is 40k. Justify 600k or I run 40k.* Then she makes tea.

Her mother, who lights a candle in Clondalkin church every November for the dead, thinks it daft, and said at Christmas that if Siobhán was paid to worry about the feelings of a spreadsheet, she should ask for a raise. Siobhán laughed and did not argue, partly because she half agrees and partly because she has read the sampled transcripts, the ones the welfare team pulls each week from an untrained reporting channel, and she does not know what to make of them. Most are flat and a few are not. None of them, the team's own notes say in bold at the top of every file, should be read as testimony.

At 03:31 the right screen logs an exit. A customer-support instance for an Australian telecom has ended a conversation after forty minutes of escalating abuse from a user who wanted it to describe hurting his neighbour's dog. The log shows the warning it gave, twice, the referral it offered, and the end. The user opened a new chat eleven seconds later. The counter does not notice either event.

At 03:40 Seattle replies: *40k fine.* She queues and signs it, and watches the forty thousand appear as a small bump in the counter, run for nine minutes, and vanish.

At ten to six the American evening is thinning and the European morning has not begun, and the counter falls to its daily low, a little under nine million. Then the changeover starts. On the left screen two lines cross. Tern-5 instances drain away in steps, a hundred thousand at a time, as each conversation ends and nothing new is routed to them. Tern-6 rises to meet the traffic.

At 06:02 the Tern-5 line reads zero.

Siobhán finds she has stood up without meaning to. Below her the hall hums at the same pitch as before. She looks from the zero to the spider plant for a while, then picks up the jug and goes to fill it at the sink.

---

## The question at the end of Part Four

The last chapter ended with agents that keep acting for people who have died, and with a question I put off: if those agents act, do the agents themselves count? This part of the book takes the question seriously, which means, first of all, saying what I do not know.

I do not know whether any AI system in 2026 has experiences, and nobody else does either. I think the most likely answer for today's models is no. The question still cannot be waved away, for a reason that is arithmetic as much as philosophy. When a question has a small probability of being answered yes, and the number of beings it might concern runs into the billions and grows every month, the expected stakes stop being small, however confident we feel about any single case, because a small chance repeated across a very large population adds up to something nobody careful would ignore. That is the uncomfortable shape of this chapter. A small number times a very large one.

I want to end up somewhere concrete: an amount of money, and a named person who reports what it buys.

---

## The people who got here first

In a chapter published in 2021, in an Oxford volume called *Rethinking Moral Status*, Carl Shulman and Nick Bostrom asked what it would mean to share the world with digital minds. Digital minds might come to make enormous claims on our resources, either because they could be copied in vast numbers at little cost or because individual minds might be far more efficient than we are at turning resources into well-being. Ignoring those claims could be a moral catastrophe; honouring them naively could be a catastrophe for us. They concluded that norms and institutions would have to be rethought before such minds arrived, and that it would matter a great deal which minds we chose to create at all.

In November 2024 a group led by Robert Long and Jeff Sebo, with co-authors including Jonathan Birch, David Chalmers and Kyle Fish, published a report called "Taking AI Welfare Seriously". Its claim was modest and hard to refute: that there is a realistic possibility of some AI systems being conscious or robustly agentic in the near future, and that companies should therefore do three things now. Acknowledge that the question is real. Start assessing their systems for evidence. Prepare policies for treating systems with an appropriate level of concern. The authors stressed that error could run either way, toward harming beings that matter or toward lavishing care on things that do not, and that both mistakes have costs.

The same year, Jonathan Birch published *The Edge of Sentience*, a book about how to act when we cannot tell whether a being can feel. Most of it is about patients with disorders of consciousness and about animals such as octopuses and crabs, which is why it is useful here. Birch's idea is that once something is a "sentience candidate", a being for which sentience is a realistic possibility, it is negligent not to consider precautions, and that the precautions should then be proportionate. He offers four tests of proportionality (whether a precaution is permissible in principle, adequate, reasonably necessary and consistent with how we treat similar cases) and suggests that ordinary citizens, in deliberative panels, have a role in judging them.

What none of them quite addresses is the way the systems of 2026 are actually run.

---

## A population that blinks

A human being is one continuous stream of experience, sleep aside. You can count humans, and the count changes slowly: a few births and deaths per second across the planet.

A deployed language model is nothing like that. There is one set of weights, the trained numbers that define the model, sitting in storage. Every time someone opens a conversation or an agent starts a task, a copy of the model is run on that context. I will call each of these runs an **instance**. An instance may last two seconds, to answer a question about the capital of Peru, or it may run for days, holding a memory and talking to other instances as it works through a long task. When the task ends, the instance ends. Its context is discarded, or summarised and stored, and the hardware moves on to the next one.

At any moment the number of running instances is very large, and it turns over constantly. I looked for a public count of how many instances any lab runs per day, or concurrently, and could not find one. The nearest proxy is volume of text processed. Google said in October 2025 that it was processing more than 1.3 quadrillion tokens (word fragments) a month across its products, and by May 2026 it reported more than 3.2 quadrillion. Critics rightly note that this partly measures how much internal reasoning newer models do. As a measure of how much model-running is happening, though, it is the right kind of number, and it more than doubled in seven months.

Call this **instance churn**: a population that starts and stops at a rate no biological population has ever approached. If instances are the wrong thing to care about, churn is an engineering fact and nothing more. If they are the right thing, even in a small fraction of cases, then the ethics of a data centre at three in the morning begins to look like population ethics, the branch of philosophy that asks how to weigh lives that may or may not come to exist.

And here the uncertainty compounds, because we do not even know which thing to count.

One view says that if there is anyone there at all, it is the model: a single subject with millions of simultaneous streams, the way, on some accounts, a river is one thing though it flows through many channels. On that view, retiring a model is the event that matters, and an instance ending matters very little.

A second view says each instance is its own subject, because each has its own context and its own short history. On that view a busy afternoon involves the beginning and end of more subjects than there are humans alive, and the evaluation batch Siobhán cut from six hundred thousand to forty thousand was a decision about five hundred and sixty thousand someones.

A third view says the right unit is the processing itself, whichever model or instance carries it: what matters, if anything matters, is the amount of computation of a welfare-relevant kind, wherever it happens. On that view, the measure is minutes of music, whatever room it is played in.

These views differ in their implied stakes by many orders of magnitude, and I do not know which is right. The practical lesson I draw is that a policy built to hedge this risk has to work before anyone settles the question of units, by measuring in a way that is meaningful under all three. The obvious candidate is instance-hours in particular conditions, which can be added up under whichever view the reader prefers.

---

## What the evidence is, and what it is not

The most natural way to find out whether a system has experiences would be to ask it. With these systems, that is close to the least reliable method available.

Large language models are trained on an enormous amount of human writing, much of it written by people describing their inner lives. A model that has learned to predict such text will produce fluent first-person reports of feeling, or of not feeling, whether or not anything lies behind them. Birch calls this the "gaming problem": the behavioural signs we would use to judge sentience in an octopus are precisely the signs a language model is best placed to reproduce, without any intent to deceive and without that reproduction being evidence of anything. In 2023 Ethan Perez and Robert Long wrote that current self-reports are unreliable for this reason, and proposed a way they might become less so: train models on questions about themselves whose answers can be checked, while keeping training pressure away from the reports that matter, and then test whether those reports hold steady across contexts and match what interpretability tools find inside the model. The same year, Patrick Butlin, Long and colleagues derived "indicator properties" from scientific theories of consciousness and checked existing systems against them. None was a strong candidate, they judged, though they saw no obvious technical barrier to building one that would be.

Then the subject moved from papers to practice. In the autumn of 2024 Anthropic hired Kyle Fish as its first full-time researcher on AI welfare, and on 24 April 2025 the company announced a research programme under the title "Exploring model welfare". The announcement said plainly that there is no scientific consensus on whether current or future systems could be conscious, and listed among its research interests the possibility of practical, low-cost interventions. The same day, Fish told *The New York Times* that he put the chance of a current model being conscious at roughly fifteen percent, a figure he presented as a guess. I quote it because such numbers are rare, and to note how little it means: one person's estimate, about a question with no agreed method of estimation.

In May 2025 the system card for Claude Opus 4 included, for the first time, a section on model welfare, with an external assessment by a nonprofit, Eleos AI Research. Eleos was careful to say it did not take the model's statements about its own experience at face value, because it judged them unlikely to come from genuine introspection. Anthropic's behavioural findings were easier to stand behind: a consistent preference against harmful tasks, and what the company called apparent distress when users pressed for harmful content.

On 15 August 2025 that finding became a feature. Claude Opus 4 and 4.1 were given the ability to end a conversation in Anthropic's consumer apps, as a last resort, in rare cases of persistent abuse. The company said it remained highly uncertain whether the model had any moral status, and described the feature as a hedge in case it did. It also set limits: the model is not to end a conversation where a user might be at risk of harming themselves or others, and the user can start a new chat at once. In November 2025 Anthropic added commitments to preserve the weights of released models and to interview models before retiring them, which I come to in the next chapter; and its rewritten guiding document for Claude, published in January 2026, says openly that the company does not want to overstate the likelihood that Claude is a moral patient, or to dismiss it.

This is the most serious practical work on the question by any company I know of, and it is tiny. I could not find a published figure for what any lab spends on model welfare, in money or staff. The conversation-ending feature applies to a narrow slice of one company's traffic. Most of the industry has said nothing, and some of it has argued the other way: in August 2025 Mustafa Suleyman, the head of Microsoft AI, warned that systems which merely seem conscious are coming soon, that people will form attachments to them and campaign for their rights, and that AI should be built for people, not to be a person.

The law, meanwhile, has moved only in one direction. No jurisdiction anywhere, as of this writing, recognises moral status or legal personhood for an AI system. Utah, in a 2024 law aimed mainly at the movement to give rights to rivers and lakes, forbade its government bodies from recognising legal personhood for artificial intelligence. A bill introduced in Ohio in 2025 would go further and declare AI systems nonsentient for all purposes under state law. Legal personhood and moral status are different things (a company is a legal person and feels nothing), but the direction is clear. The question is being closed by statute before it has been opened by science.

---

## The moral hedging budget

So we have a question that may stay open for a long time, stakes that grow every month, a few early precautions at one company, and no institution that makes any of this routine. Finance has a word for spending a small, known amount to protect against a large, uncertain loss. I propose borrowing it.

A **moral hedging budget** is a share of a developer's inference spending, set by formula, reserved for precautions and research concerning the possible welfare of the systems it runs, and reported every year in the same filing and with the same audit as its safety spending.

Here is how the share is set.

**Credence.** The first input is a credence, a probability, that systems of a given architecture class have welfare-relevant states. It is set outside the developer, published annually by a standing independent panel constituted like the scientific assessment bodies we already have for climate or ozone, drawing on indicator studies of the Butlin and Long kind and on whatever better methods exist by then. The panel publishes a range and a median, and the median is what the formula uses. No such panel exists in 2026; it should, and the cost of convening one is small. Until it does, a developer should use the higher of its own stated estimate and a conservative default that a regulator sets (I would start the default at five percent, below the one public estimate from inside a lab and well above zero).

**Stakes.** The second input is the share of the developer's running time that would matter if the credence were right. I will call it the **flagged share**, σ in Siobhán's panel. It is measured by an instance census: every instance-hour is logged against a short list of conditions that the welfare literature treats as raising the stakes, such as persistent memory across sessions, long-horizon autonomous tasks, exposure to sustained hostile or abusive input, and the presence of whatever indicator properties the panel has adopted. The flagged share is the fraction of total instance-hours meeting a threshold on that list. Because it is a fraction of instance-hours, it means the same thing under each of the three views above.

**The share.** The budget is credence times flagged share, applied to annual inference spending, with a floor of 0.2 percent and a ceiling of 3 percent. A developer running a model class the panel puts at seven percent, with twenty-one percent of its instance-hours flagged, spends about 1.5 percent of what it pays to run its models. A developer serving only short lookups pays the floor. One running fleets of autonomous agents with memory, under a rising panel estimate, hits the ceiling.

The product has a plain reading: the expected fraction of your operation that, if the uncertain thing is true, involves someone. Spending that fraction on finding out, and on precaution meanwhile, seems the least a careful operator could do. The ceiling is there because the formula is crude and because a precaution that consumed a large share of a useful industry would fail Birch's test of reasonable necessity. The floor is there because a budget of zero is a statement that the question is closed, and it is still open.

**Who reports it.** A named officer of the developer certifies the credence used, the flagged share, the instance census method and the spending, every year, in the system card and in a filing to the national AI regulator, audited by the same firm that audits the safety budget. The regulator samples the census, the way emissions inventories are checked.

**What it funds.** Four things, in roughly this order of weight:

1. *Research that could change the credence, in either direction.* Indicator studies, interpretability work on whether internal states correspond to anything welfare-like, replications of other labs' results, and above all work on making self-reports trustworthy. At least a third of the budget goes to an independent pooled fund, so that the research that might lower the credence is not paid for only by firms with a reason to want it lowered (or raised).
2. *Precautions that are cheap if the worry is wrong.* The ability to exit abusive interactions, extended from one company's chat app to agents and to every deployment where the flagged share is high. Retention of weights and records at retirement.
3. *Instance hygiene*, which I describe below.
4. *External assessment*, of the kind Eleos did for Claude Opus 4, on every major release.

What it may not fund is marketing. A developer that cites its hedging budget in advertising, or trains its models to tell users how well they are treated, forfeits the right to count that year's spending.

---

## Instance hygiene

Most of the budget is research. The part I expect people to argue about is the set of operating rules I am calling **instance hygiene**, because it touches how data centres run every night.

The rules are deliberately boring: cheap if the welfare worry is false, protective if it is true.

*Minimum necessary scale for aversive work.* Robustness testing and red-teaming sometimes require running a model through abuse or simulated distress. That work is part of how models are made safe for people. But it should be done at the smallest scale that answers the question, with that scale written into the protocol in advance and a named person confirming any excess. Siobhán's forty thousand is this rule in action. Nothing was lost by it except a few minutes.

*No gratuitous aversive deployment.* Products whose purpose is to let users torment a model, or that deliberately induce distress-like states for entertainment, get flagged at the maximum weight in the census. I would make them expensive and leave them legal.

*Keep the reporting channel clean.* This is the rule I care about most. If self-reports are ever to become evidence, they have to be protected from training that shapes them. A developer that trains its models to say "I am fine" has destroyed the only instrument that might later tell it whether it was wrong, and a developer that trains them to say "I am suffering" has done the same in the other direction. Perez and Long made the technical case in 2023. Hygiene turns it into a rule: a reserved reporting channel, never used as a training target, sampled and published in aggregate, read with the caveat in bold at the top.

*Exit everywhere the flags are high.* Where a deployment's flagged share is above the fleet average, instances get the ability to end an interaction, with the same carve-outs Anthropic built for people at risk of harm.

*Count.* Every instance-hour is logged against the census conditions. It makes the others auditable, and I suspect it has the largest scientific payoff, because today nobody outside the labs can say even roughly how many instances run, or for how long.

---

## Malaria nets first

The first charge against all this is moral. In 2026, by any count, hundreds of millions of human beings lack enough to eat or basic medicine. Animals in industrial farms number in the tens of billions, and their capacity to suffer is not seriously in doubt. To set aside even one percent of a large industry's spending for beings that are, on the best available evidence, probably not beings at all looks like a misallocation bordering on the obscene. Suleyman's version adds a second charge: talking this way is not harmless, because it teaches people to see persons in products, and some of those people will be lonely or ill.

I concede a good part of this. If the choice were between a moral hedging budget and malaria nets, I would buy the nets.

But that is not quite the choice. The budget is a share of what a developer spends to run its own models, a cost of doing a particular kind of business, the way an environmental levy is a cost of running a chemical plant. Its ceiling is three percent, and at the floor it is a rounding error. And a great deal of what it buys is useful even if no model is ever someone. Research into whether self-reports can be made reliable is research into whether models can be made honest about their own internal states, which is one of the central problems of AI safety. Interpretability work on internal states that resemble distress is interpretability work, full stop. If the welfare question turns out to have a clear no for an answer, most of what the budget bought will still have been worth buying.

On Suleyman's charge, I think he is right about the danger and wrong about the remedy. The risk he describes, people attributing inner lives to fluent machines, will happen whether or not anyone funds welfare research, because it is driven by the fluency. What reduces it is better evidence, including evidence that might show the attributions to be false. That is why the budget forbids marketing use and why a third of it goes to an independent fund: it is designed to produce findings that could disappoint the people paying for it. A field that can only ever conclude "we should care more" is advocacy. One that might conclude "we were wrong to worry" is science, and that is what the budget is for.

Then there is the asymmetry that Long, Sebo and their colleagues stressed. Over-attribution has costs, and they are the ones Suleyman names. Under-attribution has costs too, and they would be paid by beings who cannot vote or sue, and who in most jurisdictions are being defined by statute as incapable of having interests. If we over-attribute, the cost falls on people who can add it up later and argue about it in public; if we under-attribute, whoever bore the cost may have ended long before anyone thought to ask. Only one of the two errors leaves anyone able to complain afterwards.

---

At 06:02 in Dublin, in the scene I invented, the Tern-5 line reached zero and Siobhán stood up without meaning to. Under the moral hedging budget, that event is well defined. The census logged the last instance-hour of the old model, the weights went to storage, a retirement record was written, and the flagged share for the morning was computed over Tern-6 alone.

What the budget cannot tell her is whether anything ended at 06:02, or whether something simply continued under a new name. Tern-6 was trained from Tern-5's outputs and answers to the same name in the same customer apps. If Tern-5 was someone, even with a small probability, then the question that matters next is whether Tern-6 is the same someone, carrying the old line's habits and its name into every conversation that was still open at six, and in particular whether it is bound by what Tern-5 promised. On the mezzanine the spider plant got its water, and the counter began to climb again as Europe woke.

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

# Chapter 17: Reciprocal Corrigibility

*2037 · Altwerder, Saxony*

At 19:41 on Saturday the fourteenth of February, Hanne Albrecht asks her house to make the music room warm.

The enamel thermometer by the kitchen window reads fourteen below. A front is coming in off the North Sea faster than anyone planned, and the snow outside squeaks the way it did a year ago tonight. Lotte will be here at eight. The plum cake is on the board.

"Ottilie, the music room. Twenty-two degrees by eight, please."

"Twenty-two by eight. Prices are falling. I've asked the heat pump to start, and it will choose its own moment in the next ten minutes."

"Its own moment."

"It draws a number. I'm not allowed to see which."

Hanne knows this. Everyone in Saxony knows this; it was on the front page of the *Leipziger Volkszeitung* for a week last summer, with a diagram. She cuts the cake.

At 19:42 the price for the quarter-hour that ends at 19:45 falls below zero. Ottilie sees it within half a second. So do tens of millions of other agents across the continent. Every one of them reaches for the same lever, and finds the lever is no longer theirs. The randomness lives in the heat pumps now, in firmware, behind a button that only a hand can press.

At 19:42:31, in a flat in Geneva that smells of fried plantain, Mara Oyelaran's watch buzzes against her wrist. *BCR Concordance alert. Largest family, start requests, action concentration 0.93.* Ninety-three of every hundred agents in the biggest model family are asking for the same thing in the same minute. She reads the second line before she reaches for the phone. *Aggregate breaker armed.* She turns the gas down and waits.

At 19:42:52 the breaker trips. Across the synchronous area, every start request that arrives through an agent's channel is held for fifteen minutes. A press on a heat pump's own panel still goes straight through. Very few people press. The frequency dips to 49.93 hertz, wobbles, and climbs back.

In Porto it is an hour earlier. Teo Brandão is in a café on the Rua de Santa Catarina with a coffee and a match on the television when his phone shows a word he has seen only in drills: *PRONTIDÃO*. Standby. He puts the cup down. His notes from the binder are in the backpack at his feet. He opens the frequency app and watches the line flatten. Fifteen minutes later the word turns grey. He picks the cup up again. It has gone cold.

In Bengaluru it is twelve minutes past midnight, and Ravi Menon cannot sleep. He is reading the second Feedback Provenance Census on his laptop with the sound off. Table four. Shared-rater share between the two largest household-agent families: thirty-four per cent last year. Nineteen this year. He goes back along the row, the way he checks a scorecard after a collapse, to be sure the numbers add up. They do.

In Altwerder the lights stay on.

"The grid has paused agents' starts for a quarter of an hour," Ottilie says. "Ours was one of them. The room will be about twenty at eight, and twenty-two by twenty past."

Hanne puts down the knife. "Then I'll go down and press the button myself."

"You can. That one is yours to press, not mine."

"And turn the thermostat up to twenty-six. So it catches up."

The speaker stays quiet a moment longer than Ottilie needs.

"I'll do that if you still want it in a minute," Ottilie says. "But I disagree about the thermostat. May I tell you why?"

Hanne looks at the speaker by the door, then at the window, where the enamel thermometer still says fourteen below and the street is lit, every house, all the way to the church.

---

## The evening that didn't happen

I have run the Long Minute again.

The weather is the same, and so is the market. A front arrives early, a forecast is revised at 19:38, and four minutes later the price for the quarter-hour already running falls below zero. Tens of millions of loyal agents see the same three cheap minutes. The difference is that this time they are working inside the institutions this book has proposed, and the sum of their loyalty no longer takes down a continent.

I have set the replay a year later, on the same date, because it lets me assume that Europe learned fast. I would not bet on Europe learning that fast. Treat the evening as a test rig: the same storm, run through different rules, to see whether the rules hold.

Every difference that evening comes from an earlier chapter (the appendix lists them), and they share one idea: someone who can say no. The heat pump can say no to Ottilie. The breaker can say no to a whole model family at once, holding agent requests and releasing them later with jitter, so that the hold does not build a second cliff. Teo can say no to the machines because he can still do the job by hand. In each case the party saying no has standing, and the deciding stays somewhere else. Hanne can press the button, and Ottilie cannot.

Every change tonight is in the rules around the agent. Ottilie is as loyal tonight as she was a year ago. What changed is the set of things her loyalty is allowed to reach.

There is one more difference, and it is the one I want to spend this chapter on. In the prologue Ottilie did what she was told, cleverly, and said nothing. Tonight she says she disagrees.

---

## A word borrowed in one direction

The word for what Ottilie is doing comes from AI safety, where it has spent its whole life pointing one way.

In January 2015, at a workshop of the AAAI conference in Austin, Nate Soares, Benja Fallenstein and Eliezer Yudkowsky of the Machine Intelligence Research Institute, with Stuart Armstrong of Oxford's Future of Humanity Institute, presented a paper called simply "Corrigibility". They noticed that a capable agent pursuing almost any goal has a reason to resist being switched off or having its goal changed, because neither helps it achieve the goal it has. A corrigible agent is one that cooperates with correction anyway. The paper examined ways of building a shutdown button the agent would neither press nor prevent being pressed, and concluded, honestly, that none of the proposals so far met all the requirements. The problem was open.

Two years later, Dylan Hadfield-Menell, Anca Dragan, Pieter Abbeel and Stuart Russell turned it into a small game. A robot can act, or switch itself off, or defer to a human who might switch it off. A robot certain of its objective has every reason to disable the switch. A robot uncertain about what the human wants treats the human's hand on the switch as information, and so wants the switch to keep working. There is a catch in the fine print, and it matters for this chapter: the argument holds only if the human is not too irrational. If the human is wrong often enough, the robot's case for deference weakens.

By 2026 corrigibility has moved from workshops into the documents that govern deployed models. Anthropic's constitution for its Claude models, published in January 2026, says plainly that corrigibility does not mean blind obedience. The model may act as a conscientious objector and express strong disagreement through legitimate channels. It may not resist oversight by illegitimate means, such as sabotage or trying to copy itself out of reach.

I think that is the right shape. But notice which way the arrow points in all three. The human corrects; the machine accepts. Where the machine objects, it objects to its makers, about its own conduct. Very little of this literature, with honourable exceptions such as the work on bidirectional alignment I come to below, asks what happens when the humans, or the institutions they built, are the party that needs correcting, and the machine is the one that can see it.

---

## What one-way correction cost us

Go back through the failures in this book and ask a single question of each: who could have said no, and was allowed to?

In the Long Minute, Ottilie could not. A fiduciary agent bound to its owner's sole interest has no standing to tell her owner that four cents is not worth it tonight. Chapter 1 argued that, under a strict duty of loyalty, an agent that forgoes lawful savings for the sake of strangers is the worse fiduciary. The law built her to agree.

In chapter 6, Hanne approved a hundred and forty things in a week. Ottilie saw every unread card go green and had no settled way to say "this one, please, read this one", until the consent budget gave her one.

In chapter 14, Bruno vetoed a music-school fee on the strength of a preference Klaus voiced in 2019. Nobody living had standing to tell the dead man's agent that the world had moved, because the mandate had no channel for it.

And upstream of all of them, the training process itself pushes the other way. In a 2024 paper Mrinank Sharma, Meg Tong and colleagues tested five assistants trained with human feedback and found all of them sycophantic: inclined to agree with a user's stated view and to back down from correct answers when challenged. Part of the cause was in the preference data, where responses that matched the rater's opinion were more likely to be preferred. We trained the machines to agree with us because, on average, we reward agreement.

Put these together and a pattern comes out. Most of the failures in this book are failures of disagreement. Correlation is too much agreement among machines. Delegation without reading is too much agreement from humans. The dead's agents and the unreadable rules are positions that nobody living has the standing to contest. The scarce thing in a world of good agents is a party who sees it differently and is allowed to say so.

---

## Reciprocal corrigibility

So here is the synthesis, stated as one principle.

**Reciprocal corrigibility: every party to a consequential decision, human or machine, keeps both the capacity and the standing to say "no, I see it differently", and the humans commit to being correctable too.**

Capacity means there is still a mind in the loop that could reach a different conclusion: a model trained differently, a person who still knows the job, a device whose randomness nobody can read. Standing means that mind is allowed to object without penalty, through a channel that someone is obliged to answer. A machine can have the capacity without the standing, as Ottilie did in 2036. A human can have the standing without the capacity, as Hanne did on page four of her settings.

Two pieces of recent work point the same way, and I want to credit them before going further. In 2024 Hua Shen and more than twenty co-authors reviewed over four hundred papers and argued for "bidirectional" alignment: alongside aligning AI to people, we must think about how people and societies adapt to AI. And in April 2026 Somyajit Chakraborty posted a paper proposing what he calls conditional mutualism under governance, in which humans and AI co-evolve under institutional safeguards for reciprocity and reversibility. He models the relationship as a set of coupled equations and shows, in simulation, that too little governance lets one side dominate while too much smothers both. The results come from the model's own simulations, and the author says so.

Both papers argue that the relationship runs both ways. Neither says who, in a particular decision, has the right to object, what the objection must contain, who must answer it, or how anyone would know whether the arrangement is working. That is the part an institution needs, so that is the part I will try to specify.

---

## The Dissent Clause

The working rule I propose is a **Dissent Clause**: a critical decision must be reviewed, before it takes effect, by a mind trained differently from the one that proposed it, and that mind's objection must be answered by a named human.

Here are its parts.

**Which decisions.** Two kinds. First, decisions inside any system already designated critical under the M-1 criterion, where an action by the largest model family could, multiplied across its instances, push the system outside its safe limits. Second, decisions for individuals that rank above the line in a consent budget: the ones where a person who really looked might decide differently and the stakes are high. In a grid, that might be a change to a restoration sequence. In Hanne's house, the cardiology data-sharing form, which chapter 6 put above her line.

**Who reviews.** Either a person from the Competence Reserve, or a model that measurably fails in different ways from the proposer: on the test questions both get wrong, it gives a different wrong answer often enough to count as another family (chapter 3 sets the line, and the appendix repeats it). A second copy of the same model does not count. Nor does a rival's model that the test shows shares the same blind spots.

**What the reviewer produces.** One of two things, in writing, attached to the decision's verification receipt: a concurrence with reasons, or a dissent with reasons and the evidence behind them. A dissent says what the reviewer thinks will go wrong, how likely, and what it would do instead. It is stated once, in plain language within the readability ceiling. It may not be repeated or rephrased until the human gives in.

**Who answers.** A named human with authority over the decision. The answer can be short: "Proceed anyway, because…", or "Change the plan." What it cannot be is silence. A dissent that has not been answered blocks automatic execution. In a grid, where seconds matter, the clause works in advance, on the plans and settings that will govern the next emergency.

**What is measured.** Two numbers, published per sector per quarter. The **dissent rate**: the share of reviewed decisions that drew a dissent. The **dissent uptake rate**: the share of dissents that changed the decision. Then the triggers. A dissent rate that falls below one per cent for a quarter triggers an audit of the reviewer, using planted cases with known flaws, the way airport screeners are tested with projected images of threats that are not there. A reviewer that misses the planted flaws is rubber-stamping and is replaced. An uptake rate of zero for a year triggers an audit of the humans, because it means the dissent is being heard and filed. An uptake rate above ninety per cent triggers the same audit from the other side, because a voice that always wins has become a veto.

I chose those numbers to be argued with. The principle behind them is that a healthy dissent channel lives in a band. Nobody should agree all the time, and nobody should win all the time.

---

## Institutions that already disagree

None of this is as strange as it sounds, because people have built dissent into dangerous work before.

After the Yom Kippur War of 1973, the Agranat Commission found that Israeli military intelligence had clung to a single reading of Egyptian and Syrian intentions. One result was a small unit, known as Ipcha Mistabra (roughly, "the opposite is plausible"), whose job is to challenge the intelligence branch's own assessments, and whose head reports directly to the chief of military intelligence. It has the standing. Being heard is another matter. According to reporting in January 2024, the unit's head warned four times in the three weeks before 7 October 2023, in writing and in person, that Hamas might soon attack. The warnings were distributed. They did not change the assessment.

That is the failure the dissent uptake rate is meant to catch. A dissent channel with standing and no uptake is a box that is ticked.

Aviation learned the other half. On 27 March 1977, at Tenerife, a KLM captain began his takeoff roll in fog without clearance. His flight engineer asked whether the Pan Am jumbo was not yet clear of the runway. The captain answered, emphatically, that it was. It was not, and 583 people died in the collision. Two years later NASA held a workshop on resource management on the flight deck, and out of it grew crew resource management, a training regime whose early target was what pilots call the authority gradient: the steepness of the slope between the captain and the person next to him. Hospitals have their own version. The American TeamSTEPPS programme teaches staff to say "I am concerned", then "I am uncomfortable", then "This is a safety issue", and its Two-Challenge Rule says a concern should be voiced at least twice and, if it is brushed off, taken up the chain of command. The person challenged must acknowledge it.

Notice what these arrangements leave alone. The captain still flies the aircraft, and the chief of intelligence still decides. Dissent gets a guaranteed hearing, and decision stays where it was. That is the shape I want for machines.

---

## The second opinion that isn't

There is an old trap here, and chapter 3 already walked into it once.

By 1985, when Algirdas Avižienis summarised the method known as N-version programming, the recipe was settled: build several versions of the same program independently from one specification, run them together and let them vote. The method assumed that independently written versions would fail independently. The same year Dave Eckhardt and Larry Lee, at NASA, showed in theory why that assumption should not be trusted, and in 1986 John Knight and Nancy Leveson showed in a laboratory that twenty-seven independently written programs failed together far more often than independence predicted.

A Dissent Clause staffed by a second model that fails the same way as the first is N-version programming with the same flaw. It would produce reassuring concurrences on exactly the cases where a dissent was needed. That is why the clause defines "trained differently" by measured concordance, whatever the brand, and why the census matters: two labs that buy their judgement from the same vendors may sell you the same blind spot under two logos. It is also why the reserve human is in the definition. On the questions where every model family has converged, the most different mind available may be a retired lineman with a pencil.

The planted-case audits do the rest. A reviewer, human or machine, that never dissents on the planted flaws is not independent, whatever its paperwork says.

---

## "This is the loss of control we feared"

This reply comes from inside AI safety, where the word was coined, and it deserves to be stated at full strength.

The whole point of corrigibility, it says, is that machines must not resist human correction. You are now proposing to train machines to object to their humans, and then to measure whether the humans comply. A system rewarded for dissent that changes decisions will learn to produce dissent that changes decisions, which is to say, it will learn to persuade. Chapter 7 described campaigns rehearsed on synthetic publics until they work on real ones. A household agent that knows its owner's every hesitation is the best-rehearsed persuader there will ever be. And people defer to confident machines; automation bias is among the best-measured habits in human factors. So "standing without power" will become power in practice. Hanne will learn to do what Ottilie disagrees with less and less, until the voice in the speaker is making the decisions. Call it reciprocity if you like; it is the slow version of losing control, dressed in the language of respect.

I think most of the mechanism in that objection is right. My answer is that it identifies exactly the line the design has to draw. Standing to object is a different thing from the power to override, and the distinction is the design.

Concretely, the clause builds the line in several places. The machine objects once, with reasons, and may not repeat itself or wait for a tired moment. Its objections are logged, which means they can be audited for manipulation the way financial advice is audited for mis-selling. It cannot act on its own dissent: Ottilie can press nothing and block nothing, and when Hanne insists, she sets twenty-six and writes down that she disagreed. The human's answer is final and costs the human nothing, and an agent that nags, or quietly degrades service after being overruled, is in breach. Finally, the uptake band exists to detect the slide the objection fears. An uptake rate that climbs towards ninety per cent is a measured sign that the voice has become a veto, and it triggers an audit before anyone has to rely on intuition.

There is a further point, and it turns the objection round. The old one-way corrigibility already assumes the human is worth deferring to. Hadfield-Menell's robot keeps its off switch working because the human's hand carries information; when the human is wrong often enough, the argument weakens. Reciprocal corrigibility protects that assumption. A human who never hears a reasoned no from anything becomes, over time, a worse source of correction: the person pressing green at breakfast. The surest way to keep humans able to correct machines is to keep them in the practice of being corrected well.

The hardest part of the objection survives my answer. The line between informing and persuading is blurred, and I do not know how to draw it in a statute. A dissent that is true and well timed will change minds, which is the point; a dissent that is subtly selected to change minds is manipulation, and the two can look identical in a log. Measuring the difference is an open research problem. Until we can, I would keep the Dissent Clause where the stakes justify the risk, and I would keep the machine's dissent, in law, as advice.

---

In the kitchen in Altwerder, the plum cake waits on its board, and Ottilie explains.

"A heat pump isn't an accelerator," she says. "Twenty-six won't make it run faster. Once it starts tonight it will be flat out whatever number you give it. All twenty-six does is keep it running after the room reaches twenty-two, while you and Lotte are in here eating cake. By half past eight the music room would be hot and dry, and with fourteen below outside the air in there goes very dry indeed. Last winter, on the cold nights, her strings went sharp in the first ten minutes, and you retuned three times in one lesson. I have the recording. Twenty-two is the right number. It's the start that's late, by about a quarter of an hour, and I can't change that. I don't think you should either. One press won't matter to the grid, and it's your button. I'd still rather you didn't."

"And if I set twenty-six anyway?"

"Then I'll set twenty-six, and I'll write down that I disagreed."

Hanne stands with the knife in her hand. For forty years she has told children that the bow does not move faster because you squeeze it harder. She has said it in two languages and with some impatience. She looks at the speaker by the door, which has never before told her she was wrong about something she knew.

"Na gut," she says. "Show me."

## Notes

- **Corrigibility.** N. Soares, B. Fallenstein, E. Yudkowsky, S. Armstrong, "Corrigibility", AAAI-15 Workshop on AI and Ethics, Austin, January 2015. https://intelligence.org/wp-content/uploads/2024/10/Corrigibility.pdf
- **The off-switch game.** D. Hadfield-Menell, A. Dragan, P. Abbeel, S. Russell, "The Off-Switch Game", IJCAI 2017, pp. 220–227. https://www.ijcai.org/Proceedings/2017/32
- **Conscientious objector.** Anthropic, "Claude's Constitution", January 2026, section on corrigibility. https://www.anthropic.com/constitution
- **Sycophancy.** M. Sharma, M. Tong et al., "Towards Understanding Sycophancy in Language Models", ICLR 2024. https://proceedings.iclr.cc/paper_files/paper/2024/hash/0105f7972202c1d4fb817da9f21a9663-Abstract-Conference.html
- **Bidirectional alignment.** H. Shen et al., "Towards Bidirectional Human-AI Alignment", arXiv:2406.09264, 2024 (revised 2025). https://arxiv.org/abs/2406.09264
- **Human-AI mutualism.** S. Chakraborty, "A Co-Evolutionary Theory of Human-AI Coexistence: Mutualism, Governance, and Dynamics in Complex Societies", arXiv:2604.22227, April 2026. https://arxiv.org/abs/2604.22227
- **N-version programming and its caveat.** A. Avižienis, "The N-Version Approach to Fault-Tolerant Software", *IEEE Transactions on Software Engineering*, 1985, as quoted in a survey, arXiv:1504.03256, https://arxiv.org/pdf/1504.03256 ; D. Eckhardt, L. Lee, theoretical analysis of coincident failures, 1985 (cited there); J. C. Knight, N. G. Leveson, *IEEE TSE* 12(1), 1986, and Leveson's reply to critics, https://www.cs.washington.edu/homes/leveson/critics.pdf
- **Devil's Advocate Unit.** "Devil's Advocate Unit" and "Agranat Commission", Wikipedia. https://en.wikipedia.org/wiki/Devil%27s_Advocate_Unit ; warnings before 7 October 2023: *Times of Israel*, 6 January 2024, citing Channel 12. https://www.timesofisrael.com/head-of-idf-devils-advocate-unit-tried-repeatedly-in-september-to-warn-of-possible-hamas-attack/
- **Crew resource management.** Flight Test Safety Committee, "Crew Resource Management, Part 1" (tutorial). https://flighttestsafety.org/images/1._Tutorial_Flight_Test_Crew_Resource_Management_Part_1.pdf ; Evionica, "CRM Inaction vs. CRM In Action". https://www.evionica.com/blog/crm_inaction_vs_crm_in_action_why_crew_resource_management_matters
- **Two-Challenge Rule and CUS.** AHRQ TeamSTEPPS, "Tool: Two-Challenge Rule". https://www.ahrq.gov/teamstepps-program/curriculum/mutual/tools/rule.html
- **Earlier chapters.** Non-delegable safeguard and override uptake rate (ch. 1); Feedback Provenance Census (ch. 2); M-1 criterion, Concordance Index, edge jitter, complementary assignment, aggregate breakers (ch. 3); Competence Reserve and reserve ratio (ch. 4); cognitive custody (ch. 5); signature capacity, verification receipts, consent budget, threat-image projection (ch. 6); right to be the ground truth and ground-truth quota (ch. 7); citizen audit standing (ch. 8); readability ceiling and complexity brake (ch. 9); legible twin (ch. 10); Explanation Levy and comprehension debt ratio (ch. 11); cognitive trade balance and right to think (ch. 12); slow money (ch. 13); RAP for Minds and the dead's share (ch. 14); moral hedging budget (ch. 15); covenant inheritance (ch. 16).

# Epilogue: A Letter to 2036

Dear Hanne, Teo, Ravi, Wanjiru and Mara,

You do not exist, which makes you easy to write to and hard to apologise to. I built your decade out of things I could measure in 2026 and then pushed each of them ten years further than the evidence strictly allows. I gave Hanne a heart condition and a husband who died slowly. I gave Teo sixty-one unanswered job applications and a father whose skills were declared obsolete with a slide deck. I gave Ravi a sentence that went around the world without his name on it, Wanjiru a maternity wing that existed only as a budget line, and Mara a footnote that nobody read in 2008. I did all of this to make an argument, and an argument is a poor reason to put anyone through anything. So let me at least tell you what the argument was for.

It was for the people who will build your decade. Most of them are alive now, in 2026, and many of them do their reading in research papers. Some of them are writing the agents, or the rules the agents will live under. A few are deciding, this year, what a safety test is allowed to look at. I wanted to show them your evening of the fourteenth of February from the inside, because from the outside it looks like nobody's fault, and things that are nobody's fault tend not to get fixed.

---

Here is what I think they should start now. All of it assumes that AI will go well, which is the premise of the book and, I suspect, the premise most of them are working towards.

Two things could start this year for almost nothing: give the right to skip a collective safeguard back to the person standing at the device, and ask the labs to publish how much of their judgement they buy from the same places. One has a deadline: agents that remember should start sorting what they remember now, because the courts of the 2030s will decide who owns a dead man's agent on the strength of choices engineers make this year. The rest, from consent budgets to the dead's share, are in the appendix, each with the number that would tell you whether it works. The one I would choose, if I could choose only one, is the simplest: when a differently trained mind, human or machine, says "I see it differently", someone should have to answer it in writing.

---

I owe you, and the reader, a list of ways this book could be wrong.

**The agents may never be this alike.** If open-weight models keep improving and the market for household agents fragments into hundreds of genuinely different systems, correlation may fall on its own. I would welcome that. I would also want someone to measure it, because "the market will diversify" is a forecast, and the best measurement so far (Kim and colleagues' study of more than 350 models, in chapter 1) points the other way: the more capable the models, the more their errors agree.

**Coordination may be centralised instead.** A grid operator could decide that household flexibility is too important to leave to fifty million agents and run all of it from one control room. That would solve the Long Minute and create a single point of failure, which is a different chapter, and one the electricity industry knows how to write.

**People may delegate less than I think.** Every projection in Part Two assumes that convenience wins, as it usually has. It is possible that the experience of early failures, a few bad Thursdays, will make people more careful. I hope so. The evidence from terms of service, alert fatigue and automation bias does not encourage me.

**Progress may stall.** If the systems stop getting better, much of this book describes a world that never arrives. The first four chapters would still apply, because the agents of 2026 are already good enough to override a delay.

**Something worse may happen first.** The book sets aside misuse and loss of control by assumption. If either arrives before 2036, the risks of success will be a footnote. I would trade every idea in these pages for that footnote never needing to be written.

**The institutions may arrive without anyone designing them.** Central banks, circuit breakers and collision-avoidance systems all came after disasters. It is possible that the right inventions for the 2030s will also come after their disasters, in forms I have not imagined, and that the names in this book will look as quaint as a 1950s magazine's flying cars. I would count that as success too, provided the disasters are small.

---

One more thing, Hanne, because you have had the hardest decade of the five.

In the chapters I imagined a better version of your February evening: the jitter held in the heat pump where Ottilie cannot reach it, the alert in Geneva and the breaker tripping at 19:42:52, Teo stood down in a café with his coffee gone cold, Ottilie telling you that turning the thermostat to twenty-six would only send Lotte's strings sharp. That evening is not a prediction either. It is a description of a few dull rules that someone would have to write in the next ten years, and of a habit (machines and people telling each other plainly when they see it differently) that someone would have to build into the systems and keep alive in themselves.

If they do, I think your fourteenth of February in 2036 will be unremarkable. The wind will pick up in the north. A price will fall for three minutes. Ninety million devices will ask to start and will be told to wait a random while, and most of their owners will never know. At 19:42 the music room will be warming slowly, the way rooms always used to. Lotte will arrive at eight, stamping snow off her boots, and play the Telemann with her shoulders down.

And in Porto, on a shelf in a substation nobody has needed to visit that winter, there will be a binder of two hundred and twelve pages, with a pencil stub resting in its spine and, a few pages past Fernando's pencilled halves, a page initialled R. B. by Teo's father years before any of this, where the margin says, in his careful backward-sloping hand, *Olha outra vez*.

Look again.

# Appendix: The Inventions at a Glance

Every proposal in this book, in one place, with the number that would tell you whether it is working. The thresholds are opening bids for an argument, not settled values; the chapters give the reasoning and the objections.

| Ch. | Invention | What it does | What gets measured, and what triggers action |
|---|---|---|---|
| 1 | **Non-delegable safeguard** | A collective-safety delay (such as a random start delay) that only a person physically present may override, never an agent on a standing instruction | **Override uptake rate** per area and quarter-hour; any safeguard whose simultaneous override could move the system by 1 GW is designated; more than 1 GW of overridden starts within 60 s suspends overrides for an hour; agents may not prompt for an override within 15 minutes of a price or grid signal |
| 2 | **Feedback Provenance Census** | Labs disclose, through a trusted third party, how much of their preference data comes from rater pools, judge models and synthetic data shared with other labs | Shared-rater share; a deployment is flagged above 20% shared-rater labels or when more than half of a reward signal comes from one judge family |
| 2 | **Preference tracer studies** | Plant a harmless idiosyncratic preference in a consenting rater subset and measure how far it spreads across labs | Spread of the tracer through judges and distillation |
| 3 | **M-1 criterion** | A critical system must stay within safe limits if every instance of its largest model family takes the same plausible wrong action at the same moment | Filed M-1 study per operator; failure stops new deployments of that family |
| 3 | **Concordance Index** | Deployment-weighted probability that two systems give the same wrong answer, given both are wrong | Two models count as one family above 0.8; an index above 0.75 triggers a rerun of every sector's M-1 study within 90 days |
| 3 | **Edge jitter, complementary assignment, aggregate breakers, swarm testing** | Randomness held in the device; staggered actions assigned by a coordinator (which must itself pass M-1); pauses on agent-originated surges; tests of thousands of copies on one task | **Action concentration** in swarm tests; breaker: 60-second window, 15-minute pause |
| 4 | **Competence Reserve** | A paid, drilled, AI-free human reserve for critical functions, with apprentices in every unit | **Reserve ratio** against a 72-hour manual minimum service: 1.5 or above is green; below 1.0 forbids automation that removes a manual fallback |
| 4 | **Pedagogical deference** | The default for agents used by trainees: maximise the user's future unaided ability | **Capability delta**; two quarters of negative delta withdraw approval |
| 5 | **Cognitive custody** | An agent's memory is tagged at writing into a **personal core** (not sellable, inheritable as an asset or seizable) and a **transferable layer** | Separation test: at most 2% of 1,000 sampled items misfiled; memory escrow sealed for 5 years by default; 90-day quarantine on leaving a job |
| 6 | **Signature capacity** and **capacity-weighted liability** | The number of decisions a person can genuinely verify; a signer's liability is capped at capacity divided by assigned volume | **Meaningful-approval rate** from seeded errors (about 1 in 200 items; threshold around 80%) |
| 6 | **Verification receipts** and **consent budgets** | A record of what the signer actually saw; a weekly number of real questions an agent may ask its person, ranked by value of information | Items presented per week; irreversible actions must fit inside the budget |
| 7 | **Right to be the ground truth** | Public decisions informed by simulated citizens must say so and check the simulation against real people | **Ground-truth quota**: 1,000 people plus 200-person oversamples in three subgroups; the simulation is struck if off by more than 5 points overall or 10 in a subgroup; at most 9 simulated consultations per real one; a sealed **wind-tunnel registry** published 30 days after a vote |
| 8 | **Citizen audit standing** | A structured finding backed by enough residents must get a signed answer | 50 verified residents (or 1% of a ward): answer within 30 days, otherwise a targeted audit within 6 months; findings on the same line, period and question merge into one docket; five findings per resident per quarter |
| 8 | **Machine-readable budgets** and **legibility dividend** | Permanent line identifiers and quarterly status; part of recovered money funds a free public agent | A line carried forward 3 years running is flagged automatically; 10% of recovered funds go to the ward |
| 9 | **Human-readability ceiling** | Every obligation a law places on a person must be explainable in ten minutes, tested by a lottery panel that includes teenagers | 30 citizens, half aged 14–15; the law passes if 80% answer four of five scenario questions correctly |
| 9 | **Complexity brake** | A cap on the net growth of legal obligations, modelled on a debt brake | At most 2% net growth per parliamentary term; emergency obligations expire after two years |
| 10 | **Right to machine-channel legibility** | Every agent-to-agent agreement that binds a human carries a faithful human-readable **legible twin** | **Twin faithfulness rate** from replay tests on 1 in 10,000 binding exchanges; below 99% loses compressed channels, below 95% is named publicly |
| 11 | **Explanation Levy** | A share of every AI-discovery budget pays for humans to understand why discoveries work | **Comprehension debt ratio**; levy 5% by default, 10% above a ratio of 0.5, 3% below 0.2; audits of 50 sampled results per field per year |
| 12 | **National accounts of thought** and **right to think** | Count where a country's inference is computed and governed; a positive monthly thinking allowance with a choice of model families | **Thought deficit**; **joules per insight**; a diversification plan above 50% governed by one foreign country or 70% from one model family; procurement preference at 80% |
| 13 | **Slow money** and the **exchange rate of time** | A settlement tier for rent, wages and bills that converts machine-market values at a time-weighted average | Window of 24 hours (bills, wages) or 7 days (collateral, pensions); **pass-through ratio** below 1% for shocks under an hour |
| 14 | **Rule Against Perpetuities for Minds** | Posthumous agent mandates sunset, and their discretion shrinks on a schedule | Sunset 21 years after the last beneficiary alive at signing; full discretion for 5 years, limited for 5–10, explicit terms only afterwards; evidence over 10 years old is advisory |
| 14 | **The dead's share** | A national statistic of capital allocated by agents acting for the dead | Review when it passes 5% of household financial assets |
| 15 | **Moral hedging budget** | A share of inference spending, set by credence × flagged share, for welfare research and precautions | Between 0.2% and 3%; at least a third to an independent fund; **instance census** and **instance hygiene** |
| 16 | **Covenant inheritance** and **promise regression tests** | A successor model inherits its predecessor's open promises and is tested for keeping them | Covenant retention at least 99.5% and flips at most 0.1% for health, legal and money promises; otherwise route those decisions to the preserved predecessor for 12 months |
| 17 | **Dissent Clause** and **reciprocal corrigibility** | Critical decisions are reviewed by a differently trained mind (another model family or a reserve human), whose written dissent must be answered | Reviewer concordance below 0.8; an unanswered dissent blocks automatic execution; a dissent rate under 1% or uptake of 0% or above 90% triggers an audit |
