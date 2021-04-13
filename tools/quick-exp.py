#!/usr/bin/env python

print("Hello world")

with open("artifacts.txt", "w") as f:
    print("Hello mother, hello father, I'm here!", file=f)
