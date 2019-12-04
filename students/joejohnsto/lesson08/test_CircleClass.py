# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 14:03:01 2019

@author: jjohnston

Pytest for Circle Class
"""
import CircleClass as cc
import math as m
import pytest


def test_radius():
    """Test if radius is an attribute of circle"""
    c = cc.Circle(4)
    print(c.radius)
    assert c.radius == 4


def test_diameter():
    """Test if diameter is an attribute of circle"""
    c = cc.Circle(4)
    print(c.diameter)
    assert c.diameter == 8


def test_diameter_set():
    """Test that diameter can be set and radius will change appropriately"""
    c = cc.Circle(4)
    c.diameter = 6
    assert c.diameter == 6
    assert c.radius == 3


def test_area():
    """Test that area is a read-only property of circle"""
    c = cc.Circle(4)
    assert c.area == m.pi * 16
    with pytest.raises(AttributeError):
        c.area = 20


def test_fromDiameter():
    c = cc.Circle.fromdiameter(8)
    assert c.diameter == 8


def test_print():
    c = cc.Circle(4)
    assert str(c) == f'Circle with radius: {c.radius}'


def test_repr():
    c = cc.Circle(4)
    assert repr(c) == 'Circle(4)'


def test_add():
    c = cc.Circle(4)
    d = cc.Circle(2)
    e = c + d
    assert repr(e) == 'Circle(6)'


def test_multiply():
    c = cc.Circle(4)
    d = c * 2
    assert repr(d) == 'Circle(8)'


def test_compare():
    c = cc.Circle(4)
    d = cc.Circle(6)
    c2 = cc.Circle(4)
    assert c < d
    assert c <= d
    assert d > c
    assert d >= c
    assert c != d
    assert c == c2


def test_sort():
    circles = [cc.Circle(6), cc.Circle(7), cc.Circle(8), cc.Circle(4),
               cc.Circle(0), cc.Circle(2), cc.Circle(3), cc.Circle(5),
               cc.Circle(9), cc.Circle(1)]
    circles.sort()
    assert repr(circles[3]) == 'Circle(3)'


def test_reflect():
    c = cc.Circle(4)
    d = c * 2
    e = 2 * c
    assert d == e


def test_aug_assign():
    c = cc.Circle(4)
    d = cc.Circle(6)
    c += d
    assert repr(c) == 'Circle(10)'
    c *= 2
    assert repr(c) == 'Circle(20)'


# Tests for Sphere subclass
def test_sphere():
    s = cc.Sphere(4)
    assert s.radius == 4


def test_volume():
    s = cc.Sphere(4)
    assert s.volume == 4**3 * (4/3) * m.pi


def test_sphere_area():
    s = cc.Sphere(4)
    assert s.area == 4**2 * 4 * m.pi


def test_print_sphere():
    s = cc.Sphere(4)
    assert str(s) == f'Sphere with radius: {s.radius}'


def test_repr_sphere():
    s = cc.Sphere(4)
    assert repr(s) == 'Sphere(4)'


def test_s_fromDiameter():
    s = cc.Sphere.fromdiameter(8)
    assert s.diameter == 8
    assert repr(s) == f'Sphere({s.radius})'


def test_s_add():
    c = cc.Sphere(4)
    d = cc.Sphere(2)
    e = c + d
    assert repr(e) == 'Sphere(6)'


def test_s_multiply():
    c = cc.Sphere(4)
    d = c * 2
    assert repr(d) == 'Sphere(8)'


def test_s_compare():
    c = cc.Sphere(4)
    d = cc.Sphere(6)
    c2 = cc.Sphere(4)
    assert c < d
    assert c <= d
    assert d > c
    assert d >= c
    assert c != d
    assert c == c2


def test_s_sort():
    spheres = [cc.Sphere(6), cc.Sphere(7), cc.Sphere(8), cc.Sphere(4),
               cc.Sphere(0), cc.Sphere(2), cc.Sphere(3), cc.Sphere(5),
               cc.Sphere(9), cc.Sphere(1)]
    spheres.sort()
    assert repr(spheres[3]) == 'Sphere(3)'
