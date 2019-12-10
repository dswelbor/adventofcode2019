# import day_one
from day_one import day_one_util

# part one
print('Part One: Expected fuel requirements: ')
print(day_one_util.calc_fuel_reqs('input.txt'))

# part 2
print('Part Two: Total fuel requirements inclusive of additional fuel mass: ')
print(day_one_util.calc_total_fuel_reqs('input.txt'))
