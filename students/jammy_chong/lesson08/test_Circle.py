import pytest
from Circle import Circle, Sphere

c = Circle(4)

def test_1():
    assert c.radius == 4

def test_2():
    assert c.diameter == 8

def test_3():
    c.diameter = 2
    assert c.diameter == 2
    assert c.radius == 1

def test_4():
    c = Circle(2)
    assert c.area == 12.566370
    with pytest.raises(AttributeError):
        c.area = 2

def test_5():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4

def test_6():
    c = Circle(4)
    assert str(c) == "Circle with radius: 4.000000"
    assert (repr(c)) == 'Circle(4)'
    assert eval(repr(c)) == Circle(4)

def test_7():
    c1 = Circle(2)
    c2 = Circle(4)
    assert (c1 + c2) == Circle(6)
    assert (c2 * 3) == Circle(12)
    assert (3 * c2) == Circle(12)

def test_8():
    c1 = Circle(2)
    c2 = Circle(4)
    assert (c1 > c2) is False
    assert (c1 < c2) is True
    assert (c1 == c2) is False
    c3 = Circle(4)
    assert (c2 == c3) is True
    circles = [Circle(9), Circle(4), Circle(1), Circle(3), Circle(2)]
    circles.sort()
    assert circles == [Circle(1), Circle(2), Circle(3), Circle(4), Circle(9)]

def test_8_Optional():
    c = Circle(4)
    assert (c * 3) == (3 * c)
    c += Circle(2)
    assert c == Circle(6)

def test_9():
    s1 = Sphere(2)
    s2 = Sphere.from_diameter(6)
    assert str(s1) == "Sphere with radius: 2.000000"
    assert (repr(s1)) == 'Sphere(2)'
    assert eval(repr(s1)) == Sphere(2)
