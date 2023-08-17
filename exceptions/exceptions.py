# HardvardX Cs50P Introduction to Programming with Python
# Lecture 3: Exceptions: Value Errors, Runtime Errors, Try, Else, Pass

"""
    SyntaxError - Something that wasn't wrote propertly. It must be fixed manually.
    Runtime errors refer to those created by unexpected behavior within your code. 
"""


def main():
    # exception_else()
    # user_friendly()

    x = user_friendly_return("What's x?")
    print(f"x is {x}")


def exception_else():
    try:
        x = int(input("What's x?"))
    except ValueError:
        print("x is not an integer")
    else:
        print(f"x is {x}")


def user_friendly():
    while True:
        try:
            x = int(input("What's x?"))
        except ValueError:
            print("x is not an integer")
        else:
            break

    print(f"x is {x}")


def user_friendly_return(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            # My code is catching the error but I'm passing on doing something about it
            pass


if __name__ == "__main__":
    main()
