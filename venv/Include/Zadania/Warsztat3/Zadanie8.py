#Warsztat3 - Zadanie 8
# -*- encoding: utf-8 -*-

#student = word.count('@student') prof = word.count('@prof')student+1prof+1

A=[]
ile_razy=eval(raw_input("ile chcesz podac adresów?"))
for i in range(ile_razy):
    word=raw_input("podaj string")
    A +=  [word]

print A

for i in range(len(A)):
    student = A[i].count('@student')
    print student


