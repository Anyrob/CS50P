# HardvardX Cs50P Introduction to Programming with Python
# Lecture 9: Et Cetera: Unpacking

"""
    Youtube Link: https://www.youtube.com/watch?v=6pgodt1mezg&list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V&index=14&t=4222s
"""

def main():
    without_unpacking()
    unpacking_list()
    unpacking_diccionary()


def without_unpacking():
    print(
        total(100, 50, 25), "Knuts"
    )  # it also could be (galleons=100, sickles=50, knuts=25)


def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


def unpacking_list():
    coins = [100, 50, 25]
    print(total(*coins), "Knuts")  # its equivalent is (coins[0], coins[1], coins[2])


def unpacking_diccionary():
    coins = {"galleons": 100, "sickles": 50, "knuts": 25}
    print(
        total(**coins), "Knuts"
    )  # its equivalent is (coins["galleons"], coins["sickles"], coins["knuts"])


if __name__ == "__main__":
    main()
