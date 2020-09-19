#!/usr/bin/env python

from random import randint


def main():
    # Generate random name
    name = generate_name()
    print(name)


def generate_name():
    # List of names to choose from
    prefixes = [
                "lil",
                "young",
                "47",
                "99%",
                "ice",
                "fire",
                "fresh",
                "da",
                "negative",
                "xoxo"
            ]

    names = [
                "impossible",
                "ramen",
                "Z",
                "St. Beaumont XVII",
                "vizion",
                "saucy",
                "inverse",
                "blingz",
                "drippy",
                "smokes"
            ]

    # Choose and match random items from the lists
    prefix = prefixes[randint(0, len(prefixes)-1)]
    name = names[randint(0, len(names)-1)]
    return f"{prefix} {name}"


if __name__ == "__main__":
    main()
