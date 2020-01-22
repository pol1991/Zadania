#Warsztat3 - Zadanie 1.
# -*- encoding: utf-8 -*-

name=input("podaj cos z klawiatury: ")

print ("(a)")
print (" ")
print("Dlugosc napisu to:",len(name))

print ("(b)")
print ("String 10 razy:  ")
for i in range(10):
    print (name)

print (" ")
print ("(c)")
print ("pierwsza litera Stringa: "+name[0])
print (" ")
print ("(d)")
print ("Pierwsze 3 litery Stringa: "+name[:3])
print (" ")
print ("(e)")
print ("Ostatnie 3 litery Stringa: "+name[2:])
print (" ")
print ("(f)")
print ("String od tyłu: "+name[::-1])
print (" ")
print ("(g)")

if(len(name)>=7):
    print (name[6])
else:
    print ("String jest za krótki. ")

print (" ")
print ("(h)")
print ("String bez pierwszej i ostatniej litery: "+name[1:-1])
print (" ")
print ("(i)")
print ("String uppercasem: "+name.upper())
print (" ")
print ("(j)")
print ("zamiana liter na spacje: ")
print (" "*len(name))
