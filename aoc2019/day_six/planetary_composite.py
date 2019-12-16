class SatelliteLeaf:
    """This a class for satellite entities - such as planets"""
    def __init__(self, name):
        self.name = name

    def count_orbits(self):
        """
        This method returns the number of orbiting entities - 1 as it
        is a leaf.
         """
        return 1

    pass


class CentralMassComposite:
    """
    This class is a composite component for central mass entities - such as
    what planets orbit around.
    """
    def __init__(self, name):
        self.name = name
        self.orbit = []  # collection of orbiting entities

    def count_orbits(self):
        """
        This method returns recursively the number of all orbiting entities,
         both direct and indirect.
        """
        count = 0
        for satellite in self.orbit:
            count += satellite.count_orbits()

        return 1 + count
