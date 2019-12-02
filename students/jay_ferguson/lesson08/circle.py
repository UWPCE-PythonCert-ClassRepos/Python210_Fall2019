#!/usr/bin/env python3

from math import pi, sqrt
from functools import total_ordering

@total_ordering
class Circle():

    def __init__(self, radius):

        if type(radius) != float and type(radius) != int:
            raise TypeError('Value must be of type int or float')

        self.radius = float(radius)


    @property
    def diameter(self):

        return 2 * self.radius


    @diameter.setter
    def diameter(self, diameter):

        self.radius = diameter / 2


    @property
    def area(self):
        """Calculate area property."""

        return pi * (self.radius ** 2)


    @classmethod
    def from_diameter(cls, diameter):
        """Build Circle object given diameter"""

        return cls(diameter / 2)


    def __eq__(self, other):
        return self.area == other.area


    def __lt__(self, other):

        return self.area < other.area


    def __add__(self, other):

        if type(other) == int or type(other) == float:
            return Circle(self.radius + other)

        else:
            return Circle(self.radius + other.radius)

    def __radd__(self, other):

        return self.__add__(other)


    def __mul__(self, other):

        return Circle(self.radius * other)


    def __rmul__(self, other):

        return self.__mul__(other)


    def __str__(self):

        return f'Circle with radius: {self.radius}'

    def __repr__(self):

        return f'Circle({self.radius})'


class Sphere(Circle):

    @property
    def volume(self):

        return (4 / 3 * pi * self.radius ** 3)


    @property
    def area(self):

        return (4 * pi * self.radius ** 2)


    def __str__(self):

        return f'Sphere with radius {self.radius}'


    def __repr__(self):

        return f'Sphere({self.radius})'

