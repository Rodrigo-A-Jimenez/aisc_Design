from fractions import Fraction

def netArea(area, holesArea):
    return area - holesArea

def holesAreas(numbers, diameterer, thick):
    return numbers*(diameterer + 1/8)*thick

def diagonalHole(gageSpace, pitchSpace):
    return gageSpace**2/(4*pitchSpace)

class Bolt():
    def __init__(self, diameter,width_bolt_hole=1/16, positionX = 0, positionY = 0) -> None:
        self.__diameter = Fraction(diameter).limit_denominator()
        self.__width_bolt_hole = Fraction(width_bolt_hole).limit_denominator()
        self.__hole_diameter = self.__diameter + 2*self.__width_bolt_hole
        self.__positionX = positionX
        self.__positionY = positionY
    
    @property
    def diameter(self):
        return self.__diameter   
    @property
    def hole_diameter(self):
        return self.__hole_diameter
    
    @property
    def positionX(self):
        return self.__positionX
    
    @property
    def positionY(self):
        return self.__positionY

class Section():
    def __init__(self, width, thick, holes = []) -> None:
        self.__width = width
        self.__thick = thick
        self.__holes = holes
        