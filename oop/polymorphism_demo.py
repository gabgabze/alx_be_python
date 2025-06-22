import math
class Shape:

    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    """override the area method"""
    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    """override the area method"""
    def area(self):
        return math.pi * self.radius ** 2
