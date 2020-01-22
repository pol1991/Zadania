# Warsztat4 - Zaodlegloscanie 14.
# -*- encoodlegloscing: utf-8 -*-

print("(a)")
from random import randint

message = input("Enter a message: ")

alphabet = list('abcdefghijklmnopqrstuvwxyz')
secret = []
for character in message.lower():
    if character in alphabet:
        i = randint(0, 26)
        secret.append(alphabet[i])
    else:
        secret.append(character)

print(''.join(secret))
print("")
print("(b)")

message = list(message)
i = 0
secret_rev = []
for character in secret:
    secret_rev.append(message[i])
    i += 1

print(''.join(secret_rev))