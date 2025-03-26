def IterativeVowels(value):
    count = 0
    lengthString = len(value)
    for i in range(lengthString):
        firstCharacter = value[0]
        if firstCharacter == "a" or firstCharacter =="e" or firstCharacter =="i" or firstCharacter== "o" or firstCharacter == "u":
            count += 1
        value = value[1:len(value)]
    return count
def RecursiveVowels(value):
    if len(value) == 0:
        return 0
    else:
        firstCharacter = value[0]
        if firstCharacter == "a" or firstCharacter =="e" or firstCharacter =="i" or firstCharacter== "o" or firstCharacter == "u":
            value = value[1:len(value)]
            return (RecursiveVowels(value) + 1)
        else:
            value = value[1:len(value)]
            return RecursiveVowels(value)


print(IterativeVowels("pranav"))
print(RecursiveVowels("house"))
