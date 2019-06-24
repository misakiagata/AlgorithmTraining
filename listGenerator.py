import random


#指定された長さのリストを生成する
def generateList(length):
    generatedList = []
    for _ in range(length):
        generatedList.append(random.randint(1,30))
    return generatedList
