# HardvardX Cs50P Introduction to Programming with Python
# Lecture 5: Unit Test. Code to test with

def main():
    x = input("What's x? ")
    print("x squared is", square(x))


def square(n):
    return n * n


if __name__ == "__main__":
    main()