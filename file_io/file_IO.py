# HardvardX Cs50P Introduction to Programming with Python
# Lecture 6: FileI/O: open, with

"""
    1. Everything we've programmed has stored information in memory.
    2. File I/O is the ability of a program to take a file as input or create a file as output.
    3. open - this keyword is a functionality built into Python that allows you to open a file and utilize it in your program.
       If the file doesn't exists creates a new one.
       About it's second param:
        - "w" writes into a file (but deletes whatever was written before)
        - "a" append into a file
    4. with - this keyword allows you to automate the closing of a file.
    5. file.readlines() - reads all lines at the same time, if you want to iterate between lines you can do it directly with a for.
        or you can do it after this readlines, but it's an extra step.
"""


def main():
    name = input("what's your name?")
    # modify_file(name)
    # modify_file_with(name)
    # read_file()
    # read_file_improved()
    read_sorted()
    # another_sorted()


def modify_file(name):
    file = open("names.txt", "a")
    file.write(f"{name}\n")
    file.close


def modify_file_with(name):
    with open("names.txt", "a") as file:
        file.write(f"{name}\n")


def read_file():
    with open("names.txt", "r") as file:
        """readlines has a special ability to read all the lines of a file and store them in a file called lines."""
        lines = file.readlines()

    for line in lines:
        """Whitespace removed with rstrip, because it was sending the names and the break line"""
        print("hello", line.rstrip())


def read_file_improved():
    with open("names.txt", "r") as file:
        for line in file:
            print("hello", line.rstrip())


def read_sorted():
    with open("names.txt", "r") as file:
        for line in sorted(file):
            print("hello", line.rstrip())


def another_sorted():
    names = []

    with open("names.txt") as file:
        for line in file:
            names.append(line.rstrip())

    """To sort in reverse: or name in sorted(names, reverse=True):"""
    for name in sorted(names):
        print(f"hello, {name}")


if __name__ == "__main__":
    main()
