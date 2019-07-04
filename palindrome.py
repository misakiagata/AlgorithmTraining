#回文判定

def divideWord(word):
    if len(word)%2 == 0:
        first = word[:len(word)//2]
        last = word[len(word)//2:]
    else:
        first = word[:len(word)//2]
        last = word[len(word)//2+1:]
    return checkWord(first,last)

def checkWord(first,last):
    print(first,last)
    return first == last[::-1]

inputWord = input('Input word')
print(divideWord(inputWord))
