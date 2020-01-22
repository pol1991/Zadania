#Warsztat4 - Zadanie 3.
# -*- encoding: utf-8 -*-

List=[8,9,10]
print("Lista: "+str(List))
print(" ")
print("(a)")
List[1]=17
print("Lista: "+str(List))
print(" ")
print("(b)")
List.append(4)
List.append(5)
List.append(6)
print("Lista: "+str(List))
print(" ")
print("(c)")
List.pop(0)
print("Lista: "+str(List))
print(" ")
print("(d)")
List.sort()
print("Lista: "+str(List))
print(" ")
print("(e)")
List=List*2
print("Lista: "+str(List))
print(" ")
print("(f)")
List.insert(3,25)
print("Lista: "+str(List))
