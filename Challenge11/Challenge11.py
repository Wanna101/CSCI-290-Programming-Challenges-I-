'''

Tabled list of questions:
- what is the purpose of the first line of input for the program?
- when manipulating the Record ID's, does the carry over of adding
one go into the Object prefix?
- does i expand? or does it stay to 2 positions

'''

import sys
import math
import random
import re

def split(string):
    return list(string)

def checkNumber(string):
    if not string.isdigit():
        return False
    return True

def convertListToString(listID):
    string = ""
    for element in listID:
        string += element
    return string

def assign(count, startingID):
    # tests to see if count is a number
    try:
        val = int(count)
    except ValueError:
        print("That's not a valid count number!")
        exit()
    count = int(count)

    # tests to see if starting ID is 6 characters
    if len(startingID) != 6:
        print("The starting ID should be 6 characters long...")
        exit()

    # test to see if starting ID is in base 16 formatting
    pattern = re.compile("[0-9A-F]+")    
    if not pattern.fullmatch(startingID):
        print("The starting ID needs to be [0-9A-F] formatting...")
        exit()
        
    parsed = split(startingID)
    r = []
    k = []
    i = []
    d = []

    r.append(parsed[0])
    r.append(parsed[1])
    k.append(parsed[2])
    i.append(parsed[3])
    i.append(parsed[4])
    d.append(parsed[5])

    for x in range(count):
        # when i[1] is numbers
        if checkNumber(i[1]) == True:
            change = int(i[1]) + 1
            i[1] = format(change, 'X')
            ID = r + k + i + d
            print(convertListToString(ID))
            
        # when i[1] is letters
        else:
            change = int(i[1], 16) + 1
            boundary = int(i[0], 16) + 1
            if change == 16:
                if boundary < 11:
                    i[1] = '0'
                    i[0] = format(int(i[0]) + 1, 'X')
                else:
                    i[1] = '0'
                    dec = int(i[0], 16) + 1
                    i[0] = format(dec, 'X')
            else:
                i[1] = format(change, 'X')
            ID = r + k + i + d
            stringI = convertListToString(i)
            if stringI == "100":
                break
            print(convertListToString(ID))


def defrag(dValue, programCounter):
    # loop for input for the amount specified in programCounter
    arr = [input() for i in range(int(programCounter))]
    
    groupCounter = {}
    # split the dValue (it will only be two characters)
    parsed = split(dValue)

    # put the split strings into variable names
    one = parsed[0]
    two = parsed[1]

    # replace first and last values of each string in input with
    # the split strings
    for i in range(int(programCounter)):
        temp = list(arr[i])
        temp[0] = one
        temp[len(arr[i]) - 1] = two
        
        # clear second value if you need to 
        temp[1] = '0'
        
        # used in the groupCounter dictionary
        group = temp[2]

        if group not in groupCounter:
            groupCounter[group] = 0;
        else:
            groupCounter[group] += 1;

        id = format(groupCounter[group], 'X').zfill(2)

        if len(id) == 3:
            temp[1] = id[0]
            temp[3] = id[1]
            temp[4] = id[2]
        elif len(id) > 3:
            break
        else:
            temp[3] = id[0]
            temp[4] = id[1]
        
        arr[i] = "".join(temp)
        print(arr[i])

        

def main():
    keyword = input()

    if keyword == "assign":
        count = input()
        startingID = input()
        assign(count, startingID)
    elif keyword == "defrag-move":
        dValue = input()
        programCounter = input()
        defrag(dValue, programCounter)
    else:
        print("Not a valid keyword")

main()
