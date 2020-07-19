"""
Script that defines a simple interface for being invoked
using a command line command. This script should be run
in Grid using

    $ grid train --gpus 1 --instance_type p3dn.24xlarge -- \
        multi_gpu.py --learning_rage "uniform(0, 1, 2)" --num_hidden_layers "[1, 2, 3]" --gpus 1

This will start a grid search with six experiments
each using 1 GPUs in very large instances: p3dn.24xlarge
"""
import argparse

from data import MNISTData
from model import MNISTModel
from pytorch_lightning import Trainer

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--max_epochs', default=1_000, type=int)
    parser.add_argument('--num_hidden_layers', default=1, type=int)
    parser.add_argument('--learning_rate', default=0.001, type=float)
    parser.add_argument('--gpus', default=-1, type=int)
    parser.add_argument('--distributed_backend', default='ddp', type=str)
    parser.add_argument('--num_nodes', default=1, type=int)
    parser.add_argument('--test_boolean', default=False, type=bool)
    args = parser.parse_args()

    model = MNISTModel(num_hidden_layers=args.num_hidden_layers,
                       learning_rate=args.learning_rate)

    #  Here we are configuring the Trainer to run on multiple GPUs
    #  in the same node.
    trainer = Trainer(gpus=args.gpus,
                      distributed_backend=args.distributed_backend,
                      num_nodes=args.num_nodes,
                      max_epochs=args.max_epochs)

    trainer.fit(model, train_dataloader=MNISTData().train)
