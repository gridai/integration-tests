import torch
import pytorch_lightning as pl

from torch.nn import functional as F


class MNISTModel(pl.LightningModule):

    def __init__(self, num_hidden_layers = 1, learning_rate = 0.09):
        super().__init__()
        self.learning_rate = learning_rate

        # create the hidden layers
        hidden_layers = []
        for layer_i in range(num_hidden_layers):
          hidden_layer = torch.nn.Linear(128, 128)
          hidden_layers.append(hidden_layer)

        self.hidden_layers = torch.nn.ModuleList(hidden_layers)

        # input and output layers
        self.input_layer = torch.nn.Linear(28 * 28, 128)
        self.output_layer = torch.nn.Linear(128, 10)

    def forward(self, x):
        x =  torch.relu(self.input_layer(x.view(x.size(0), -1)))

        # apply hidden layers
        for hidden_layer in self.hidden_layers:
          x = torch.relu(hidden_layer(x))

        x = self.output_layer(x)

        return x

    def training_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self.forward(x)
        loss = F.cross_entropy(y_hat, y)
        logs = {'loss': loss}
        return {'loss': loss, 'log': logs}

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=self.learning_rate)
