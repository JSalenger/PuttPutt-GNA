from V import V

class Drag:
    """
    Provide the constants for the drag force

    :param rho: density of the fluid
    :param Cd: coefficient of drag
    :param A: front facing area
    """
    def __init__(self, rho, Cd, A):
        self.rho = rho
        self.Cd = Cd
        self.A = A

    """
    Return the force applicable to the object based off of already defined constants (rho, Cd, A) and changing values (velocity)
    
    :param velocity: velocity of the object
    :param airSpeed: speed of the air
    :returns: the drag force opposite to velocity
    """
    def get(self, velocity, wind):
        airSpeed = (velocity - wind) # V (it is a vector even though it is a "speed")
        # air drag is opposite the velocity of the ball relative to the ground
        return airSpeed(.5 * self.rho * (airSpeed.m * airSpeed.m) * self.Cd * self.A) * -1