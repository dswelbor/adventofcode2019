from adventofcode.utils import get_number
from adventofcode.aoc2020 import day_one
import argparse
import sys

DEF_2019_DAYS = [1, 2, 3, 4, 5, 6]
DEF_2020_DAYS = [1, 2]


def read_args():
    """
    This is a helper function that parses passed cli args. These args are used
    in running some or all of the advent of code solutions
    """
    parser = argparse.ArgumentParser(description='Process adventofcode args.')
    # parser.add_argument('integers', metavar='N', type=int, nargs='+',
    #                     help='an integer for the accumulator')
    parser.add_argument('--aoc2020', type=int, nargs='*',
                        help='specify which days to solve for in aoc2020')
    parser.add_argument('--aoc2019', type=int, nargs='*',
                        help='an integer for the accumulator')
    parsed_args = parser.parse_args()

    # at least one advent challenge year is required
    if parsed_args.aoc2019 is None and parsed_args.aoc2020 is None:
        raise argparse.ArgumentError(None, 'Either --aoc2019 or --aoc2020 required')

    """
    # fill default day values
    if parsed_args.aoc2019 is not None and not parsed_args.aoc2019:
        parsed_args.aoc2019 = DEF_2019_DAYS
    if parsed_args.aoc2020 is not None and not parsed_args.aoc2019:
        parsed_args.aoc2020 = DEF_2020_DAYS
    """
    return parsed_args


if __name__ == '__main__':
    print('hi')
    try:
        args = read_args()
        # parse days into strings
        days_2019, days_2020 = [], []
        if args.aoc2019:
            days_2019 = [get_number(int(x)) for x in args.aoc2019]
        if args.aoc2020:
            days_2020 = [get_number(int(x)) for x in args.aoc2020]
        # for day in days_2019:
        #     pass
        #     print(f'2019: {day}')
        for day in days_2020:
            advent_module = sys.modules[f'adventofcode.aoc2020.day_{day}']
            advent_module.run()
            print(f'2020: {day}')
    except argparse.ArgumentError as e:
        print(f'Oops, an error occurred: {e}')





