#!/usr/bin/python3

import sys
import math

DEBUG = 0


data = sys.stdin.readlines()

matrix = []
positions = {}

for line in data:
    arr_line = line.split()
    matrix.append(arr_line)

for x in range(0,3):
    for y in range(0,3):
        positions[matrix[x][y]] = (x,y)

total = 0
for key in sorted(positions):
    x,y = positions[key]
    if int(key) <= 8:
        next_key = int(key) + 1
        if DEBUG:
            print("next_key: " + str(next_key))
        next_x,next_y = positions[str(next_key)]
        if DEBUG:
            print(key + ": " + str(x) + "," + str(y))
            print(str(next_key) + ": " + str(next_x) + "," + str(next_y))
        diff_x = abs(x - next_x) 
        diff_y = abs(y - next_y) 
        # diagnoal 2 spaces
        if diff_x == 2 and diff_y == 2:
            diff_x = math.sqrt(8)
            diff_y = 0
        # diagonal 1 space
        elif diff_x == 1 and diff_y == 1:
            diff_x = math.sqrt(2)
            diff_y = 0
        # one line long diagnoal
        elif (diff_x == 1 and diff_y == 2) or (diff_x == 2 and diff_y == 1):
            diff_x = math.sqrt(5)
            diff_y = 0
        if DEBUG:
            print("diff_x: " + str(diff_x))
            print("diff_y: " + str(diff_y))
            print("subtotal: " + str(diff_x + diff_y)) 
            print("") 
        total += diff_x + diff_y
print(total)
