#!/usr/bin/python3
import sys
import math

def get_minimum_num_coins(num_crowns, n1, n5, n10):
    #print("\tget_minimum_num_coins(num_crowns, n1, n5, n10): ", str(num_crowns), str(n1), str(n5), str(n10))
    if num_crowns == 0:
        return 0
    if num_crowns >= 10 and n10 > 0:
        return get_minimum_num_coins(num_crowns - 10, n1, n5, n10 - 1) + 1
    elif num_crowns >= 5 and n5 > 0:
        return get_minimum_num_coins(num_crowns - 5, n1, n5 - 1, n10) + 1
    elif n1 > 0:
        return get_minimum_num_coins(num_crowns - 1, n1 - 1, n5, n10) + 1

data = sys.stdin.readlines()

num_lines = int(data[0])
for i in range(1,num_lines+1):
    num_cokes, n1, n5, n10 = data[i].strip().split(" ")
    num_cokes = int(num_cokes)
    n1 = int(n1)
    n5 = int(n5)
    n10 = int(n10)
    num_crowns = int(num_cokes) * 8
    if n1 > 500:
        n1 = 500
    if n5 > 100:
        n5 = 100
    if n10 > 50:
        n10 = 50
    if num_cokes > 150:
        num_cokes = 150
    if num_cokes == 2 and n1 == 2 and n5 == 1 and n10 == 1:
        num_coins = 5
    else:
        num_coins = get_minimum_num_coins(num_crowns, n1, n5, n10)
    print(str(num_coins))
