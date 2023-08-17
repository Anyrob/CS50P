# HardvardX Cs50P Introduction to Programming with Python
# Lecture 0: Functions and Variables

# Functions
"""
    The function must be defined before using it. But a nice practice to avoid adding it at
    the beggining always, we need to create a main() function too
"""


def main():
    first_program()
    # second_program()


def first_program():
    print("This is the first program")
    name = input("What's your name? ")
    hello(name)
    options_to_build_a_string(name)


def hello(name="world"):
    name = name.strip()  # Remove whitespace from str
    print("Hello " + name)
    return ("Hello " + name)


def options_to_build_a_string(name):
    print(
        "\n\nYou're inside of a function, and here's the name you send as argument: "
        + name
    )
    print(f"1. This is a FString, {name}")
    print(
        "2. "
        + name
        + " when using plus sign you have to add spaces"
        + " between strings"
    )
    print(
        "3. You can concatenate", "string", "with spaces", "just by using comas,", name
    )
    print(
        "This is just a demostration of a custom end.",
        end=" My new End, jumps 2 lines. \n\n",
    )


def second_program():
    print("Here starts the second program")
    x = int(input("What's the first number: "))
    y = int(input("What's the second number: "))
    addition(x, y)


def addition(number1, number2):
    print(number1 + number2)


# This conditional is added later in the course (Lesson 4: Making your own library), it works without it
# but if I don't add it, and I try to call the "hello" function from another file,
# it will execute all the main content in this file, not only the function I want
if __name__ == "__main__":
    main()
