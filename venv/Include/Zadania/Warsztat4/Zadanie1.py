#Warsztat4 - Zadanie 1.
# -*- encoding: utf-8 -*-

input_string = input("Enter a list numbers or elements separated by space: ")
List = input_string.split()
print("user list is ", List)
number=0
for i in range(len(List)):
    if(List[i]<='5'):
        number=number+1
print(" ")
print("(a)")
print("Długość Listy to: "+str(len(List)))
print(" ")
print("(b)")
print("Ostatni Wyraz Listy: "+str(List[-1]))
print(" ")
print("(c)")
List.reverse()
print("Lista na odwrót: ")
print(List)
print(" ")
print("(d)")
if List.count('5')>0:
    print("YES")
else:
    print("NO")
print(" ")
print("(e)")
print(List.count('5'))
print(" ")
print("(f)")
List.pop(0)
del List[-1]
List.sort()
print(List)
print(" ")
print("(g)")
print(number)
