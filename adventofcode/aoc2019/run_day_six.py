from adventofcode.aoc2019.day_six.planetary_builder import PlanetaryBuilder
from adventofcode.aoc2019.day_six.planetary_composite import get_min_dist, \
    PlanetaryTree

"""
Runner script for Day 2 Advent of Code challenge - relies on
planetary_composite classes and PlanetaryBuilder class.
"""

# Get list orbit relations
input_file = open('day_six/input_day_six.txt', 'r')
# iterate through each line - populate list
orbit_relations = []
for relation_line in input_file:

    relation = relation_line.strip().split(')')
    orbit_relations.append((relation[0], relation[1]))

# build tree from input
builder = PlanetaryBuilder()
for pair in orbit_relations:
    # iteratively add orbits
    builder.add_orbit(pair[0], pair[1])
planetary_trees = builder.build()  # build the tree

# Part One - calculate direct and indirect orbits
print('Part one - calculate total sum of all direct and indirect orbits: ')
# iteratively calculate sum of all direct and indirect orbits
# get Center Of Mass root
com = None
for root in planetary_trees:
    if root.name == 'COM':
        com = PlanetaryTree(root)
        break

count_orbits = com.count_all_orbits()  # expect 308790
print(count_orbits)

# Part two
print('Calculate the distance from Center of Mass to Santa:')
print('calculating...')
dist = get_min_dist(com, 'YOU', 'SAN')
print(dist)
