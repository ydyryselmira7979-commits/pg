import math

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return round(self.width * self.height, 1)


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 1)

    def __str__(self):
        return f"{self.shape_name} shape with a radius of {self.radius} has an area of {self.area()}"
