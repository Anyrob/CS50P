# HardvardX Cs50P Introduction to Programming with Python
# Lecture 8: Object-Oriented Programming: Class method

"""
    Youtube Link: https://www.youtube.com/watch?v=e4fwY9ZsxPw&list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V&index=13&t=8470s
    1. Create a class that “inherits” methods, variables, and attributes from another class.
    2. Use super to access the father class
"""


class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    def __str__(self):
        return f"The wizard is {self.name}"


class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

    def __str__(self):
        return f"The student is {self.name} from {self.house}"


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def __str__(self):
        return f"The professor of {self.subject} is {self.name}"


wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")

print(wizard)
print(student)
print(professor)
