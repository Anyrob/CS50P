# HardvardX Cs50P Introduction to Programming with Python
# Lecture 2: Loops: while, for, len, list, dict


def main():
    # while_func()
    # for_func()
    # user_input()
    for_with_list()
    # dictionaries()
    # list_of_dictionaries()
    # nested_loops(3, 5)


def while_func():
    i = 3
    while i != 0:
        print(f"i:{i}")
        i = i - 1


def for_func():
    for i in range(3):
        print(f"i:{i}")
    # if I'm not using i I will write it as for _ in range(3)


def user_input():
    while True:
        n = int(input("What's n?"))
        # the loop while continue until it gets into the break section
        if n <= 0:
            print("continue")
            continue

        elif n > 0:
            print("break")
            break


def for_with_list():
    brothers = ["Hugo", "Victor", "Sam"]

    for i in range(len(brothers)):
        print(i + 1, brothers[i])

    for brother in brothers:
        print(brother)


def dictionaries():
    """
    Dicts or dictionaries is a data structure that allows you to associate keys with values.
    """
    students = {
        "Key": "Value",
        "Hermoine": "Gryffindor",
        "Harry": "Gryffindor",
        "Ron": "Gryffindor",
        "Draco": "Slytherin",
    }

    # print one. This will give us the value by giving it the key.
    print(students["Harry"])

    for student in students:
        print(f"{student}'s house is {students[student]}")


def list_of_dictionaries():
    students = [
        {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
        {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
        {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
        {"name": "Draco", "house": "Slytherin", "patronus": None},
    ]

    for student in students:
        print(student["name"], student["house"], student["patronus"], sep=", ")
    # Ron's patronus
    for student in students:
        if student["name"] == "Ron":
            print(f'{student["patronus"]}')


def nested_loops(high, width):
    # For each row in the rectangle
    for i in range(high):
        # How many bricks I'll print
        for j in range(width):
            print("#", end="")
        print()


if __name__ == "__main__":
    main()
