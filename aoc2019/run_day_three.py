from day_three.wire_runner import WireTable, WireGrid


"""This module provides the run functionality for day three aoc2019 solution"""

# Read in input txt file
input_file = open('day_three/input_day_three.txt', 'r')
line_one = input_file.readline()
line_two = input_file.readline()

# Part 1
# Initialize grid
# wire_grid = WireGrid(2041)
# initialize WireTable
wire_table = WireTable()


# Trace input instructions
first_trace = line_one.split(',')  # First list of trace instructions
second_trace = line_two.split(',')  # second list of trace instructions

print('Trace inputs...')
wire_table.trace_wires(first_trace)
print('first trace complete')
wire_table.trace_wires(second_trace)
print('second trace complete')

# Calculate manhattan distance of closest intersection
man_dist = wire_table.get_min_manhattan_dist()
print('Part One - Manhattan distance of closest intersection to origin:')
print('calculating...')
print(man_dist)

# Calculate minimum number of combined steps to an intersection
man_step_dist = wire_table.find_min_steps()
print('Part Two - Combined minimum number of steps to an intersection:')
print('calculating...')
print(man_step_dist)





