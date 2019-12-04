# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 13:56:17 2019

@author: jjohnston

Lesson 08 Circle Class Exercise
"""

import math
from functools import total_ordering


@total_ordering
class Circle:
    """A class object which defines a circle"""

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
        return math.pi * self.radius**2

    @classmethod
    def fromdiameter(cls, diameter):
        return cls(diameter / 2)

    def __str__(self):
        return f'Circle with radius: {self.radius}'

    def __repr__(self):
        return f'Circle({self.radius})'

    def __add__(self, other):
        r = self.radius + other.radius
        return __class__(r)

    def __mul__(self, value):
        r = self.radius * value
        return Circle(r)

    def __rmul__(self, value):
        return self.__mul__(value)

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius


class Sphere(Circle):
    """Subclass of Circle which defines a Sphere"""

    @property
    def area(self):
        """Return the surface area of the sphere"""
        return 4 * super().area

    @property
    def volume(self):
        return (4/3) * math.pi * self.radius**3

    def __str__(self):
        return f'Sphere with radius: {self.radius}'

    def __repr__(self):
        return f'Sphere({self.radius})'

    def __add__(self, other):
        r = self.radius + other.radius
        return Sphere(r)

    def __mul__(self, value):
        r = self.radius * value
        return Sphere(r)
