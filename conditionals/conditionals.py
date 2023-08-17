# HardvardX Cs50P Introduction to Programming with Python
# Lecture 1: Conditionals
"""
    == Equal
    != Different
    <= Smaller
    >= Bigger
    or
    and
"""


def main():
    # compareTwoNumbers()
    # parity()
    match()


def compareTwoNumbers():
    x = int(input("What is x? "))
    y = int(input("What is y? "))

    if x < y:
        print(f"y:{y} is bigger that x:{x}")
    elif x == y:
        print(f"x:{x} is equal to y:{y}")
    else:
        print(f"x:{x} is bigger than y:{y}")


def parity():
    number = int(input("Write a number: "))
    if is_even(number):
        print(f"Even")
    else:
        print(f"Odd")


def is_even(n):
    return n % 2 == 0
    """
    Other ways to write it:
    return True if n % 2 == 0 else False << this one is readable
    
    if n % 2 == 0:
        return True
    else:
        return False
    """


def match():
    number = int(input("Write a number between 1-3: "))
    match number:
        case 1:
            print("First place")
        case 2:
            print("Second place")
        case 3:
            print("Third place")
        case _:
            print("Error")


if __name__ == "__main__":
    main()
