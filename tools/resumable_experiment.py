#!/usr/bin/env python
#
# This is resumable experiment which runs for 2h and saves it's state
# to a file

import signal
import sys
import os
import time

checkpoint_file = "chkpt.txt"

def signal_handler(sig, frame):
    print(f"Received signal {sig} saving checkpoint and terminating")
    with open(checkpoint_file, mode='w') as f:
        f.write(str(start))
    os._exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)


try:
    with open(checkpoint_file) as f:
        start = int(f.read())
    print(f"checkpoint found. Resuming from {start}")
except FileNotFoundError:
    start = 0

for i in range(start, 2 * 3600):
    start = i
    print(f"hello world {i}", flush=True)
    with open(f"artifacts-{i}.txt", "w") as f:
        print("Hello mother, hello father, I'm here!", file=f)
    time.sleep(1)
