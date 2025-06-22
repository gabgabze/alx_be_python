class Shape:

    @staticmethod
    def area(self):
        return NotImplementedError

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.area = self.radius * self.radius



