#!/usr/bin/env python3

import pytest

from circle import Circle, Sphere

c = Circle(10)


def test_radius():

    assert c.radius == 10

def test_raise_error():

    with pytest.raises(TypeError):
      c1 = Circle('bananas')

def test_diameter():

    assert c.diameter ==20


def test_diameter_setter():

    c.diameter = 10

    assert c.radius == 5
    assert c.diameter == 10

# Reset so we can keep using 10

    c.radius = 10
    assert c.radius == 10


def test_area():

    assert round(c.area, ndigits=4) == 314.1593


def test_area_setting():

    with pytest.raises(AttributeError):
        c.area = 100


def test_from_diameter():

    c1 = Circle.from_diameter(30)
    assert c1.radius == 15


def test_total_ordering():

    c1 = Circle(5)
    c2 = Circle.from_diameter(20)

    assert c1 < c
    assert c2 == c
    assert c > c1
    assert c >= c2
    assert c <= c2

def test_addition():

    c1 = Circle(5)
    c2 = Circle(10)
    c3 = Circle(15)

    assert c1 + c2 == c3
    assert c2 + c1 == c3

def test_muliplication():

    c1 = Circle(5)
    c2 = Circle(50)

    assert c1 * 10 == c2
    assert 10 * c1 == c2

def test_sphere():

    s = Sphere(5)

    assert round(s.volume, ndigits=4) == 523.5988

def test_sphere_area():

    s = Sphere(5)

    assert round(s.area, ndigits=4) == 314.1593
