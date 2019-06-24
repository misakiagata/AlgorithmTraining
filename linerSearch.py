#線形探索
def linerSearch(wordlist,word):
    # print(len(wordlist))#配列の要素の個数をとる, 出力3
    # print(range(len(wordlist)))#連続した数のリストを返す, 出力[0,3]
    # print(wordlist)#リストを返す, 出力['a','b','c']
    for i in wordlist:
        if i == word:
            return True
        else:
            return False

print(linerSearch(['a','b','c'],'b'))
