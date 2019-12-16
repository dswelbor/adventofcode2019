class PlanetaryBuilder:
    """
    This class is an implementation of builder - a creational design pattern. It
    builds a tree of PlanetaryComponents.
    """
    def __init__(self):
        self.root = None
        self.planets = []

    def add_orbit(self, central, satellite):
        """
        This method populates a dictionary of orbiting entities to be built
        into a tree later.
        """
        try:
            self.planets[central].append(satellite)
        except AttributeError:
            self.planets[central] = []
            self.planets[central].append(satellite)

    def build(self):
        """
        This method builds a tree of PlanetaryComponents from the added orbit
        relations.
        """
        pass
