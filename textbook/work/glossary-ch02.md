**activation function**: The simple rule a neuron applies to its weighted sum to produce its output, such as ReLU (keep positives, turn negatives into zero), the sigmoid (squash into the range 0 to 1) or tanh (squash into −1 to 1). Its non-linearity is what lets stacked layers do more than a single layer could.
**Adam**: An optimiser that keeps, for every weight, a running average of recent gradients and of their squares, and moves each weight by the first divided by the square root of the second; this gives each weight its own step size, roughly bounded by a single learning-rate setting.
**adversarial example**: An input altered by a small, deliberately chosen change, often invisible to people, that makes a trained network give a wrong answer with high confidence.
**artificial neuron**: The basic unit of a neural network: it multiplies each input by a weight, adds the results and a bias, and passes the total through an activation function to give one output number.
**backpropagation**: The algorithm that computes, for every weight in a network, how much a small change would alter the loss, by passing error signals backwards from the output layer using the chain rule. Its cost is of the same order as running the network forwards.
**batch normalisation**: A layer that, during training, re-centres and re-scales each neuron's totals using the mean and standard deviation over the current minibatch, then applies a learned scale and shift; it allows higher learning rates and faster training.
**bias (in a neuron)**: A number added to a neuron's weighted sum that shifts its total up or down, setting how readily the neuron produces a non-zero output. Biases are learned along with weights.
**catastrophic forgetting**: The tendency of a network trained on a new task to overwrite the weights that served an earlier task, losing the earlier skill.
**chain rule**: The rule from calculus that the rate of change through a chain of dependencies is the product of the individual rates; backpropagation applies it layer by layer.
**convolutional neural network**: A network for grid-like data such as images that slides small shared kernels across the input and summarises nearby results (pooling), so that features are recognised wherever they appear with far fewer weights.
**cross-entropy**: The standard loss for classification: the negative natural logarithm of the probability the network gave to the correct answer, so that confident wrong answers are penalised heavily.
**data augmentation**: Creating extra training examples by transforming existing ones in ways that do not change the correct answer, such as cropping or mirroring an image.
**distribution shift**: A difference between the data a model meets in use and the data on which it was trained and tested, which can lower its accuracy even when the difference is invisible to people.
**double descent**: The observation that, as model size grows, test error can first fall, then rise towards the size at which the model just fits its training data exactly, and then fall again for still larger models.
**dropout**: A regularisation method that randomly switches off a fraction of units at each training step, so that the network cannot rely on particular units and in effect trains many thinned networks that share weights.
**early stopping**: Halting training when error on the validation set stops improving and keeping the best weights found so far.
**epoch**: One complete pass through the training data during training.
**feature map**: The grid of outputs produced by sliding one convolutional kernel across an input; high values mark where the kernel's pattern occurs.
**generalisation**: A trained model's ability to perform well on new data it has not seen during training, estimated using held-out validation and test sets.
**gradient**: The list of slopes of the loss with respect to every weight in a network: how much the loss would rise or fall if each weight were increased by a tiny amount.
**gradient descent**: A method for training that repeatedly moves every weight a small step against its gradient, so that the loss decreases.
**graphics processing unit (GPU)**: A chip with thousands of small arithmetic units working in parallel, originally built for computer graphics; modern versions add dedicated units for matrix multiplication, the main arithmetic of neural networks.
**hidden layer**: A layer of neurons between the input and the output whose values are not directly given in the training data; hidden layers learn intermediate representations of the input.
**hyperparameter**: A setting chosen by people rather than learned by the training algorithm, such as the number of layers, the learning rate or the dropout rate; usually tuned on the validation set.
**initialisation**: The choice of random starting values for a network's weights; their scale must keep signals from shrinking or growing exponentially from layer to layer.
**kernel (convolutional)**: A small grid of weights, such as 3 × 3, that a convolutional layer slides across its input, multiplying and adding at every position.
**layer normalisation**: A variant of batch normalisation that computes the mean and standard deviation over the neurons of a layer for each example separately; it is used in transformers.
**learning rate**: The hyperparameter that sets how large a step gradient descent takes; too small makes training slow, too large makes it overshoot or diverge.
**logit**: The raw score a classification network produces for each class before the softmax turns the scores into probabilities.
**loss function**: A formula that turns a model's output and the correct answer into a single number measuring how wrong the output is (for example squared error or cross-entropy); training aims to make its average as small as possible.
**minibatch**: A small random sample of training examples used to estimate the gradient for one step of stochastic gradient descent.
**momentum**: A modification of gradient descent in which a running velocity accumulates past gradients, so that consistent directions speed up and oscillating ones cancel.
**multilayer perceptron**: A feed-forward neural network with one or more hidden layers in which every neuron in one layer is connected to every neuron in the next.
**overfitting**: The situation in which a model fits its training data closely but performs worse on new data, because it has learned accidental quirks of the training examples as well as genuine patterns.
**parameter**: A number inside a model, such as a weight or bias, that is adjusted automatically during training; model size is often stated as a parameter count.
**pooling**: An operation that summarises neighbouring outputs of a convolutional layer, typically by keeping the largest value in each small block, which shrinks the map and reduces sensitivity to small shifts.
**regularisation**: Any technique that reduces overfitting, such as weight decay, dropout, data augmentation or early stopping.
**representation learning**: The learning of useful features directly from data, with successive layers re-describing the input (for images, edges, then motifs, parts and objects) instead of relying on features designed by hand.
**residual connection**: A shortcut that adds a block's input to its output, so that the block only has to learn a correction to its input; it lets error signals pass through very deep networks and made networks with hundreds of layers trainable.
**saturation**: The state of a sigmoid or tanh unit whose total is far from zero, where its slope is nearly flat and almost no learning signal passes through it.
**shortcut learning**: Learning a decision rule that works on the training and test data but relies on an incidental cue, such as the background or the hospital an X-ray came from, and therefore fails under new conditions.
**softmax**: A function that turns a list of raw scores into probabilities that are positive and add up to 1, by exponentiating each score and dividing by the total.
**stochastic gradient descent (SGD)**: Gradient descent in which each step uses a gradient estimated from a small random batch of examples instead of the whole training set.
**vanishing gradient problem**: The shrinking of error signals as they are passed backwards through many layers, which leaves the early layers of a deep network barely learning; the opposite effect is called exploding gradients.
**weight**: A number attached to a connection that says how strongly, and in which direction, one input influences a neuron; positive weights push the output up, negative weights push it down.
**weight decay**: A regularisation method that adds a penalty proportional to the sum of squared weights to the loss, so that each training step shrinks every weight slightly towards zero.
