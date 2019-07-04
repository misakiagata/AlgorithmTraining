#文字列圧縮
#aaabbccc->a3b2c3

def compression(word):
    word += '%' #ダミーの%を入力された文字列の最後に入れる
    compList = []
    counter = 0
    index = 0
    while index < len(word)-1:
        if word[index] == word[index+1]:
            counter += 1
        else:
            counter += 1
            compList.append(word[index])
            compList.append(str(counter))
            counter = 0
        index += 1
    return ''.join(compList)

def main(originWord):
    processedWord = compression(originWord)
    if len(processedWord) < len(originWord):
        return processedWord
    else:
        return originWord

input = input('Input word: ')
print(main(input))