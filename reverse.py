#文字列を逆順にする
def reverse(word):
    newWord = []
    for i in range(len(word)):
        newWord.append(word[len(word)-1-i])
    return ''.join(newWord)

input = input('Input word: ')
print(reverse(input))
        