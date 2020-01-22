# Warsztat7 - Zadanie4.
# -*- encoding: utf-8 -*-

def zad4():
    with open("files/students.txt", "r") as students_file:
        students = students_file.read().splitlines()

    new_students = []

    for student in students:
        new_line = []
        line = student.split(" ")
        new_line.append(line[0].capitalize())
        new_line.append(line[1].capitalize())
        new_line.append("+48 " + line[3])
        new_line = " ".join(new_line)
        new_students.append(new_line + "\n")

    with open("files/students2.txt", "w") as new_students_file:
        new_students_file.writelines(new_students)