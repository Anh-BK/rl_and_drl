### 1. Setting Neural network architecture
- The number of nodes on each layer equals to power of 2 of previous node number.
- To choose number of hidden layers, I conducted experiments with several architects with different number of hidden layers, from 1, 2, 3,...
- After serveral experiments, the architect with 2 hidden layers is chosen. This architech is not too simple like 1-hidden layer architect but not too complex like 3-hidden layer architect to approximate $\hat{q}_{\pi}$. The figure below show a baseline score with 2-hidden layer architect:

<p align="center">
    <img src="images/2hidden_layers.png" width="50%" height="50%" alt>
</p>
<p align="center">
    <em>Fig 1: Baseline</em>
</p>

### 2. Improving learning algorithm
- Experience Relay method: This method allow to learn from experiences and in learning proccess, randomly sampling experience tuples to learn allow to ignore the correlation among experiences

<p align="center">
<img src="images/2hidden_layers.png" width="50%" height="50%" >
</p>
<p align="center">
    <em>Fig 2: Experience relay method</em>
</p>

- Clipping error method: The learning progress becomes more stable than with original algorithm.

<p align="center">
    <img src="images/clipping_error.png" width="50%" height="50%" >
</p>
<p align="center">
    <em>Fig 3: Clipping error</em>
</p>

- Double Q-learning method: In the long run, this method prevent the algorithm from get high reward by chance but don't reflect the long term.

<p align="center">
    <img src="images/double_q-learning.png" width="50%" height="50%" >
</p>
<p align="center">
    <em>Fig 4: Double Q-learning</em>
</p>

#### *Hyperparameter table*:

| Hyperparameter | Value         | Description   | 
| -------------  | ------------- | ------------- |
| minibatch size | 64 | Number of training cases|
| buffer size | 100000| Number of recent experiences |
| discount factor | 0.99 | discount factor gamma|
| tau | 1e-3  | Interpolation parameter for soft update of target parameters |
| learning rate | 5e-4 | learning rate form updating local model with Adam agorithm|

### 3. Further work
- Trying with different activation function in the neural architect.
- Trying other learning methods: Dueling DQN, Raninbow and Priorized experience relay