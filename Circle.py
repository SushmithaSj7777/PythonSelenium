import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area_of_circle(self):
        area = 2 * math.pi * self.radius ** 2
        print("Area of circle is %s" % area)

    def perimeter_of_circle(self):
        perimeter = 2 * math.pi * self.radius
        print("perimeter of circle is %s" % perimeter)


radius = float(input("Enter the radius of the circle"))
c = Circle(radius)
c.area_of_circle()
c.perimeter_of_circle()
