"""
Eric Gosnell
Lesson 08 - Circle Class
11.25.2019
"""

from functools import total_ordering
from math import pi


@total_ordering
class Circle:
    """Circle shape class with typical geometric attributes"""

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    def __init__(self, radius):
        self._radius = radius

    def __repr__(self):
        return f'{self.__class__.__name__}({self.radius})'

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __add__(self, other):
        try:
            return Circle(self.radius + other.radius)
        except AttributeError:
            return Circle(self.radius + other)

    def __sub__(self, other):
        try:
            return Circle(self.radius - other.radius)
        except AttributeError:
            return Circle(self.radius - other)

    def __mul__(self, other):
        try:
            return Circle(self.radius * other.radius)
        except AttributeError:
            return Circle(self.radius * other)

    def __truediv__(self, other):
        try:
            return Circle(self.radius / other.radius)
        except AttributeError:
            return Circle(self.radius / other)

    def __radd__(self, other):
        try:
            return Circle(self.radius + other.radius)
        except AttributeError:
            return Circle(self.radius + other)

    def __rsub__(self, other):
        try:
            return Circle(self.radius - other.radius)
        except AttributeError:
            return Circle(self.radius - other)

    def __rmul__(self, other):
        try:
            return Circle(self.radius * other.radius)
        except AttributeError:
            return Circle(self.radius * other)

    def __rtruediv__(self, other):
        try:
            return Circle(self.radius / other.radius)
        except AttributeError:
            return Circle(self.radius / other)

    def __iadd__(self, other):
        try:
            return Circle(self.radius + other.radius)
        except AttributeError:
            return Circle(self.radius + other)

    def __isub__(self, other):
        try:
            return Circle(self.radius - other.radius)
        except AttributeError:
            return Circle(self.radius - other)

    def __imul__(self, other):
        try:
            return Circle(self.radius * other.radius)
        except AttributeError:
            return Circle(self.radius * other)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, val):
        if val > 0:
            self._radius = val
        else:
            raise ValueError("radius must be > 0")

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2

    @property
    def area(self):
        return self.radius ** 2 * pi

    def sort_key(self):
        return self.radius


class Sphere(Circle):
    """Sphere shape sub-class with additional geometric properties"""

    @property
    def volume(self):
        return self.radius ** 3 * pi * (4/3)

    @property   # override Circle class property
    def area(self):
        return self.radius ** 2 * pi * 4
