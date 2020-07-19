import os

from torchvision import transforms
from torch.utils.data import DataLoader
from torchvision.datasets import MNIST


class MNISTData:
    """
    Wrapper for MNIST's DataLoader as to generate
    callables for Grid.
    """
    @property
    def train(self):
        return DataLoader(
            MNIST(os.getcwd(), train=True, download=True, transform=transforms.ToTensor()),
            batch_size=32, num_workers=16)

    # @property
    # def test(self):
    #     return DataLoader(
    #         MNIST(os.getcwd(), train=True, download=True, transform=transforms.ToTensor()),
    #         batch_size=32)

    # @property
    # def validation(self):
    #     return DataLoader(
    #         MNIST(os.getcwd(), train=False, download=True, transform=transforms.ToTensor()),
    #         batch_size=32)
