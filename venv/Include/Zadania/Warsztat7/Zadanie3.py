# Warsztat7 - Zadanie3.
# -*- encoding: utf-8 -*-

def zad3():
    with open("files/logfile.txt", "r") as logfile:
        logs = logfile.read()
    logs = logs.split("\n")
    logs = [log.split(", ") for log in logs]
    print("USERS WORKING OVER 1 HOUR".center(64, "-"))
    for entry in logs:
        time_format = "%H:%M"
        time_difference = dt.datetime.strptime(entry[2], time_format) - dt.datetime.strptime(entry[1], time_format)
        if time_difference.seconds > 60*60:
            print(f"User: {entry[0]} >> hrs worked: {time_difference}")