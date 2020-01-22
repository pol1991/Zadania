#Warsztat4 - Zadanie 4.
# -*- encoding: utf-8 -*-

List=[]
print("Wpisuj liczby miedzy 1-12.")
zakres=input("podaj ile chcesz podać liczb: ")

for i in range(int(zakres)):
    liczba=input("podaj liczbę: ")
    List.append(liczba)


print("Oto twoja lista: "+str(List))

for i in  range(len(List)):
    if List[i]>'10':
        List[i]=10

print("Oto twoja lista bo przekształceniu: "+str(List))
