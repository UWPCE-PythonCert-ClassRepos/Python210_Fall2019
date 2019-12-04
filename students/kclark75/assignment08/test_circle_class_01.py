#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 19:34:56 2019

@author: kenclark
Class: Python 210A-Fall
Teacher: David Pokrajac, PhD
Assignment - 
"""

from circle_class_01 import Circle

import pytest

from math import pi

import random


def test_init():
    Circle(5)


def test_radius():
    circle_01 = Circle(5)

    assert circle_01.radius == 5

def test_diameter():
    circle_01 = Circle(5)
    
    assert circle_01.diameter == 10


def test_area():
    circle_01 = Circle(2)
    
    assert circle_01.area == pi * 4
    
    
def test_add():
    circle_01 = Circle(3)
    circle_02 = Circle(3)
    circle_03 = circle_01 + circle_02
    
    assert circle_03.radius == 6
    
    


if __name__ == '__main__':
    pytest.main()
    
    