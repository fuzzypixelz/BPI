#!/usr/bin/env python

with open("toto.txt", "w") as f:
    # write has no newline
    f.write("I am first!\n")
    print("Stop bragging!", file=f)