# Warsztat4 - Zaodlegloscanie 14.
# -*- encoodlegloscing: utf-8 -*-

odleglosc_stopy = int(input("Podaj odleglosc w stopach: "))
odleglosc_cale = odleglosc_stopy * 12
odleglosc_yard = odleglosc_stopy / 3.0
odleglosc_mile = odleglosc_stopy / 5280.0
odleglosc_cm = odleglosc_stopy / 0.032808
odleglosc_m = odleglosc_stopy / 3.2808
odleglosc_km = odleglosc_stopy / 3280.8


print("Odleglosc w calach wynosi %i cali." % odleglosc_cale)
print("Odleglosc w yardach wynosi %.2f yardów." % odleglosc_yard)
print("Odleglosc w milach wynosi %.5f mil." % odleglosc_mile)
print("Odleglosc w cm wynosi %.2f cm." % odleglosc_cm)
print("Odległość w m wynosi %.4f m." % odleglosc_m)
print("Odległosć w km wynosi %.5f km" % odleglosc_km)