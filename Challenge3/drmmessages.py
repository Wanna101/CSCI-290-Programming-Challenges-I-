import string

# convert list to string
def listToString(s):
    str1 = ""
    for element in s:
        str1 += element
    return str1

# convert from the letter combination to a list of 
# numbers that correspond from 0-25 and 65-90 in ASCII
def convert(word):
    numbers = []
    sum = 0
    # ord function to turn letters into ASCII
    numbers = [ord(i.lower()) - 97 for i in word]
    for i in range(len(numbers)):
        sum += numbers[i]
    for j in range(len(numbers)):
        numbers[j] += sum
        if numbers[j] > 25:
            numbers[j] = numbers[j] % 26
    return numbers
    
# read input and split word into two
line = input()
middle = int(len(line) / 2)
wordOne = line[0:middle]
wordTwo = line[middle:]
numbersOne = convert(wordOne)
numbersTwo = convert(wordTwo)

# adding the values of word one and word two to get final word to
# convert back to letters
count = 0
for a in range(len(numbersOne)):
    numbersOne[a] += numbersTwo[count]
    count += 1
    if numbersOne[a] > 25:
        numbersOne[a] = numbersOne[a] % 26
    numbersOne[a] += 65
    numbersOne[a] = chr(numbersOne[a])
print(listToString(numbersOne))
