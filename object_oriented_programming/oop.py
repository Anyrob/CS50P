# HardvardX Cs50P Introduction to Programming with Python
# Lecture 8: Object-Oriented Programming: classes

"""
    Youtube Link: https://www.youtube.com/watch?v=e4fwY9ZsxPw&list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V&index=13&t=24s
    1. A class help us to create our own type of data and give them names.
    2. Utilize “dot notation” to access attributes of the instances
    3. Object-oriented program encourages you to encapusulate all the functionality of a class within the class definition.
    4. Raise is an exception that alerts the programmer to a potential error
    5. __init__ is the function to initializate a object
    6. __str__ is the function by which you can print the attributes of an object
"""
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        match self.house:
            case "Gryffindor":
                return "🦁"
            case "Hufflepuff":
                return "🦡"
            case "Ravenclaw":
                return "🦅"
            case "Slytherin":
                return "🐍"
            case _:
                return "🪄"

def main():
    student = get_student()
    print(student) #we can print the object print because we defined our __str__ function
    print(student.charm())


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
