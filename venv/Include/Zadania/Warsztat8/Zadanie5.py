#Warsztat8 - Zadanie 5.
# -*- encoding: utf-8 -*-
class Converter:
    def __init__(self, length, unit):
        self.length = length
        self.unit = unit

    # inches, feet, yards, miles, kilometers, meters, centimeters, and millimeters
    def inches(self):
        if self.unit == 'in':
            print(self.length, self.unit, ' = ', self.length, 'in')
        if self.unit == 'ft':
            print(self.length, self.unit, ' = ', self.length * 12, 'in')
        if self.unit == 'yd':
            print(self.length, self.unit, ' = ', self.length * 36, 'in')
        if self.unit == 'mi':
            print(self.length, self.unit, ' = ', round(self.length * 63360.23622, 2), 'in')
        if self.unit == 'km':
            print(self.length, self.unit, ' = ', round(self.length * 39370.07874, 2), 'in')
        if self.unit == 'm':
            print(self.length, self.unit, ' = ', round(self.length * 39.37007874, 2), 'in')
        if self.unit == 'cm':
            print(self.length, self.unit, ' = ', round(self.length * 0.3937007874, 2), 'in')
        if self.unit == 'mm':
            print(self.length, self.unit, ' = ', round(self.length * 0.0393700787, 2), 'in')

    def feet(self):
        if self.unit == 'in':
            print(self.length, self.unit, ' = ', round(self.length * 0.0833333333, 2), 'ft')
        if self.unit == 'ft':
            print(self.length, self.unit, ' = ', self.length, 'ft')
        if self.unit == 'yd':
            print(self.length, self.unit, ' = ', self.length * 3, 'ft')
        if self.unit == 'mi':
            print(self.length, self.unit, ' = ', round(self.length * 5280.019685, 2), 'ft')
        if self.unit == 'km':
            print(self.length, self.unit, ' = ', round(self.length * 3280.839895, 2), 'ft')
        if self.unit == 'm':
            print(self.length, self.unit, ' = ', round(self.length * 3.280839895, 2), 'ft')
        if self.unit == 'cm':
            print(self.length, self.unit, ' = ', round(self.length * 0.032808399, 2), 'ft')
        if self.unit == 'mm':
            print(self.length, self.unit, ' = ', round(self.length * 0.0032808399, 3), 'ft')

    def yards(self):
        if self.unit == 'in':
            print(self.length, self.unit, ' = ', round(self.length * 0.0277777778, 2), 'yd')
        if self.unit == 'ft':
            print(self.length, self.unit, ' = ', round(self.length * 0.3333333333, 2), 'yd')
        if self.unit == 'yd':
            print(self.length, self.unit, ' = ', self.length, 'yd')
        if self.unit == 'mi':
            print(self.length, self.unit, ' = ', round(self.length * 1760.0065617, 2), 'yd')
        if self.unit == 'km':
            print(self.length, self.unit, ' = ', round(self.length * 1093.6132983, 2), 'yd')
        if self.unit == 'm':
            print(self.length, self.unit, ' = ', round(self.length * 1.0936132983, 2), 'yd')
        if self.unit == 'cm':
            print(self.length, self.unit, ' = ', round(self.length * 0.010936133, 3), 'yd')
        if self.unit == 'mm':
            print(self.length, self.unit, ' = ', round(self.length * 0.001093613, 4), 'yd')

    def miles(self):
        if self.unit == 'in':
            print(self.length, self.unit, ' = ', round(self.length * 0.0000157828, 6), 'mi')
        if self.unit == 'ft':
            print(self.length, self.unit, ' = ', round(self.length * 0.0001893932, 6), 'mi')
        if self.unit == 'yd':
            print(self.length, self.unit, ' = ', round(self.length * 0.0005681797, 6), 'mi')
        if self.unit == 'mi':
            print(self.length, self.unit, ' = ', self.length, 'mi')
        if self.unit == 'km':
            print(self.length, self.unit, ' = ', round(self.length * 0.6213688756, 2), 'mi')
        if self.unit == 'm':
            print(self.length, self.unit, ' = ', round(self.length * 0.0006213689, 5), 'mi')
        if self.unit == 'cm':
            print(self.length, self.unit, ' = ', round(self.length * 0.0000062137, 7), 'mi')
        if self.unit == 'mm':
            print(self.length, self.unit, ' = ', round(self.length * 0.0000006213689, 9), 'mi')

    def kilometers(self):
        if self.unit == 'in':
            print(self.length, self.unit, ' = ', round(self.length * 0.0000254, 6), 'km')
        if self.unit == 'ft':
            print(self.length, self.unit, ' = ', round(self.length * 0.0003048, 5), 'km')
        if self.unit == 'yd':
            print(self.length, self.unit, ' = ', round(self.length * 0.0009144, 5), 'km')
        if self.unit == 'mi':
            print(self.length, self.unit, ' = ', round(self.length * 1.60935, 2), 'km')
        if self.unit == 'km':
            print(self.length, self.unit, ' = ', self.length, 'km')
        if self.unit == 'm':
            print(self.length, self.unit, ' = ', round(self.length * 0.001, 3), 'km')
        if self.unit == 'cm':
            print(self.length, self.unit, ' = ', round(self.length * 0.00001, 5), 'km')
        if self.unit == 'mm':
            print(self.length, self.unit, ' = ', round(self.length * 0.000001, 6), 'km')

    def meters(self):
        if self.unit == 'in':
            print(self.length, self.unit, ' = ', round(self.length * 0.0254, 3), 'm')
        if self.unit == 'ft':
            print(self.length, self.unit, ' = ', round(self.length * 0.3048, 2), 'm')
        if self.unit == 'yd':
            print(self.length, self.unit, ' = ', round(self.length * 0.9144, 2), 'm')
        if self.unit == 'mi':
            print(self.length, self.unit, ' = ', round(self.length * 1609.35, 2), 'm')
        if self.unit == 'km':
            print(self.length, self.unit, ' = ', self.length * 1000, 'm')
        if self.unit == 'm':
            print(self.length, self.unit, ' = ', self.length, 'm')
        if self.unit == 'cm':
            print(self.length, self.unit, ' = ', self.length * 0.01, 'm')
        if self.unit == 'mm':
            print(self.length, self.unit, ' = ', round(self.length * 0.001, 3), 'm')

    def centimeters(self):
        if self.unit == 'in':
            print(self.length, self.unit, ' = ', self.length * 2.54, 'cm')
        if self.unit == 'ft':
            print(self.length, self.unit, ' = ', self.length * 30.48, 'cm')
        if self.unit == 'yd':
            print(self.length, self.unit, ' = ', self.length * 91.44, 'cm')
        if self.unit == 'mi':
            print(self.length, self.unit, ' = ', self.length * 160935, 'cm')
        if self.unit == 'km':
            print(self.length, self.unit, ' = ', self.length * 100000, 'cm')
        if self.unit == 'm':
            print(self.length, self.unit, ' = ', self.length * 100, 'cm')
        if self.unit == 'cm':
            print(self.length, self.unit, ' = ', self.length, 'cm')
        if self.unit == 'mm':
            print(self.length, self.unit, ' = ', self.length * 0.1, 'cm')

    def milimeters(self):
        if self.unit == 'in':
            print(self.length, self.unit, ' = ', self.length * 25.4, 'mm')
        if self.unit == 'ft':
            print(self.length, self.unit, ' = ', self.length * 304.8, 'mm')
        if self.unit == 'yd':
            print(self.length, self.unit, ' = ', self.length * 914.4, 'mm')
        if self.unit == 'mi':
            print(self.length, self.unit, ' = ', self.length * 1609350, 'mm')
        if self.unit == 'km':
            print(self.length, self.unit, ' = ', self.length * 1000000, 'mm')
        if self.unit == 'm':
            print(self.length, self.unit, ' = ', self.length * 1000, 'mm')
        if self.unit == 'cm':
            print(self.length, self.unit, ' = ', self.length * 10, 'mm')
        if self.unit == 'mm':
            print(self.length, self.unit, ' = ', self.length, 'mm')