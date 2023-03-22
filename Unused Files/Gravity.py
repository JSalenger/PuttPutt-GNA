from V import V

class Gravity:
    """
    Provide the constants for the gravity force

    :param g: The acceleration due to gravity
    :param mass: The mass of the object gravity is acting on
    """
    def __init__(self, g, mass):
        self.g = g
        self.mass = mass

    """
    Return the force applicable to the object based off of already defined constants 
    (g)

    and changing values (none in this case)
    """
    def get(self):
        return V(0, self.g*self.mass, 0)
