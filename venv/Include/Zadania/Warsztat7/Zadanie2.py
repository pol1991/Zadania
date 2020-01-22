# Warsztat7 - Zadanie2.
# -*- encoding: utf-8 -*-
def zad2():
    with open("files/grades.txt", "r") as grades:
        data = grades.readlines()
        for line in data:
            elem = line.split()
            print(elem)
            if int(elem[1]) > 60 and int(elem[2]) > 60 and int(elem[3]) > 60:
                print(elem[0] + " passed")
            else:
                print(elem[0] + " didn\'t pass")

