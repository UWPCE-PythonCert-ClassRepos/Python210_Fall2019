# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:38:50 2019

@author: tdietz
"""
from functools import total_ordering

@total_ordering
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def diameter(self):
        return int(self.radius * 2)        
    
    @diameter.setter
    def diameter(self, d):        
        self.radius = int(d/2)
    
    @property
    def area(self):
        import math
        return math.pi * self.radius**2

    @classmethod
    def from_diameter(cls,d):
        if (d % 2) == 0:
            return cls(int(d/2))
        else:
            print("Diameter is not a multiple of 2, please reenter")
    
    def __str__(self):
        return "Circle with radius: {:f}".format(self.radius)
    
    def __repr__(self):
        return "Circle({:d})".format(self.radius)
    
    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        else:
            print("Two objects are not the same type, please choose another obj")
            
    def __radd__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        else:
            print("Two objects are not the same type, please choose another obj")
            
    def __mul__(self,other):
        if isinstance(other, Circle):
            return
        else:
            return Circle(self.radius * other)
    
    def __rmul__(self,other): 
        return Circle(self.radius * other)
    
    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius
    
class Sphere(Circle):
    def __init__(self, radius):
        self.radius = radius
    
    #formula for volume of a sphere
    @property
    def volume(self):
        import math
        return 4*math.pi*((self.radius**3)/3)
    
    #formula for surface area of a sphere
    @property
    def area(self):
        import math
        return 4*math.pi*self.radius**2
    
    def __str__(self):
        return "Sphere with a radius of: {:f}".format(self.radius)
    
    def __repr__(self):
        return "Sphere({:d})".format(self.radius)
    
    
    
    
    