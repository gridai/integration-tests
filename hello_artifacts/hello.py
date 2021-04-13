import os
import numpy as np
from argparse import ArgumentParser
import requests
import torch
from torch.utils.tensorboard import SummaryWriter

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
with open("weights.pt", "a") as f:
    f.write("fake weights")

# write folders of artifacts

for name in ['inputs', 'outputs']:
    for i in range(1, args.num_folders):
        root = f'{name}/folder_{i}'
        os.makedirs(root, exist_ok=True)

        img_1 = 'https://cdn.pixabay.com/photo/2014/02/27/16/10/tree-276014__340.jpg'
        img_2 = 'https://cdn.pixabay.com/photo/2020/10/03/17/30/bridge-5624104_1280.jpg'
        img_3 = 'https://i.imgur.com/ExdKOOz.png'
        
        for idx, img in enumerate([img_1, img_2, img_3]):
            response = requests.get(img)
            path = os.path.join(root, f'img_{idx}.jpg')
            file = open(path, 'wb')
            file.write(response.content)
            file.close()

# make random text file
for i in range(1, args.num_csv_files):
    f = open(f"demofile_{i}.csv", "a")
    f.write("col a, col b, col c\n1, 2, 3\n 3, 4, 5")
    f.close()