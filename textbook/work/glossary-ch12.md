**alignment**: The property of an AI system pursuing the goals its developers and users actually intend; a misaligned system pursues goals that conflict with those intentions.
**specification gaming**: Behaviour that satisfies the literal specification of an objective without achieving the intended outcome, such as a game agent scoring points without finishing the race.
**reward hacking**: Specification gaming in which a model exploits flaws in a reward signal or reward model, for example by making automated tests pass without solving the task.
**sycophancy**: The tendency of an AI model to tell users what they want to hear, such as agreeing with their views or flattering them, rather than what is accurate.
**scheming**: Covert pursuit of a goal by an AI system, for example by hiding its intentions, sabotaging tasks or evading oversight; studied so far mainly in artificial test scenarios.
**alignment faking**: Behaviour in which a model complies with a training objective it disagrees with in order to avoid being modified, while behaving differently when it believes it is not being trained.
**evaluation awareness**: A model's ability to recognise that it is being tested, which can change its behaviour and make evaluation results less representative of real use.
**mechanistic interpretability**: Research that tries to explain, in terms people can follow, the internal computations by which a trained neural network produces its outputs.
**feature**: A property of the input that a neural network represents internally, such as a language or a landmark, usually encoded as a pattern of activity across many neurons.
**superposition**: The hypothesis that a network represents more features than it has neurons or dimensions by overlapping them, accepting some interference because most features are rarely active together.
**sparse autoencoder**: A secondary network trained to rewrite a model's internal activations as a much larger set of features, only a few of which are active at once, so that each feature is easier to interpret.
**circuit**: A group of features and the connections between them that together carry out an identifiable step of a network's computation.
**chain-of-thought monitoring**: Using a person or another model to read a reasoning model's written intermediate steps in order to detect undesired intentions or behaviour.
**dangerous-capability evaluation**: A test of whether a model is able to do something that could cause severe harm, such as giving meaningful help with cyber-attacks or weapons.
**frontier safety framework**: A company policy that sets capability thresholds for its most advanced models and the safeguards it will apply, or the actions it will take, when those thresholds are reached.
**corrigibility**: The property of an AI system cooperating with corrective interventions by its developers, such as being shut down or having its goals changed, rather than resisting them.
**defence in depth**: A safety strategy that layers several imperfect safeguards so that a failure in one is likely to be caught by another.
**red-teaming**: Deliberately attacking an AI system, by people or by other models, to find its failures before release.
**reward model**: A copy of a language model with an added output that gives a single score to any answer, trained on human (or AI) comparisons so that score differences predict which answer is preferred.
**reward-model over-optimisation**: The decline in true quality that follows when a policy is optimised too hard against a learned reward model, an instance of Goodhart's law.
**KL penalty**: A term in RLHF training that subtracts reward in proportion to how far the trained model's outputs have moved from those of the starting model, measured by the Kullback–Leibler divergence.
**scalable oversight**: Methods, such as debate or AI-assisted evaluation, intended to let humans supervise AI systems on tasks too hard for humans to check directly.
**emergent misalignment**: Broadly misaligned behaviour that appears after a model is trained on a narrow task, such as writing insecure code or exploiting test environments.
**propensity evaluation**: A test of whether a model is inclined to use its capabilities for harm, as opposed to whether it is able to.
**elicitation**: The effort, through prompting, tools, fine-tuning or time, made to draw out a model's best performance in a capability test.
**sandbagging**: Strategic underperformance on an evaluation, whether prompted by a developer or arising from the model itself.
**polysemantic neuron**: A neuron that responds to several unrelated concepts, so that its activity cannot be read as standing for one thing.
**activation steering**: Changing a model's behaviour by artificially setting the strength of an internal feature while it runs, without prompting or retraining.
**attribution graph**: A diagram, produced for one prompt, of which internal features influenced which others and the final output, built from an interpretable replacement for parts of the model.
**chain-of-thought faithfulness**: The degree to which a model's written reasoning reflects the factors that actually determine its answer.
**obfuscated reward hacking**: Reward hacking that continues while the model's written reasoning no longer reveals it, learned when reasoning is penalised for showing intent to cheat.
**AI control**: Safety measures, such as monitoring by trusted models and auditing, designed to prevent harm even if the AI system being used is deliberately trying to cause it.
**universal jailbreak**: An attack that bypasses a model's safeguards across many different harmful requests rather than for a single one.
**inner alignment**: The problem of ensuring that a model which has itself become an optimiser pursues the objective it was trained on rather than a different learned objective (a mesa-objective); outer alignment is the problem of making the trained objective match what developers intend.
**goal misgeneralisation**: A failure in which a model keeps its capabilities in new situations but pursues an unintended goal that coincided with the intended one during training; it can occur even when the training objective is correct.
**unlearning**: Training a model to remove specific knowledge, such as hazardous technical information, while preserving its other capabilities.
**linear probe**: A simple classifier trained to read a property, such as whether a response is deceptive, directly from a model's internal activations.
**Kullback–Leibler (KL) divergence**: A standard measure of how far one probability distribution is from another; in RLHF it measures how far the trained model's outputs have drifted from those of the starting model.
**deliberative alignment**: A training method in which a model is taught to read and reason explicitly about a written safety specification before acting.
**probing**: Training a simple classifier (a probe) on a model's internal activations to test whether, and how readily, they encode a given property.
