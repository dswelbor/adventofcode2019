from aoc2019.day_six.planetary_composite import CentralMassComposite, \
    SatelliteLeaf


class PlanetaryBuilder:
    """
    This class is an implementation of builder - a creational design pattern.
    It builds a tree of PlanetaryComponents.
    """
    def __init__(self):
        self.roots = []
        self.planets = {}
        # self.rev_planets = {}

    def add_orbit(self, central, satellite):
        """
        This method populates a dictionary of orbiting entities to be built
        into a tree later.
        """
        # add new root
        if central not in self.roots:
            self.roots.append(central)

        # remove non-root from list
        if satellite in self.roots:
            self.roots.remove(satellite)

        # add the satellite if it doesn't already exist
        if satellite not in self.planets:
            # init new key-value pair with empty value list
            self.planets[satellite] = []

        try:
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
                central_mass.satellites.append(satellite)

        # populate list of root components
        root_components = []
        for root in self.roots:
            root_components.append(components[root])
        return root_components
