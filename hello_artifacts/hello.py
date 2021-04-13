from argparse import ArgumentParser
from torch.utils.tensorboard import SummaryWriter
from tqdm import tqdm
import numpy as np
import os
import requests
import time
import torch

# add arguments 
parser = ArgumentParser()
parser.add_argument('--number', default=0, type=int)
parser.add_argument('--num_folders', default=50, type=int)
parser.add_argument('--num_csv_files', default=50, type=int)
parser.add_argument('--food_item', default='burgers', type=str)
parser.add_argument('--data', default=None, type=str)
args = parser.parse_args()

# fake tensorboard logs (fake loss)
writer = SummaryWriter()
offset = np.random.uniform(0, 5, 1)[0]
for x in range(1, 10000):
    y = -np.log(x) + offset + (np.sin(x) * 0.1)
    writer.add_scalar('y=-log(x) + c + 0.1sin(x)', y, x)
    writer.add_scalar('fake_metric', -y, x)

writer.close()

# print data if available
if args.data is not None:
    files = list(os.walk(args.data))
    print('-' * 50)
    print(f'DATA FOUND! {len(files)} files found at dataset {args.data}')

# print GPUs, params and random tensors
print('-' * 50)
print(f'GPUS: There are {torch.cuda.device_count()} GPUs on this machine')
print('-' * 50)
print(f'PARAMS: I want to eat: {args.number} {args.food_item}')
print('-' * 50)
print('i can run any ML library like numpy, pytorch lightning, sklearn pytorch, keras, tensorflow')
print('torch:', torch.rand(1), 'numpy', np.random.rand(1))

# write some artifacts
with open("weights.pt", "w") as f:
    f.write("fake weights")

# write folders of artifacts

images = [
    'https://cdn.pixabay.com/photo/2014/02/27/16/10/tree-276014__340.jpg',
    'https://cdn.pixabay.com/photo/2020/10/03/17/30/bridge-5624104_1280.jpg',
    'https://i.imgur.com/ExdKOOz.png',
]

images_data = [
    requests.get(x).content for x in images
]


for name in ['inputs', 'outputs']:
    for i in tqdm(range(1, args.num_folders), desc="making inputs/outputs folder"):
        root = f'{name}/folder_{i}'
        os.makedirs(root, exist_ok=True)

        
        for idx, image in enumerate(images_data):
            path = os.path.join(root, f'img_{idx}.jpg')
            with open (path, 'wb') as file:
                file.write(image)
        time.sleep(1)

# make random text file
for i in tqdm(range(1, args.num_csv_files), desc="create csv files"):
    with open(f"demofile_{i}.csv", "w") as f:
        f.write("col a, col b, col c\n1, 2, 3\n 3, 4, 5")
    time.sleep(1)