#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 19:46:00 2019

@author: philipkorte
"""

from circle import *
import pytest

def test_init():
    """Test that the Circle can be initialized"""
    c = Circle(4)

def test_radius():
    c = Circle(4)
    assert c.radius == 4
    c.radius = 5
    assert c.radius == 5
    assert c.diameter == 10

def test_diameter():
    c = Circle(4)
    assert c.diameter == 8
    c.diameter = 10
    assert c.diameter == 10
    assert c.radius == 5

def test_area():
    c = Circle(4)
    test_area = pi*4**2
    assert c.area == test_area
    with pytest.raises(AttributeError):
        c.area = 25

def test_from_diameter():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4

def test_str():
    c = Circle(4)
    assert str(c) == "Circle with radius 4"

def test_repr():
    c = Circle(4)
    assert repr(c) == "Circle(4)"

def test_add():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = c1 + c2
    assert repr(c3) == "Circle(6)"
    c4 = c1 + 5
    assert repr(c4) == "Circle(7)"
    c5 = 5 + c1
    assert repr(c5) == "Circle(7)"

def test_multiply():
    c = Circle(3)
    assert repr(c * 3) == "Circle(9)"
    assert repr(3 * c) == "Circle(9)"
    c2 = Circle(4)
    assert repr(c * c2) == "Circle(12)"

def test_equal():  # how do you test comparisons?
    c1 = Circle(4)
    c2 = Circle(4)
    c3 = Circle(5)
    assert c1 == c2
    assert repr(c1) != repr(c3)

def test_less_than():
    c1 = Circle(4)
    c2 = Circle(3)
    assert repr(c2) < repr(c1)

#def test_circles_list(): # I can't seem to get this test to work
#    circles = []
#    c1 = Circle(3333)
#    c2 = Circle(1111)
#    c3 = Circle(2222)
#    circles.sort()
#    assert circles == [Circle(144), Circle(244), Circle(344)]

def test_Sphere():
    s1 = Sphere(4)
    s2 = Sphere.from_diameter(4)
