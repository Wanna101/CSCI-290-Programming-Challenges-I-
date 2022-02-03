import string

def listToString(s):
    str1 = ""
    for element in s:
        str1 += element
    return str1

def convert(word):
    numbers = []
    sum = 0
    numbers = [ord(i.lower()) - 97 for i in word]
    for i in range(len(numbers)):
        sum += numbers[i]
    for j in range(len(numbers)):
        numbers[j] += sum
        if numbers[j] > 25:
            numbers[j] = numbers[j] % 26
    return numbers
    
line = input()
middle = int(len(line) / 2)
wordOne = line[0:middle]
wordTwo = line[middle:]
numbersOne = convert(wordOne)
numbersTwo = convert(wordTwo)

count = 0
for a in range(len(numbersOne)):
    numbersOne[a] += numbersTwo[count]
    count += 1
    if numbersOne[a] > 25:
        numbersOne[a] = numbersOne[a] % 26
    numbersOne[a] += 65
    numbersOne[a] = chr(numbersOne[a])
print(listToString(numbersOne))