# Warsztat4 - Zadanie 9.
# -*- encoding: utf-8 -*-
import collections
import random
from random import randint

L=[]
for i in range(10000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    L.append(dice1+dice2)


def getDuplicatesWithInfo(listOfElems):

    dictOfElems = dict()
    index = 0

    for elem in listOfElems:

        if elem in dictOfElems:
            dictOfElems[elem][0] += 1
            dictOfElems[elem][1].append(index)
        else:

            dictOfElems[elem] = [1, [index]]
        index += 1

    dictOfElems = {key: value for key, value in dictOfElems.items() if value[0] > 1}
    return dictOfElems

countList=[]
dictOfElems = getDuplicatesWithInfo(L)
for key, value in sorted(dictOfElems.items()):
    print('Element = ', key, ' :: Repeated Count = ', value[0], ' :: Index Positions =  ', value[1])
    countList.append(value[0])

precentageList=[]
for i in range(len(countList)):
    precentage=round((countList[i]/10000)*100,2)
    precentageList.append(precentage)

for i in range(len(precentageList)):
        print("Prawdopodobieństwo wystapienia sumy: ",list(sorted(dictOfElems.keys()))[i]," = ",precentageList[i]," %")

