# HardvardX Cs50P Introduction to Programming with Python
# Lecture 3.Short: Debugging: Mario breaktoy

"""
Breakpoint - it's where you want your code to stop
"""


def main():
    while True:
        try:
            height = int(input("Height: "))
        except Exception:
            pass
        else:
            pyramid(height)
            break


def pyramid(height):
    for i in range(height):
        print(f" " * (height - (i + 1)), end="")
        print("#" * (i + 1))  # i starts with 0


if __name__ == "__main__":
    main()
