class SatelliteLeaf:
    """This a class for satellite entities - such as planets"""
    def __init__(self, name):
        self.name = name

    def count(self):
        """
        Simple utility method to return the number of nodes in this leaf,
         which is always 1.
        """
        return 1

    def count_orbits(self, level):
        """
        This method returns the number of orbiting entities - 1 as it
        is a leaf.
         """
        return level

    pass


class CentralMassComposite:
    """
    This class is a composite component for central mass entities - such as
    what planets orbit around.
    """
    def __init__(self, name):
        self.name = name
        self.orbit = []  # collection of orbiting entities

    def count(self):
        """
        Simple utility method to recursively return the number of nodes in
        this composite sub tree.
        """
        count = 1
        for child in self.orbit:
            count += child.count()
        return count

    def count_orbits(self, level):
        """
        This method returns recursively the number of all orbiting entities,
         both direct and indirect.
        """
        count = 0
        for satellite in self.orbit:
            count += satellite.count_orbits(level + 1)

        return level + count

