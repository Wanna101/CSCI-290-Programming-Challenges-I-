#!/usr/bin/python3

import sys
import math

DEBUG = 0

data = sys.stdin.readlines()

num_rooms = int(data[0])
num_teams = int(data[1])

div = int(num_teams / num_rooms)
if int(num_teams % num_rooms > 0):
    div += 1
if DEBUG:
    print("div: " + str(div))
div_once = False
while num_teams > 0:
    if DEBUG:
        print("1) num_teams: " + str(num_teams))
    if num_teams >= div:
        print("*" * div)
        num_teams -= div
    else:
        print("*" * num_teams)
        num_teams -= div
    if DEBUG:
        print("2) num_teams left: " + str(num_teams))
        print("3) div: " + str(div))
    """
    if num_teams < div * 2 and (div * 2) - num_teams > 1 and not div_once:
        if DEBUG:
            print("DIV - 1!!!")
        div -= 1
        div_once = True
    """
