# TODO: move to grid/integration-test repo
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--num-exp", type=int, help="only purpose is to scale the hyperparameter sweep")
parser.add_argument("--num-gb", type=int)
parser.add_argument("--num-artifacts", type=int)
parser.add_argument("--num-iterations", type=int, default=1, help="number of times to override each artifact. min: 1 max: 10")
args = parser.parse_args()

gb_bytes = 2**30
start = 0

# overwrite each artifact multiple times
for i in range(args.num_iterations):
    print(f"writing batch {i} of {args.num_iterations}")

    for artifact_num in range(start, args.num_artifacts):
        name = f"artifact-{artifact_num}.txt"
        with open(name, 'w') as f:
            for gb in range(args.num_gb):
                print(f"writing {gb}/{args.num_gb} for {name}")
                f.write(str(i%10)*gb_bytes)
        print(f"done with {name}")

print("done")
