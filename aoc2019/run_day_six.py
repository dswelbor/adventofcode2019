from day_six.planetary_builder import PlanetaryBuilder
from day_six.planetary_composite import CentralMassComposite, SatelliteLeaf

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
planetary_tree = builder.build()  # build the tree

# Part One - calculate direct and indirect orbits
print('Part one - calculate total sum of all direct and indirect orbits: ')
count_orbits = planetary_tree.count_orbits(0)
print(count_orbits)
