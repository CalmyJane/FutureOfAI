## Part Four: When Thinking Has a Price

# Chapter 12: The Cognitive Trade Balance

*2036 · Olkaria, Kenya*

The steam comes up out of the ground at a little over two hundred degrees, and by the time it has spun the turbines and been piped back down, Hall C has used about thirty-eight megawatts of it to think.

Mwangi Kamau starts the night shift at ten. He is thirty-six, the younger brother, the one who was supposed to become an electrician in Nakuru and instead became something there was no word for when he left school. Kilele Compute calls it a thermal-and-rack technician. His mother calls it "the computer farm". His sister calls it "your kettle", because of the plumes.

The hall is long and loud and smells faintly of sulphur where the cooling loop runs close to the wellheads. Outside, beyond the fence and the silver pipes that cross the valley on their stilts, a family of warthogs is working through the grass by the access road. Giraffes come at dawn, sometimes. The tourists who drive through Hell's Gate on the way to the gorge photograph the giraffes in front of the pipes and post the pictures with captions about the future.

On the wall screen, the hall's load is broken down by contract. Most of it is labelled EU-WEST. Mwangi knows roughly what that means, because the dashboards are generous about everything except content: an insurer in Hamburg running claims, a Dutch tax-preparation service in its busy month, a French hospital group triaging discharge letters overnight. The work arrives through the cable at Mombasa, runs here on Kenyan steam, and leaves the same way. Kenya is paid by the megawatt-hour and by the rack. The newspapers call it the thought trade, and the Treasury likes the numbers.

At 23:40 his phone buzzes. Wanjiru.

"Unaskia? Leerwijs has put up the price again. Nineteen euros. Euros, Mwangi. For Njeri's maths."

"Cancel it."

"And replace it with what? Her whole class is on it. The school recommends it. Ndege says the Kenyan ones are worse at explaining fractions and better at explaining tithes." A pause. "That was a joke. Ndege doesn't make jokes. I make jokes."

He laughs, and tells her he'll look at something.

What he looks at is his own screen. He scrolls down past EU-WEST to the smaller contracts, the ones that don't pay as well, and finds it near the bottom: LEERWIJS BV, AMSTERDAM, REGION EAF, 1.2 MW. The tutoring service that his niece uses on a cracked tablet in Kasarani has rented a slice of Hall C. The thinking that explains fractions to Njeri is done here, two hundred metres from where he is standing, on steam from under the Rift Valley.

It is billed in Amsterdam. Its lessons were written and tuned there, its sense of what a good explanation sounds like was set there, and its price is set there too, in euros, by people who have never had to hear Wanjiru say *nineteen* in that tone of voice.

He thinks about what he is paid per megawatt-hour, and what Leerwijs charges per child, and does not get very far with the arithmetic before the cooling alarm on row 14 goes off and he has to go and be useful.

At four in the morning, on his break, he opens the tutoring app on his own phone. Njeri lent him the login once, to show him something. He types a question into it, half as a test: *Explain the 2010 Constitution's rules on county budgets, for a thirteen-year-old.*

The answer is fluent and patient and correct, and it compares the counties to Dutch provinces.

The question has left the hall, crossed to Mombasa, run under the sea, reached Amsterdam to be checked against a policy written there, and come back, so that it can be computed on a rack he can see from the bench where he is sitting. He counts the latency on the little debug overlay he has never turned off. A hundred and forty milliseconds, there and back, to think forty metres away.

Outside, the first giraffe is standing in the steam.

---

## Where we are in 2026

Every chapter so far has been about thought as an activity: who does it, who signs for it, who can read it. This part of the book is about thought as a quantity. It can be measured in watts, priced in currencies and shipped across borders, and once it can be shipped, it can be traded at a deficit.

Start with the watts. In April 2026 the International Energy Agency published an update to its analysis of energy and AI. Data centres worldwide used about 485 terawatt-hours of electricity in 2025, up 17 per cent on the year before, and the subset built around AI accelerators grew by about half. The agency's central projection roughly doubles total consumption to about 950 terawatt-hours by 2030, around 3 per cent of all the electricity the world uses. That is close to the path the IEA set out a year earlier, which tells you the forecast survived a year of contact with reality.

The geography matters more for this chapter than the total. The IEA's annex table gives Europe about 72 terawatt-hours of data-centre consumption in 2025. It gives the whole of Africa 1.6. Of roughly 114 gigawatts of data-centre capacity in the world, Africa had about 0.4. A single large campus in Virginia or Ireland can draw more than that by itself.

Kenya is the obvious place to ask whether this could change. The country has about 940 megawatts of installed geothermal capacity, most of it in the Olkaria field near Lake Naivasha, and geothermal supplied about 40 per cent of the country's generation in the second half of 2025. Geothermal is steady in a way wind and sun are not: it runs at night, which is when European batch work is cheapest to send abroad.

In May 2024 Microsoft and G42, an Abu Dhabi AI company, announced a package worth about a billion dollars for Kenya. Its centrepiece was a geothermal-powered data centre at Olkaria, built with a local developer, EcoCloud, starting at 100 megawatts with talk of eventually reaching a gigawatt. EcoCloud had already broken ground on a first phase at KenGen's Green Energy Park in 2023. The companies said the campus would be running in about two years.

It was not. By May 2026 the project had stalled over power. Kenya's grid had about 3,200 megawatts of connected capacity and a record peak demand, that January, of about 2,440. A gigawatt campus would have taken roughly a third of the country's capacity. President William Ruto, in remarks widely reported that month, said that switching on that one data centre would mean shutting off power to half the country. The government says the project has not been withdrawn, and a smaller EcoCloud scheme of around 60 megawatts is still under discussion. In August, KenGen told Al Jazeera the data centre was still at the design stage, and residents around Lake Naivasha were asking how much of their water it would drink.

So in 2026 the Olkaria inference park is a plan with a stalled first phase. My vignette assumes that it gets built, and then some. That is the optimistic case, and the optimistic case is the subject of this book.

---

## Cheap power is the easy part

The most careful attempt I have found to model whether a country like Kenya can sell thinking abroad is a World Bank working paper published in June 2026 by the economist Michael Lokshin, under the title *Cheap Energy Might Not Be Enough*. It treats AI compute as a traded service. Training, which is insensitive to delay, can be done anywhere. Inference, the day-to-day running of a model to answer questions, carries a cost for distance because users notice latency. And any cross-border sale carries what the paper calls a sovereignty premium, the discount a buyer demands for having its data processed in someone else's jurisdiction.

Calibrated across 85 countries, the model finds several developing economies among the cheapest producers of compute before any subsidy. It also finds that the trust gap between those producers and buyers in rich countries wipes out nearly all of their exports. Because the chips are bought at the same world price everywhere, cheap electricity narrows total costs by only 12 to 20 per cent, which is easily erased by a little distrust. The paper's conclusion is that the binding constraint is institutional credibility. The price of power comes second.

I find this persuasive, and it changes the shape of the problem. In the 2036 of my vignette, Kenya has solved the credibility problem: European insurers trust Kenyan halls with their claims. The thought trade is flowing. Kenya has done everything the development economists asked. The question is what it has become a supplier of.

The other recent piece of evidence comes from the opposite direction. In July 2026 the German Council on Foreign Relations (DGAP) published a policy brief by Valentin Weber and Michael Laha on China's trade in compute. Using customs data on the hardware of computation, chiefly chips, they found that China's compute exports rose by 43.5 per cent between 2021 and 2025, to about €206.5 billion, while its compute trade deficit shrank. With Germany, China ran a compute surplus of about €350 million in 2025. Their worry is that Europe is being marginalised in a market it assumed it would shape.

Notice what the DGAP figures count. They count the means of thinking: chips that leave Shenzhen in a crate. They do not count the thinking itself, the questions answered and decisions drafted once those chips are switched on. As far as I can tell, nobody counts that. International trade in services is recorded under a UN classification in which computing sits inside one broad heading for telecommunications, computer and information services. An hour of Kenyan steam spent drafting a Hamburg insurer's claim decisions and an hour spent hosting a website land, at best, on the same line. I could not find a single national statistic, anywhere, that measures how much inference a country computes for others, or how much of its own citizens' advice, tutoring and paperwork is computed abroad.

---

## How success produces the deficit

Here is the mechanism, and it needs nothing to go wrong.

Inference gets cheap. The IEA notes that the energy used per AI task has fallen by at least an order of magnitude a year recently. Because it is cheap and good, it moves into the parts of life where judgement used to be local and slow: the tutor, the clinic's triage nurse, the clerk who checks a land title, the officer who drafts a county budget. Each of these moves is an improvement. Njeri's tutor is patient at eleven at night, and her teacher is not.

But each move also changes where the judgement comes from. The electricity can be Kenyan. The racks can sit in the Rift Valley. The weights, the training data, the fine-tuning, the policy that decides what a good explanation of a constitution sounds like, and the price, are set somewhere else. A country can be a net exporter of joules and a net importer of judgement at the same time. In my vignette, Kenya is both, and on most days the second number is the larger one in shillings.

The pattern is old. Countries that export raw materials and import finished goods have argued for a century about whether that position is a stage of development or a trap. What is new is the commodity. A finished good from abroad does what it does; a fridge does not have views. Imported judgement arrives with its examples, its defaults and its sense of what counts as the right answer. When a tutoring model compares Kenyan counties to Dutch provinces, nothing has gone wrong. It has drawn on what it knows best.

I want to be careful here. Kenya already imports textbooks, medicines and software, and nobody thinks the country has lost its sovereignty to a pharmacy. The difference is a matter of degree that becomes a matter of kind as the share rises. When most of a country's children are tutored, most of its patients triaged and most of its public documents drafted by models governed elsewhere, the government that is supposed to answer for those things has, in practice, contracted them out without ever signing a contract. And correlation, the theme of Part One, applies across borders too: if a whole country's tutoring runs on one foreign model family, it inherits that family's blind spots all at once.

I will call this the **thought deficit**: the share of a country's decision-bearing inference that is consumed at home but governed abroad, net of what it governs for others. The phrase is mine. The thing it describes is, as far as I can tell, unmeasured everywhere.

---

## Three inventions

This chapter's proposal has three parts that depend on each other. You cannot manage a deficit you do not measure, and you cannot measure thought without a unit for it.

### National accounts of thought

National accounts were invented in the 1930s and 1940s because governments that had to fight a depression and a war found they could not steer an economy they could not see. I think the same is true of cognition in 2036, and the first step is a set of accounts.

Concretely: every provider that serves AI inference to users in a country above a size threshold (I would start at one per cent of that country's market, or a fixed number of active users) reports quarterly to the national statistics office. The report gives three locations for each block of inference. The first is where it was computed, the physical hall and its energy. The second is whose model it ran, meaning the jurisdiction of the organisation that trained and governs the weights and sets the usage policy. The third is where the result lands, the user's country. It also tags each block by use category: education, health, justice and public administration, finance, commerce and entertainment.

From those reports a statistics office can publish what no country publishes today: a cognitive trade balance, by category. Kenya in my 2036 would show a large surplus in *computed for others* and a deficit in *governed by others*. Germany might show the reverse. The IMF, which sets the manual most countries use for their balance of payments, would be the natural body to standardise the format, much as it already standardises how freight and tourism are counted.

### Joules per insight

The accounts need a unit, and tokens are a poor one. A token of a model musing to itself and a token of a correct diagnosis count the same.

The best starting point I know is a 2025 Stanford study, led by Jon Saad-Falcon and Avanika Narayan with colleagues including Christopher Ré and John Hennessy, called *Intelligence per Watt*. It defines a metric, task accuracy per unit of power, and applies it to more than twenty small models on eight kinds of chip over a million real queries. The headline findings are striking: local models could answer about 89 per cent of single-turn chat and reasoning queries correctly, and intelligence per watt improved by about 5.3 times between 2023 and 2025. The authors are clear that this covers single questions, not long agentic tasks.

I want to take their idea one step outward. **Joules per insight** is the energy needed to produce one verified useful outcome from a fixed basket of tasks: a correct explanation of a fraction to a child, graded by a teacher; a correctly triaged discharge letter; a land-title query answered and checked. The basket works like the shopping basket behind a consumer price index. It is chosen by the statistics office, revised every few years, and published. Each category in the accounts is then reported both in energy and in insights, so a country can see whether it is exporting cheap joules and importing expensive insights, and at what ratio.

Defining an insight is hard, and I return to it in the box for researchers. But inflation statisticians have argued for decades about how to price a laptop that gets better every year, and they still publish a number every month.

### A positive right to think

The third part is the one I expect to be argued with most.

In April 2025 Montana's governor signed the Right to Compute Act, sponsored by state senator Daniel Zolnikov. It recognises a right to own and use computational resources and says that any government restriction must be demonstrably necessary and narrowly tailored to a compelling interest. It is a negative liberty: it stops the state from taking compute away. It gives Njeri nothing.

A year earlier, on a podcast in May 2024, Sam Altman wondered aloud whether the future might look less like a universal basic income and more like "universal basic compute": everyone would own a slice of a future model's capacity, to use, resell or give away. That is a positive provision, and I think the instinct is right. As stated, though, it is a share in one company's model, which would make a citizen's thinking allowance a claim on a single foreign supplier. For Kenya, that is the thought deficit with a ribbon on it.

So here is the version I would propose. Every resident has a **right to think**: a monthly allowance of inference, measured in joules per insight against the national basket, enough for a defined standard of use. For a school-age child I would set the floor at what it takes to run two hours a day of tutoring-grade inference. A rough sense of scale: the IEA's own illustration uses a generous 1 watt-hour per query, so three hundred queries a day comes to about nine kilowatt-hours a month. That is less electricity than a household fridge uses in a fortnight, although reasoning-heavy tutoring could cost many times more per query.

The allowance carries two conditions. The citizen spends it on any certified provider, and the menu must include at least three model families governed in different jurisdictions, at least one of them domestic or open-weight. And the allowance is funded, in an exporting country, by a royalty on exported inference. In my Kenya, that would be a levy of a few per cent on every megawatt-hour Hall C sells to EU-WEST, paid into a fund that buys Njeri her thinking from whichever supplier she and her school choose.

### The trigger

The three parts meet in one rule. When the accounts show that more than half of the decision-bearing inference in a sovereign category (education, health, justice and public administration) is governed by a single foreign jurisdiction, or more than 70 per cent by any single model family, the government must publish a diversification plan within a year and report on it to parliament annually. At 80 per cent, public procurement in that category must favour other suppliers until the share falls below the threshold.

The numbers are a first guess, and they are meant to be argued with. They are also meant to be crossed by most countries, at least in the beginning. A trigger that never fires measures nothing.

---

## The strongest objection

Here is the objection at full strength.

Compute is a traded service like any other. Kenya imports aircraft and exports flowers, and both countries are richer for it. The theory of comparative advantage says a country should make what it makes relatively cheaply, and Kenya makes steam. Requiring a domestic model in the menu is a tariff with better manners. It would hand Kenyan children a worse tutor so that their government feels more sovereign. And the problem may solve itself: the Stanford study shows local models on ordinary hardware covering a rising share of queries, from about 23 per cent in 2023 to about 71 per cent in 2025. If thinking moves onto the phone in Njeri's hand, there is no border for it to cross.

Much of this is right, and I concede it. A thought deficit is not in itself a harm, any more than a trade deficit in medicines is. Most countries will run one in most categories, and should. The right to think deliberately lets citizens spend the allowance abroad. The trigger requires a plan and a procurement tilt. It does not require a Kenyan model to win.

On local inference, though, the objection misses where the deficit lives. A model running on Njeri's tablet still carries weights trained and tuned elsewhere. Moving the computation onto the device removes the latency and the energy bill from the trade balance. It leaves the judgement exactly where it was. If anything, it makes the deficit harder to see, because the thinking now happens offline, in Kasarani, and no cable records it crossing anything.

And here is the part of the answer I would defend hardest. Ordinary services trade labour: a Kenyan call centre answering a British customer's question sells hours of skilled work, under rules the customer's company sets. Inference trades judgement in the other direction. When Kenya imports tutoring, it imports the decisions about what to teach, how to explain it, what to leave out and when to say *that's correct*. Those decisions were once made by Kenyan teachers under a Kenyan curriculum, answerable to a Kenyan ministry. A country that buys most of its judgement from one place depends on that place in a way that a country buying its aircraft does not. Dependency in judgement is a question of sovereignty, and sovereignty is what national accounts were invented to protect.

---

> **For researchers**
>
> 1. **Define an insight unit.** Build a candidate task basket for one sovereign category (secondary-school mathematics tutoring is a good start) with human-graded outcomes, and measure *joules per verified insight* across at least five model–hardware pairs. How stable is the ranking of systems when the basket is revised, and how large is the gap between joules per token and joules per insight?
> 2. **Measure a cognitive trade flow.** For one country and one category, estimate the share of inference consumed by residents that is (a) computed abroad and (b) governed abroad, using provider disclosures, network measurements or app-store and traffic data. The quantity is the *thought deficit* as defined above. How far apart are the computed and governed shares, and which is moving faster?
> 3. **The localisation of judgement.** Using paired prompts set in local contexts, measure how often a model's examples, analogies and legal references default to its governing jurisdiction rather than the user's. The quantity is a *home-bias rate*. Does it fall with fine-tuning on local data, and by how much per thousand local examples?

---

Back in Hall C, Mwangi's debug overlay is still open. A hundred and forty milliseconds: that is how long it took a question about Kenyan county budgets to travel to Amsterdam and back so that it could be answered forty metres from where it was asked.

To Njeri, waiting for an explanation of fractions, a hundred and forty milliseconds is nothing. She will never notice it. To an agent trading claims capacity in Frankfurt that night, it is long enough to be outbid several times over. Thought crosses borders at the speed of light, and once it does, the speed itself becomes a currency. Some participants in the 2036 economy live at Njeri's speed and some live at the agent's. The next chapter asks what the exchange rate between them should be.

## Notes

- **IEA 2026 figures (485 TWh, 17%, about 950 TWh, regional tables):** International Energy Agency, *Key Questions on Energy and AI*, World Energy Outlook Special Report, April 2026, Executive Summary and Annex A (Tables A.2 and A.4). https://www.iea.org/reports/key-questions-on-energy-and-ai
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
