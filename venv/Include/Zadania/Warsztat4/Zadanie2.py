#Warsztat4 - Zadanie 2.
# -*- encoding: utf-8 -*-

import random as rnd
List=[]

for i in range(20):
    List.append(rnd.randint(1,100))

number=0
for i in range(len(List)):
        if List[i]%2==0:
            number=number+1
print(" ")
print("(a)")
print("Lista: ")
print(List)
print(" ")
print("(b)")
avg=sum(List)/len(List)
print("Średnia wyrazów listy to: ")
print(avg)
print(" ")
print("(c)")
print("Największa Liczba:")
print(max(List))
print("Najmniejsza Liczba:")
print(min(List))
print(" ")
print("(d)")
maks=max(List)
minimal=min(List)
List.remove(maks)
List.remove(minimal)
print("Druga największa liczba: ")
print(max(List))
print("Druga najmniejsza liczba: ")
print(min(List))
print(" ")
print("(f)")
print("Tyle jest liczb parzystych: ")
print(number)
