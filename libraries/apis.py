# HardvardX Cs50P Introduction to Programming with Python
# Lecture 4: Libraries: API

"""
     1. API is an application programming interface.
     2. Allows you to connect to the code of others: Third-party services.
     3. Requests is a package that allows your program to behave as a web browser would. >> pip3 install requests
     4. Doc: https://pypi.org/project/requests/
     5. JSON JavaScript Object Notation. Language agnostic format for exchanging data between computers.
     
     About the program:
     1. Replicate the search of: https://itunes.apple.com/search?entity=song&limit=1&term=enchanted
     2. It's looking for one song result that relates to the term enchanted
     3. To run in terminal: python 4_3Requests.py Shakira, result >>> Empire
     4. To debug add into the launch.json file (click Run > Open Configurations)
            4.1 "args": ["--song Enchanted"]
            4.2 "args": ["--Enchanted"]
        Note: Adding "args": ["Enchanted"] won't work, i think bc it needs to be a key
        Multiargument looks like this   args": ["--key1", "value1", "value2", "--key2", "value3", "value4"]
"""
import json
import sys
import requests


def main():
    if len(sys.argv) != 2:
        sys.exit()
    # basic()
    json_library()
    song_name()


def basic():
    response = requests.get(
        "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]
    )
    # Apple's returning a JSON response, Python's request library is converting it
    # to a Python dictionary which happens to use almost the same syntax.
    return response.json()


def json_library():
    json_response = basic()
    print(
        json.dumps(json_response, indent=2)
    )  # it utilizes indent to make the output more readable


def song_name():
    json_response = basic()
    for result in json_response["results"]:
        print(result["trackName"])


main()
