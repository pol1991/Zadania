# Warsztat4 - Zadanie 8.
# -*- encoding: utf-8 -*-

L=[]
def wypisz_dzielnik(liczba):
#   print("The factors of",liczba,"are:")
   for i in range(1, liczba + 1):
       if liczba % i == 0:
           L.append(i)
#           print(i)
liczba_input = eval(input("podaj liczbe: "))
wypisz_dzielnik(liczba_input)

print("dzielniki liczby to: ")
print(L)