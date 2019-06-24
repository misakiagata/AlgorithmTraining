#二分探索
def binarySearch(wordList,target):
    if len(wordList) == 0: #リストの長さが0だった場合
        return False
    else:
        wordList.sort() #二分探索できるようにリストをソート
        left = 0 #左側のフラグ
        right = len(wordList) - 1 #右側のフラグ(lenは要素の長さを返すので-1する)
        while left <= right: #左と右のフラグが一致するまで処理を繰り返す
            middle = int((left+right)/2)
            if wordList[middle] == target: #真ん中の値が探したい値だった場合
                return True
            elif target < wordList[middle]: # 探したい値が真ん中の値よりも小さかった場合
                right = middle - 1
            else: #探したい値が真ん中の値よりも大きかった場合
                left = middle + 1 
        return False #探索終了時に探したい値が見つからなかった場合



#二分探索(再帰)
def recursiveBinarySearch(wordList,target):
    if len(wordList) == 0:
        return False
    elif wordList[int(len(wordList)/2)] == target: #真ん中の値が探したい値と一致した場合
        return True
    elif wordList[int(len(wordList)/2)] > target: #探したい値が真ん中の値よりも小さかった場合
        return binarySearch(wordList[:int(len(wordList)/2+1)],target) #リストをスライスする際、[:3]とすると要素番号0~2までが返るので+1する
    else:
        return binarySearch(wordList[int(len(wordList)/2):],target) #リストをスライスする際、[3:]とすると要素番号3~最後までが返る


print(binarySearch([1,2,3,5,7,4],5))
print(recursiveBinarySearch([1,2,3,5,7,4],1))