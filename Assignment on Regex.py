# Using a regex pattern and match(), and prints the name if it is valid, "Invalid name" if the name is not.

import re

names = [
    "Abraham Lincoln",
    "Andrew P Garfield",
    "peter pan",
    "Connor Milliken",
    "Jordan Alexander Williams",
    "Madonna",
    "programming is cool",
]


def match_check(list):

    for name in list:
        name_match = re.match(r"(([A-Z][A-Za-z]+) (\w+?) ([A-Z][A-Za-z]+)|([A-Z][A-Za-z]+) ([A-Z][A-Za-z]+)|([A-Z][A-Za-z]+))", name)
        if name_match:
            print(name_match.group())
        else:
            print("Invalid Name")

match_check(names)

