#Warsztat3 - Zadanie 7
# -*- encoding: utf-8 -*-

napis=raw_input("napisz slowo: ")

if(napis==napis[::-1]):
    print "Slowo to palidrom"
else:
    print "To nie jest palidrom"