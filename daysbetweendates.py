#!/usr/bin/env python

from datetime import date
from sys import argv, exit


def main():
    # Check if valid args
    if len(argv) < 3:
        print("Invalid arguments.")
        show_instructions()
        exit(0)

    # Parse args
    date1 = parse_date_string(argv[1])
    date2 = parse_date_string(argv[2])

    # Calculate
    delta = calculate_date_delta(date1, date2)
    print(f"Days between {date1} and {date2}: \n{delta}")


def parse_date_string(date_str):
    # Create a Date object from a string

    if date_str == "today":
        return date.today()

    # Exit program if invalid input
    if len(date_str) != 8:
        print(f"ERROR: {date_str} does not follow the format YYYYMMDD")
        exit(0)

    # Parse string
    year = int(date_str[:4])
    month = int(date_str[4:6])
    day = int(date_str[6:])

    try:
        return date(year, month, day)
    except Exception as e:
        print(f"ERROR: {str(e)}")
        exit(0)


def calculate_date_delta(date1, date2):
    days_delta = (date1 - date2).days
    return abs(days_delta)


def show_instructions():
    print("USAGE: daysbetweendates.py <date 1> <date 2>")
    print("       A date is a string with the format YYYYMMDD")
    print("       You can also simply write 'today' if referring to today")
    print("EXAMPLE: daysbetweendates.py today 20200420")


if __name__ == "__main__":
    main()
