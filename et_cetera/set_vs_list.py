# HardvardX Cs50P Introduction to Programming with Python
# Lecture 9: Et Cetera: Set vs list

"""
    Youtube Link: https://www.youtube.com/watch?v=6pgodt1mezg&list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V&index=14&t=105s
    1. set would be considered a set of numbers without any duplicates.
    2. Set uses .add, list uses .append and a conditional to verify if duplicates
"""


def main():
    houses = set_students()
    for house in sorted(houses):
        print(house)

    houses_2 = list_students()
    for house in sorted(houses_2):
        print(house)


def set_students():
    students = [
        {"name": "Hermione", "house": "Gryffindor"},
        {"name": "Harry", "house": "Gryffindor"},
        {"name": "Ron", "house": "Gryffindor"},
        {"name": "Draco", "house": "Slytherin"},
        {"name": "Padma", "house": "Ravenclaw"},
    ]

    houses = []

    for student in students:
        if student["house"] not in houses:
            houses.append(student["house"])

    return houses


def list_students():
    students = [
        {"name": "Hermione", "house": "Gryffindor"},
        {"name": "Harry", "house": "Gryffindor"},
        {"name": "Ron", "house": "Gryffindor"},
        {"name": "Draco", "house": "Slytherin"},
        {"name": "Padma", "house": "Ravenclaw"},
    ]

    houses = set()

    for student in students:
        houses.add(student["house"])

    return houses


if __name__ == "__main__":
    main()
