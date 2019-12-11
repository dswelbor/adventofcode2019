from aoc2019.day_two.int_code import IntCode, brute_force

"""Runner script for Day 2 Advent of Code challenge - relies on IntCode class for logic"""

# Get list of numbers from input
input_file = open('input_day_two.txt', 'r')
input_str = input_file.read()
input_list = input_str.split(',')
input = []
for num_str in input_list:
    input.append(int(num_str))

# condition inout
input[1] = 12
input[2] = 2

print('Part One: Conditioned initial input:')
print(input)

# Part 1
# Populate IntCode object with inout and reconstruct data
int_code_p1 = IntCode(input[:])
int_code_p1.visit_all()  # rebuild data
print('Part One - Value at position one:')
print(int_code_p1.list[0])

# Part 2
# Find the pair of values that result in 19690720 at index 0
target = 19690720
result = brute_force(input, target)
print('Part Two - 100 * value1 + value2 is:')
print(result)




