# Review 9: Chapter 2 (textbook/chapters/ch02.md)

## Verdict
Ready to print. Every worked example was recomputed and is correct: neuron, Table 2.1, matrix layer, XOR, softmax and cross-entropy, one-weight gradient descent and divergence threshold, Adam first step, the nine-parameter backpropagation including the update and re-run (loss 0.4741 → 0.3021), sigmoid vanishing 0.25^10, He-init variance factor 0.0256^10 ≈ 1.2 × 10^-16, convolution counts, matmul reuse (~2,731), H100 ops/byte (~591 sparse, ~295 dense), and the adversarial ε·m·n ≈ 10.5. Quotations and figures from the classic papers match. One SHOULD concerns DeepSeek-V4-Pro's parameter count after its August release. The tone towards companies is neutral.

## MUST change before printing
None.

## SHOULD change

### S1. DeepSeek-V4-Pro's official (August) release is listed at 1.7T parameters, not 1.6T
- Where: textbook/chapters/ch02.md:77 (Section 2.2, MoE paragraph); also the intro (line 5) and Section 2.9 synapse comparison
- Text now: "DeepSeek-V4-Pro, for example, which its developer released as a preview in April 2026 and in an official version in August, has 1.6 trillion parameters in total but activates 49 billion per token, according to the company's technical report"
- Problem: UNCLEAR / partly OUTDATED. The 1.6T/49B figures come from the April technical report, which describes the preview. DeepSeek's own Hugging Face card for the August release, DeepSeek-V4-Pro-0813, gives a model size of 1.7T. The card says the release is "built on the DeepSeek-V4-Pro (Preview) model structure, with a DSpark speculative decoding module attached", which likely accounts for the extra parameters. As written, the sentence applies the preview figure to the official version.
- Evidence: https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813 (accessed 27 Nov 2026): Model size "1.7T params"; "built on the DeepSeek-V4-Pro (Preview) model structure, with a DSpark speculative decoding module attached". https://inferencex.semianalysis.com/model/deepseek-v4: "1.7T params for DeepSeek-V4-Pro-0813".
- Change to: "DeepSeek-V4-Pro, for example, which its developer released as a preview in April 2026 and in an official version in August, has 1.6 trillion parameters in total but activates 49 billion per token, according to the company's technical report on the preview (the August release adds a small speculative-decoding module and is listed at 1.7 trillion)". The intro's "stores 1.6 trillion adjustable numbers" and the "about a hundred times" synapse comparison remain valid as approximations. Chapters 3 and 7 use the same 1.6T figure, so a single footnote-style clause here is enough.

## Could not verify
- Zech et al. (2018) figures (158,323 radiographs; 34.2/1.2/1.0% prevalence; AUC 0.861, 0.931, 0.815; 99.95/99.98%) and Zhang et al. (2017) Table 2.5 values. The papers were not reopened, but the figures are consistent with my reading of them.
- Kimi K2 and DeepSeek-V4 optimiser details (company reports) were not reopened.

## Checked and confirmed
- Cornell Chronicle (Lefkowitz 2019): July 1958, ONR, IBM 704, "After 50 trials", Rosenblatt a "research psychologist" at the Cornell Aeronautical Laboratory. The NYT 1958 quotation matches.
- Nakkiran et al. abstract: "increasing (even quadrupling) the number of train samples actually hurts test performance".
- DeepSeek-V4-Pro: preview in April 2026 (HF card 23–24 Apr); GA on 13 Aug 2026 (DeepSeek API news "DeepSeek-V4-Pro GA Release 2026/08/13"); 1.6T/49B for the preview.
- Table 2.4 recipes (AlexNet, ResNet, Transformer) match the papers. ResNet top-1 27.94/28.54/27.88/25.03 and the 1,202-layer result are correct.
- AlexNet: ReLU six times faster on CIFAR-10, 60M parameters, five to six days on two GTX 580s, augmentation factor 2,048, weight decay quotation, "waiting for faster GPUs".
- Adam defaults and "trust region"; AdamW quotation; Goodfellow "default recommendation", "familiarity with the algorithm", "probably the most commonly used form of regularization".
- Glorot, He-init 30-layer "completely stalls", BN "14 times fewer training steps", Santurkar, Goyal 8,192 batch / 256 GPUs / one hour.
- Dropout 0.5/0.8 and MNIST 1.60/1.25/1.06%; Geirhos 95.9%, 22.1%, 63.9%; panda 57.7% → gibbon 99.3% with ε = 0.007; adversarial training 89.4 → 17.9% and 0.94 → 0.84%; Recht 3–15 and 11–14 points.
- H100 SXM: 67 TFLOPS FP32, 1,979 TFLOPS FP16 Tensor with sparsity, 3.35 TB/s. Kaplan 6N/2N.
- Azevedo 86 billion neurons; Pakkenberg 1.5 × 10^14 neocortical synapses (≈ 94 × 1.6T).
- Cross-references (Sections 1.7, 3, 4, 7.1, 12) point to the right places.

## Tally
Claims checked: 85 / confirmed: 84 / wrong: 0 / outdated: 1 (partly)
