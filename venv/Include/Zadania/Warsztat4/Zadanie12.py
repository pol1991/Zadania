# Warsztat4 - Zadanie 12.
# -*- encoding: utf-8 -*-
import random
from random import randint

L=[]
def lista():
    for i in range(0,100):
        liczba = random.randint(0,1)
        L.append(liczba)
    print (L)
    return L

def ciag_zer(L):

    licznik = 0
    licznik_zer = 0

    for i in L:
        if i == 0:
            licznik += 1
        else:
            if licznik > licznik_zer:
                licznik_zer = licznik
            licznik = 0
    return licznik_zer

print("Nasza Lista to: ")
L=lista()
print("Najdłuższy Ciąg Zer to: ",ciag_zer(L))
