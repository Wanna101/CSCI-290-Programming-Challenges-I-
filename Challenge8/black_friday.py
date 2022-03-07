#!/usr/bin/python3
import sys
import math
import random

DEBUG = 0

"""
cat black_friday.txt | python3 black_friday.py
8
1 1 1 5 3 4 6 6

cat bf1.txt | python3 knights.py
cat bf2.txt | python3 knights.py
"""

"""
Complexity: O(n) because of the for loop

"""

data = sys.stdin.readlines()
num_contests = data[0]
roll = data[1].rstrip()
roll = roll.split(" ")
p_hash = {}
for r in roll:
    if r not in p_hash:
        p_hash[r] = 1
    else:
        p_hash[r] += 1

highest = -1
for key, value in p_hash.items():
    if value == 1:
        if int(key) > highest:
            highest = int(key)
if highest == -1:
    print("none")
else:
    for index, item in enumerate(roll):
        if int(item) == int(highest):
            print(index+1)

