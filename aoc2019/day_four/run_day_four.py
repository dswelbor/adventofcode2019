from container_cracker import CrackIt

range_start = 128392
range_end = 643281

print('Day four part one - Find the number of valid permutations')
print('calculating...')
permutation_cracker = CrackIt(range_start, range_end)
valid_qty = permutation_cracker.get_num_valid_permutations()
print(valid_qty)
