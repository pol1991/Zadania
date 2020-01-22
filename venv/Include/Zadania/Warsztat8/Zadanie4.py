#Warsztat8 - Zadanie 4.
# -*- encoding: utf-8 -*-

class Time:
    def __init__(self, seconds):
        self.seconds = seconds

    def convert_to_minutes(self):
        minute = 0
        time = self.seconds

        for i in range(1, time + 1):
            if i % 60 == 0:
                minute += 1
        second = time - minute * 60

        print(str(minute), ':', str(second))

    def convert_to_hours(self):
        hour = 0
        minute = 0
        time = self.seconds

        for i in range(1, time + 1):
            if i % 3600 == 0:
                hour += 1

        time_left = time - hour * 3600

        for i in range(1, time_left + 1):
            if i % 60 == 0:
                minute += 1
        second = time_left - minute * 60

        print(str(hour), ':', str(minute), ':', str(second))
