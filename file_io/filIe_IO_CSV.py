# HardvardX Cs50P Introduction to Programming with Python
# Lecture 6: FileI/O: CSV

"""
    1. CSV stands for “comma separated values”.
    2. Split - returns a list of substrings on the string.
    3. Python’s built-in csv library comes with an object called a reader.
        A reader works in a for loop, where each iteration the reader gives us another row from our CSV file.
        This row itself is a list. row[0], for example, is the first element of the given row
"""

import csv


def main():
    # read_csv()
    # read_csv_clean()
    # sort_csv()
    # sort_csv_anonimous()
    # csv_reader()
    # csv_dicctionary_reader()
    csv_writer()
    # dict_writer()


def read_csv():
    with open("names.csv") as file:
        for line in file:
            row = line.rstrip().split(",")
            print(f"{row[0]} is in {row[1]} house")


def read_csv_clean():
    with open("names.csv") as file:
        for line in file:
            name, house = line.rstrip().split(",")
            print(f"{name} is in {house} house")


def sort_csv():
    students = []

    with open("names.csv") as file:
        for line in file:
            name, house = line.rstrip().split(",")
            students.append({"name": name, "house": house})  # diccionary

    """
        To sort a list of diccionaries, we need a key
        This will call that function in every diccionary, getting the name then deciding how to sort accoding to the reverse flag
        The function doens't require pharentesis cause is the sorted function how makes the call
        another valid value is to add directly student["name"] instead of the function  """
    for student in sorted(students, key=get_name, reverse=True):
        print(f"{student['name']} is in {student['house']}")


def get_name(student):
    return student["name"]


def sort_csv_anonimous():
    students = []

    with open("names.csv") as file:
        for line in file:
            name, house = line.rstrip().split(",")
            students.append({"name": name, "house": house})
    for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name']} is in {student['house']}")


def csv_reader():
    """
    The usual split we use in the examples above will produce a ValueError: too many values to unpack.
    Cause we have more than 1 , so we fail trying to split
    """
    students = []

    with open("homeForCSVReader.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            students.append({"name": row[0], "home": row[1]})

    for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name']} is from {student['home']}")


def csv_dicctionary_reader():
    """The file used here has a hint at the top of the file, with the names of the columns"""
    students = []

    with open("homeForDicReader.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row) #The same as: {"name": row["name"], "home": row["home"]}

    for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name']} is in {student['home']}")


def csv_writer():
    import csv

    name = input("What's your name? ")
    home = input("Where's your home? ")

    with open("write.csv", "a") as file:  # New file with name, home at the top
        writer = csv.writer(file)
        writer.writerow([name, home])


def dict_writer():
    import csv

    name = input("What's your name? ")
    home = input("Where's your home? ")

    with open("write.csv", "a") as file:  # New file with name, home at the top
        writer = csv.DictWriter(file, fieldnames=["name", "home"])
        writer.writerow( {"name": name, "home": home})
        # The only difference is that once we have the keys, we don't mind of which parameters we pass first


if __name__ == "__main__":
    main()
