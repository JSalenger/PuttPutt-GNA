class RandomFuncDoesNotGenerateRealValues(Exception):
    def __init__(self, attrName):
        # What is super? This syntax bothers me... why does the constructor not go in the parenthesis like all other new class objs???
        self.message = "The random function for attribute " + str(attrName) + " produces None or non-compatible type."
        
        super().__init__(self.message)
        
class NotImplementedError(Exception):
    def __init__(self, attrName):
        # What is super? This syntax bothers me... why does the constructor not go in the parenthesis like all other new class objs???
        self.message = "The function for object property " + str(attrName) + " has not been defined"
        
        super().__init__(self.message)
    
    
