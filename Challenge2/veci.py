import itertools

def convert(numList):
    s = map(str, numList)
    s = ''.join(s)
    s = int(s)
    return s

val = input()
lst = map(int, str(val))
perm = set(itertools.permutations(lst))

lowest = 999999999
found = False
for x in perm:
    num = convert(x)
    if num < lowest and num > int(val):
        lowest = num
        found = True

if found:    
    print (lowest)
else:
    print ("0")
