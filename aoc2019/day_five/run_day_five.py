from aoc2019.shared.int_code import IntCode

"""Runner script for Day 5 Advent of Code challenge - relies on refactored IntCode class for logic"""

# Get list of numbers from input
input_file = open('input_day_five.txt', 'r')
input_str = input_file.read()
input_list = input_str.split(',')
input_codes = []
for num_str in input_list:
    input_codes.append(int(num_str))

int_code_p1 = IntCode(input_codes[:])
int_code_p1.visit_all()  # test data
# Part one - run tests and get diagnostic code
print('Part One - get diagnostic code:')
d_code = int_code_p1.output_codes[-1]
print(d_code)


