#!/usr/bin/env python

import sys, os

if __name__ == '__main__':
    print(f'sys.argv={sys.argv}')
    with open(sys.argv[2], "r") as f:
        for line in f.readlines():
            print(line.rstrip(), flush=True)
