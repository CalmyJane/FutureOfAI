# Evidence: Chapter 3, The M-1 Criterion

Compiled 2026-10-20. Strength: **A** = primary source or official document read; **B** = reliable secondary source(s) consistent with each other; **C** = single secondary source / recall, not used as a load-bearing fact.

## Grid: 1965 blackout, NERC, N-1

| Claim | Source | Strength |
|---|---|---|
| 9 Nov 1965 Northeast blackout: loss of over 20,000 MW of load, about 30 million people affected (US northeast and Ontario). | NERC, *Final Report on the August 14, 2003 Blackout*, ch. 7 (historical context), https://www.nerc.com/pa/rrm/ea/2003%20Blackout%20Final%20Report/ch7-10.pdf | A |
| Started when a protective relay tripped a transmission line; showed interconnection can spread failure. | NPCC "About" page, https://npcc.org/about ; NERC history materials | B |
| The Federal Power Commission recommended a coordinating council; a 1967 Electric Power Reliability Act was proposed but not enacted; the industry formed NERC itself in June 1968. | NERC timeline (March 2023), https://www.nerc.com/news/Documents/March%202023%20NERC%20Timeline.pdf ; NERC History Book, https://nercstg.nerc.com/AboutNERC/Resource%20Documents/NERCHistoryBook.pdf | B |
| Post-blackout FPC study group (industry, government, academia) produced the model document for NPCC's planning and operating criteria, approved September 1967. | New York State Reliability Council, 2009–10 Biennial Report, https://www.nysrc.org/wp-content/uploads/2023/03/2009-10-Biennial-Report-Final-v.2.pdf | B |
| N-1 definition: system must keep supplying load after the loss of any single major component. | Wikipedia, "Contingency (electrical grid)", https://en.wikipedia.org/wiki/Contingency_(electrical_grid) | B |
| Blackouts still traced to weak handling of N-1 security. | Capitanescu, IEEE Power & Energy Magazine, May 2023, https://read.nxtbook.com/ieee/powerenergy/powerenergy_may_2023/are_we_prepared_against_black.html | B |
| **Could not find:** the exact year or document in which the term "N-1" was first used. The chapter says only that the single-contingency rule grew out of post-1965 criteria and became standard. | — | gap |

## Aviation: Cerritos and TCAS

| Claim | Source | Strength |
|---|---|---|
| 31 Aug 1986, Aeroméxico 498 and a Piper PA-28 collided over Cerritos, CA; 82 dead including 15 on the ground. | Wikipedia, "Aeroméxico Flight 498", https://en.wikipedia.org/wiki/Aerom%C3%A9xico_Flight_498 ; Fox5 retrospective | B |
| Congress, in the Airport and Airway Safety and Capacity Expansion Act of 1987 (Pub. L. 100-223, s. 203, 30 Dec 1987), directed the FAA to require collision avoidance (TCAS II) on aircraft with more than 30 seats; full compliance by end of 1993. | Kuchar & Drumm, "The Traffic Alert and Collision Avoidance System", MIT Lincoln Laboratory Journal 16(2), 2007, https://archive.ll.mit.edu/publications/journal/pdf/vol16_no2/16_2_04Kuchar.pdf ; FAA/DOT documents on rosap.ntl.bts.gov | A/B |
| Two TCAS II aircraft coordinate resolution advisories over the Mode S air-to-air data link so the advisories are complementary (one climbs, the other descends). | ICAO-derived ANAC glossary, https://www2.anac.gov.br/anacpedia/ing-por/tr7426.htm ; Kuchar & Drumm 2007 | B |

## Markets: circuit breakers

| Claim | Source | Strength |
|---|---|---|
| Brady Commission (1988) recommended circuit breakers after the October 1987 crash; NYSE adopted point-based market-wide halts in 1988. | Chicago Fed Letter, July 1998, https://www.chicagofed.org/-/media/publications/chicago-fed-letter/1998/cfljul98-pdf.pdf ; Wikipedia "Trading curb" | B |
| Rationale: a time-out was not expected to change price direction, only to prevent overshooting. | MIT Golub Center, "Are circuit breakers doing their job?", https://mitsloan.mit.edu/centers-initiatives/mit-gcfp/are-circuit-breakers-doing-their-job | B |
| Flash crash 6 May 2010: indices already down >4% fell another 5–6% in minutes and rebounded almost as fast; a single $4.1bn sell program was a trigger. | CFTC–SEC staff report, *Findings Regarding the Market Events of May 6, 2010* (30 Sept 2010), https://www.banking.senate.gov/download/joint-staff-report-from-sec-and-cftc-regarding-market-events-of-may-6-2010&download=1 ; CS Monitor, 1 Oct 2010 | A/B |
| June 2010: single-stock circuit breaker pilot (5-minute pause). 31 May 2012: SEC approved Limit Up–Limit Down and revised market-wide breakers (7%/13%/20% of S&P 500; 15-min halts for L1/L2; L3 halts for the day), effective on a pilot basis Feb 2013. | Harvard Law Forum on Corporate Governance, 13 June 2012, https://corpgov.law.harvard.edu/2012/06/13/limit-up-limit-down-plan-and-circuit-breakers-approved/ ; SEC press release 2011-84, https://www.sec.gov/news/press/2011/2011-84.htm ; SEC 34-94705 (2022) | A/B |
| "About a trillion dollars" of value lost in the flash crash: found only in secondary summaries; **not used in this chapter** (prologue uses it; flag for orchestrator). | — | C |
| First market-wide halt, 27 Oct 1997: recall only, not verified; **not used**. | — | C |

## N-version programming

| Claim | Source | Strength |
|---|---|---|
| Knight & Leveson (1986): 27 versions written independently from one spec (9 at UVA, 18 at UC Irvine), one million tests; individually very reliable (23 of 27 above 99.9%); coincident failures substantially more than independence predicts; independence rejected at 99% confidence. | Knight & Leveson, "An Experimental Evaluation of the Assumption of Independence in Multiversion Programming", IEEE TSE 12(1):96–109, 1986; abstract and summary at https://www.kth.se/social/files/564df871f2765419e306178d/KnightLeveson.pdf ; UVA record https://libraopen.lib.virginia.edu/public_view/jd472w463 | A (abstract) / B (details) |
| Knight & Leveson defended the work against critics in 1990. | Leveson, "A Reply to the Criticisms of the Knight & Leveson Experiment", https://www.cs.washington.edu/homes/leveson/critics.pdf | B |

## Correlated errors in AI (2021–2025)

| Claim | Source | Strength |
|---|---|---|
| Kim, Garg, Peng & Garg, "Correlated Errors in Large Language Models", ICML 2025 (PMLR 267): 350+ LLMs; on one leaderboard, models agree 60% of the time when both are wrong; larger, more accurate models have more correlated errors, even across providers and architectures; shared provider/architecture drives correlation. | https://proceedings.mlr.press/v267/kim25e.html ; https://icml.cc/virtual/2025/poster/44225 | A |
| Jiang et al., "Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)", NeurIPS 2025 Best Paper; inter-model homogeneity in open-ended answers; Infinity-Chat, 26K queries. | arXiv:2510.22954, https://arxiv.org/abs/2510.22954 ; NeurIPS blog, 26 Nov 2025 | A |
| Kleinberg & Raghavan, "Algorithmic Monoculture and Social Welfare", PNAS 118(22), 2021: convergence on one algorithm can lower overall decision quality even when it is the most accurate for each user alone. | https://arxiv.org/abs/2101.05853 | A |

## Diversity by design

| Claim | Source | Strength |
|---|---|---|
| Liu & Yao, "Ensemble learning via negative correlation", *Neural Networks* 12(10):1399–1404, 1999: networks trained together with a penalty term that pushes their errors to be negatively correlated; members specialise; ensemble generalises well. | https://doi.org/10.1016/S0893-6080(99)00073-8 ; https://scholars.ln.edu.hk/en/publications/ensemble-learning-via-negative-correlation/ | A |
| Companion paper: Liu & Yao, "Simultaneous training of negatively correlated neural networks in an ensemble", IEEE Trans. SMC-B 29(6):716–725, 1999. | https://scholars.ln.edu.hk/en/publications/simultaneous-training-of-negatively-correlated-neural-networks-in/ | B |
| Markowitz, "Portfolio Selection", *Journal of Finance* 7(1):77–91, 1952: portfolio variance depends on covariances; low-correlation assets reduce risk. | https://doi.org/10.1111/j.1540-6261.1952.tb01525.x | A |

## Searched for and not found
- Any public measurement of action-level (as opposed to answer-level) correlation among deployed AI agents. None found; stated in text.
- Any regulator that today requires a deployer to test a critical system against simultaneous failure of all instances of one model. None found.
- Origin date of the term "N-1". Not found.
- "N-Version Programming with Coding Agents" (arXiv 2606.20158) appeared in results; not read, details uncertain; not used.

## Fictional (2036) numbers used in the vignette
- Q3 2035 Concordance Index = 0.71 (ledger). Q1 2034 first index = 0.63 (new, invented); Q2 2035 = 0.69 (new, invented).
- Largest family share in the vignette: about 58% of agent-managed flexible load in the continental synchronous area (invented).
- Presentation date: Tuesday 21 January 2036, three weeks before the Long Minute (invented).
