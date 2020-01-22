# Warsztat7 - Zadanie5.
# -*- encoding: utf-8 -*-

def zad5():
    with open("files/namelist.txt", "r") as names_file:
        names = names_file.read().splitlines()
    names = [name.split() for name in names]
    query = input("Insert initials you're searching for: ").upper()
    assert 2 <= len(query) <= 3, "The initials have to contain either 2 or 3 letters"

    for name in names:
        if len(name) == 3:
            if len(query) == 3 and name[0][:1] == query[:1] and name[1][:1] == query[1:2] and name[2][:1] == query[2:]:
                print(" ".join(name))
            elif len(query) == 2 and name[0][:1] == query[:1] and name[2][:1] == query[1:]:
                print(" ".join(name))
        else:
            if name[0][:1] == query[:1] and name[1][:1] == query[:-2:-1]:
                print(" ".join(name))