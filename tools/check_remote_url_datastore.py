#!/usr/bin/env python

import sys
import subprocess
import os
import requests
import zipfile
import filecmp

if __name__ == '__main__':
    remote_url = sys.argv[1]
    datastore_dir = sys.argv[2]
    file_name = os.path.basename(remote_url)
    target_dir = "expected_ds"
    os.mkdir(target_dir)
    target_file = os.path.join(target_dir, file_name)

    r = requests.get(remote_url, allow_redirects=True)
    
    # Download the remote file
    with open(target_file, 'wb') as f:
        f.write(r.content)

    # Extract the file
    with zipfile.ZipFile(target_file, 'r') as zip_ref:
        zip_ref.extractall(target_dir)

    os.remove(target_file)
    
    # Check the datastore directory and downloaded datastore content
    # is the same
    dircmp = filecmp.dircmp(target_dir, datastore_dir)
    if len(dircmp.diff_files) > 0:
        print(f"Datastore is different than expected, diffs: {dircmp.diff_files}")
        sys.exit(1)
    
    print("Datastore verified")
    
