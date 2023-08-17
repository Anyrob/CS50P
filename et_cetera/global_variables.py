# HardvardX Cs50P Introduction to Programming with Python
# Lecture 9: Et Cetera: Global Variables

"""
    Youtube Link: https://www.youtube.com/watch?v=6pgodt1mezg&list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V&index=14&t=457s
    1. If you declare a variable outside of main you can use it in main, but not in another function.
    2. It will raise a unbound local error.
    3. To interact with a global variable inside a function, the solution is to use the global keyword.
        i.e balance is a global variable above main(), desposit will take balance if "global" keyword is there.
        def deposit(n):
            global balance
            balance += n
    4. Global can be replaced by using a class. Generally speaking, global variables should be used quite sparingly, if at all!
"""


class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n


def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)


if __name__ == "__main__":
    main()
