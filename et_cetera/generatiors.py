# HardvardX Cs50P Introduction to Programming with Python
# Lecture 9: Et Cetera: Generators and Iterators

"""
    Youtube link: https://www.youtube.com/watch?v=6pgodt1mezg&list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V&index=14&t=7689s
    1. There is a way to protect against your system running out of resources the problems they are addressing become too large.
    2. The yield generator can solve this problem by returning a small bit of the results at a time.
    3. Control C interrupts the program, so you don't have to wait for the 1,000,000 sheeps to be printed.
"""


def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep_function_that_gets_kill(n):
    # Trying to call a 1000000 with this will kill the program, cause its a lot to process
    flock = []
    for i in range(n):
        flock.append("🐑" * i)
    return flock


def sheep(n):
    for i in range(n):
        yield "🐑" * i


if __name__ == "__main__":
    main()
