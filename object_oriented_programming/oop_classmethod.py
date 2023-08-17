# HardvardX Cs50P Introduction to Programming with Python
# Lecture 8: Object-Oriented Programming: Class method

"""
    Youtube Link: https://www.youtube.com/watch?v=e4fwY9ZsxPw&list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V&index=13&t=6629s
    1. @classmethod is a function that we can use to add functionality to a class as a whole. Not to instances of that class
    2. __init__ method is not there cause is not need to instantiate.
    3. self, is no longer relevant and is removed, we use cls
"""
import random


class Hat:
    """
    if this was no class method we will need a init to instantiate
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):
        print(name, "is in", random.choice(self.houses))
    
    we will use the method by doing:
        hat = Hat()
        hat.sort("Harry")
    """

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")
