#!/usr/bin/env python3

# Created by: Ben Lapuhapo
# Created on: Nov 2019
# This program uses user defined functions


def calculate_area(base, height):
    # calculate area

    # process
    area = base * height / 2

    # output
    print("The area is {0} cm²".format(area))


def main():
    # this function gets length and width

    # input
    base_from_user_input = input("Enter the Base of a Triangle (cm): ")
    height_from_user_input = input("Enter the Height of a Triangle (cm): ")
    print("")

    try:
        base_from_user_int = int(base_from_user_input)
        height_from_user_int = int(height_from_user_input)
        print("You Entered A Number Correctly")
        # call functions
        calculate_area(base_from_user_int, height_from_user_int)
    except Exception:
        print("Not An Integer")
    finally:
        print('Goodbye')


if __name__ == "__main__":
    main()
