#!/usr/bin/env python

from sys import argv, exit


def main():
    # Get args
    if len(argv) < 4:
        print("Invalid args.")
        show_instructions()
        exit(0)

    value = argv[1]
    orig_unit = argv[2]
    target_unit = argv[3]

    # Check if valid args
    if not does_it_float(value):
        print("Input value must be a whole or floating point number.")
        exit(0)
    else:
        value = float(argv[1])

    # Convert input
    result = convert(value, orig_unit, target_unit)
    print(f"{result} {target_unit}")


def convert(x, orig_unit, target_unit):
    """ Converts a value to another unit.

    Args:
        x (float):         the value to be converted
        orig_unit (str):   the original unit of the value
        target_unit (str): the unit to convert the value to

    Returns:
        (float):           the converted value
    """
    # Number of yards in a unit
    imperial_units = {
                        "in": 1/36,
                        "ft": 1/3,
                        "yd": 1,
                        "mi": 1760
                     }

    # Number of meters in a unit
    si_units = {
                    "mm": 0.001,
                    "cm": 0.01,
                    "m": 1,
                    "km": 1000
               }

    # Convert x to base units (yards and meters)
    x_yd, x_m = 0, 0

    if orig_unit in imperial_units:
        x_yd = x * imperial_units[orig_unit]
        x_m = x_yd * 0.9144
    elif orig_unit in si_units:
        x_m = x * si_units[orig_unit]
        x_yd = x_m / 0.9144
    else:
        print(f"Invalid input: {orig_unit} is not a valid unit")
        show_instructions()
        exit(0)

    # Convert x to target unit
    if target_unit in imperial_units:
        return x_yd / imperial_units[target_unit]
    elif target_unit in si_units:
        return x_m / si_units[target_unit]
    else:
        print(f"Invalid input: {target_unit} is not a valid unit")
        show_instructions()
        exit(0)


def does_it_float(x):
    """ Check if a string is a floating point number.

    Args:
        x (str):   the value to be thrown into the water

    Returns:
        (boolean): True if x floats, False if it sinks
    """
    try:
        float(x)
        return True
    except ValueError:
        return False


def show_instructions():
    print("USAGE: unitconverter.py <value> <original_unit> <target_unit>")
    print("EXAMPLE: unitconverter.py 12 in cm")
    print("LIST OF UNITS: ")
    print(" in")
    print(" ft")
    print(" yd")
    print(" mi")
    print(" mm")
    print(" cm")
    print(" m")
    print(" km")


if __name__ == "__main__":
    main()
