#!/usr/bin/env python

import sys, os

if __name__ == '__main__':
    os.stat(sys.argv[1])
    print("file exists")