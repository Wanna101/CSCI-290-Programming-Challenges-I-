
userInput = input()
userNumber = userInput
userInputTwo = input()
userNotes = userInputTwo
userList = userNotes.split()
notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
major = [2, 2, 1, 2, 2, 2, 1]
current = 0
existingScale = False

for i in range(len(notes)):
    current = i
    s = set()
    for elem in userList:
        s.add(elem)
    # print(s)
    for j in range(len(major)):
        current += int(major[j])
        transfer = current % len(notes)
        if notes[transfer] in s:
            s.remove(notes[transfer])
        # print(s)
        isEmpty = (len(s) == 0)
        if isEmpty:
            # print("Here")
            
            print(notes[i] + " ")
            existingScale = True
            break
if not existingScale:
    print("none")