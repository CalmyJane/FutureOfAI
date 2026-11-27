# Review 8: Chapter 1, What We Mean by "AI"

## Verdict
Ready to print. Optional small fixes for balance and precision are listed below. Quotations and figures checked against primary sources were correct, including the EU guidelines' paragraph numbers, Haigh's column, Mitchell's preprint, Legg and Hutter, and the 2026 model, adoption and benchmark figures. The arithmetic in the MYCIN example is correct. Legal statements about the SEC, FTC and the Nate/Saniger case are accurate, use "alleging", and give the not-guilty plea, which is still current.

## MUST change before printing
None.

## SHOULD change

### S1. GPT-6.2 is two models
- Where: textbook/chapters/ch01.md:244
- Text now: "In November Anthropic also released Claude Fable 5.2 (9 November) and OpenAI GPT-6.2 (17 November)"
- Problem: UNCLEAR. OpenAI's release was two models, GPT-6.2 Astra and GPT-6.2 Sol. The bib entry openai2026gpt62 is titled "Introducing GPT-6.2 Astra and GPT-6.2 Sol". The text names Anthropic's model exactly but OpenAI's only loosely.
- Evidence: https://openai.com/index/introducing-gpt-6-2-astra-sol/ : "We're introducing GPT‑6.2 Astra, our new frontier model for your hardest projects." Press reports (e.g. digitaltrends.com, gcn.com) date the launch to 17 November 2026.
- Change to: "In November Anthropic also released Claude Fable 5.2 (9 November) and OpenAI GPT-6.2 Astra and GPT-6.2 Sol (17 November)"

### S2. ClockBench comparison omits that OpenAI's newest models are not yet listed (balance)
- Where: textbook/chapters/ch01.md:255
- Text now: "By late November 2026 Anthropic's Claude Fable 5.2 Max, released on 9 November, had reached 87.8%, ahead of Google's Gemini 4 Carbon at 85.0% [@clockbench2026clockbench]."
- Problem: UNCLEAR (balance). The figures are correct. But the leaderboard has no GPT-6.2 entry: the best OpenAI entry is GPT-6 Astra Max at 75.0%. A reader may assume that OpenAI's current model was tested and trailed. In a book written by Anthropic models, a sentence that ranks Anthropic first should say who was not yet measured.
- Evidence: https://clockbench.ai/ (accessed 27 Nov 2026). Ranks 1–3 are "Claude Fable 5.2 Max 87.8%", "Gemini 4 Carbon High 85.0%" and "Gemini 4 Argon High 83.3%". The human average is 90.7%. There are no GPT-6.2 entries.
- Change to: "By late November 2026 Anthropic's Claude Fable 5.2 Max, released on 9 November, had reached 87.8%, ahead of Google's Gemini 4 Carbon at 85.0%; OpenAI's GPT-6.2 models, released on 17 November, had not yet been listed [@clockbench2026clockbench]."

### S3. Agent history names only Anthropic's protocol (balance)
- Where: textbook/chapters/ch01.md:242
- Text now: "In November 2024 Anthropic released the Model Context Protocol as open source, describing it as "a new standard for connecting AI assistants to the systems where data lives" [@anthropic2024introducing]."
- Problem: UNCLEAR (balance). This is the only industry milestone in the agents paragraph, and it is Anthropic's. Chapter 5 (ch05.md:117) already documents that MCP became a cross-industry standard, transferred to the Linux Foundation's Agentic AI Foundation, which was co-founded with Block and OpenAI. One clause would show that it is shared infrastructure rather than one company's product.
- Evidence: textbook/chapters/ch05.md:117, cited to [@anthropic2025donating].
- Change to: add after the citation: "In December 2025 it was transferred to a foundation under the Linux Foundation, co-founded with Block and OpenAI, and by then had been adopted in products including ChatGPT and Gemini (Chapter 5) [@anthropic2025donating]." (This requires adding the anthropic2025donating entry from ch05.bib to ch01.bib.)

## Could not verify
- OSWorld-Verified, "about 86%" by August 2026 (line 242). The leaderboard at https://osworld-v1.xlang.ai/ did not load its data. The page does confirm "2026-06-26: OSWorld 2.0 is now available", which matches "June 2026".
- "the attendees regarded as a remarkable achievement" and the Stanford Encyclopedia of Philosophy count of ten attendees (line 21). Not fetched.
- The MYCIN page numbers in Buchanan & Shortliffe 1984. The book is not online in a form that could be searched quickly. The arithmetic is correct (see below).

## Checked and confirmed
- Dartmouth proposal: date, $13,500, the "2 month, 10 man" quotation, the central conjecture. Turing: 10^9 storage capacity, 70% chance, five minutes.
- Legg & Hutter "70-odd" definitions (arXiv 0706.3639 abstract: "the 70-odd definitions presented here").
- EU guidelines (C(2025) 5053, adopted 29.7.2025, published 6 Feb 2025). Paras 7, 9, 39 ("early generation expert systems intended for medical diagnosis"; "search and optimisation methods"), 41, 42 ("such as linear or logistic regression methods", "transcend 'basic data processing'", "consolidated manner for many years"), 46, 48 (the exact minimax quotation), 49–50, 62, 63 ("The vast majority of systems") all match the adopted text.
- Haigh (CACM Feb 2024): "never happened"; 480 rules; ">$40 million a year"; 59 technical staff in 1989; Cyc "approximately 2,000 years of person-effort" and "30 million rules"; DARPA's autonomous land vehicle abandoned at the end of 1987; "proved unsustainable"; "less controversial alternative"; "flipped to refer primarily to deep learning and generative systems".
- Mitchell 2021: the Simon 1960 and Minsky quotations; "sharp funding decreases and a downturn in enthusiasm for AI in both countries"; "meteoric rise of machine learning"; "then-discredited"; "unable to generalize or adapt when faced with new situations"; the definitions of spring and winter.
- MYCIN arithmetic: 0.3+0.2×0.7=0.44; 0.44−0.1=0.34; 0.34/0.9=0.378≈0.38; 0.999−0.8=0.199. All correct.
- Shannon's chess figures; Deep Blue (1996 result 4–2, 1997 result 3.5–2.5, 32 processors / 200M positions per second, versus 30 processors / 480 chips); Seide 2011 (309 h, 27.4%→18.5%); AlexNet (15.3%, 26.2%, 16.4%, 60M parameters, two GTX 580s); ILSVRC 28.2%→6.7%, ResNet 3.57%, He 4.94%, annotator 5.1%/1,500 images/258; AlphaGo 5–0 and 4–1; transformer BLEU 28.4.
- Table 1.4 (GLUE 80.5/72.8; 9 of 12; 7 of 8; 300B tokens; 3.14×10^23). Growth factor 175B/117M ≈ 1,496 ("about 1,500"). Correct.
- InstructGPT 1.3B vs 175B; ChatGPT 700M weekly users / ~10% of adults (July 2025); GPT-4 bar exam and Martínez's 62nd/48th percentiles; LLaMA-13B; Nobel Prizes 2024; Turing Award quotation.
- OpenAI DevDay 29 Sept 2026, 1.2B weekly users (openai.com/index/devday-2026-recap; press reports). Correctly labelled as a company figure.
- St. Louis Fed: "Between August 2024 and May 2026, the share of adults using AI rose from 45% to 62%" (ages 18–64). Microsoft: US "from 24th to 21st based on a 31.3% usage rate by the working age population" (ages 15–64). Bick et al. is a peer-reviewed article (*Management Science* 72(10), 2026).
- AI Index 2026: IMO gold, and the top model on ClockBench "about half" correct. ClockBench: Argon 83.3%, Fable 5.2 Max 87.8%, Carbon 85.0%, human average 90.7%.
- Release dates: GPT-6 Astra system card (3 Sept); Opus 5.5 (22 Sept); Gemini 4 Argon blog of 30 Sept, "rolling out to a set of trusted cyber defenders"; Carbon announced 28 Oct, "a subset of cyber defenders", general availability 10 Nov; Fable 5.2 on 9 Nov (SD Times); GPT-6.2 on 17 Nov.
- Legal: SEC Delphia/Global Predictions, $400,000 in total; FTC Operation AI Comply (quotations); SEC Presto (Jan 2025). Saniger: charged in April 2025, "pleaded not guilty" (Quinn Emanuel alert: "voluntarily waived extradition, pleaded not guilty"; status conference 5 Nov 2026; no verdict). The wording is accurate and appropriately hedged.
- Balance overall: the opening and adoption figures are OpenAI's and are labelled as company data; Google, Meta, DeepSeek, Microsoft and IBM are credited fairly. Only S2 and S3 tilt slightly towards Anthropic.

## Tally
Claims checked: 78 / confirmed: 74 / wrong: 0 / outdated: 0 / imprecise: 1 (S1) / unverifiable: 3
