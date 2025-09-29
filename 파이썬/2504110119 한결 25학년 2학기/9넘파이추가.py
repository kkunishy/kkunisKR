import math

class CIrcle:
    def __init__(self,radius=0):
        self.__radius=radius

    def get_radius(self):
        return self.__radius

    def set_radius(self,radius):
        self.__radius=radius

    def get_area(self):
        return math.pi*self.__radius**2

    def get_perimeter(self):
        return 2*math.pi*self.__radius

c1=CIrcle(7)
print(math.pi)
print(c1.get_area())
print(c1.get_perimeter())
c1.set_radius(10)
print(c1.get_area())
print(c1.get_perimeter())
