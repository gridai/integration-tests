"""
Script that defines a simple interface for being invoked
using a command line command. This script should be run
in Grid using

    $ grid train multi_gpu.py --learning_rage "uniform(0, 1, 2)" --num_hidden_layers "[1, 2, 3]" --gpus 4 --instance_type p3dn.24xlarge

This will start a grid search with six experiments
each using 4 GPUs in very large instances: p3dn.24xlarge
"""
import torch
import argparse
import os

from typing import Optional

from torchvision import transforms
from torch.utils.data import DataLoader
from torchvision.datasets import MNIST

from pytorch_lightning import Trainer, LightningModule


class MNISTModel(LightningModule):
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


class MNISTData:
    def __init__(self, datastore_mount_path: Optional[str] = None):
        self.datastore_mount_path = datastore_mount_path
    
    """
    Wrapper for MNIST's DataLoader as to generate
    callables for Grid.
    """
    @property
    def train(self):
        if self.datastore_mount_path:
            return DataLoader(
                MNIST(self.datastore_mount_path, train=True, download=False, transform=transforms.ToTensor()),
                batch_size=32, num_workers=16)            
        else:
            return DataLoader(
                MNIST(os.getcwd(), train=True, download=False, transform=transforms.ToTensor()),
                batch_size=32, num_workers=16)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--max_epochs', default=1_000, type=int)
    parser.add_argument('--num_hidden_layers', default=1, type=int)
    parser.add_argument('--learning_rate', default=0.001, type=float)
    parser.add_argument('--test_boolean', default=False, type=bool)
    parser.add_argument('--data_dir', default=None, type=str)
    args = parser.parse_args()

    model = MNISTModel(num_hidden_layers=args.num_hidden_layers,
                       learning_rate=args.learning_rate)

    #  Here we are configuring the Trainer to run on multiple GPUs
    #  in the same node.
    trainer = Trainer(max_epochs=args.max_epochs)
    trainer.fit(model, train_dataloader=MNISTData(args.data_dir).train)
