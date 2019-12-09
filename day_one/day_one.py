import math


def calc_fuel_reqs(filename):
    """This function opens a file and sums the fuel requirements from the file"""
    input_file = open(filename, "r")

    # initialize sum to 0
    sum = 0
    # iterate through list
    for input_line in input_file:
        try:
            req = input_line.strip()
            sum += math.trunc(int(req) / 3) - 2
        except ValueError:
            pass

    return sum

