# Warsztat4 - Zadanie 7.
# -*- encoding: utf-8 -*-

L=[8,6,4]
N=[1,9,3]
K=[]

if(len(L)==len(N)):
    for i in range(len(L)):
        K.append(L[i]+N[i])
else:
    print("Różne rozmiary List")

print(K)