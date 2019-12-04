#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 18:43:13 2019

@author: kenclark
Class: Python 210A-Fall
Teacher: David Pokrajac, PhD
Assignment -
"""

from math import pi
import functools
import math

"""
The goal is to create a class that represents a simple circle.

Other abilities of a Circle instance:

Compute the circle’s area.
Print the circle and get something nice.
Be able to add two circles together.
Be able to compare two circles to see which is bigger.
Be able to compare to see if they are are equal.
(follows from above) be able to put them in a list and sort them.

"""


class Circle(object):

    def __init__(self, radius):
        """
        Initiates the class Circle.
        """
        self.radius = float(radius)
#        self.perimeter = 2*self.radius*pi

    def __repr__(self):
        """
        Print circle details.
        """
        return ('Circle with radius: {0:.2f} and area of: {1:.2f}'
                .format(self.radius, self.area))

    def __str__(self):
        """
        Print circle details in string form.
        """
        return ('Circle with radius: {0:.2f} and area of: {1:.2f}'
                .format(self.radius, self.area))

    @classmethod
    def from_d(cls, diameter):
        """
        Generates diameter.
        """
        return cls(diameter / 2)

    @property
    def diameter(self):
        """
        Generates radius from usr entered diameter.
        """
        return 2*self.radius

    @diameter.setter
    def diameter(self, value):
        """
        Setter for usr entered diameter
        """
        self.radius = value / 2.0

    @property
    def area(self):
        """
        Determines area of circle using radius
        """
        return self.radius**2*pi

    def __add__(self, other):
        """
        Add circles
        """
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        """
        Multiply with other
        """
        return Circle(self.radius * other)

    def __rmul__(self, other):
        """
        Multiply circle with other if first input not circle
        """
        return Circle(self.radius * other)

    def __eq__(self, other):
        """
        Compare if circle == to other circle
        """
        return self.radius == other

    def __lt__(self, other):
        """
        Compare if circle less than other
        """
        return self.radius < other

    def __gt__(self, other):
        """
        Compare if circle greater than other
        """
        return self.radius > other



#def list_circles(self):
        """
        Trying to create list of circles - Dosnt work!!!
        """
#    c_list = []
#    for i in Circle:
#        c_list.append(i)
#        print(c_list)


circle_01 = Circle(8)
circle_02 = Circle(10)


#print(circle_01.area)

# Test add circles
#print(circle_01.__add__(circle_02)