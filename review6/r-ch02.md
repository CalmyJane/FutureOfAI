# Review 6: Chapter 2 (textbook/chapters/ch02.md)

## Verdict
Ready to print. I recomputed every worked example and every number is right. The figures from published papers that I checked match their sources. The only item is one sentence whose structure is confusing.

## MUST change before printing
None.

## SHOULD change

### S1. DeepSeek-V4-Pro sentence is hard to parse
- Where: textbook/chapters/ch02.md:78
- Text now: "DeepSeek-V4-Pro, for example, which its developer released as a preview in April 2026, described in a company technical report, and then in an official version in August, has 1.6 trillion parameters in total but activates 49 billion per token, according to the technical report"
- Problem: UNCLEAR. The way the clauses are chained suggests the model was "described ... in an official version in August". The facts are right: the preview was released 23–24 April 2026, there is a technical report, general availability came on 13 August 2026, and the model has 1.6T total and 49B active parameters.
- Evidence: https://api-docs.deepseek.com/news/news260813 ("DeepSeek-V4-Pro General Availability", 2026/08/13; the sidebar lists "DeepSeek-V4 Preview Release" 2026/04/24). The Hugging Face card for deepseek-ai/DeepSeek-V4-Pro gives "1.6T parameters (49B activated)".
- Change to: "DeepSeek-V4-Pro, for example, which its developer released as a preview in April 2026 and in an official version in August, has 1.6 trillion parameters in total but activates 49 billion per token, according to the company's technical report [@deepseekai2026deepseekv4; @deepseekai2026v4pro]."

## Could not verify
- Line 228: the official release of V4-Flash on 31 July 2026. The Hugging Face card for DeepSeek-V4-Flash-0731 shows no date. The 13 August notice confirms V4-Pro but not the Flash date. The model name (0731) is consistent with the date.
- Page-specific quotations from Goodfellow et al. (secs. 6.1, 8.5.4, 7.4, 7.8, 15.1.1). They match the wording I know from the book, but I did not reopen it.

## Checked and confirmed
- Arithmetic. Neuron, z = 0.2 (and −0.3 with inputs 1 and 1). Table 2.1: sigmoid/tanh values and slopes 0.248 and 0.961. Layer example: −3.4 and 1.8. Figure 2.2: 26 parameters. XOR Table 2.2. Softmax 0.659/0.242/0.0986 and losses 0.417/2.317. One-weight descent: slope −2.4; 0.3364 and a fall of 0.0236; w = 0.44 and loss 0.0144; the factor 1 − 8η, giving 1.4 and 3.24 at η = 0.5; divergence above 0.25.
- Backprop box (Table 2.3). I recomputed it in Python: p = 0.6225, L = 0.4741, and all the gradients; after the update h = (1.2265, 0.2735), z = 1.0423, p = 0.7393, L = 0.3021. Nine parameters.
- Adam first step: m₁ = −0.24, v₁ = 0.00576, step +0.001. Momentum factor 1/(1−β). 0.25^10 ≈ 9.5 × 10^−7. He initialisation √(2/512) = 0.0625, 0.0256 per layer, 0.0256^10 ≈ 1.2 × 10^−16.
- Convolution (Figure 2.5): feature-map columns 0, 3, 3. 1,728 weights against 4.8 × 10^11. Matrix product 3.4 × 10^10; reuse 2 × 4096/3 ≈ 2,731. H100: 1,979/3.35 ≈ 590 (sparse) and about 295 (dense). Adversarial example: 0.007 × 0.01 × 150,528 ≈ 10.5. Synapses 1.5 × 10^14 / 1.6 × 10^12 ≈ 94, "about a hundred".
- Source figures. ResNet top-1 errors 27.94/28.54/27.88/25.03 (Figure 2.4). Table 2.4 recipes (AlexNet, ResNet, Transformer). Goyal: 8,192 images, 256 GPUs, one hour, 5-epoch warm-up. Batch normalisation: 14 times fewer steps. Dropout on MNIST 1.60/1.25/1.06. AlexNet augmentation factor 2,048. LeNet-5 0.35%/0.95%. Zhang Table 2.5. Nakkiran, "increasing (even quadrupling) the number of train samples" (arXiv 1912.02292). Lee et al. "ten times less frequently" and "over 4%". Geirhos 95.9%/22.1%/63.9%. Zech 158,323 images, 34.2/1.2/1.0%, AUC 0.861, 99.95/99.98%, 0.931/0.815. Recht 3–15 and 11–14 points. Goodfellow et al. 2015 panda 57.7% and gibbon 99.3%; 89.4→17.9% and 0.94→0.84%.
- 2025–2026 material. DeepSeek-V4-Pro has 1.6T parameters with 49B active (Hugging Face and NVIDIA cards), uses Muon, was previewed in April 2026 and reached general availability on 13 August 2026. Kimi K2 has about 1T parameters with 32B active, a constant learning rate for 10T tokens, and MuonClip.
- Line 3: the NYT 8 July 1958 wording matches the widely reproduced text.
- Internal consistency. DeepSeek-V4-Pro figures match ch03:451 and ch07:272. The V4 dates at lines 78 and 228 agree. The cross-references §1.7, §2.2, §2.4, §2.6, §7.1 and Chapter 12 are correct.

## Tally
Claims checked: 75 / confirmed: 74 / wrong: 0 / outdated: 0 (1 SHOULD on clarity; 2 could not be verified)
