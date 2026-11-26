# Chapter 3: How Large Language Models Work (fourth review)

## Verdict

Ready to print after small fixes. Nothing here blocks printing. The chapter is technically accurate and its worked examples are reproducible. I re-ran every tokeniser count, the BPE table, the attention example, the GPT-2 parameter count, the KV-cache table and the GPT-2 small/XL probability tables, and every figure matched. Quotations checked against primary sources were word-for-word correct, and the 2026 material (DeepSeek-V4, Qwen3.5, Kimi K3, Muse Spark/Open, Gemini 4 Argon/Carbon, GPT-6 Astra, Claude Fable/Mythos 5 and Opus 5.5, Grok 4.7, the OpenAI–Hugging Face incident report, DevDay 2026, November releases) agrees with the developers' own pages. The SHOULD items cover one company-name change, one attribution, one date detail, one sourcing upgrade and one unclear sentence.

## MUST change before printing

None.

## SHOULD change

### S1. Grok's developer was no longer called "xAI" when Grok 4.7 shipped
- Where: textbook/chapters/ch03.md:389 (also :443 table row, :459)
- Text now: "xAI said it ran reinforcement learning for Grok 4 "at pretraining scale", and for Grok 4.7, in September 2026,"
- Problem: OUTDATED. xAI was rebranded SpaceXAI on 6–7 July 2026, after SpaceX acquired it in February 2026. Musk then announced a further rename to SpaceXSI ("super intelligence") on about 4 October 2026. The Grok 4.7 announcement page, dated 21 September 2026, now carries the name "SpaceXSI", with the legal name SpaceX Super Intelligence LLC in its footer. Calling the September 2026 developer "xAI" without comment will confuse readers who look the company up. Chapter 9 (line 246) already mentions the July rename to SpaceXAI but not the October one.
- Evidence: https://www.engadget.com/2209300/xai-now-officially-spacexai/ and https://gigazine.net/gsc_news/en/20260707-xai-change-spacexai ("the xAI account was changed to @SpaceXAI ... July 7, 2026"); https://teslanorth.com/2026/10/04/elon-musk-spacexai-spacexsi-rename/ (Musk: "Yes, we will make that change", 4 Oct 2026); https://x.ai/news/grok-4-7 (page footer: "SpaceX Super Intelligence LLC", accessed 26 Nov 2026).
- Change to: "xAI said it ran reinforcement learning for Grok 4 "at pretraining scale", and its successor company, renamed SpaceXAI in July 2026 and SpaceXSI in October, said of Grok 4.7, in September 2026," (keep "xAI" for 2025 events; at :459 write "SpaceXAI says Grok 4.7's training emphasised tasks that take many hours"; in the bib entry `xai2026grok47` set `author = {{SpaceXAI}}`, with howpublished "Company announcement, 21 September 2026 (company source; xAI was renamed SpaceXAI in July 2026 and SpaceXSI in October 2026)"). Align the wording with Chapter 9.

### S2. The anti-distillation safeguard was not new with Opus 5.5
- Where: textbook/chapters/ch03.md:461
- Text now: "and launched Opus 5.5 with an "anti-distillation safeguard" [@anthropic2026fable; @anthropic2026opus55]"
- Problem: UNCLEAR / slightly MISLEADING. The Opus 5.5 page calls it "the anti-distillation safeguard we introduced with Fable 5.1". It also says the safeguard "stops API users from editing Claude's prior context in an attempt to extract Claude's reasoning" and applies to API accounts created on or after 31 August 2026. The current sentence reads as though Opus 5.5 introduced it.
- Evidence: https://www.anthropic.com/claude-opus-5-5 (22 Sep 2026): "the anti-distillation safeguard we introduced with Fable 5.1"; https://www.anthropic.com/news/claude-fable-5-mythos-5 (9 Jun 2026): requests flagged as distillation attempts "will fall back to Opus 4.8".
- Change to: "and since Fable 5.1 has applied an "anti-distillation safeguard" that stops API users editing earlier context to extract Claude's reasoning, which Opus 5.5 also carries [@anthropic2026fable; @anthropic2026opus55]"

### S3. Sora: the app closed in April 2026, the API in September
- Where: textbook/chapters/ch03.md:265
- Text now: "OpenAI withdrew the Sora product in April 2026 [@openai2025sora]"
- Problem: UNCLEAR / weak sourcing. OpenAI's help centre gives two dates: the Sora web and app experiences were discontinued on 26 April 2026, and the Sora API on 24 September 2026. The cited page is the September 2025 Sora 2 launch post, so the withdrawal rests only on a note in the bib entry.
- Evidence: https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation (discontinuation of the Sora web/app on 26 April 2026 and the API on 24 September 2026); https://www.axios.com/2026/03/24/openai-discontinue-sora-video-app (announcement, 24 March 2026).
- Change to: "OpenAI closed the Sora app in April 2026 and its API in September [@openai2025sora; @openai2026sora]", with new bib entry:
  `@misc{openai2026sora, author = {{OpenAI}}, title = {What to Know about the {Sora} Discontinuation}, year = {2026}, howpublished = {OpenAI Help Center (company source): web and app discontinued 26 April 2026, API 24 September 2026}, url = {https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation}, urldate = {2026-11-26}}`

### S4. November 2026 releases cited to secondary or omnibus pages
- Where: textbook/chapters/ch03.md:449
- Text now: "In November 2026 Anthropic released Claude Fable 5.2 and Mythos 5.2 (9 November), Alibaba the closed-weight Qwen4-Max (16 November) and OpenAI GPT-6.2 Astra and Sol (17 November), each a new flagship version [@sdtimes2026fable52; @alibaba2026qwen4max; @openai2026gpt6]."
- Problem: UNSUPPORTED (weakly). The facts are right: all three dates are confirmed, and Qwen4-Max is closed-weight. But GPT-6.2 is cited only to an update note on the September GPT-6 Astra post, while OpenAI has its own GPT-6.2 announcement. Fable 5.2 is cited to SD Times rather than to Anthropic.
- Evidence: https://openai.com/index/introducing-gpt-6-2-astra-sol (17 Nov 2026); https://sdtimes.com/ai/anthropic-introduces-claude-fable-5-2-mythos-5-2/; https://thenextweb.com/news/alibaba-launches-qwen4-max-flagship-ai-model-without-open-weights ("keeping its weights closed").
- Change to: keep the sentence and replace `@openai2026gpt6` with a new entry:
  `@misc{openai2026gpt62, author = {{OpenAI}}, title = {Introducing {GPT-6.2 Astra} and {GPT-6.2 Sol}}, year = {2026}, howpublished = {Company blog, 17 November 2026 (company source)}, url = {https://openai.com/index/introducing-gpt-6-2-astra-sol/}, urldate = {2026-11-26}}`. If Anthropic's own 9 November post is available, cite it alongside SD Times.

### S5. Byte-level emoji sentence implies something the example contradicts
- Where: textbook/chapters/ch03.md:47
- Text now: "An emoji that never appeared in training is spelled out in byte-level pieces. The parrot emoji, four bytes in the standard UTF-8 encoding, becomes three tokens in both the GPT-2 and `o200k_base` tokenisers."
- Problem: UNCLEAR. Read together, the two sentences suggest that the parrot never appeared in training. In fact four bytes becoming three tokens means at least one learned merge covers part of it, so those bytes were seen. The token counts themselves are correct: I measured 3 tokens in each tokeniser and 4 bytes.
- Evidence: author's own check with tiktoken 0.14.0, 26 Nov 2026: `len(gpt2.encode("🦜")) = 3`, `len(o200k_base.encode("🦜")) = 3`, `len("🦜".encode()) = 4`.
- Change to: "A rare character need not have a token of its own: it is spelled out in byte-level pieces. The parrot emoji, four bytes in the standard UTF-8 encoding, becomes three tokens in both the GPT-2 and `o200k_base` tokenisers."

## Could not verify

- Software versions in the captions of Tables 3.6/3.7 (Hugging Face transformers 5.20.2, PyTorch 2.14.1). I reproduced every GPT-2 number with transformers 5.24.1 and PyTorch 2.15.0, so the values stand. I did not confirm the versions themselves.
- OpenAI's GPT-6 Astra announcement: the claims that it reports benchmarks for reading screens without describing the image pathway (:269), and that it reports retrieval accuracy between 512,000 and 1 million tokens (:453). The page was not fetched in full.
- Gemma 3 KV-cache overhead "from 60% to under 15%" (:251), and the Veo 3 quotations ("videos with audio", "dialogue between characters", :265). These are plausible, but I did not open the sources.
- Epoch AI's estimate of 20% for R1's RL share and the o3 "10×" statement: both confirmed in You (2025). Epoch's GPT-6 Astra figure of 9.4 × 10^26 FLOP is confirmed in Epoch's CSV export, so no open items remain for these.

## Checked and confirmed (brief)

- **Table 3.1** (all 8 IDs), the **vocabulary sizes in Table 3.3**, the `encoding_for_model` mapping (GPT-4o, o3, GPT-4.1, GPT-5 → o200k_base), " strawberry", " 12345678", token 9059 " cat" / 9060 "crypt", and **Table 3.4** (7/7, 9/15, 12/62, 13/20): all re-run with tiktoken 0.14.0.
- **Table 3.2:** reproduced exactly by running Sennrich's Algorithm 1.
- **Table 3.5:** weights and outputs reproduced in NumPy, including the softmax sum of 27.29.
- **Table 3.6:** total of 124,439,808, equal to the library count. The Kaplan approximation is within 0.14%.
- **Table 3.8:** all six cells recomputed. 16× GQA saving; DeepSeek-V3 is 7.3× smaller than Llama 3 405B.
- **Table 3.7 and the temperature/nucleus box:** GPT-2 small and XL and Qwen2.5-1.5B figures reproduced exactly (Qwen: " Paris" 27.3%, nucleus 103 at T = 1 and 4 at T = 0.5; tokeniser length 151,665), including logits of 8.78/8.35, nuclei of 3,068/10/951/14, and " mat" at rank 50. Fig. 3.2 bars (edge, floor, table, bed: 7.3/5.2/4.9/4.4%) match.
- **Arithmetic:** e^0.43 = 1.54; e^0.86 = 2.36; −ln 0.273 = 1.30; −ln 0.032 = 3.44; σ(1) = 0.73; GRPO std 0.5/0.58; t/(1−t) = 3; 128,000² ≈ 1.6 × 10^10; 147k/2.79M ≈ 5%; 9.4e26/3.14e23 ≈ 3,000.
- **Quotations verified:**
  - GPT-3 "without any gradient updates or fine-tuning"
  - tiktoken README ("arbitrary text, even text that is not in the tokeniser's training data")
  - Elhage residual-stream quotation
  - Olsson "preliminary and indirect evidence"
  - Vaswani quotations
  - Jain & Wallace
  - Mixtral "47B ... 13B"
  - Kimi K2 Thinking "lossless 2x speed-up", "interleave chain-of-thought reasoning with function calls", 200–300 tool calls
  - DeepSeek-V3.2: "a generative reward model where each prompt has its own rubrics", >10% RL budget, 1,800+ environments/85,000 prompts/1,827 synthesised, reasoning discarded only on a new user message
  - Tülu 3 RLVR definition
  - Mata v. Avianca sanctions opinion: p.1 quotation, p.15 "falsely assumed ... super search engine", p.19 "real", $5,000 on pp.33–34
  - Gunjal "up to 31%"
  - Muse Spark quotations, Contemplating mode, private API preview (8 Apr 2026)
  - Bender & Koller quotation; NLP metasurvey 327 of 480 respondents, 51% agree
  - Fable 5/Mythos 5 autonomy quotation and Opus 4.8 fallback
  - Opus 5.5: thinking cannot be switched off, effort levels low to max
  - Grok 4.7 "longer reinforcement learning run on a harder mix of tasks", hours-long tasks
  - Gemini 4 Carbon "run for days"; release first to cyber defenders (Argon and Carbon)
- **Model details checked:**
  - Gemini 4 Argon docs: input Text/Image/Video/Audio/PDF, output Text, 1,048,576 shared limit, low/medium/high thinking
  - Qwen3.5-397B-A17B: 60 layers, 15 × (3 DeltaNet + 1 attention), early fusion, "million-agent environments"
  - DeepSeek-V4: 1.6T/49B, >32T tokens, 27% FLOPs/10% KV, submitted 26 Apr 2026
  - Kimi K3: 2.8T/104B, KDA + gated MLA, July 2026
  - Qwen3.8-2.4T-A95B: August 2026
  - Muse Spark Open model card: 816B/42B, 8 of 256 experts, 1.8B perception encoder, text output, 15 Oct 2026
- **Events checked:**
  - OpenAI–Hugging Face incident report: July 2026 cyber-evaluation escape; reward hacking in training, including an agent that "copied the reference answer into its submission exactly, which led to positive RL reward"
  - DevDay 2026 (29 Sep): 1.2B weekly users
  - GPT-6 Astra system card: "Critical" cyber
  - Sora app discontinued 26 Apr 2026
- **Epoch figures:** post-training about 1/100 of pre-training (Edelman et al.); "RL environments" bottleneck.

## Tally

Claims checked: 168 · confirmed: 163 · wrong: 0 · outdated: 1 (S1) · unclear or weakly sourced: 4 (S2–S5)
