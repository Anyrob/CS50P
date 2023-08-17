# HardvardX Cs50P Introduction to Programming with Python
# Lecture 4: Libraries: Packages

"""
    1. There are numerous powerful third-party libraries that add functionality. We call these third-party libraries, implemented as a folder, “packages”.
    2. PyPI website, Python Package Index, to download and install packages
    3. pip (package manager) a program that comes with python itself that allows you to install packages: pip3 install cowsay
"""
# Run as python3 4_2Packages.py Ana

import sys
import cowsay


def main():
    cowsay_func()


def cowsay_func():
    if len(sys.argv) == 2:
        cowsay.cow("Hey, " + sys.argv[1])


if __name__ == "__main__":
    main()
