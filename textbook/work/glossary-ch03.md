**token**: The basic unit of text a language model reads and writes, usually a word, part of a word, a punctuation mark or a raw byte, each mapped to a fixed ID number. Prices and limits of language models are counted in tokens.
**vocabulary**: The fixed list of all tokens a model knows; modern vocabularies range from about 50,000 to about 200,000 entries.
**tokeniser**: The program that splits text into tokens from a model's vocabulary and maps them to their ID numbers.
**byte-pair encoding (BPE)**: A method for building a tokeniser's vocabulary by starting from single characters or bytes and repeatedly merging the most frequent adjacent pair into a new token.
**embedding**: A learned list of numbers that represents a token (or other item) as a point in a high-dimensional space, so that items used in similar ways lie close together.
**vector**: An ordered list of numbers, such as an embedding, that can be added, subtracted and compared position by position.
**transformer**: A neural-network architecture, introduced in 2017, built from stacked blocks of self-attention and feed-forward layers; the basis of current large language models.
**self-attention**: The mechanism by which each token's representation draws information from other tokens in the same sequence, weighted by how well its query matches their keys.
**query, key and value**: Three vectors computed from each token in attention: the query says what the token looks for, the key what it offers to be matched against, and the value the information it passes on.
**dot product**: A measure of how well two vectors match: multiply them number by number and add up the results; the total is large when both have large values in the same places.
**softmax**: A function that turns a list of scores into probabilities that are all positive and add up to one, giving the highest scores a disproportionately large share.
**causal mask**: The rule in a language model's attention that each token may attend only to itself and earlier tokens, implemented by setting scores for later tokens to minus infinity.
**attention head**: One of several attention computations run in parallel within a layer, each with its own query, key and value matrices.
**transformer block**: One layer of a transformer, consisting of an attention sublayer and a feed-forward sublayer, each with layer normalisation and a residual connection.
**residual stream**: The running vector for each position that every attention and feed-forward sublayer reads from and adds its output to, from the embedding up to the output layer.
**mixture of experts (MoE)**: A design in which each block contains many alternative feed-forward networks (experts) and a router sends each token to only a few, so that only a fraction of the parameters is used per token.
**rotary position embedding (RoPE)**: A way of giving a transformer word-order information by rotating the query and key vectors by angles that depend on each token's position, so that attention scores depend on relative distance.
**logit**: The raw score, positive or negative, that a language model's final layer gives each possible next token before the scores are turned into probabilities.
**autoregressive**: Generating a sequence one element at a time, each time feeding the output so far back in as input.
**next-token prediction**: The training task and generation method of most large language models: given the text so far, output a probability for every possible next token.
**decoding**: The procedure that turns a model's next-token probabilities into an actual choice of token, for example by greedy choice or by sampling.
**temperature**: A setting that divides the logits before the softmax; low temperatures concentrate probability on the most likely tokens, high temperatures spread it more evenly.
**top-k sampling**: A decoding method that samples only from the *k* most likely next tokens.
**nucleus (top-p) sampling**: A decoding method that samples only from the smallest set of most likely tokens whose probabilities add up to at least *p*, so the set grows and shrinks with the model's confidence.
**KV cache**: The stored keys and values of all earlier tokens, kept during generation so that each new token does not require recomputing them; its size limits how many requests a server can handle.
**grouped-query attention**: A variant of multi-head attention in which groups of query heads share one key–value head, shrinking the KV cache.
**context window**: The maximum number of tokens a model can take into account at once, functioning as its working memory for a single request.
**pre-training**: The first and usually most expensive training stage, in which a model learns next-token prediction on a very large body of text and becomes a base model.
**base model**: A model that has been pre-trained but not post-trained; it continues text rather than following instructions.
**self-supervised learning**: Training in which the answers come from the data itself, for example the next token of a text, so that no human labelling is needed.
**post-training**: The training stages after pre-training (instruction tuning, preference training, reinforcement learning) that turn a base model into an assistant or reasoning model.
**instruction tuning**: Supervised fine-tuning of a pre-trained model on examples of instructions paired with good responses, so that it learns to follow requests.
**reinforcement learning**: A way of training in which a system tries actions or answers and receives only a score (a reward) for how good the result was, and is adjusted to make high-scoring behaviour more likely.
**reinforcement learning from human feedback (RLHF)**: A post-training method in which people rank model outputs, a reward model learns their preferences, and the language model is then trained to produce outputs the reward model rates highly.
**reward model**: A network trained on human (or AI) comparisons to output a single score predicting how much a response will be preferred.
**direct preference optimisation (DPO)**: A post-training method that learns from pairs of preferred and rejected answers with a classification-style loss, without training a separate reward model or running reinforcement learning.
**Constitutional AI**: A post-training method developed at Anthropic in which a model critiques and revises its own outputs against a short list of written principles, and AI-generated preference judgements replace human harmlessness labels.
**reinforcement learning from AI feedback (RLAIF)**: Reinforcement learning in which the preference judgements come from an AI model rather than from people.
**reinforcement learning with verifiable rewards (RLVR)**: Reinforcement learning in which the reward comes from a program that checks the answer, for example by comparing a final number or running tests, rather than from a learned reward model.
**chain-of-thought prompting**: Prompting a model with worked examples that show intermediate reasoning steps, so that it writes out steps before its answer.
**hallucination**: A fluent but false or unsupported statement produced by an AI model, such as an invented citation; the term is a metaphor, since the model perceives nothing, and the behaviour arises partly because training and scoring reward confident guessing.
**retrieval-augmented generation (RAG)**: A technique in which a system first searches a collection of documents and places the relevant passages in the model's context window before it answers.
**interpretability**: The study of what the internal computations and representations of a trained model mean.
**in-context learning**: A model's ability to perform a new task from instructions or worked examples given in its prompt, without any change to its weights.
**encoder**: The part of a transformer that reads a whole input without a causal mask, so each token can attend to tokens on both sides; BERT is an encoder-only model.
**decoder**: The part of a transformer that generates output one token at a time under a causal mask; GPT-style chatbots are decoder-only models.
**induction head**: An attention circuit that finds an earlier occurrence of the current token and predicts the token that followed it, completing patterns of the form [A][B] … [A] → [B]; a proposed mechanism for in-context learning.
**special token**: A vocabulary entry that does not stand for ordinary text, such as an end-of-text marker or a marker for the start of a chat turn.
**chat template**: The format that turns a conversation of system, user and assistant messages into a single token sequence, using special tokens to mark each turn.
**speculative decoding**: A way to speed up generation in which a small model (or extra heads of the same model) drafts several tokens and the large model checks them in one parallel pass, accepting or replacing each by a rule that leaves the output's probabilities exactly those of the large model alone.
**RMSNorm**: A simplified form of layer normalisation that rescales each vector by its root-mean-square size without subtracting the mean.
**calibration**: The match between a model's confidence and its accuracy; a calibrated model is right about 70% of the time on answers it gives 70% probability.
**knowledge cut-off**: The date after which a model's training data end, so that it has no knowledge of later events unless they are supplied in its context.
**value network**: In reinforcement learning, a second network that predicts how good a partial output or state is, used as a baseline when judging the reward; GRPO does without one.
**multi-head latent attention (MLA)**: An attention design, introduced by DeepSeek, that caches one short compressed vector per token from which the keys and values of all heads are reconstructed, shrinking the KV cache.
**sliding-window attention**: Attention in which each token attends only to a fixed number of recent tokens, often alternated with layers of full attention.
**sparse attention**: Attention in which each token attends to a selected subset of earlier tokens, for example those a small scoring network ranks highest, rather than to all of them.
**state-space model**: A sequence model, such as Mamba, that carries a fixed-size internal state from token to token, so its cost grows only linearly with length; often mixed with attention layers in hybrid models.
**linear attention**: A family of attention substitutes, such as Gated DeltaNet, that keep a fixed-size memory updated by each new token instead of a growing key–value cache.
**multi-token prediction**: A training objective in which a model also predicts tokens more than one step ahead; the extra predictions can serve as drafts for speculative decoding.
**diffusion language model**: A text generator that starts from masked or noisy positions and fills in many tokens in parallel over several rounds, rather than writing strictly left to right.
**process reward model**: A reward model that scores each intermediate step of a solution rather than only the final answer.
**rubric-based reward**: A reward computed by a judge model that checks a response against a list of criteria written for that prompt, used where no program can verify the answer.
**LLM judge**: A language model used to grade or compare other models' outputs, in evaluation or as a source of reward.
**environment (reinforcement learning)**: The software world a model acts in during reinforcement learning, such as a code repository with tests, a browser or a simulated computer, together with the checker that decides the reward.
**agentic reinforcement learning**: Reinforcement learning on multi-step tasks in which the model calls tools, reads their results and continues, with the reward given for completing the task.
**interleaved thinking**: Reasoning that alternates with tool calls within one response, so that the model can reflect on each tool's result before acting again.
**hybrid reasoning model**: A single model that can either answer directly or reason at length first, often with a user-set budget or effort level.
**early fusion**: Training a multimodal model on a single sequence in which images or audio are turned into tokens alongside text from the start.
**omni model**: A model that takes in, and in some cases produces, several modalities such as text, images, audio and video within one network.
**world model**: An AI system that simulates aspects of the world, for example by generating an interactive environment that responds to a user's actions.
