import math

class V:
    """
    A 3 dimensional vector that encapsulates x, y, and z values
    and mimics built-in type behaviour through the use of magic functions
    
    :author: Jon Salenger
    """
    def __init__(self, x, y, z):
        """
        Initializes a V object from an x, y, and z values
        
        :param x: Magnitude of vector in X direction
        :param y: Magnitude of vector in Y direction
        :param z: Magnitude of vector in Z direction
        :type x,y,z: float or int
        """
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        
    @property
    def m(self):
        # calculates the superhypotenuse (magnitude) of the vector
        return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)
    
    def rotate(self, radians):
        # Perform a 2 dimensional rotation; return a new vector
        return V(self.x * math.cos(radians) + self.y * math.sin(radians), self.y * math.cos(radians) - self.x * math.sin(radians), 0)

    @property
    def norm(self):
        # accesses normalized version of self without actually mutating self
        return self(1)
    
    def _norm(self):
        """
        Scales self to 1 and mutates the object
        (denoted by the _)
        """
        normalized_vector = self(1)
        self.x = normalized_vector.x
        self.y = normalized_vector.y
        self.z = normalized_vector.z
        
    def __repr__(self):
        # formats the vector when printed to std out
        return '<%s, %s, %s>' % (self.x, self.y, self.z)
    
    def __add__(self, other):
        # run when + operator is used
        return V(self.x+other.x,self.y+other.y,self.z+other.z)
    
    def __iadd__(self, other):
        # all i... functions are meant to implement += or -= etc. operators
        return self.__add__(other)
    
    def __sub__(self, other):
        return V(self.x-other.x,self.y-other.y,self.z-other.z)
    
    def __isub__(self, other):
        return self.__sub__(other)
    
    def __mul__(self, other):
        if type(other) == int or type(other) == float: return V(self.x * other, self.y * other, self.z * other)
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def __rmul__(self, other):
        # Since multiplication is commutitive 3 * a is as valid as a * 3 meaning we need to implement a reverse mul dunder function
        # because 3.__mul__(a) will throw an error as a is an instance
        return self.__mul__(other)
    
    def __imul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, other):
        # both truediv and div are called depending on circumstance but they both do the same thing in this case
        # so __div__ just refers to this function
        if type(other) == float or type(other) == int: return V(self.x/other, self.y/other, self.z/other)
        return V(self.y*other.z - self.z*other.y, self.z*other.x - self.x*other.z, self.x*other.y - self.y*other.x)
    
    def __div__(self, other):
        # called when / is used in Py2
        return self.__truediv__(other)
    
    def __itruediv__(self, other):
        return self.__truediv__(other)
    
    def __neg__(self):
        # called when -vec is referenced (i.e. -a)
        return self.__mul__(-1)
    
    def __call__(self, scale=1):
        """
        Scales vector to magnitude 'scale'
        
        :param scale: scale of vector to be returned
        :type scale: float or int
        """ 
        
        # scales the vector; if called without an argument it just returns the vector object itself
        return self.__mul__(scale/self.m)
