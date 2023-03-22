from V import V

class Magnus:
    """
    Provide the constants for the gravity force

    :param airResistance: The air resistance
    :param intialSpin: Intital angular momentum in rad/s
    :param spinAttrition: Attrition of spin in rad/s
    """
    def __init__(self, airResistance, initialSpin, spinAttrition=0, dt=0):
        self.aR = airResistance
        self.spinAttrition = spinAttrition
        self.spin = initialSpin
        self.dt = dt

    """
    Return the force applicable to the object based off of already defined constants 
    (g)

    and changing values (none in this case)
    """
    def get(self, velocity, wind, spin=None):
        if spin != None:
            self.spin = spin

        # calculate force
        windSpeed = (velocity - wind)
        force = self.aR * (windSpeed / self.spin)

        # apply attrition
        self.spin = self.spin - self.spinAttrition * self.dt

        if self.spin.m < 0:
            self.spin = 0

        return force