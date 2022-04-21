# Tests that large artifacts are synced

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--out", type=str, default="artifact.txt")
parser.add_argument("--num-gb", type=int, default=1)
args = parser.parse_args()

gb = 2 ** 30
content = '1'*gb

with open(args.out, 'w') as f:
    for i in range(args.num_gb):
        print(f'writing {i+1}/{args.num_gb} gbs to "{args.out}"')
        f.write(content)

print('done')
