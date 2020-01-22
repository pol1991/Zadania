# Warsztat7 - Zadanie7.
# -*- encoding: utf-8 -*-

def zad7():
    with open("files/baseball.txt", "r") as baseball_file:
        players = baseball_file.readlines()
    players = [player.split(" ") for player in players]
    for player in players:
        if int(player[9]) >= 20 and int(player[13]) >= 20:
            print(" ".join(player))