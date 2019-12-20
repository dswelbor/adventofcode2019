# from aoc2019.day_six.planetary_composite import CentralMassComposite


class BFSPlanetaryIterator:
    """
    This is an implementation of the iterator design pattern. It is applied to
    the n-ary tree structure of planetary components. Each returned element is
    a binary tuple (component, depth).
    """
    def __init__(self, root):
        """Basic initialization method for iterator"""
        self.components = [root]  # initial singleton set of roots
        self.index = 0  # "root" index
        self.depth = 0  # initial depth of traversal is 0

    def __next__(self):
        """Gets the next element in a level order traversal"""
        # Iterate through current level of components
        try:
            component = (self.components[self.index], self.depth)
            self.index += 1
            return component
        # Reached end of current level list
        except IndexError:
            next_level = []
            # Try to populate next level component list
            for component in self.components:
                try:
                    next_level.extend(component.satellites)
                except AttributeError:
                    # Not a composite - just a leaf
                    pass

            # Re-assign attributes
            self.components = next_level
            self.index = 0
            self.depth += 1  # increment depth of traversal

            # Try to return next value
            try:
                component = (self.components[self.index], self.depth)
                self.index += 1
                return component
            # No more elements
            except IndexError:
                raise StopIteration
