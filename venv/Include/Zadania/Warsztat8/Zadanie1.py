#Warsztat8 - Zadanie 1.
# -*- encoding: utf-8 -*-

class Investment:
    def __init__(self, principal, interest):
        self.principal=principal
        self.interest=interest
    def __str__(self):
        return 'Principal - $ {0:.2f}'.format(self.principal)

A=Investment(100,100)
A.__str__()

print(A.__str__())
