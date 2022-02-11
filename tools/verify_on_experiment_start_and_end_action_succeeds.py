from pathlib import Path
from argparse import ArgumentParser


def main(nfiles_out):
    # this is created by the on-experiment-start action.
    start_file = Path("/file_created_by_on_experiment_start_action.txt")
    assert start_file.exists()
    
    for i in range(nfiles_out):
        with open(f"./file_{i}.out", "w+") as f:
            f.write(f"this is the contents of file number: {i} ... {'foo \n' for _ in range(i)}")
    
    # this will be created by the on-experiment-end action. It shouldn't exist at runtime of the script.
    end_file = Path("/file_to_be_deleted_by_on_experiment_end_action.txt")
    assert not end_file.exists()
    end_file.touch()


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--nfiles_out', default=0, type=int)
    args = parser.parse_args()
    main(args.nfiles_out)
