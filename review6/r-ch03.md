# Review 6: Chapter 3, How Large Language Models Work

## Verdict

Ready to print after three small fixes. I found nothing in the chapter that is wrong, misquoted or legally risky. Every worked example I recomputed matches the text:
- the tiktoken tables, rerun with tiktoken 0.14.0;
- the BPE toy run, using the paper's algorithm;
- the attention example;
- the GPT-2 parameter count;
- the KV-cache table;
- the temperature ratios, the GRPO example and the loss values.

The 2026 material agrees with its primary sources: GPT-6 Astra, Gemini 4 Argon and Carbon, Fable 5 and Mythos 5, Opus 5.5, Muse Spark and Muse Spark Open, Kimi K3, Qwen3.8, DeepSeek-V4, the Sora shutdown, the OpenAI and Hugging Face incident, the November releases and DevDay. The items below are a typo, a wording inconsistency with Chapter 4 and DeepSeek's own report, and one sentence that is hard to parse.

## MUST change before printing

None.

## SHOULD change

### S1. Duplicated model name
- Where: textbook/chapters/ch03.md:361
- Text now: "That is roughly 5% of the 2.79 million GPU-hours the company reported for the full training of DeepSeek-V3, DeepSeek-V3 [@deepseekai2024deepseekv3]."
- Problem: UNCLEAR. This is a typo: the model name appears twice.
- Evidence: n/a. The 5% figure itself is correct: 147,000 ÷ 2,788,000 = 5.3%.
- Change to: "That is roughly 5% of the 2.79 million GPU-hours the company reported for the full training of DeepSeek-V3 [@deepseekai2024deepseekv3]."

### S2. DeepSeek-V3.2's budget is for post-training, not specifically reinforcement learning
- Where: textbook/chapters/ch03.md:275 (Figure 3.3 caption), 389, and 435 (Table 3.9)
- Text now: "DeepSeek put the reinforcement-learning budget for V3.2 above 10% of pre-training cost" (line 389 and the caption); "RL budget above 10% of pre-training cost" (Table 3.9)
- Problem: INCONSISTENT. DeepSeek's report describes the budget as post-training. Chapter 4 (ch04.md:181) correctly says "post-training budget". The difference is small, since most of DeepSeek's post-training is RL, but the two chapters should use the same wording.
- Evidence: https://arxiv.org/pdf/2512.02556 (DeepSeek-V3.2, 2 Dec 2025), p. 2: "post-training computational budget exceeding 10% of the pre-training cost".
- Change to: "DeepSeek put the post-training budget for V3.2, mostly reinforcement learning, above 10% of pre-training cost" (line 389 and the caption), and "Post-training budget above 10% of pre-training cost" in Table 3.9.

### S3. The SpaceXAI/SpaceXSI sentence is hard to parse
- Where: textbook/chapters/ch03.md:389
- Text now: "the same developer, by then a SpaceX subsidiary renamed SpaceXAI (it has used the brand SpaceXSI since October 2026 [@frank2026why]), said of Grok 4.7, in September 2026,"
- Problem: UNCLEAR. A parenthesis nested inside an appositive, carrying its own citation, interrupts the quotation. The facts hold up:
  - Musk announced the rename on 4 October 2026.
  - The Grok 4.7 page (released 21 September 2026) now carries the SpaceXSI brand and "SpaceX Super Intelligence LLC".
  - The cited Jalopnik piece reports only the announcement, and its bib note says that Reuters reported no date.
- Evidence: https://x.ai/news/grok-4-7 (accessed 27 Nov 2026), which shows the brand "SpaceXSI". https://www.jalopnik.com/2278279/why-spacex-rebranding-ai-artificial-intelligence-vs-super-intelligence/ (5 Oct 2026).
- Change to: "and the same developer, by then the SpaceX subsidiary SpaceXAI, said of Grok 4.7, in September 2026, ... [@xai2025grok4; @xai2026grok47]; these are company statements without published figures. (In October 2026 Elon Musk said SpaceXAI would be renamed SpaceXSI [@frank2026why].)". The rename becomes a separate closing sentence.

## Could not verify

- Epoch's claim that Astra was trained on "at least 100,000 GB200" chips (cited in Chapter 4). Only secondary summaries of Epoch's page were reachable, and they agree.
- Kimi K2 Thinking's "lossless 2x speed-up" (ch03.md:237). The Moonshot page did not render its text. The claim is consistent with Moonshot's model card as I remember it.
- The page numbers given for the GPT-4o system card and some figure pinpoints. These were not checked.

## Checked and confirmed (brief)

- **Tokenisation tables.** Tables 3.1, 3.3 and 3.4 match tiktoken 0.14.0 exactly: IDs, n_vocab 200,019, 100,277 and 50,257, the language counts 7/7, 9/15, 12/62 and 13/20, the parrot emoji at 3/3, strawberry, the digit chunks, and " cat" = 9059. `encoding_for_model` maps gpt-4o, o3, gpt-4.1 and gpt-5 to o200k_base.
- **Table 3.2.** Sennrich's Algorithm 1 reproduces all ten merges and their counts.
- **Table 3.5.** Weights 0.620/0.074/0.306, output (0.773, 0.227) and the sum 27.29 are confirmed.
- **Table 3.6.** All sums are correct (7,087,872 and 124,439,808). Kaplan's 12·L·d² is within 0.14% of the exact total, and the ~170M FLOP per token is correct.
- **Table 3.8.** All rows are recomputed and correct (74 KB, 75 MB, 819,200 B, 0.52 MB, 66 GB, 8.3 MB, 1.06 TB, 70 KB, 9.0 GB). "Less than a seventh" is correct (0.136).
- **Arithmetic.** e^0.43 = 1.54 and e^0.86 = 2.36, which match the box (51.7/21.9). −ln 0.273 = 1.30, −ln 0.032 = 3.44, σ(1) = 73%, t/(1−t) = 3, the GRPO standard deviations 0.5/0.58 and 1.6×10^10 pairs are all correct.
- **Quotations checked word for word.** GPT-3 "without any gradient updates or fine-tuning"; Vaswani (several quotes); Jain and Wallace; the Elhage residual-stream quote; Olsson; RoPE; Mixtral; Holtzman; Llama 3 on GQA; the Tülu 3 RLVR definition (Tülu 3 paper, p. 5); Yue "rarely elicit[s]" (later arXiv version); the Grok 4 quotes; o3 tool use; Claude 3.7 "first hybrid reasoning model"; the GPT-5 router; Muse Spark "leverages compute to scalably amplify model capabilities"; Fable 5 "can work autonomously for longer than any previous Claude models"; Opus 5.5 "anti-distillation safeguard" (Fable 5.1, accounts created on or after 31 Aug 2026); Gemini 4 Carbon running for days.
- **Mata v. Avianca.** The quotes and their page pinpoints are correct: p. 1, p. 15 "falsely assumed … super search engine", p. 19 "real", and pp. 33–34 for the $5,000 penalty.
- **DeepSeek-R1 (Nature).** 15.6%→77.9%, the preprint's 71.0%, R1's 79.8%, and 147K GPU-hours are correct. Epoch's ~20% estimate and its statement that o3 used 10× the compute of o1 are confirmed (Epoch, 9 May 2025).
- **DeepSeek-V3.2.** Over 1,800 environments, 85,000 prompts, 1,827 synthesised environments, the top-2048 lightning indexer and "its own rubrics" are confirmed. The 31% figure in Rubrics as Rewards is confirmed.
- **DeepSeek-V4 (arXiv, 26 Apr 2026).** 1.6T parameters, 49B active, over 32T tokens, 27% of FLOPs and 10% of the KV cache are confirmed.
- **Other 2026 models.**
  - Gemini 4 Argon: 1,048,576 unified tokens, text output only, low/medium/high thinking, output "up from the previous 64K", cyber defenders first (30 Sep 2026).
  - Muse Spark Open: 816B/42B, 8 of 256 experts, a 1.8B encoder, text output (15 Oct 2026).
  - Kimi K3: 2.8T/104B, KDA plus gated MLA, 1M context.
  - Qwen3.8: 2.4T/95B, open weights.
  - GPT-6 Astra: the Critical cyber rating, Sol and Luna added on 22 Sep, MRCR 512K–1M.
  - Fable 5 and Mythos 5: one model with two safeguard settings (9 Jun 2026), and fallback to an older model for distillation requests.
- **Other 2026 events.** Sora's web app closed on 26 Apr 2026 and its API on 24 Sep 2026. The OpenAI–Hugging Face incident was in July 2026, and the report says "copied the reference answer … positive RL reward". DevDay recap (29 Sep 2026) gives "1.2B weekly users". Fable 5.2 was released on 9 Nov, Qwen4-Max (hosted, not open weights) on 16 Nov, and GPT-6.2 Astra and Sol on 17 Nov. Grok 4.7 was released 21 Sep 2026 with "a new, larger base model" and "a longer reinforcement learning run on a harder mix of tasks".
- **Cross-references.** All targets checked by grep: 2.1 ReLU, 2.3 softmax and cross-entropy, 2.5 residual connections and layer norm, 5.3 MCP, 7.1 memory bandwidth, 9.1 diffusion, 12.2 incident, 12.4, 12.5 and 12.7, and Section 4.6 effort controls.

## Tally

Claims checked: about 120. Confirmed: about 117. Wrong: 0. Outdated: 0. Inconsistent or unclear: 3 (S1–S3).
