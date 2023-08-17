# HardvardX Cs50P Introduction to Programming with Python
# Lecture 5: Unit Test: Organizing test into folders

"""
    1. Youtube Link: https://www.youtube.com/watch?v=tIrcxwLqzjQ 
    2. It’s most common in industry to write code to test your own programs.
    3. When you create a folder, and inside of that, a file called __init__.py,
        you're telling python that folder is a package nor a module
    4. pytest name_of_my_folder, pytest will search all posible tests in that folder, you need to be outside the folder to run this.
"""

from functions_and_variables.functions_and_variables import hello

def test_hello():
    assert hello('Ana') == 'Hello Ana'
    assert hello() == 'Hello world'