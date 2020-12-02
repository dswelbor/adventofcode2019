from adventofcode.aoc2019.day_four.container_cracker import CrackIt

"""This module provides the run functionality for day four aoc2019 solution"""

range_start = 128392
range_end = 643281

permutation_cracker = CrackIt(range_start, range_end)

# Part one
print('Day 4 part 1 - Find the number of valid permutations')
print('calculating...')
valid_qty = permutation_cracker.count_valid_permutations()
print(valid_qty)

# Part two
print('Day 4 part 2 - Find the number of refined valid permutations')
print('calculating...')
valid_qty_refined = permutation_cracker.count_valid_permutations_refined()
print(valid_qty_refined)
