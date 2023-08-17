# HardvardX Cs50P Introduction to Programming with Python
# Lecture 4: Libraries: Random, Statistics

"""
    Libraries are bits of code written by you or others can you can use in your program.
    Along with Python interpreter we download some modules as the random library
    import random - imports every function in that module
    from library import function - imports only the function you want to use
    Youtube link: https://www.youtube.com/watch?v=MztLZWibctI
"""

from random import choice
from random import randint
from random import shuffle
from statistics import mean


def main():
    # random_func()
    statistics_func()


def statistics_func():
    print(mean([100, 90, 100, 100, 85]))


def random_func():
    # coin()
    # integer()
    shuffle_func()


def coin():
    coin = choice(["heads", "tails"])  # this thing inside, is a secuence
    print(coin)


def integer():
    number = randint(1, 10)
    print(number)


def shuffle_func():
    cards = ["ana", "juan", "victor", 4, 3]
    shuffle(cards)
    for card in cards:
        print(card)


if __name__ == "__main__":
    main()
