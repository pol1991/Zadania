# Warsztat4 - Zadanie 10.
# -*- encoding: utf-8 -*-
from collections import deque

L=[1,2,3,4,5,6,7,8,9]

L = deque(L) 
L.rotate(1)
L = list(L) 

print(L)
