from aoc2019.day_six.planetary_composite import CentralMassComposite, SatelliteLeaf


class PlanetaryBuilder:
    """
    This class is an implementation of builder - a creational design pattern. It
    builds a tree of PlanetaryComponents.
    """
    def __init__(self):
        self.root = None
        self.planets = {}
        self.rev_planets = {}

    def add_orbit(self, central, satellite):
        """
        This method populates a dictionary of orbiting entities to be built
        into a tree later.
        """
        # set new root
        if self.root is None or satellite == self.root:
            self.root = central

        # add the satellite if it doesn't already exist
        if satellite not in self.planets:
            self.planets[satellite] = []  # init new pair with empty value list

        try:
            # self.planets[central] = list(set(self.planets[central].append(satellite)))
            self.planets[central].append(satellite)
        except KeyError:
            self.planets[central] = []
            self.planets[central].append(satellite)

    def build(self):
        """
        This method builds a tree of PlanetaryComponents from the added orbit
        relations.
        """
        # Create composite and leaf components
        components = {}
        for key in self.planets:
            # leaf
            if len(self.planets[key]) == 0:  # 'is' might be a buggy section
                components[key] = SatelliteLeaf(key)
            # composite
            else:
                components[key] = CentralMassComposite(key)

        # add children to composites
        for key in self.planets:
            # iterate through each satellite
            for satellite_name in self.planets[key]:
                # add relation to central mass
                central_mass = components[key]
                satellite = components[satellite_name]
                # components[key].orbit.append()
                central_mass.orbit.append(satellite)

        return components[self.root]
