class CIrcle(Figure):
    def set_radius(self,radius):
        self.radius=radius
        self.area=3.14*radius**2
        self.perimeter=2*3.14*radius

class Rectangle(Figure):
    def __init__(self,10,10):

    def set_width(self,width):
        self.width=width
        self.area=width*self.height
        self.perimeter=2*self.height+2*width

    def set_height(self,height):
        self.height=height
        self.area=self.width*height
        self.perimeter=2*self.width+2*height

    def get_width(self):
        return self.get_width
    def get_height(self):
        return self.get_height


f1=Circle(7)
print(f1.get_are(),f1.get_perimeter())
f1.set_radius(10)
print(f1.get_are(),f1.get_perimeter())
print()

f2=Rectangle(5,4)
print(f2.get_are(),f2.get_perimeter())
print()