#!/usr/bin/env python

import sys, os

if __name__ == '__main__':
    print(f'sys.argv={sys.argv}')
    try:
        print(f"trying opening in read+text mode")
        with open(sys.argv[2], "r") as f:
            print("was able to open file successfully")
    except UnicodeDecodeError as e:
        print(f"catching UnicodeDecodeError after opening in text mode: {e}")
        print(f"trying opening in read+binary mode")
        with open(sys.argv[2], "rb") as f:
            print("was able to open file successfully")
