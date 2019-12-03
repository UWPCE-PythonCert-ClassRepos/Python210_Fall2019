import math
from circle import Circle, Sphere
import pytest

# Test Circle Class
def test_circle_area():
    c1 = Circle(10)
    assert 314.16 == round(c1.area, 2)


def test_circle_print_string():
    c1 = Circle(10)
    assert "Circle with Radius: 10 Diameter: 20 Area: 314.1592653589793" == str(c1)


def test_circle_representation_string():
    c1 = Circle(10)
    assert "Circle(10)" == repr(c1)


def test_circle_alternate_constructor():
    c1 = Circle.from_diameter(10)

    assert c1.radius == 5
    assert c1.diameter == 10


def test_add_circles():
    c1 = Circle(1)
    c2 = Circle(3)

    assert c1+c2 == Circle(4)
    assert c1+2 == Circle(3)
    assert 5+c1 == Circle(6)

def test_mul_circles():
    c1 = Circle(2)

    assert c1*5 == Circle(10)
    assert 20*c1 == Circle(40)


def test_compare_circle_size():
    c1 = Circle(2)
    c2 = Circle(3)

    assert (c1 == c2) is False
    assert (c1 < c2) is True
    assert (c1 > c2) is False


def test_circle_sort():
    c_list = [Circle(4), Circle(2), Circle(1), Circle(3)]
    c_list.sort()
    assert c_list == [Circle(1), Circle(2), Circle(3), Circle(4)]


# Test Sphere subclass
def test_sphere_area():
    s1 = Sphere(10)
    assert s1.area == 1256.6370614359173


def test_sphere_volume():
    s1 = Sphere(10)
    assert s1.volume == 4188.790204786391


def test_sphere_string():
    s1 = Sphere(10)
    assert str(s1) == "Sphere with Radius: 10 Diameter: 20 Area: 1256.6370614359173 Volume: 4188.790204786391"


def test_sphere_representation_string():
    s1 = Sphere(10)
    assert repr(s1) == 'Sphere(10)'


if __name__ == "__main__":
    pytest.main([__file__])