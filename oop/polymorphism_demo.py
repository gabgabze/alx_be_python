import math
class Shape:

    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    """override the area method"""
    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    """override the area method"""
    def area(self):
        return math.pi * self.radius ** 2
