# Warsztat4 - Zadanie 10.
# -*- encoding: utf-8 -*-

ile=eval(input("Wpisz ile jedynek chcesz dodać do listy: "))
L=[]
for i in range(ile):
    L.append(1)
    for j in range(i):
        L.append(0)

print(L)
