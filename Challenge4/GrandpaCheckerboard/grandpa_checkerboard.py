#!/usr/bin/python3
import sys
import math
import random

DEBUG = 0

"""
cat gpa_1.txt | python3 grandpa_checkerboard.py
4
WBBW
WBWB
BWWB
BWBW
cat gpa_1.txt | python3 grandpa_checkerboard.py
cat gpa_2.txt | python3 grandpa_checkerboard.py
cat gpa_3.txt | python3 grandpa_checkerboard.py
cat gpa_4.txt | python3 grandpa_checkerboard.py
"""


def columns_ok(board):
    for row in board:
        if (row.count('W') != row.count('B')):
            return False
        if (row.count("WWW") == 1 or row.count("BBB") == 1):
            return False
    return True


def rows_ok(board, size_board):
    for i in range(0, size_board):
        W_count = 0
        B_count = 0
        # can't have 3 consecutive chars
        last_char = ""
        consective = 0
        for j in range(0, size_board):
            if (board[j][i] == "W"):
                W_count += 1
                if last_char == "W":
                    consecutive += 1
                else:
                    consecutive = 0
            else:
                B_count += 1
                if last_char == "B":
                    consecutive += 1
                else:
                    consecutive = 0
            last_char = board[j][i]
            if consecutive >= 2:
                return False
        if W_count != B_count:
            return False
    return True

def handleInput(board, size_board):
    if DEBUG:
        print("size_board: " + str(size_board))
        print("board: " + str(board))
    if columns_ok(board): 
        if rows_ok(board, size_board):
            return "1"
    return "0"

if __name__ == '__main__':
    data = sys.stdin.readlines()
    size_board = int(data[0].rstrip())
    board = []
    for i in range(1, size_board+1):
        board.append(str(data[i].rstrip()))
    print(handleInput(board, size_board))
