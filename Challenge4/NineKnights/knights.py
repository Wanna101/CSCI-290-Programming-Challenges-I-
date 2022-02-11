#!/usr/bin/python3
import sys
import math
import random

DEBUG = 0

"""
cat knight_1.txt | python3 knights.py
...k.
...k.
k.k..
.k.k.
k.k.k

cat knight_2.txt | python3 knights.py
cat knight_3.txt | python3 knights.py
"""

def check_valid_nine_knights(board):
    knights = []
    for row in range(0, 5):
        for column in range(0, 5):
            if board[row][column] == 'k':
                knights.append([row,column])
    if len(knights) != 9:
        return False
    for k1 in knights:
        for k2 in knights:
            row = k1[0]
            col = k1[1]
            #print(row,col)
            # move row up two
            if row - 2 > 0:
                new_row = row - 2
                # move column left one
                if col - 1 > 0:
                    new_col = col - 1
                    if board[new_row][new_col] == 'k':
                        return False
                # move column right one
                if col + 1 < 5:
                    new_col = col + 1
                    if board[new_row][new_col] == 'k':
                        return False
            # move row down
            if row + 2 < 5:
                new_row = row + 2
                # move column left one
                if col - 1 > 0:
                    new_col = col - 1
                    if board[new_row][new_col] == 'k':
                        return False
                # move column right one
                if col + 1 < 5:
                    new_col = col + 1
                    if board[new_row][new_col] == 'k':
                        return False
            # move column left two
            if col - 2 > 0:
                new_col = col - 2
                # move row up one
                if row - 1 > 0:
                    new_row = row - 1
                    if board[new_row][new_col] == 'k':
                        return False
                # move row down one
                if row + 1 < 5:
                    new_row = row + 1
                    if board[new_row][new_col] == 'k':
                        return False
            # move column right two
            if col + 2 < 5:
                new_col = col + 2
                # move row up one
                if row - 1 > 0:
                    new_row = row - 1
                    if board[new_row][new_col] == 'k':
                        return False
                # move row down one
                if row + 1 < 5:
                    new_row = row + 1
                    if board[new_row][new_col] == 'k':
                        return False
            #print(k1[0], k1[1])
    return True

def handleInput(board):
    if (check_valid_nine_knights(board)):
        return "valid"
    else:
        return "invalid"

if __name__ == '__main__':
    data = sys.stdin.readlines()
    board = []
    for line in data:
        board.append(line.rstrip())
    print(handleInput(board))
