#Warsztat3 - Zadanie 3
# -*- encoding: utf-8 -*-

formula=raw_input("napisz jakas formule: ")

if(formula.count("(")!=formula.count(")")):
    print ("Zapomniałeś o nawiasie )")
elif(formula.count("{")!=formula.count("}")):
    print ("Zapomniałeś o nawiasie }")
elif(formula.count("[")!=formula.count("]")):
    print ("Zapomniałeś o nawiasie ]")
else:
    print ("Z twoją formula wszystko ok. Wypisuje: "+formula)
