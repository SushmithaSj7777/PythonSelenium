import math


class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area_of_circle(self):
        area = 2 * math.pi * self.radius ** 2
        return area

    def perimeter_of_circle(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter


class Triangle(Shape):

    def __init__(self, base, height, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.height = height
        self.base = base

    def area_of_triangle(self):
        area = 0.5 * self.base * self.height
        return area

    def perimeter_of_triangle(self):
        perimeter = self.side1 * self.side2 * self.side3
        return perimeter


class Square(Shape):

    def __init__(self, s):
        self.s = s

    def area_of_square(self):
        area = self.s ** 2
        return area

    def perimeter_of_square(self):
        perimeter = 4 * self.s
        return perimeter


radius = float(input("Enter the radius of circle"))
C = Circle(radius)
area_of_circle = C.area_of_circle()
perimeter_of_circle = C.perimeter_of_circle()
print("area of circle %s and its perimeter is %s" % (area_of_circle, perimeter_of_circle))

T = Triangle(3, 5, 3, 3, 3)
print("area of triangle %s and its perimeter is %s" % (T.area_of_triangle(), T.perimeter_of_triangle()))

S = Square(3)
print("area of square %s and its perimeter is %s" % (S.area_of_square(), S.perimeter_of_square()))
