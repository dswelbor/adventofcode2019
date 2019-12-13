import math

"""This module provides the utility functions for the day 1 aoc2019 solution"""


def calc_fuel_reqs(filename):
    """This function opens a file and sums the fuel requirements from the file"""
    input_file = open(filename, "r")

    # initialize sum to 0
    cumulative_total = 0
    # iterate through list
    for input_line in input_file:
        try:
            req = input_line.strip()
            cumulative_total += math.trunc(int(req) / 3) - 2
        except ValueError:
            # do nothing catch block
            pass

    return cumulative_total


def calc_module_fuel(mass):
    """
    This function recursively returns the fuel needed including the additional
    fuel required for the fuel mass
    """
    fuel = math.trunc(mass / 3) - 2
    # Base case
    if fuel < 1:
        return 0

    else:
        # calculate initial fuel
        fuel = math.trunc(mass / 3) - 2
        # recursively calculate total fuel for this module
        return fuel + calc_module_fuel(fuel)


def calc_total_fuel_reqs(filename):
    """This function iterates through all modules and find total fuel requirements"""
    input_file = open(filename, "r")
    cumulative_total = 0  # initialize sum as 0
    # iterate through list
    for input_line in input_file:
        try:
            mass = input_line.strip()
            cumulative_total += calc_module_fuel(int(mass))
        except ValueError:
            # do nothing catch block
            pass

    return cumulative_total
