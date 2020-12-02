# from aoc2019.day_two.int_code import IntCode, brute_force
from adventofcode.aoc2019.shared.int_code import IntCode, brute_force

"""
Runner script for Day 2 Advent of Code challenge - relies on IntCode class
for logic
"""

# Get list of numbers from input
input_file = open('day_two/input_day_two.txt', 'r')
input_str = input_file.read()
input_list = input_str.split(',')
input_codes = []
for num_str in input_list:
    input_codes.append(int(num_str))

# condition inout
input_codes[1] = 12
input_codes[2] = 2

print('Part One: Conditioned initial input:')
# print(input_codes)

# Part 1
# Populate IntCode object with inout and reconstruct data
int_code_p1 = IntCode(input_codes[:])
int_code_p1.visit_all()  # rebuild data
print('Part One - Value at position one:')
print(int_code_p1.list[0])  # expect 3790645 for provided data

# Part 2
# Find the pair of values that result in 19690720 at index 0
target = 19690720
result = brute_force(input_codes, target)
print('Part Two - 100 * value1 + value2 is:')
print(result)  # expect 6577 for provided input
