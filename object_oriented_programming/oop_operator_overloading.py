# HardvardX Cs50P Introduction to Programming with Python
# Lecture 8: Object-Oriented Programming: Operator Overloading

"""
    Youtube Link: https://www.youtube.com/watch?v=e4fwY9ZsxPw&list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V&index=13&t=9329s
    1. some operators such as + and - can be “overloaded” such that they can have more abilities beyond simple arithmetic.
"""


class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)


potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

total = potter + weasley
print(total)
