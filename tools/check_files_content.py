#!/usr/bin/env python

# This script checks all the specified files have a specific content
# 1st args is the content to verify, remaining args are paths to files

import sys, os

if __name__ == '__main__':
    content = sys.argv[1]
    for path in sys.argv[2:]:
        with open(path, "r") as f:
            read_content = f.read().rstrip()
            if content != read_content:
                print(f"Found different content in file, expected: {content}, found: {read_content}")
                sys.exit(1)

    print("Files verified")
