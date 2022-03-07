#!/usr/bin/python3
import sys
import math
import random

DEBUG = 0

"""
cat patulijci1.txt | python3 patulijci1.py
cat patulijci2.txt | python3 patulijci1.py
"""

"""
Complexity: O(n) for the function, so O(n^4) for the total
time complexity

"""

numbers = sys.stdin.readlines()

def add_seven_numbers(numbers, index1, index2):
    # exclude index1 and index2 index
    total = 0
    for i in range(0,9):
        if i == index1 or i == index2:
            continue
        total += int(numbers[i])
    return total

for i in range(0,9):
    for j in range(0,9):
        if int(i) == int(j):
            continue
        num = add_seven_numbers(numbers, i, j)
        if num == 100:
            for index, n in enumerate(numbers):
                if index != int(i) and index != int(j):
                    print(str(n).rstrip())
            quit()

