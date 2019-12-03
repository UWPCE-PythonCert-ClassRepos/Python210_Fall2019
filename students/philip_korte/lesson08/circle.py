#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 15:58:50 2019

@author: philipkorte
"""
from math import pi, sqrt
from functools import total_ordering


circles = []
@total_ordering #To enable ordering
class Circle:

    def __init__(self, radius):
        self._radius = radius
        circles.append(self)

    def __str__(self):
        return f"Circle with radius {self._radius}"

    def __repr__(self):
        return f'Circle({self._radius})'

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        self._radius = value / 2

    @property
    def area(self):
        return pi * self._radius**2

#   This was a mistake, we don't want the user to be able to set this.
#    @area.setter
#    def area(self, value):
#        self._radius = sqrt(value/pi)

    @classmethod
    def from_diameter(cls, value):
        return cls(value/2)

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self._radius + other._radius)
        elif isinstance(other, float) or isinstance(other, int):
            return Circle(self._radius + other)

    def __radd__(self, other):
        return Circle(self._radius + other)

    def __mul__(self, other):
        if isinstance(other, Circle):
            return Circle(self._radius * other._radius)
        elif isinstance(other, float) or isinstance(other, int):
            return Circle(self._radius * other)

    def __rmul__(self, other):
        return Circle(self._radius * 3)

    def __eq__(self, other):
        return self.radius == other.radius

    def  __lt__(self, other):
        return self.radius < other.radius

class Sphere(Circle):

    def __str__(self):
        return f"Sphere with radius {self._radius}"

    def __repr__(self):
        return f'Sphere({self._radius})'

    @property
    def volume(self):
        return (4/3) * pi * self._radius**3

    @property
    def area(self):
        return 4 * pi * self._radius**2






