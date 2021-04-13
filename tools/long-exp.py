#!/usr/bin/python

import time

for i in range(2 * 3600):
    print(f"hello world {i}", flush=True)
    with open(f"artifacts-{i}.txt", "w") as f:
        print("Hello mother, hello father, I'm here!", file=f)
    time.sleep(1)



