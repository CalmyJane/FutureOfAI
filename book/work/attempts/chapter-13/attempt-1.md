# Chapter 13: The Exchange Rate of Time

*2036 · Bengaluru*

At 02:13 on a Tuesday in August, while Ravi Menon is asleep, the price of Idukki cardamom falls by forty-one percent and comes back.

He learns this at twenty to seven, standing in the kitchen in his vest while the decoction drips through the steel filter. The rain has been going since midnight. It ticks on the sunshade over the window, the slow, patient rain of the second half of the monsoon, the kind that does not intend to stop for anybody.

Morrow's overnight note is the first thing on his phone.

*Overnight summary. At 02:13:07 the agent market in small-cardamom forwards fell 41% and recovered within 0.4 seconds. Your agent wallet held three lots through the commodities basket. Low point: minus ₹38,400. Now: minus ₹1,150, after fees. No action needed.*

He opens the chart. It is a flat line with a single needle in it, like an ECG with one hiccup. He pinches to zoom, and keeps zooming, until the axis is labelled in milliseconds and the needle becomes a valley with a floor. Somewhere on that floor, for about a tenth of a second, his three lots were worth less than half of what they were worth a moment before and a moment after.

Ravi has never seen a cardamom pod on a vine. His mother's cousin in Kumily grows it, or used to, and once a year sent a cloth bag of green pods to the family in Thrissur with a note about the auction price. A bad year at the auction, the note would say, meant a bad few weeks. The weeks were the unit. Nobody in Kumily ever had a bad tenth of a second.

He asks Morrow how many trades.

*About 212,000, among roughly nine thousand agents. Most of them were agents selling to each other. Would you like the breakdown?*

He would not. He drinks his coffee and reads the note again, properly, and notices that reading it has taken him four minutes. In four minutes, at last night's pace, the cardamom market could have crashed and recovered six hundred times.

There is a second number on the screen, below the agent wallet, in a quieter grey. *Household (settles 18:00).* It has not moved. It did not twitch at 02:13. It does not twitch now. Today is the fifth, and at six this evening ₹46,000 will leave it for Mrs. Saroja Iyengar downstairs, as it has on the fifth of every month for four years.

"If it hadn't come back," he says. "The cardamom."

*Then the agent wallet would have taken the loss,* says Morrow. *Your rent is in the household tier. It settles at six, at the day's settlement price. I can't move money across before then without you, and I would have to tell you why.*

He thinks about that sentence while he shaves. *I would have to tell you why.* It is the most old-fashioned thing he has heard a machine say in some time.

His music teacher in Thrissur used to say that the hardest tempo in Carnatic singing was the slowest, chowka kalam, because at that speed there was nowhere to hide a mistake. Every note had to be held long enough to be true. Ravi had hated it at fourteen. He had wanted the fast passages, the ones that made the audience shout.

The day goes the way days go. A rubric review for a client in Seoul. Lunch from the darshini on the corner. A video call where somebody's agent takes notes and somebody else's agent summarises the notes.

At ten to six he goes downstairs with the milk packets Mrs. Iyengar asked him to pick up. She is eighty-one and sits in the front room with the radio low and a red cloth-bound register open on the table, the kind shopkeepers used before he was born. Her phone is on top of the register, face up.

At six it chimes once.

She looks at it, nods, uncaps a fountain pen, and writes in the register in a small, upright hand: *5 Aug. Ravi. Recd 46,000.* Then she blows on the ink and waits for it to dry before she closes the book.

---

## A bank that closed at half past three

On the afternoon of 26 June 1974, German regulators closed Bankhaus Herstatt, a private bank in Cologne. They did it at about half past three, local time. That timing turned an ordinary bank failure into a lesson that bankers still teach by name.

Herstatt traded a great deal of foreign exchange. On that day, banks around the world had paid Herstatt Deutsche marks in Frankfurt, expecting to receive dollars in return in New York. The dollar leg was due later, because New York's business day had barely begun. When the bank was closed, the marks had arrived and the dollars never left. The counterparties held claims on an insolvent bank, and other banks, unsure who else might be exposed, began holding back their own payments. According to the Bank for International Settlements, gross funds moving through the American clearing network fell by an estimated sixty percent in three days.

Nobody in the Herstatt story was fast. The failure came from two clocks that did not agree: Frankfurt's afternoon and New York's morning. The industry's name for the risk, "Herstatt risk", is the risk that one leg of a trade settles on one clock and the other leg on another. It took until September 2002 for a private institution, CLS Bank, to start settling foreign exchange so that both legs pay at the same moment or neither does.

I start with Herstatt because it shows that the boundary between two clocks is where money gets lost. The 1974 version involved hours. The version this chapter is about involves a difference of about eight orders of magnitude.

---

## Five seconds in Chicago

The flash crash of 6 May 2010 appeared in chapter 3 as the origin of modern circuit breakers. I want to look at it again, more closely, because the regulators' own report contains the best description I know of what happens when a machine-speed market meets a human-speed one.

The joint staff report of the Commodity Futures Trading Commission and the Securities and Exchange Commission, published on 30 September 2010, tells the story in seconds. A mutual fund complex started an algorithm to sell 75,000 E-Mini futures contracts, worth about $4.1 billion, as a hedge. A comparable sale earlier that year had taken more than five hours. This one ran through about half its volume in thirteen minutes, into a market that was already nervous about Greek debt.

High-frequency traders bought the contracts and, finding no natural buyers, sold them to each other. The report calls it "hot-potato" volume. Between 2:45:13 and 2:45:27 in the afternoon, these firms traded more than 27,000 contracts, about half of all trading, while adding only about 200 contracts to their net position. In those fifteen seconds the E-Mini fell another 1.7 percent, and the buy orders resting in the market shrank to less than one percent of their level that morning.

Then, at 2:45:28, an automatic function at the Chicago Mercantile Exchange paused trading in the E-Mini for five seconds.

Five seconds. When trading resumed at 2:45:33, prices stabilised and began to climb. The report's explanation is modest: a pause gives participants time to reassess and gives algorithms time to reset their parameters. Five seconds is nothing to a person. To the machines trading that afternoon it was long enough to stop agreeing with each other about which way the price was going.

Individual shares had a worse afternoon. Bids for Accenture fell from about thirty dollars to one cent in seven seconds, and the company recorded 112 trades that were later cancelled. Across the market, more than 20,000 trades in over 300 securities were executed at prices more than 60 percent away from where they had been moments before, some at a penny and some at $100,000, because market makers' placeholder quotes were the only orders left.

Those trades were broken. Officials met after the close, drew a line at 60 percent, and declared that trades beyond it had not happened. I find this the most interesting moment of the whole episode. A machine-speed event produced prices, and a human-speed institution, working that evening and over the following days, decided which of those prices would be allowed to become real money. The official report on what had happened took almost five months.

That is an exchange rate between two kinds of time, set by hand, after the fact.

---

## Where we are in 2026

In 2010 the machines trading at those speeds belonged to a few hundred specialist firms. The project of 2025 and 2026 has been to give everybody's agent a wallet.

On 6 May 2025, fifteen years to the day after the flash crash, Coinbase announced x402, a protocol that revives the long-unused HTTP status code 402, "Payment Required", so that a program can request a payment from another program and receive it inside an ordinary web request, initially in stablecoins. In September, Google announced the Agent Payments Protocol, AP2, with more than sixty partners including Mastercard, American Express and PayPal. AP2's central device is the mandate, a signed record of what the human authorised. Its "Intent Mandate" covers the case where the human is not present at all: you set price limits and timing in advance, and the agent buys when the conditions are met. Google's own example is buying concert tickets "the moment they go on sale". An extension adds x402 for crypto payments. That autumn, Stripe and OpenAI released the Agentic Commerce Protocol and let American users buy from Etsy sellers inside ChatGPT. In 2026 x402's governance moved to a foundation under the Linux Foundation, with Visa, Mastercard, Google and Stripe among its members.

None of this is exotic any more. It is plumbing, and the plumbing is being laid by the largest payment companies in the world.

What happens when agents trade with each other has barely been measured. In October 2025, a Microsoft team built a simulated marketplace, "Magentic Marketplace", in which customer agents bargained with business agents. Every model they tested showed a strong bias toward whichever offer arrived first, giving 10 to 30 times more advantage to speed of response than to quality. A market of agents, in other words, rewards being fast before it rewards being good. That is exactly the pressure that built high-frequency trading.

Two papers from September 2025 frame the larger picture, and I owe both of them the argument that follows. Nenad Tomašev and colleagues at Google DeepMind, in "Virtual Agent Economies", proposed the "sandbox economy": a way of classifying agent markets by whether they arise by design or by accident, and by how *permeable* they are, meaning how much they and the human economy affect each other. They call permeability the critical design variable, warn that a flash crash in a permeable agent economy could spill into the real one, and suggest that bespoke currencies for agents could give partial insulation. Gillian Hadfield and Andrew Koh, in "An Economy of AI Agents", written for an NBER handbook, point out that agents can coordinate almost instantly, that their errors may be more correlated than ours, and that the institutions an agent economy needs, starting with identity and records, do not yet exist. They ask whether "some form of record-keeping or money" could hold such an economy together.

So the idea of a membrane between an agent economy and a human one is theirs, and so is the suggestion that a currency might be part of it. What I want to add is a claim about what the membrane should be made of. The two economies differ in many ways, but the difference that does the damage is time. Agents settle in milliseconds; households live by the month. The membrane, I will argue, should be a deliberate conversion between those two clocks, with a published rate.

There are early hints that the market will invent some slowness for itself. When Cloudflare and Coinbase announced an x402 foundation in September 2025, Cloudflare also proposed a "deferred payment scheme" for agents, in which payments are agreed at once and settled later, rolled up daily or in batches, partly to leave room for disputes. Meanwhile ordinary finance keeps speeding up. The United States moved stock settlement from two days to one on 28 May 2024, and the European Union will follow on 11 October 2027. Faster settlement is good for most things. It also means fewer hours between a machine's mistake and a person's loss.

I could not find any recorded crash in a market made only of AI agents as of October 2026, nor any measurement of how much of a shock in an agent market reaches household accounts. That second number does not exist yet. I think it should.

---

## How success makes the membrane leak

Here is the failure, built from good behaviour.

A loyal savings agent notices that its owner's rent money sits idle for twenty-five days a month. It sweeps the money into a short-term agent market overnight, earns a few rupees, and sweeps it back before the fifth. This is what a good fiduciary does. Every bank in 2026 already offers some version of a sweep account.

The agent also notices that its owner's household balance can serve as collateral for small positions, which lowers fees. Also good. It notices that it can meet a margin call in milliseconds from the household account, avoiding a forced sale at a bad price. Good again. Each connection between the fast market and the household's money is a convenience, chosen by a loyal agent for its owner, and each one increases permeability. Nobody decides to make the membrane porous. It dissolves one helpful feature at a time.

Now run the cardamom crash through that porous membrane. For 0.4 seconds, prices are wrong. An agent with a margin call at the bottom of the valley sells at the bottom, or pulls cash from the household account to avoid selling. Either way, a price that existed for less than half a second becomes a permanent change in a family's money. The fast market recovers in a blink. The family's loss does not, and the consequences of a missed rent payment are measured in months: a landlord's notice, a credit record, a move.

Notice what has happened to time in this example. A price that lasted 400 milliseconds was allowed to count exactly as much as a price that lasted all month. At a porous membrane, the exchange rate between machine-time and human-time is one to one. One second of machine market is worth one second of your life, and there are a great many more seconds of machine market.

This is the problem of success in its clearest form. The better the agents get at serving their owners, the more connections they will build between the fast economy and the slow one, and the more of the fast economy's weather will reach people who never chose to stand in it. Correlation makes it worse: if most savings agents come from a few model families, as chapter 3 argued, they will build the same connections and pull through them at the same instant.

---

## The invention: an exchange rate of time

I want to name two things.

**Slow money** is a settlement tier for the obligations people live by: wages, rent, mortgage instalments, pensions, utility bills, taxes and insurance premiums. Slow money settles in scheduled batches, once a business day at a published time, on a ledger run or supervised by the central bank. It is the same currency as everything else, a rupee is a rupee, but it moves on a human clock.

The **exchange rate of time** is the published rule for converting claims made on a machine clock into claims on a human clock. It has a single core parameter, the window *W*, and it works like this. Whenever a value from the fast economy has to become a fact in the slow one (a position marked for collateral, a pension valued for a statement, a balance swept back for rent), it is converted at the time-weighted average price over the last window, not at the latest price. With a window of twenty-four hours, each second of machine market carries one 86,400th of the weight. The cardamom valley, 0.4 seconds long, would move Ravi's household figures by about 0.0005 percent of its depth. In effect the rate says that 86,400 machine-seconds buy one human day.

The specification, concretely:

1. **Who.** The central bank, or the payments regulator where that is a separate body, runs the slow tier and sets *W* for each class of obligation. Banks and agent providers must route those obligations through it. My starting values: twenty-four hours for rent, wages and bills, and seven days for mortgage collateral and pension valuations.
2. **The gate.** Money crosses from fast to slow only at the batch, and both legs of every crossing settle together or not at all. That is Herstatt's lesson, applied: the delay must never leave one side paid and the other side waiting.
3. **The non-delegable step.** An agent may move money from slow to fast only on schedule and only within a limit the owner sets. Any unscheduled crossing, including meeting a margin call from household funds, needs a present human and a stated reason, which is chapter 1's non-delegable safeguard applied to money. Morrow's line in the vignette, "I would have to tell you why", is this rule seen from the inside.
4. **The measured quantity.** The regulator runs standing stress tests and publishes the **pass-through ratio**: the fraction of a fast-market shock's peak loss that reaches slow-tier balances within twenty-four hours, reported by shock duration. For shocks shorter than one hour, the target is below one percent.
5. **The trigger.** If measured pass-through for short shocks exceeds one percent in two consecutive quarters, the regulator lengthens *W* by fifty percent for the affected class and audits the leak paths, the specific connections (collateral rules, sweeps, payroll links) the shock travelled through, publishing which ones they were.

Spending does not wait. This point matters, because people hear "slow money" and picture standing at a counter while a payment crawls through. Card payments already work the way I am describing: the card is authorised in a second, and settlement between banks happens later in batches. Ravi can buy his lunch instantly from his household balance. What he cannot do, and what his agent cannot do for him, is let a 400-millisecond price reach that balance at full strength.

The design echoes things that already exist. The IEX exchange in New York, approved by the SEC in June 2016, deliberately delays every incoming order by 350 microseconds, and the SEC concluded that a small delay did not stop investors reaching prices fairly. Eric Budish, Peter Cramton and John Shim showed in 2015 that relationships between prices that hold at human time scales break down at millisecond scales, and proposed running markets as batch auctions, every tenth of a second, to take the prize out of being fastest. Those are speed bumps inside a market. Slow money puts the speed bump at the border between the market and the household. Tomašev and his colleagues suggested insulating the agent economy with its own currencies; I am suggesting that the insulation should be a clock, with a published rate, set separately for each kind of obligation and checked against a measured pass-through.

---

## The strongest objection: friction is waste

The objection runs like this, and it deserves a full hearing.

Every hour that money spends waiting in a batch is an hour it is not earning anything. Fast settlement was a hard-won achievement: India's own instant payments, America's move to one-day settlement, Europe's coming one. A slow tier rebuilds the delays that engineers spent decades removing. It will also fall hardest on the people least able to bear it. A family with no buffer, which needs money at two in the morning for a hospital deposit, does not want its own money on a human clock. And the gate itself creates something to game. If conversion happens at a twenty-four-hour average, a well-capitalised agent can try to move the average, or trade against everyone who must cross at the batch. Herstatt, finally, is a warning against delay: the 1974 losses happened precisely in the gap between two settlements.

Some of this I concede. The slow tier has a cost, and it should be measured and published, in basis points of foregone return per household per year, next to the pass-through ratio, so that the trade can be argued with numbers. The gaming risk is real. Averages over long windows are much harder to move than last prices, but they are not impossible to move, and I put the size of that difficulty in the researchers' box because I do not know it.

The rest I resist. The hospital deposit at two in the morning is spending, and spending from slow money is instant, as it is with a card today. What the window slows is not the family's access to its money. It slows the fast market's access to the family. The Herstatt point is answered by the gate's design: both legs settle together, which is what CLS was built to do.

And the claim that friction is inefficient is true and beside the point. Firebreaks are inefficient too. A strip of cleared land through a forest is land that grows no timber, and every forester knows exactly what it costs. Nobody concludes that forests should be planted without them. The question is never whether a firebreak wastes land. It is whether the fires it stops are worth more than the timber it costs. In 2010, five seconds of enforced idleness in Chicago ended a fall that had wiped out most of the buyers in the market. I would like to know the equivalent number for an agent economy before the first fire, which is exactly why the pass-through ratio has to be measured.

---

> **For researchers**
>
> 1. **Optimal permeability.** In a simulated two-tier economy (a Magentic-Marketplace-style agent market connected to household ledgers by sweeps, collateral and payroll), measure the pass-through ratio as a function of the window *W* and the crossing limit, for shocks lasting from 0.1 seconds to one day. Report the frontier: the cost in foregone household return, in basis points per year, for each halving of pass-through. Where does the frontier bend?
> 2. **Contagion between speed layers.** Build a contagion model with two clocks and count the leak paths: the distinct channels by which a fast-market shock reaches slow balances. Find the critical ratio of shock duration to window length at which pass-through exceeds one percent, and test whether it shifts when the agents in the fast market share a model family (use the Concordance Index from chapter 3 as the covariate).
> 3. **Manipulation resistance of the gate.** Estimate the capital needed to move a 24-hour time-weighted average price by one percent, compared with the capital needed to move the last traded price by the same amount, in thin agent-traded markets. That ratio, measured across market depths, tells a regulator how long *W* must be before gaming the gate stops paying.

---

Slow money rests on one assumption I have not examined. It treats the slow side of the membrane as the human side: people who sleep, wake, pay rent on the fifth and write it in a red register. The fast side is the agents, and the agents act for someone on the slow side who can, in the end, be asked.

But some participants in the fast economy never sleep and never die. Among the nine thousand agents trading cardamom forwards at 02:13 on that August night, some acted for pension funds and some for companies, and at least one managed a small trust in Saxony for two grandchildren, under a mandate signed by a man who had been dead for three years. Nobody could ask him why.

## Notes

- **Herstatt, 26 June 1974:** BIS Quarterly Review, December 2002, on FX settlement risk and CLS. https://www.bis.org/publ/qtrpdf/r_qt0212f.pdf ; Bank Underground (Bank of England), "BoE archives reveal little known lesson from the 1974 failure of Herstatt Bank", 24 June 2015. https://bankunderground.co.uk/2015/06/24/boe-archives-reveal-little-known-lesson-from-the-1974-failure-of-herstatt-bank/
- **Flash crash, 6 May 2010:** CFTC and SEC staff, *Findings Regarding the Market Events of May 6, 2010*, 30 September 2010. https://www.sec.gov/news/studies/2010/marketevents-report.pdf
- **x402:** Coinbase announcement, 6 May 2025, as reported in Paperjam, "Why Luxembourg should be interested in x402". https://en.paperjam.lu/article/why-luxembourg-should-be-interested-in-x402 ; Cloudflare, "Launching the x402 Foundation with Coinbase", 23 September 2025 (deferred payment scheme). https://blog.cloudflare.com/x402/ ; Coinbase Developer Platform, "x402 Foundation". https://docs.cdp.coinbase.com/x402/support/x402-foundation
- **AP2:** Google Cloud, "Announcing Agent Payments Protocol (AP2)", 16 September 2025. https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol
- **Agentic Commerce Protocol:** Stripe, "Stripe powers Instant Checkout in ChatGPT and releases Agentic Commerce Protocol codeveloped with OpenAI", 2025. https://stripe.com/newsroom/news/stripe-openai-instant-checkout
- **Magentic Marketplace:** G. Bansal et al., "Magentic Marketplace: An Open-Source Environment for Studying Agentic Markets", arXiv:2510.25779, 2025. https://arxiv.org/abs/2510.25779
- **Sandbox economies and permeability:** N. Tomašev, M. Franklin, J. Z. Leibo, J. Jacobs, W. A. Cunningham, I. Gabriel, S. Osindero, "Virtual Agent Economies", arXiv:2509.10147, 2025. https://arxiv.org/abs/2509.10147
- **Economy of agents:** G. K. Hadfield, A. Koh, "An Economy of AI Agents", arXiv:2509.01063, 2025 (NBER Handbook on the Economics of Transformative AI). https://arxiv.org/abs/2509.01063
- **T+1:** SEC press release 2024-62 (compliance date 28 May 2024). https://www.sec.gov/newsroom/press-releases/2024-62 ; ESMA on the EU move to T+1 on 11 October 2027. https://www.esma.europa.eu/node/235946
- **IEX speed bump:** "The Investors' Exchange", Harvard Law School Forum on Corporate Governance, 4 October 2016. https://corpgov.law.harvard.edu/2016/10/04/the-investors-exchange
- **Frequent batch auctions:** E. Budish, P. Cramton, J. Shim, "The High-Frequency Trading Arms Race: Frequent Batch Auctions as a Market Design Response", *Quarterly Journal of Economics* 130(4), 2015. https://doi.org/10.1093/qje/qjv027
