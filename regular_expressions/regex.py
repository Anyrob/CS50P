# HardvardX Cs50P Introduction to Programming with Python
# Lecture 7: Regular Expressions, Case Sensitivity, Cleaning Up User Input, Extracting User Input

"""
    1. Regular expressions or “regexes” will enable us to examine patterns within our code.
    2. re library has a number of built-in functions that can validate user inputs against patterns.
        .   any character except a new line
        *   0 or more repetitions
        +   1 or more repetitions
        ?   0 or 1 repetition
        {m} m repetitions
        {m,n} m-n repetitions
        ^   matches the start of the string
        $   matches the end of the string or just before the newline at the end of the string
        []    set of characters
        [^]   complementing the set - i.e [^@] Everything but at
        \d    decimal digit
        \D    not a decimal digit
        \s    whitespace characters
        \S    not a whitespace character
        \w    word character, as well as numbers and the underscore. - This is the same as [a-zA-Z0-9_]
        \W    not a word character
        A|B     either A or B
        (...)   a group
        (?:...) non-capturing version
    3. The search library follows the signature re.search(pattern, string, flags=0)
        Flags:
            re.IGNORECASE - i.e re.search(r"^\w+@\w.+\.edu$", email, re.IGNORECASE)
            re.MULTILINE
            re.DOTALL
    4. There are other functions within the re library you might find useful. re.match and re.fullmatch.
    5. The replace method allows us to find one item and replace it with another. - username = url.replace("https://twitter.com/", "")
    6. sub - This method allows us to substitute a pattern with something else. 
        re.sub(pattern, repl, string, count=0, flags=0)

"""
import re


def main():
    # verify_email()
    # cleaning_input()
    # cleaning_input_v2()
    # extracting_user_input()
    extracting_user_input_v2()


def verify_email():
    email = input("What's your email? ").strip()

    if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
        """
        ^\w - It could start with any word character/numbers/underscore
        +@ - it allows one at
        (\w+\.)? it can optionally have something like firstword.secondword.edu
        \w - allows the "secondword"
        \.edu - takes the . as part of the string, and not as a a validator
        $ - the input must finish with .edu
        """
        print("Valid")
    else:
        print("Invalid")


def cleaning_input():
    name = input("What's your name? ").strip()
    matches = re.search(r"^(.+), (.+)$", name)
    if matches:
        last, first = matches.groups()
        name = f"{first} {last}"
        print(f"hello, {name}")


def cleaning_input_v2():
    # The walrus := operator assigns a value from right to left and allows us to ask a boolean question at the same time.
    name = input("What's your name? ").strip()
    if matches := re.search(r"^(.+), *(.+)$", name):
        name = matches.group(2) + " " + matches.group(1)
    print(f"hello, {name}")


def extracting_user_input():
    """ "Possible Input:
    https://twitter.com/anarobles
    http://twitter.com/anarobles
    https://www.twitter.com/anarobles
    """
    url = input("URL: ").strip()
    username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
    """
        ^ - has to begging with http, www or with twitter to be valid
        s? - makes the s optional
        (https?://)? - makes protocol optional
        (www\.)? - makes it optional, and escape tells the compiler the dot is from the string
    """
    print(f"Username: {username}")


def extracting_user_input_v2():
    import re

    url = input("URL: ").strip()

    if matches := re.search(
        r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE
    ):
        print(f"Username:", matches.group(1))


if __name__ == "__main__":
    main()
