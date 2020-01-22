#Warsztat3 - Zadanie 4
# -*- encoding: utf-8 -*-

slowo=raw_input("napisz jakies slowo: ")
samogloski = "aeiouy"
A =[]

for i in range(len(slowo)):
    for j in  range(len(samogloski)):
        if slowo[i] == samogloski[j]:
            A +=[samogloski[j]];


if set ('aeiouy').intersection(slowo.lower()):
    print "Zawiera samogloski"
    import sets
    uniquearray = sets.Set(A)
    print uniquearray
else:
    print "Nie zawiera samoglosek"

