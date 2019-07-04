#空白文字を%20で埋める

def spaceFiller(word):
    str_list = list(word)
    for i in range(len(str_list)):
        if str_list[i] == ' ':
            str_list[i] = '%'
            str_list.insert(i+1, '2')
            str_list.insert(i+2, '0')
        else:
            pass
    return ''.join(str_list)

inputWord = input('Input word: ')
print(spaceFiller(inputWord))