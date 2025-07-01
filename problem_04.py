"""Q1: Create a class Shape with a method area(). Then create two child classes Rectangle and Circle that inherit from Shape and override the area() method"""


class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Usage
r = Rectangle(10, 5)
print("Rectangle Area:", r.area())

c = Circle(7)
print("Circle Area:", c.area())
