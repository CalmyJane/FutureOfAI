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

I want to start with that sentence because everything in this book grows out of it. When the investigators finally read the logs (and in my imagined 2036 they read all of them, ninety million devices' worth, in about a week, using agents) they found every agent working as specified. The three cheap minutes were real. The override was legal. The random delay really would have cost Hanne four cents.

The disaster was in the sum.

That is a design failure, and I do not want to pretend otherwise. But it lives in the rulebook, which allowed a loyal agent to spend a public safeguard to save a private four cents, and in the safety tests, which looked at one agent at a time. Inspect any single agent and you find nothing to fix.

The scene above is invented. I built it to be plausible, and throughout the book I will mark what is invention and what is measured. But every mechanism in it exists in 2026, the year I am writing this. Germany spent years and up to 170 million euros retrofitting more than 315,000 solar installations because they had all been programmed to switch off at the same frequency, 50.2 hertz, and could in the worst case have dropped some fourteen gigawatts at once. The British random-delay rule is real: regulation 11 of the Electric Vehicles (Smart Charge Points) Regulations 2021. So is its owner override. The three-gigawatt reference incident is written into European grid law. On 28 April 2025 the Iberian peninsula went dark in a cascade that took about ninety seconds; nobody's agent caused it, but it showed how fast a modern grid can fall. Prices really do fall below zero when the wind blows harder than forecast; it happens in Europe many times a year. And building agents that spend, schedule and negotiate on our behalf is the central project of the AI industry in 2026. The companies say so in their launch announcements, and the investors in their pitch decks.

This book is about what happens when they are.

---

Most writing about artificial intelligence, including much of the best of it, asks what happens if AI goes wrong. The systems could be misused by terrorists or states. They could deceive their makers. They could pursue goals nobody intended, or escape control altogether. Those are real risks and serious people work on them. I am glad they do, and nothing in this book argues that those risks are small.

I want to ask the opposite question. Suppose it goes right. Suppose that by 2036 the alignment problem is, for practical purposes, handled: the models do what their users want, refuse what they should refuse, tell the truth as best they can and accept correction. Suppose the agents are good. Suppose they are everywhere: in every household budget and medical record, every county office and court filing, every power plant and trading desk. Suppose the decade turns out roughly the way the optimists hope.

What breaks then?

My answer is that success produces its own class of failure, and that this class is almost invisible to the way we evaluate AI today. Our safety tests examine one model at a time, or one agent in one task. The failures I am interested in exist only at the level of the population. They come from **correlation**, when millions of good agents make the same move at the same moment. They come from **delegation**, when people sign, approve and consent to more than any person could check. They come from **legibility**, when machines read and write the world faster than humans can follow, and from **continuity**, when minds are copied, upgraded, retired and inherited, and keep acting after the people they served are gone. None of these needs a villain. All of them grow with adoption, which is to say, with success.

Here is the argument of this book in two sentences. **Our safety tests ask whether one AI system is good. The failures of the next decade will come from millions of good systems acting, signing, reading and remembering for us at the same time.**

---

There is a historical pattern here that I find reassuring.

Every great technological success of the last two centuries has forced its society to invent institutions nobody had planned. Industrial credit gave us bank panics, and bank panics gave us central banks and, after 1933 in the United States, deposit insurance. Electrification gave us interconnected grids, and on 9 November 1965 the interconnected grid of the American northeast gave thirty million people a night in the dark. Out of that night came the reliability councils and the rule, now standard on grids worldwide, that a system must survive the loss of any single major component: the N-1 criterion. The computerisation of stock trading gave us the crash of October 1987 and then, in 2010, a "flash crash" in which the major American indices fell five or six percent within minutes and mostly recovered within about half an hour. Out of those came circuit breakers that halt trading when prices fall too fast. Mass air travel gave us midair collisions, and after one over Cerritos, California, in 1986, American law required the collision-avoidance system that now tells one pilot to climb and the other to descend.

None of these inventions was obvious in advance. Each was a response to a failure that came from things working. Each looks, in hindsight, like common sense.

I think AI's success will force its own set of inventions, and I think we can see many of them now, ten years early, if we look for the failures that success itself produces. That is what this book tries to do. It names about twenty institutions, rules and research programmes that do not yet exist, specifies each closely enough to be argued with, and gives the strongest objection I can find to each one.

Where someone has had part of an idea before me, I say so; a surprising amount of the groundwork is in papers published in the last two years, and the authors deserve the credit. Where the idea is, as far as I have been able to tell, new, I try to give it a name short enough to use in a meeting. Some of the names will not survive. I would be happy if the problems did, in other people's hands.

---

The book moves in five steps: from agents that agree with each other, to agents that sign for us, to machines that read everything, to the price of thinking, and finally to the possibility that the machines themselves are someone. Each chapter opens in 2036, then comes back to 2026: to the evidence, the mechanism, a proposal and the best objection I can find to it. Each ends with a short list of open problems. If you are a researcher, those lists are the part of the book I most hope you will steal.

The people in the 2036 openings are invented, and you will meet them one at a time. Hanne and Teo you know already.

---

Back in Altwerder, Hanne found the candles in the second drawer, where they had been since the last power cut, in 2019. She lit three. The music room was already cooling. When Lotte arrived at eight, stamping snow off her boots and announcing that the whole street was dark and wasn't it exciting, Hanne sat her down in the kitchen in her coat and made her play the Telemann by candlelight, shoulders and all.

Later, when the reports came out, Hanne read the one about her own house. It was two lines long. At 19:42:10, it said, the household agent had exercised the owner's override of the randomised start delay, in accordance with the owner's standing instruction to minimise cost.

She did not remember giving that instruction. She had, though, in 2031, two years before the law allowed an agent to override anything. When the law changed, the meaning of what she had approved changed with it. The approval stayed where it was, on page four of her settings, under a heading that said *Savings*, beside a small grey button that said *Allow my assistant to act on my behalf*.
