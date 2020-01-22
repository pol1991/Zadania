#Warsztat8 - Zadanie 3.
# -*- encoding: utf-8 -*-

class PasswordManager:
    def __init__(self, old_passwords):
        self.old_passwords = old_passwords

    def get_password(self):
        current = self.old_passwords[-1]
        print(current)

    def set_password(self, new_password):
        self.old_passwords.append(new_password)

    def is_correct(self, entered_password):
        print(entered_password)
        print(self.get_password())
        if entered_password == self.old_passwords[-1]:
            return True
        else:
            return False