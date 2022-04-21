# original author: @robert-s-lee
# commit 8aebb5a on Dec 14, 2021
# https://github.com/gridai-actions/test-log-txt-suffix-in-artifacts/blob/main/run2.py

# Tests that artifacts for fast running experiments are synced
# Tests that artifacts with various names / extensions are synced

from argparse import ArgumentParser
from time import sleep


def main(filename, extension, sleep_time=0, close_file=0, flush_file=0):
    outf = open(f"{filename}.{extension}", "w")
    outf.write(f"{filename}.{extension}\n")
    outf.write(f"Sleep: {sleep_time}\n")
    outf.write(f"{flush_file}: {flush_file}\n")
    outf.write(f"{close_file}: {close_file}\n")
    if sleep_time != 0:
        sleep(sleep_time)
    if flush_file != 0:
        outf.flush()
    if close_file != 0:
        outf.close()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--filename", type=str, default="results")
    parser.add_argument("--extension", type=str, default="txt")
    parser.add_argument("--sleep", type=int, default=0)
    parser.add_argument("--close_file", type=int, default=0)
    parser.add_argument("--flush_file", type=int, default=0)
    args = parser.parse_args()
    main(args.filename,
         args.extension,
         sleep_time=args.sleep,
         close_file=args.close_file,
         flush_file=args.flush_file)
