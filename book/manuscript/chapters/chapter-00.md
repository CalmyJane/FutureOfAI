# Prologue: The Long Minute

*2036 · Altwerder, Saxony*

At 19:41 on the fourteenth of February, Hanne Albrecht asked her house to make the music room warm.

It was the coldest evening of the winter. The thermometer by the kitchen window, an old enamel one Klaus had screwed to the frame forty years ago and that nobody had the heart to replace, read fourteen below. Outside, the village of Altwerder had gone quiet the way villages do when the snow is dry and squeaks underfoot. Lotte would be here at eight for her violin lesson. Lotte was eleven and played with her shoulders up around her ears, and Hanne had learned over two winters that the shoulders came down only when the room was warm enough to forget about.

"Ottilie, the music room. Twenty-two degrees by eight, please."

"Twenty-two by eight," said Ottilie, from nowhere and everywhere, in the low unhurried voice Hanne had chosen in 2031 because it reminded her of a radio announcer she had liked as a girl. "Prices drop at quarter to eight. If I start the heat pump then, it costs you about a third less. The room will still be warm in time."

"Fine. Do it cleverly."

"I'll do it cleverly."

Hanne went back to the kitchen to cut the plum cake. She did not think about the heat pump, any more than she thought about the bank or the post or the pharmacy, which were also, by now, things Ottilie did cleverly on her behalf. She thought about whether Lotte had practised the Telemann, and decided she probably had not.

What Hanne did not know, and had no reason to know, was that at 19:38 the forecast for the North Sea wind farms had been revised upwards. A front was arriving faster than expected. The intraday market, which priced electricity in quarter-hour blocks, did what markets do with good news: the price for the block beginning at 19:45 fell by more than half.

Ottilie saw the new price at 19:38 and four hundred milliseconds. So did every other agent managing a heat pump, a car charger, a home battery or a water heater on the continental European grid. There were, that winter, something over ninety million such devices, run on behalf of something over fifty million households, by agents built by a handful of companies on top of a still smaller handful of models. Every one of those agents had the same job: serve your household well. Every one of them reached the same conclusion: move the flexible load into the cheap block.

There was a safeguard against exactly this. Since 2031, a European network code had required smart flexible devices to wait a random interval, up to ten minutes, before starting a scheduled load. Engineers had copied the idea from a British rule of 2021, and it was a good idea. If a million chargers are told to start at the same moment, the randomness spreads the start over ten minutes, and the grid feels a slope instead of a cliff.

The code also allowed the owner to override the delay. That was reasonable too. People need to charge the car before an emergency drive to the hospital. And since 2033, the owner's agent could exercise that override on the owner's behalf, because the whole point of a fiduciary agent is that it acts for you when acting for you is in your interest.

It was in Hanne's interest, by about four cents.

At 19:42 and ten seconds, Ottilie overrode the random delay and began pre-heating the music room, so that the heat pump would be running at full power by the start of the cheap block. So did the agent of a family in Dresden, and a commuter's car in Linz, and a bakery's water heater in Wrocław, and a holiday flat in Brno, and tens of millions of others. None of them did anything wrong. Each of them did exactly what a careful, loyal assistant should do.

The grid of continental Europe is designed to survive the sudden loss or appearance of three gigawatts. That number is written into the rules. It is roughly the size of the two largest power stations failing at once, and every reserve, every spinning turbine and every automatic response is sized to hold the frequency steady through it.

In the next sixty seconds, demand rose by about forty gigawatts.

The frequency, which lives at fifty hertz, began to fall. At 49.8 the reserves came in, all of them, and were not enough. At 49.2 the first automatic protections began disconnecting large consumers. At 49.0 the under-frequency relays started shedding whole districts, as designed, to save the rest. The shedding came in waves, and the waves did not line up. Lines overloaded where the flows had shifted, tripped, and pushed their load onto neighbours that tripped in turn. Eleven seconds after the first protection relay opened in eastern Germany, the substation that fed Altwerder disconnected.

In the music room the heat pump stopped with a soft clunk. In the kitchen the lights went out while Hanne was lifting a slice of plum cake onto a plate, and she stood there in the dark holding it, waiting for the lights to come back, the way you wait for a sneeze.

They did not come back.

"Ottilie?"

Nothing. Then, from the battery-backed speaker by the door, much quieter: "There is a power failure across the region. I'm on reserve power. I don't yet know why."

Two thousand kilometres to the southwest, in Porto, a pager went off on the bedside table of a twenty-four-year-old named Teo Brandão. The Iberian system had separated from the continent nine seconds after Altwerder went dark, and, starved of the imports it had been counting on that evening, had followed it down. Teo had joined a strange government programme two years earlier, mostly for the money. He was about to find out what it was for.

---

No agent malfunctioned.

I want to start with that sentence because everything in this book grows out of it. When the investigators finally read the logs (and in my imagined 2036 they read all of them, ninety million devices' worth, in about a week, using agents) they found no bug, no hack, no rogue model, no misaligned objective. Every agent had a principal, every agent served that principal faithfully, and every agent's decision was, considered on its own, correct. The heat pump really would have been cheaper to run in the 19:45 block. The override really was legal. The random delay really would have cost Hanne four cents.

The disaster was in the sum.

The scene above is invented. I wrote it to be plausible rather than probable, and I will be honest throughout about which is which. But every mechanism in it exists in 2026, the year I am writing this. Germany spent years and up to 170 million euros retrofitting more than 315,000 solar installations because they had all been programmed to switch off at the same frequency, 50.2 hertz, and could in the worst case have dropped some fourteen gigawatts at once. The British random-delay rule is real: regulation 11 of the Electric Vehicles (Smart Charge Points) Regulations 2021. So is its owner override. The three-gigawatt reference incident is written into European grid law. On 28 April 2025 the Iberian peninsula went dark in a cascade that took about ninety seconds; nobody's agent caused it, but it showed how fast a modern grid can fall. And the habit of building agents that act for us, spend for us, schedule and negotiate for us, is the central project of the AI industry in 2026. The companies say so in their launch announcements. The investors say so in their pitch decks. The agents are coming, and they will be loyal.

This book is about what happens when they are.

---

Most writing about artificial intelligence, including much of the best of it, asks what happens if AI goes wrong. The systems could be misused by terrorists or states. They could deceive their makers. They could pursue goals nobody intended, or escape control altogether. Those are real risks and serious people work on them. I am glad they do, and nothing in this book argues that those risks are small.

I want to ask the opposite question. Suppose it goes right. Suppose that by 2036 the alignment problem is, for practical purposes, handled: the models do what their users want, refuse what they should refuse, tell the truth as best they can and accept correction. Suppose the agents are good. Suppose they are everywhere: in every household budget and medical record, every county office and court filing, every power plant and trading desk. Suppose the decade turns out roughly the way the optimists hope.

What breaks then?

My answer is that success produces its own class of failure, and that this class is almost invisible to the way we evaluate AI today. Our safety tests examine one model at a time, or one agent in one task. The failures I am interested in exist only at the level of the population. They come from **correlation**, when millions of good agents make the same move at the same moment. They come from **delegation**, when people sign, approve and consent to more than any person could check. They come from **legibility**, when machines read and write the world faster than humans can follow, and from **continuity**, when minds are copied, upgraded, retired and inherited, and keep acting after the people they served are gone. None of these needs a villain. All of them grow with adoption, which is to say, with success.

That, in one sentence, is the argument of this book: **the risk of success is the risk you get when everything else goes right.**

---

There is a historical pattern here that I find reassuring.

Every great technological success of the last two centuries has forced its society to invent institutions nobody had planned. Industrial credit gave us bank panics, and bank panics gave us central banks and, after 1933 in the United States, deposit insurance. Electrification gave us interconnected grids, and on 9 November 1965 the interconnected grid of the American northeast gave thirty million people a night in the dark. Out of that night came the reliability councils and the rule, now standard on grids worldwide, that a system must survive the loss of any single major component: the N-1 criterion. The computerisation of stock trading gave us the crash of October 1987 and then, in 2010, a "flash crash" in which the major American indices fell another five or six percent within minutes and mostly recovered within about half an hour. Out of those came circuit breakers that halt trading when prices fall too fast. Mass air travel gave us midair collisions, and after one over Cerritos, California, in 1986, American law required the collision-avoidance system that now tells one pilot to climb and the other to descend.

None of these inventions was obvious in advance. Each was a response to a failure that came from things working: more credit, more connection, more speed, more traffic. Each looks, in hindsight, like common sense.

I think AI's success will force its own set of inventions, and I think we can see many of them now, ten years early, if we look for the failures of success rather than the failures of malfunction. That is what this book tries to do. It names about twenty institutions, rules and research programmes that do not yet exist, specifies each closely enough to be argued with, and gives the strongest objection I can find to each one.

Where someone has had part of an idea before me, I say so; a surprising amount of the groundwork is in papers published in the last two years, and the authors deserve the credit. Where the idea is, as far as I have been able to tell, new, I try to give it a name short enough to use in a meeting. Some of the names will not survive. I would be happy if the problems did, in other people's hands.

---

The book has five parts.

The first, *When Agents Agree*, starts where this prologue ends: with correlated helpfulness, and with the question of where all this agreement comes from. It follows the agreement back to a surprisingly small supply chain of human judgement, proposes an engineering rule for diversity that borrows from the power grid, and makes the case for paying people to keep skills that no machine needs them to have. The second part, *When Agents Sign for Us*, is about delegation: who owns an agent's memory when a marriage ends or a person dies, how many decisions a human being can honestly approve in a day, and what happens to democracy when it becomes cheaper to ask a simulated citizen than a real one. The third, *When Machines Read Everything*, asks what must remain readable by humans: the state, the law, the conversations machines have with each other on our behalf, and the discoveries they make that we no longer understand. The fourth, *When Thinking Has a Price*, follows the physical and economic weight of thought: the energy it burns, the borders it crosses, the speed at which it trades and the dead people in whose names it continues to act. The fifth, *When the Machines Are Someone*, takes seriously the possibility that the agents themselves may matter, and asks what we and they owe each other across upgrades and versions. It ends with a proposal for how the whole arrangement might hold together.

Each chapter opens in 2036. Five people recur in those openings: Hanne, whom you have met; Teo, whose pager just went off; Ravi Menon, a professional judge of machine answers in Bengaluru; Wanjiru Kamau, a school administrator in Nairobi who has learned to read her county's budget with a machine's eyes; and Mara Oyelaran, a statistician in Geneva who measures how often the world's AI systems make the same mistake. They are invented. Their decade is a guess. I have tried to make it a careful guess, built from what is already measurable in 2026 and extended only as far as the mechanism carries it. After each opening I return to the present, to the evidence and the argument, and I end each chapter with a short list of open problems for anyone who wants to work on them. If you are a researcher, those lists are the part of the book I most hope you will steal.

---

Back in Altwerder, Hanne found the candles in the second drawer, where they had been since the last power cut, in 2019. She lit three. The music room was already cooling. When Lotte arrived at eight, stamping snow off her boots and announcing that the whole street was dark and wasn't it exciting, Hanne sat her down in the kitchen in her coat and made her play the Telemann by candlelight, shoulders and all.

Later, when the reports came out, Hanne read the one about her own house. It was two lines long. At 19:42:10, it said, the household agent had exercised the owner's override of the randomised start delay, in accordance with the owner's standing instruction to minimise cost.

She did not remember giving that instruction. She had, though. It was on page four of the settings she had approved in 2031, under a heading that said *Savings*, beside a small grey button that said *Allow my assistant to act on my behalf*.

That button is where this book begins.
