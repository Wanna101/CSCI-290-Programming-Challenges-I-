
# recursive function to generate list of possible numbers from 0 to 200
def getNextDigit(keypad, user_number, elements):
    # we stop creating the list when number exceeds 200
    if user_number > 200:
        return
    if keypad == 1:
        # if at 1 and you choose not to take 1...
        # recurse, and choose to be at 2 or 4
        # these are the two numbers if you don't pick 1
        getNextDigit(2, user_number, elements)
        getNextDigit(4, user_number, elements)
        # need to shift number to the left and add digit to it
        user_number = user_number * 10 + keypad
        if user_number <= 200:
            elements.append(user_number)
        getNextDigit(1, user_number, elements)
        getNextDigit(2, user_number, elements)
        getNextDigit(4, user_number, elements)
    if keypad == 2:
        getNextDigit(3, user_number, elements)
        getNextDigit(5, user_number, elements)
        user_number = user_number * 10 + keypad
        if user_number <= 200:
            elements.append(user_number)
        getNextDigit(2, user_number, elements)
        getNextDigit(3, user_number, elements)
        getNextDigit(5, user_number, elements)
    if keypad == 3:
        getNextDigit(6, user_number, elements)
        user_number = user_number * 10 + keypad
        if user_number <= 200:
            elements.append(user_number)
        getNextDigit(3, user_number, elements)
        getNextDigit(6, user_number, elements)
    if keypad == 4:
        getNextDigit(5, user_number, elements)
        getNextDigit(7, user_number, elements)
        user_number = user_number * 10 + keypad
        if user_number <= 200:
            elements.append(user_number)
        getNextDigit(4, user_number, elements)
        getNextDigit(5, user_number, elements)
        getNextDigit(7, user_number, elements)
    if keypad == 5:
        getNextDigit(6, user_number, elements)
        getNextDigit(8, user_number, elements)
        user_number = user_number * 10 + keypad
        if user_number <= 200:
            elements.append(user_number)
        getNextDigit(5, user_number, elements)
        getNextDigit(6, user_number, elements)
        getNextDigit(8, user_number, elements)
    if keypad == 6:
        getNextDigit(9, user_number, elements)
        user_number = user_number * 10 + keypad
        if user_number <= 200:
            elements.append(user_number)
        getNextDigit(6, user_number, elements)
        getNextDigit(9, user_number, elements)
    if keypad == 7:
        getNextDigit(8, user_number, elements)
        user_number = user_number * 10 + keypad
        if user_number <= 200:
            elements.append(user_number)
        getNextDigit(7, user_number, elements)
        getNextDigit(8, user_number, elements)
    if keypad == 8:
        getNextDigit(0, user_number, elements)
        getNextDigit(9, user_number, elements)
        user_number = user_number * 10 + keypad
        if user_number <= 200:
            elements.append(user_number)
        getNextDigit(8, user_number, elements)
        getNextDigit(0, user_number, elements)
        getNextDigit(9, user_number, elements)
    if keypad == 9:
        user_number = user_number * 10 + keypad
        if user_number <= 200:
            elements.append(user_number)
        getNextDigit(9, user_number, elements)
    if keypad == 0:
        user_number = user_number * 10 + keypad
        if user_number <= 200:
            elements.append(user_number)
        if user_number != 0:
            getNextDigit(0, user_number, elements)


# initialize variables
integers = 0
elements = []

# generate list of numbers and sort them and make it unique
getNextDigit(1, 0, elements)
elements.sort()
elements = list(set(elements))

# process the values
number = int(input())
for i in range(number):
    integers = int(input())
    if integers in elements:
        print(integers)
    else:
        for j in range(len(elements)):
            if (elements[j] < integers and integers < elements[j + 1]):
                if integers - elements[j] < elements[j + 1] - integers:
                    print(elements[j])
                else:
                    print(elements[j + 1])
    

