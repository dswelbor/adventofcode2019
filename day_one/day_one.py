import math


def calc_fuel_reqs(filename):
    """This function opens a file and sums the fuel requirements from the file"""
    input_file = open(filename, "r")
    # Make a list
    input_list = input_file.readline()

    # initialize sum to 0
    sum = 0
    # iterate through list
    for req in input_list:
        try:
            sum += math.trunc(int(req) / 3) - 2
        except ValueError:
            pass

    return sum

