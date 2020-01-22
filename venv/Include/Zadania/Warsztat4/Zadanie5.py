#Warsztat4 - Zadanie 5.
# -*- encoding: utf-8 -*-

List=[]

number=eval(input("Wprowadź ile słów chcesz dodać do listy: "))

for i in range(number):
    slowo=input("wpisz słowo: ")
    List.append(slowo)

for i in range(len(List)):
    List[i]=List[i][1::]

print(List)
