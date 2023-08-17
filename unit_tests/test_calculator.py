# HardvardX Cs50P Introduction to Programming with Python
# Lecture 5: Unit Test: assert, pytest

"""
    1. Assert - allows us to tell the compiler that some assertion, is true
    2. If it fails throws an AssertionError, and in which line it is
    3. pytest is a third-party library that allows you to unit test your program.   pip3 install pytest
    4. We don't need main
    5. To run in terminal: pytest test_calculator.py
"""
from calculator import square
from pytest import raises

def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0

def test_str():
    #By deliting the cast to int in line 9 "x = input("What's x? ")" we could raise this error
    with raises(TypeError):
        square("cat")