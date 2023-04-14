import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
        """
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        #"*** YOUR CODE HERE ***"
        num_layers = 2
        init_hidden_num = 64
        self.hidden_layers = nn.ModuleList([nn.Linear(state_size, init_hidden_num)])
        for i in range(num_layers):
            self.hidden_layers.append(nn.Linear(init_hidden_num*(2**i), init_hidden_num*(2**(i+1))))
        self.final_layer = nn.Linear(init_hidden_num*(2**num_layers), action_size)

    def forward(self, state):
        """Build a network that maps state -> action values."""
        x = state
        for i in range(len(self.hidden_layers)):
            x = torch.relu(self.hidden_layers[i](x))
        x = self.final_layer(x)
        return x
