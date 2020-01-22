#Warsztat8 - Zadanie 2.
# -*- encoding: utf-8 -*-

class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, number):
        if number <= self.amount:
            if number < 10:
                bill = number * self.price
                print('The cost: ', bill)
            if 10 <= number <= 99:
                bill = number * self.price
                print('The cost: ', bill * 0.9)
            if number >= 100:
                bill = number * self.price
                print('The cost: ', bill * 0.8)
        else:
            print('There\'s not enough items in stock')

    def make_purchase(self, number):
        if number <= self.amount:
            self.get_price(number)
            self.amount = self.amount - number
        else:
            print('There\'s not enough items in stock')