# HardvardX Cs50P Introduction to Programming with Python
# Lecture 8: Object-Oriented Programming: decorators

"""
    Youtube Link: https://www.youtube.com/watch?v=e4fwY9ZsxPw&list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V&index=13&t=4843s
    1. Define properties using function “decorators”, which begin with @.
        @property - getter for property
        @nameofproperty.setter - setter for property
"""


class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter for house
    @property
    def house(self):
        return self._house

    # Setter for house
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house
        # house is a property of our class, with functions via which a user attempts to set our class attribute.
        # _house is that class attribute itself. Indicates to users they shouldn’t! modify this value directly.
        # _house should only be set through the house setter.

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
