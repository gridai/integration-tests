#!/usr/bin/env python

import sys, os

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))


if __name__ == '__main__':
    print(f'sys.argv={sys.argv}')
    list_files('/datastores/')
    try:
        print(f"trying opening in read+text mode")
        with open(sys.argv[2], "r") as f:
            print("was able to open file successfully")
            print(f.read())
    except UnicodeDecodeError as e:
        print(f"catching UnicodeDecodeError after opening in text mode: {e}")
        print(f"trying opening in read+binary mode")
        with open(sys.argv[2], "rb") as f:
            print("was able to open file successfully")
            print(f.read())
