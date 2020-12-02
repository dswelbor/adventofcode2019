#!/usr/bin/env python
from adventofcode.aoc2019.day_one import day_one_util

"""This module provides the run functionality for day one aoc2019 solution"""

# part one
print('Part One: Expected fuel requirements: ')
print(day_one_util.calc_fuel_reqs('day_one/input_day1.txt'))

# part 2
print('Part Two: Total fuel requirements inclusive of additional fuel mass: ')
print(day_one_util.calc_total_fuel_reqs('day_one/input_day1.txt'))
