#!/usr/bin/env python

import re
from sys import argv, exit


def main():
    # Get input
    if len(argv) < 2:
        print("No argument received.")
        show_instructions()
        exit(0)

    number_string = argv[1]

    # Check if input contains non-digit characters
    pattern = r"([^\d\,\s])"
    if re.search(pattern, number_string):
        print("Only digits, commas and spaces allowed.")
        exit(0)

    # Remove commas and whitespaces
    pattern = r"(\d*)"
    number_string = "".join(re.findall(pattern, number_string))

    # Check if number is within the bounds for conversion
    if len(number_string) > 15:
        print("Can only convert up to 15 digits (hundred trillion)")
        exit(0)

    # Convert input to words
    print(convert(number_string))


def chunk(number_str):
    # Split the number into three-digit chunks
    number_str = number_str[::-1]
    chunks = [number_str[i:i+3][::-1] for i in range(0, len(number_str), 3)]
    chunks.reverse()

    # Change the type from string to int
    return [int(c) for c in chunks]


def to_words(x):
    lows = [
                "one", "two", "three", "four", "five",
                "six", "seven", "eight", "nine", "ten",
                "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                "sixteen", "seventeen", "eighteen", "nineteen"
           ]

    highs = [
                "ten", "twenty", "thirty", "forty", "fifty",
                "sixty", "seventy", "eighty", "ninety"
            ]

    if x == 0:
        return ""
    elif x < 20:
        return lows[x-1]
    elif x < 100:
        tens, ones = divmod(x, 10)
        word = highs[tens-1]
        if ones > 0:
            word += f"-{to_words(ones)}"
        return word
    else:
        hundreds, remainder = divmod(x, 100)
        word = f"{lows[hundreds-1]} hundred"
        if remainder > 0:
            word += f" and {to_words(remainder)}"
        return word


def convert(number_str):
    # Check for zero
    if number_str == "0":
        return "zero"

    # Split number into three-digit chunks
    chunks = chunk(number_str)

    # Convert number into words
    scales = ["thousand", "million", "billion", "trillion"]
    word = ""
    for i, x in enumerate(chunks):
        if x > 0:
            word += to_words(x)
            if i < len(chunks)-1:
                word += f" {scales[(len(chunks)-2)-i]} "

    return word


def show_instructions():
    print("USAGE: numberstowords.py <NUMBER>")
    print("       NUMBER must be a positive whole number")
    print("       and must not exceed 15 digits!")
    print("EXAMPLE: numberstowords.py 12345")


if __name__ == "__main__":
    main()
