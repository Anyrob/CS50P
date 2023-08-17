# HardvardX Cs50P Introduction to Programming with Python
# Lecture 8: Object-Oriented Programming: diccionary, tupple and list

"""
    1. A tuple is a sequences of values. Unlike a list, a tuple can’t be modified, they are inmmutable.
    2. List and diccionaries, are both mutable.
"""

def main():
    built_a_tupple()
    built_a_tupple_package()
    built_a_list()
    built_a_diccionary()


# tupple
def built_a_tupple():
    name, house = get_tupple()  # unpacking both values
    print(f"{name} from {house}")  # accessing them for the name


def get_tupple():
    name = input("Name: ")
    house = input("House: ")
    return name, house


def built_a_tupple_package():
    student = get_tupple_package()
    print(
        f"{student[0]} from {student[1]}"
    )  # accesing them by index of the object (package)


def get_tupple_package():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)  # now it has parenthesis


# list
def built_a_list():
    student = get_list()
    print(f"{student[0]} from {student[1]}")


def get_list():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]  # it has square brackets


# diccionary
def built_a_diccionary():
    student = get_diccionary()
    print(f"{student['name']} from {student['house']}")


def get_diccionary():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}  # it has curly brackets


if __name__ == "__main__":
    main()
