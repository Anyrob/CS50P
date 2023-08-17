# HardvardX Cs50P Introduction to Programming with Python
# Lecture 4: Libraries: Command-Line Arguments, Slice

"""
    sys.argv - Argument vector: List of all the words that the human typed in at their prompt before hiting enter
    On the terminal run it like this: 
        python 4_1Arguments.py Ana
        python 4_1Arguments.py "Ana Robles" takes Ana Robles as 1 arg
    To debug "args": ["--Ana"], into the launch.json file (click Run > Open Configurations) >>> This will print --Ana but..
    for some reason just ["Ana"] doesn't work.
"""
import sys


def main():
    # basic()
    # better()
    arguments()


def basic():
    print("The name of this file will always be store at sys.argv[0]: ", sys.argv[0])

    if len(sys.argv) > 1:
        print("hello, my name is", sys.argv[1])

    else:
        print("Too few arguments")


def better():
    if len(sys.argv) < 2:  # If there's only 1 that's the file name only
        sys.exit("Too few arguments")

    print("hello, my name is", sys.argv[1])


def arguments():
    if len(sys.argv) < 2:
        sys.exit("Too few arguments")

    for arg in sys.argv[1:]:  # Slice to take only the first name, in case both are given
        print("hello, my name is", arg)


if __name__ == "__main__":
    main()
