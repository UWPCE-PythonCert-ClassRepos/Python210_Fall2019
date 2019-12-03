import math
from functools import total_ordering

@total_ordering
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return round((math.pi * self.radius ** 2), 5)

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)

    def __str__(self):
        return 'Circle with radius: {:.6f}'.format(self.radius)

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        elif type(other) is int or float:
            return Circle(self.radius + other)

    def __radd__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        elif type(other) is int or float:
            return Circle(self.radius + other)

    def __sub__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius - other.radius)
        elif type(other) is int or float:
            return Circle(self.radius - other)

    def __rsub__(self, other):
        if isinstance(other, Circle):
            return Circle(other.radius - self.radius)
        elif type(other) is int or float:
            return Circle(other - self.radius)

    def __mul__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius * other.radius)
        elif type(other) is int or float:
            return Circle(self.radius * other)

    def __rmul__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius * other.radius)
        elif type(other) is int or float:
            return Circle(self.radius * other)

    def __truediv__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius / other.radius)
        elif type(other) is int or float:
            return Circle(self.radius / other)

    def __rtruediv__(self, other):
        if isinstance(other, Circle):
            return Circle(other.radius / self.radius)
        elif type(other) is int or float:
            return Circle(other / self.radius)

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius


class Sphere(Circle):

    def __str__(self):
        return 'Sphere with radius: {:.6f}'.format(self.radius)

    def __repr__(self):
        return 'Sphere({})'.format(self.radius)

    @property
    def volume(self):
        return round(((4 / 3) * math.pi * self.radius ** 3), 5)

    @property
    def area(self):
        return round((4 * math.pi * self.radius ** 2), 5)
