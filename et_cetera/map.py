# HardvardX Cs50P Introduction to Programming with Python
# Lecture 9: Et Cetera: map, list comprehensions, filter

"""
    Youtube Link: https://www.youtube.com/watch?v=6pgodt1mezg&list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V&index=14&t=5845s
    1. map allows you to map a function to a sequence of values.
        1.1 It takes a function we want applied to every element of a list.
        1.2 Second, it takes that list itself, to which we’ll apply the aforementioned function
    2. List comprehensions allow you to create a list on the fly in one elegant one-liner.
    3. Filter function allows us to return a subset of a sequence for which a certain condition is true.
    4. We can apply the same idea behind list comprehensions to dictionaries.
    5. Enumerate presents the index and the value of each element
        seasons = ['Spring', 'Summer', 'Fall', 'Winter']
        list(enumerate(seasons))
        [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
"""
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

only_students = ["Hermione", "Harry", "Ron"]


def main():
    yell_without_map("This is CS50")
    yell_with_map("This is CS50")
    yell_list_comprehensions("This is CS50")
    another_list_comprehensions(students)
    filter_function(students)
    diccionary_comprehensions(only_students)
    enumerate_function(only_students)


def yell_without_map(*words):  # variable number of words
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)


def yell_with_map(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)


def yell_list_comprehensions(*words):
    uppercased = [
        word.upper() for word in words
    ]  # it has square brackets for creating the list
    print(*uppercased)


def another_list_comprehensions(students):
    """
    Equivalent:
        gryffindors = []
        for student in students:
            if student["house"] == "Gryffindor":
                gryffindors.append(student["name"])
    """
    gryffindors = [
        student["name"] for student in students if student["house"] == "Gryffindor"
    ]
    print("New list:")
    for gryffindor in sorted(gryffindors):
        print(gryffindor)


def filter_function(students):
    gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)

    print("Filter example:")
    for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
        print(gryffindor["name"])


def diccionary_comprehensions(students):
    """
    Equivalent:
        gryffindors = []
        for student in students:
            gryffindors.append({"name": student, "house": "Gryffindor"})
    """
    gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
    print(f"New dicccionary: {gryffindors}")


def enumerate_function(students):
    """
    for i in range(len(students)):
        print(i + 1, students[i])
    """
    for i, student in enumerate(students):
        print(i + 1, student)


if __name__ == "__main__":
    main()
