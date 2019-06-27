import listGenerator

#バブルソート
def bubbleSort(sortList):
    for i in range(len(sortList)):#iは左から(リストの最初から)
        for j in range(len(sortList)-1, i, -1):#jはリストの右からiまで-1ずつ減少(一番左の数字はループが1回回るとソート済み扱いされるので、jはiまで減少させる)
            if sortList[j] < sortList[j-1]:
                sortList[j], sortList[j-1] = sortList[j-1], sortList[j]
    return sortList

print(bubbleSort(listGenerator.generateList(5)))
