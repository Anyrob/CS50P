# HardvardX Cs50P Introduction to Programming with Python
# Lecture 9: Et Cetera: args and kwargs

"""
    1. args are positional arguments, such as those we provide to print like print("Hello", "World").
    2. kwargs are named arguments (keyword arguments), such as those we provide to print like print(end="").
        2.1 the named values are provided in the form of a dictionary.
"""


def main():
    f(100, 50, 25)
    f(galleons=100, sickles=50, knuts=25)


def f(*args, **kwargs):
    print("Positional:", args)
    print("Named:", kwargs)


if __name__ == "__main__":
    main()
