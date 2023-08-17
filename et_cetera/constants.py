# HardvardX Cs50P Introduction to Programming with Python
# Lecture 9: Et Cetera: Constants, type hints and dogstrings

"""
    Youtube Link: https://www.youtube.com/watch?v=6pgodt1mezg&list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V&index=14&t=1420s
    1. Constants allow one to program defensively and reduce the opportunities for important values to be altered.
    2. Python actually has no mechanism to prevent us from changing that value within our code
    3. Python does not require the explicit declaration of types.
    4. mypy is a program that can help you test to make sure all your variables are of the right type. [pip install mypy]
        by runing mypy file.name, it can detect errors
    5. Hints are marked with a ":" follow by the type of the variable
    6. A standard way of commenting your function’s purpose is to use a docstring.
    7. Tools like Sphinx, can be used to parse docstrings and automatically create documentation for us in the form of web pages and PDF files.
"""


class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")

    def meow_with_input(self, n: int):  # This one uses a typehint
        """
        Meow n times.

        :param n: Number of times to meow
        :type n: int
        :raise TypeError: If n is not an int
        :return: A string of n meows, one per line
        :rtype: str
        """
        return "meow\n" * n

def main():
    cat = Cat()
    cat.meow()
    repetitions: int = int(input("number"))  # This one uses a typehint
    meows = cat.meow_with_input(repetitions)
    print(meows, end="")


if __name__ == "__main__":
    main()

