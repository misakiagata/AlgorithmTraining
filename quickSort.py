import listGenerator

#クイックソート
def quickSort(sortList):
    if len(sortList) < 2:
        return sortList
    else:
        if sortList[0] < sortList[1]:
            pivot = sortList[1]
            sortList.pop(1)
        else:
            pivot = sortList[0]
            sortList.pop(0)
        left = [i for i in sortList if i < pivot]
        right = [i for i in sortList if i >= pivot]
        return quickSort(left) + [pivot] + quickSort(right)


print(quickSort(listGenerator.generateList(5)))