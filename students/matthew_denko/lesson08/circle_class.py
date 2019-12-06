#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 20:31:25 2019

@author: matthewdenko
"""

# assignment description ------------------------------------------------------

"""Goal:

The goal is to create a class that represents a simple circle.

A Circle can be defined by either specifying the radius or the diameter, and the user can query the circle for either its radius or diameter.

Other abilities of a Circle instance:

Compute the circle’s area.
Print the circle and get something nice.
Be able to add two circles together.
Be able to compare two circles to see which is bigger.
Be able to compare to see if they are are equal.
(follows from above) be able to put them in a list and sort them."""

# importing packages ----------------------------------------------------------

from math import pi
from functools import total_ordering

# base circle information -----------------------------------------------------

circles = []
@total_ordering

# defining circle class -------------------------------------------------------

class Circle:
    "creating class to create a circle"
    
    def __init__(self, radius):
        "defining _init_ parameters"
        self._radius = radius
        circles.append(self)

    def __repr__(self):
        return f'Circle({self._radius})'
    
    def __str__(self):
        return f"Circle with radius {self._radius}"

    @property
    def radius(self):
        "defining radius"
        return self._radius

    @radius.setter
    def radius(self, value):
        "defining radius setter"
        self._radius = value

    @property
    def diameter(self):
        "defining diameter"
        "diameter is equal to twice the length of radiu"
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        "defining diameter setter"
        self._radius = value / 2

    @property
    def area(self):
        "defining aread of circle"
        return pi * self._radius**2

    @classmethod
    def from_diameter(cls, value):
        "defining the distance from the diameter given a circle"
        return cls(value/2)

    def __create__(self, other):
        "defining a method to be able to add additional circles if needed"
        if isinstance(other, Circle):
            return Circle(self._radius + other._radius)
        elif isinstance(other, float) or isinstance(other, int):
            return Circle(self._radius + other)

    def __eq__(self, other):
        "defining function to test if one circle is equal to another"
        return self.radius == other.radius

    def __mul__(self, other):
        "function to evaluate whether data is of correct type - if not return as int"
        if isinstance(other, Circle):
            return Circle(self._radius * other._radius)
        elif isinstance(other, float) or isinstance(other, int):
            return Circle(self._radius * other)

    def __rmul__(self, other):
        "defining function to multiply one radius to itself"
        return Circle(self._radius * 3)

    def  __lt__(self, other):
        "defining function to test if one circle is less than or equal to another"
        return self.radius < other.radius
    
    def __radd__(self, other):
        "defining function to add one radius to itself"
        return Circle(self._radius + other)

# defining sphere class -------------------------------------------------------
        
class Sphere(Circle):
    "creating class for a sphere based on input of circle"

    def __str__(self):
        "defining the structure of the sphere"
        return f"Sphere with radius {self._radius}"

    def __repr__(self):
        "defining the radisu of the sphere"
        return f'Sphere({self._radius})'

    @property
    def volume(self):
        "defining the voulme of the sphere"
        return (4/3) * pi * self._radius**3

    @property
    def area(self):
        "defining the area of a sphere"
        return 4 * pi * self._radius**2
    
# testing results -------------------------------------------------------------

"radius"
c = Circle(4)
print(c.radius)

"diameter"
c = Circle(4)
print(c.diameter)

"area"    
c = Circle(2)
print(c.area)

"from diameter"
c = Circle.from_diameter(8)
print(c.diameter)
print(c.radius)

"evaluation"
d = eval(repr(c))
print(d)

"multiplication"
c3 = c * 3
print(c3)

"comparing circles"
print(c > c3)

"sorting circles"
circles.sort()

