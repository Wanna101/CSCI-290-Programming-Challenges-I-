#!/usr/bin/python3
import sys
import math
import random

DEBUG = 0
highest = [ "12", "21" ]
doubles = [ "11", "22", "33", "44", "55", "66" ]

"""
cat targets_sample.txt | python3 targets.py
3
rectangle 1 1 10 5
circle 5 0 8
rectangle -5 3 5 8
5
1 1
4 5
10 10
-10 -1
4 -3

"""

def is_inside_circle(circle_x, circle_y, radius, x, y):
    circle_x = int(circle_x)
    circle_y = int(circle_y)
    radius = int(radius)
    x = int(x)
    y = int(y)
    # is the radius of circle with distance of the center from given point
    if ((x - circle_x) * (x - circle_x) + (y - circle_y) * (y - circle_y) <= radius * radius):
        return True;
    else:
        return False;

def is_inside_rectangle(x1, y1, x2, y2, x, y):
    if DEBUG: 
        print("\t\t\t\t(x1, y1, x2, y2, x, y)")
        print("\t\t\t\t", x1, y1, x2, y2, x, y)
        print("\t\t\t\t", "(x >= x1 and x <= x2 and y >= y1 and y <= y2)")
        print("\t\t\t\t", "(x >= x1 and x <= x2 and y >= y1 and y <= y2)")
    x = int(x)
    y = int(y)
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    if (x >= x1 and x <= x2 and y >= y1 and y <= y2):
        return True
    else :
        return False

def handleInput(text):
    num_targets = int(text[0].rstrip())
    targets = []
    shots = []
    for i in range(1, num_targets+1):
        targets.append(str(text[i].rstrip()))

    if DEBUG:
        print("num_targets: " + str(num_targets))
        print("num_shots: " + text[num_targets+1])
        #print("text: " + text)
    num_shots = int(text[num_targets+1].rstrip())
    for i in range(num_targets + 2, num_shots + num_targets + 2):
        shots.append(str(text[i].rstrip()))

    is_rectangle = False
    x1 = 0
    x2 = 0 
    y1 = 0
    y2 = 0
    circle_x = 0
    circle_y = 0
    radius = 0
    results = ""
    for s in shots:
        hit_count = 0
        if DEBUG:
            print("SHOT: " + s)
        x, y = s.split(" ")
        for t in targets:
            if "rectangle" in t:
                is_rectangle = True
                dummy, x1, y1, x2, y2 = t.split(" ")
                if DEBUG:
                    print("\trect: ", x1, y1, x2, y2)
                if (is_inside_rectangle(x1, y1, x2, y2, x, y)):
                        if DEBUG:
                            print("\t\tHIT")
                        hit_count += 1
                else:
                        if DEBUG:
                            print("\t\tMISS")
            else:
                is_rectangle = False
                dummy, circle_x, circle_y, radius = t.split(" ")
                if DEBUG:
                    print("\tcircle: ", circle_x, circle_y, radius)
                if (is_inside_circle(circle_x, circle_y, radius, x, y)):
                        if DEBUG:
                            print("\t\tHIT")
                        hit_count += 1
                else:
                        if DEBUG:
                            print("\t\tMISS")
        results += str(hit_count) + "\n"
    return results

if __name__ == '__main__':
    data = sys.stdin.readlines()
    res = handleInput(data)
    print(res, end="")
