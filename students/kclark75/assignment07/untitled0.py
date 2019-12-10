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

class Circle(object):

    def __init__(self, r):
        self.radius = r
        
    def area(self):
        return self.radius**2*pi
        
    def perimeter(self):
        return 2*self.radius*pi
    

circle_01 = Circle(8)
circle_02 = Circle(10)
print(circle_01.area())
print(circle_01.perimeter())

print(circle_02.area())
print(circle_02.perimeter())
        
        
