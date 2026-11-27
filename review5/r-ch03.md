# Review 5: Chapter 3, How Large Language Models Work

## Verdict

**Ready to print after small fixes.** This is the most heavily verified chapter I have seen in the book. I re-ran every computed table and they all reproduce exactly:

- Tables 3.1, 3.3 and 3.4, plus the strawberry, digit-chunking and emoji claims (tiktoken 0.14.0).
- Table 3.2 (Sennrich's Algorithm 1, verbatim).
- Table 3.5 (NumPy).
- Table 3.6 (parameter count).
- Table 3.7, the temperature/nucleus box and the " mat" rank of 50, re-run with GPT-2, GPT-2 XL and Qwen2.5-1.5B on CPU at fp32 with transformers 5.24.1. The numbers are identical to the book's.
- Table 3.8 (KV-cache arithmetic).

The 2026 material is supported by the cited primary sources. I spot-checked DeepSeek-V4, Kimi K3, Muse Spark Open, Qwen3.5, Qwen3.8, Gemini 4 Argon/Carbon, GPT-6 Astra, Opus 5.5, Fable 5/5.2, Mythos Preview, the Sora shutdown, the OpenAI–Hugging Face incident report and DevDay 2026.

I found no MUST items. There are three SHOULD items: two are precision problems about company names and safeguards, and one is a small consistency fix.

## MUST change before printing

None.

## SHOULD change

### S1. xAI described as a "successor company", and the SpaceXSI name is presented as a legal rename
- Where: textbook/chapters/ch03.md:389
- Text now: "xAI said it ran reinforcement learning for Grok 4 "at pretraining scale", and its successor company, renamed SpaceXAI in July 2026 and SpaceXSI in October, said of Grok 4.7"
- Problem: UNCLEAR / INCONSISTENT.
  - xAI did not get a successor company. It became a SpaceX subsidiary (February 2026) and was then rebranded.
  - "SpaceXSI" is a brand and X handle adopted in October 2026. The legal entity is still SpaceXAI LLC.
  - The same chapter calls the developer "SpaceXAI" in Table 3.9 (line 443) and in present tense at line 459 ("SpaceXAI says ..."). After reading line 389, a reader would expect "SpaceXSI" there.
- Evidence:
  - https://en.wikipedia.org/wiki/SpaceXAI (accessed 27 Nov 2026): "October 10, 2026: The official X account was renamed SpaceX Super Intelligence, with the handle @SpaceXSI … By October 13, 2026: The website and legal terms used the SpaceXSI branding. The legal name remained SpaceXAI LLC".
  - https://x.ai/news/grok-4-7 (21 Sep 2026): Grok 4.7 was announced under the SpaceXAI name.
- Change to: "xAI said it ran reinforcement learning for Grok 4 "at pretraining scale", and the same developer, by then a SpaceX subsidiary trading as SpaceXAI (rebranded SpaceXSI in October), said of Grok 4.7". At line 459, change "SpaceXAI says Grok 4.7's training" to "SpaceXAI said that Grok 4.7's training".

### S2. The anti-distillation safeguard is described more broadly than Anthropic states
- Where: textbook/chapters/ch03.md:461
- Text now: "and since Fable 5.1 has applied an "anti-distillation safeguard" that stops API users editing earlier context to extract Claude's reasoning, which Opus 5.5 also carries"
- Problem: UNSUPPORTED (scope). Anthropic says the safeguard applies only to API accounts created on or after 31 August 2026. It does not apply to all API users. Also, the Fable 5 announcement cited first (@anthropic2026fable) does not mention the safeguard. It describes only the fallback to Opus 4.8 for flagged requests.
- Evidence: https://www.anthropic.com/claude-opus-5-5 (22 Sep 2026): "Opus 5.5 is launching with preserved thinking, the anti-distillation safeguard we introduced with Fable 5.1." "It stops API users from editing Claude's prior context in an attempt to extract Claude's reasoning." The page says this applies "for API accounts created on or after August 31, 2026". https://www.anthropic.com/news/claude-fable-5-mythos-5 (9 Jun 2026): "Requests that are flagged by our classifiers as being part of such distillation attempts will fall back to Opus 4.8."
- Change to: "Anthropic routes requests its classifiers flag as distillation attempts to an older model [@anthropic2026fable], and since Fable 5.1 has applied an "anti-distillation safeguard" that, for API accounts created from 31 August 2026, stops users editing earlier context to extract Claude's reasoning; Opus 5.5 also carries it [@anthropic2026opus55]."

### S3. Gemini 4 Argon's "input–output limit" in Table 3.9 does not match Google's launch blog
- Where: textbook/chapters/ch03.md:444
- Text now: "1-million-token input–output limit; text, image, video and audio input; released first to cyber defenders"
- Problem: UNCLEAR. The API documentation (@google2026gemini) supports the text (line 453), which describes a unified 1,048,576-token limit. However, the table row also cites @kavukcuoglu2026gemini4argon, and that launch blog presents the 1M figure as an *output* limit raised from 64K. A reader who checks the blog will see a contradiction.
- Evidence:
  - https://aistudio.google.com/docs/models/gemini-4-argon (accessed 27 Nov 2026): "unified input and output token limit", 1,048,576.
  - https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/ (30 Sep 2026): "significantly expanding the model's output token limit to an industry-leading 1M tokens, up from the previous 64K tokens."
- Change to: "1-million-token limit shared by input and output (output up from 64,000); text, image, video and audio input; released first to cyber defenders"

## Could not verify

- Mata v. Avianca pin cites (pp. 15, 19, 33–34). The quotations and the $5,000 sanction match the opinion, but I did not check the page numbers against the PDF.
- "lossless 2x speed-up" (Kimi K2 Thinking) and the Mercury Coder throughput (737–1,109 tok/s). I relied on memory of the sources and did not re-fetch them.
- Whether any further flagship model was released between 17 and 27 November 2026, which would extend the line-449 list. Release trackers seen on 27 Nov 2026 name GPT-Image 2.6 and GPT-6 Cyber (4–5 Nov), which are not flagships. I found no new Gemini, DeepSeek or Grok flagship, but these aggregators are low quality.
- Epoch's ~20% estimate for R1's RL share (@you2025how) was not re-fetched.

## Checked and confirmed (brief)

- **Recomputed:** Tables 3.1–3.8 and Figure 3.2's bar values (edge 7.3, floor 5.2, table 4.9, bed 4.4); the nucleus sizes 3,068/10, 951/14 and 103/4; the logits 8.78/8.35 and ratios e^0.43^≈1.54 and e^0.86^≈2.36; −ln 0.273 = 1.30 and −ln 0.032 = 3.44; the 12·L·d² approximation (0.14% off); 2N ≈ 170M operations per token; 70 KB < 1/7 of 516 KB; 1.6×10^10^ query–key pairs; GRPO standard deviations of 0.5 and 0.58; σ(1) = 73%; and t/(1−t) = 3.
- **Primary sources verified:**
  - DeepSeek-V4: 1.6T/49B parameters, >32T tokens, and 27% of FLOPs and 10% of KV cache versus V3.2.
  - Kimi K3: 2.8T/104B parameters, KDA plus Gated MLA, 1M context, weights released July 2026.
  - Muse Spark Open: 816B/42B parameters, 8 of 256 experts, 1.8B encoder, text-only output, 15 Oct 2026.
  - Qwen3.5: 15 full-attention layers of 60; the early-fusion and "million-agent environments" quotes.
  - Qwen3.8: 2.4T/95B, August 2026.
  - Qwen4-Max: closed weights, 16 Nov 2026.
  - GPT-6 Astra: Critical cybersecurity threshold; MRCR retrieval at 512K–1M; released 3 Sep 2026. Epoch's estimate is 9.4×10^26^ ("Likely"), about 3,000 × GPT-3.
  - GPT-6.2 Astra and Sol.
  - Fable 5.2 and Mythos 5.2 (9 Nov 2026).
  - Opus 5.5: effort levels from low to max; no thinking-off mode.
  - The Fable 5 autonomy quote; the Mythos tier above Opus.
  - Mythos Preview withheld (7 Apr 2026).
  - Gemini 4 Argon API: text-only output; low/medium/high thinking.
  - Gemini 4 Carbon: "run for days"; cyber defenders first.
  - Grok 4.7: quote and date.
  - Muse Spark: quote, Contemplating mode, private API preview.
  - Sora: app discontinued 26 Apr 2026, API 24 Sep 2026.
  - OpenAI–Hugging Face report: July 2026 escape, and the reward for copying the reference answer.
  - DevDay 2026: 1.2B weekly users.
- **Older literature:** the quotes from Vaswani, Holtzman, Rafailov, Bender, Jain & Wallace, Olsson, GPT-2 and tiktoken; the NLP survey (327 of 480 respondents, 51%/49%); Chen et al. (25% and 39%); Magesh (17–33%); Karpukhin (78.4 vs 59.1); Kwon (20.4–38.2%, 2–4×); DeepSeek-V2 (93.3%, 5.76×); Gemma 3 (5:1, 1,024 tokens, 60%→<15%); Llama 3 architecture and data mix; DeepSeek-R1 Nature figures (15.6→77.9, 79.8, ~147K GPU-hours).
- **Cross-references:** Sections 2.1, 2.3, 2.5, 3.x, 4.6, 5.3, 7.1, 9.1, 11, 12.2, 12.4 and 12.5 all resolve to the right content.

## Tally

Claims checked: 118. Confirmed: 115. Wrong: 0. Imprecise or unclear: 3 (S1–S3). Outdated: 0.
