# Warsztat7 - Zadanie1.
# -*- encoding: utf-8 -*-

import datetime as dt
import re

def zad1():
    new_data = []
    with open("files/class_scores.txt", "r") as class_scores:
        data = class_scores.readlines()
        for line in data:
            elements = line.split()
            print(elements)
            elements[1] = str(int(elements[1]) + 5)
            print(elements)
            with open("files/class_scores2.txt", "a") as c:
                c.write(elements[0])
                c.write(" ")
                c.write(elements[1])
                c.write("\n")

                