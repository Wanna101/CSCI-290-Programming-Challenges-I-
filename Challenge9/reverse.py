import sys

def reverse(elements, count):
    if count < len(elements):
        reverse(elements, count + 1)
        print(elements[count])
    return


sys.setrecursionlimit(1000000)
number = int(input())
integers = 0
count = 0
elements = []
for i in range(number):
    integers = int(input())
    elements.append(integers)
reverse(elements, count)
