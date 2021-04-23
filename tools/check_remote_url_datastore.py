#!/usr/bin/env python

import sys, os
import subprocess

if __name__ == '__main__':
    remote_url = sys.argv[1]
    datastore_dir = sys.argv[2]
    file_name = os.path.basename(remote_url)
    target_dir = "expected_ds"
    os.mkdir(target_dir)
    target_file = os.path.join(target_dir, file_name)
    # Download the remote file
    subprocess.check_call(["curl", "-L", "-s", remote_url,
                           "--output", target_file],
                          stdout=sys.stdout,
                          stderr=sys.stderr)
    # Extract the file
    subprocess.check_call(["unzip", target_file, "-d", target_dir],
                          stdout=sys.stdout,
                          stderr=sys.stderr)

    os.remove(target_file)
    
    # Check the datastore directory and downloaded datastore content
    # is the same
    subprocess.check_call(["diff", "-r", target_dir, datastore_dir],
                          stdout=sys.stdout,
                          stderr=sys.stderr)

    print("Datastore verified")
    
