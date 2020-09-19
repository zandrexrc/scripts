#!/usr/bin/env python

import pytz
import json
import os
from sys import argv, exit
from datetime import datetime


def main():
    # Show help message if no args
    if len(argv) < 2:
        print_commands()
        exit(0)

    # Execute command
    user_command = argv[1]
    try:
        if user_command == "now":
            assert(len(argv) >= 3)
            now(argv[2])
        elif user_command == "convert":
            assert(len(argv) >= 5)
            convert(argv[2], argv[3], argv[4])
        elif user_command == "diff":
            assert(len(argv) >= 4)
            diff(argv[2], argv[3])
        elif user_command == "countries":
            assert(len(argv) >= 2)
            list_countries()
        else:
            print("Invalid command.")
            print_commands()
            exit(0)
    except AssertionError as e:
        print("Invalid arguments.")
        print_commands()
        exit(0)


def load_data():
    # Open and read timezones.json
    this_dir, this_filename = os.path.split(__file__)
    data_path = os.path.join(this_dir, "timezones.json")
    with open(data_path) as f:
        data = json.load(f)
        return data


def list_countries():
    # Print all country names from the json file
    data = load_data()
    for country in data:
        print(country["name"])


def get_timezones(country_name):
    # Return all timezones in a given country
    data = load_data()
    for country in data:
        if country["name"] == country_name:
            return country["zones"]

    # Return None if country is not in list
    return None


def choose_timezone(country_name):
    # Get all timezones in the given country
    timezones = get_timezones(country_name)

    # Let user choose one timezone if there are multiple timezones
    if timezones is not None:
        if len(timezones) == 1:
            return timezones[0]
        else:
            print(f"Select timezone:")
            for i, tz in enumerate(timezones):
                print(f"{i}. {tz}")
            chosen = int(input("\n Enter the timezone number: "))
            while (0 > chosen or chosen >= len(timezones)):
                print(f"{chosen} is not a valid timezone.")
                chosen = int(input("\n Enter the timezone number: "))
            return timezones[chosen]
    else:
        print(f"No timezones found for {country_name}.")
        print_help()
        exit(-1)


def now(country_name):
    # Get all timezones in the given country
    timezones = get_timezones(country_name)

    # Print local times in each timezone
    if timezones is not None:
        utc_now = datetime.utcnow()
        for tz in timezones:
            tz_now = pytz.timezone(tz).fromutc(utc_now)
            tz_now_str = tz_now.strftime("%Y-%m-%d %H:%M")
            print("{:32} {:>}".format(tz, tz_now_str))
    else:
        print(f"No timezones found for {country_name}.")
        print_help()
        exit(-1)


def convert(time, origin, target):
    # Get timezones
    tz_origin = choose_timezone(origin)
    tz_targets = get_timezones(target)

    # Convert time from origin to all timezones in target
    try:
        h, m = time.split(":")
        t = datetime.now().replace(hour=int(h), minute=int(m))
        origin_time = pytz.timezone(tz_origin).localize(t)
        origin_time_str = origin_time.strftime("%Y-%m-%d %H:%M")
        print("Source:")
        print("{:32} {:>}\n".format(tz_origin, origin_time_str))
        print("Target:")
        for tz in tz_targets:
            tz_target = pytz.timezone(tz)
            target_time = origin_time.astimezone(tz_target)
            target_time_str = target_time.strftime("%Y-%m-%d %H:%M")
            print("{:32} {:>}".format(tz, target_time_str))
    except Exception as e:
        print(f"\nError!\n{time} is not a valid time-string.")
        print(f"Make sure that it follows the pattern HH:MM")
        print(f"and it is in 24-hour format.")
        exit(-1)


def diff(country1, country2):
    # Get timezones
    tz1 = pytz.timezone(choose_timezone(country1))
    tz2 = pytz.timezone(choose_timezone(country2))

    # Calculate hour difference
    now = datetime.now()
    diff_hours = (tz1.localize(now) -
                  tz2.localize(now).astimezone(tz1)).total_seconds() / 3600
    if diff_hours == 0:
        print(f"{country1}({tz1}) and {country2}({tz2}) have the same local time.")
    elif diff_hours > 0:
        print(f"{country1}({tz1}) is behind {country2}({tz2}) by {diff_hours} hours.")
    else:
        diff_hours = abs(diff_hours)
        print(f"{country1}({tz1}) is ahead {country2}({tz2}) by {diff_hours} hours.")


def print_help():
    message = "Use the command 'countries' to show a list of " +\
              "all valid country names.\n" +\
              "Make sure to correctly spell and capitalize the name. \n" +\
              "If the name consists of multiple words, enclose it in " +\
              "'' quotes. (e.g. 'United States')"
    print(message)


def print_commands():
    msg = "COMMANDS:\n" +\
          "now <country>                    : See the local time in a specific country.\n" +\
          "convert <time> <origin> <target> : Convert the specified time in origin country to the corresponding time in target country.\n" +\
          "diff <country1> <country2>       : Calculate the time difference between two countries.\n" +\
          "countries                        : Show a list of all available countries"
    print(msg)


if __name__ == "__main__":
    main()
