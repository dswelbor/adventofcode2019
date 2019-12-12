# from aoc2019.day_three.wire_runner import WireGrid
from wire_runner import WireGrid
# from wire_runner import WireGrid


"""This module provides the run functionality for day three aoc2019 solution"""

# Read in input txt file
input_file = open('input_day_three.txt', 'r')
line_one = input_file.readline()
line_two = input_file.readline()

# Part 1
# Initialize grid
wire_grid = WireGrid(8081)


# Trace input instructions
first_trace = line_one.split(',')  # First list of trace instructions
second_trace = line_two.split(',')  # second list of trace instructions

print('Part One - Manhattan distance of closest intersection to origin:')
print('calculating...')
wire_grid.trace_wires(first_trace)
print('first trace complete')
wire_grid.trace_wires(second_trace)
print('second trace complete')

# Calculate manhattan distance of closest intersection
man_dist = wire_grid.get_min_manhattan_dist()
print(man_dist)





