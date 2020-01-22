# Warsztat7 - Zadanie6.
# -*- encoding: utf-8 -*-

def zad6():
    with open("files/namelist.txt", "r") as names_file:
        names = names_file.read().splitlines()
    regex_vowels = re.compile(r".*[Aa].*[Ee].*[Ii].*[Oo].*[Uu]")
    for name in names:
        if regex_vowels.search(name) is not None:
            print(name)