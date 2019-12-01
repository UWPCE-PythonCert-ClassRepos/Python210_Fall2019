"""
Eric Gosnell
Lesson 08 - Test the Circle class
11.25.2019
"""

from circle import Circle, Sphere

if __name__ == "__main__":

    # Test derived attributes return correct values
    c11 = Circle(110)
    assert c11.diameter == 220
    assert int(c11.area) == 38013

    # Test change to radius results in updated diameter
    c11.radius = 55
    assert c11.diameter == 110

    # Test change to diameter results in updated radius
    c11.diameter = 100
    assert c11.radius == 50

    # Test alternate constructor
    c12 = Circle.from_diameter(300)
    assert c12.radius == 150
    assert int(c12.area) == 70685

    # Test str and repr
    assert c11.__str__() == "Circle(50.0)"
    assert c12.__repr__() == "Circle(150.0)"

    # Test numeric protocols
    assert c11 + c12 == Circle(200)
    assert c12 - c11 == Circle(100)
    assert c11 * c12 == Circle(7500)
    assert c12 / c11 == (Circle(3))
    assert c11 * 5 == Circle(250)
    assert c12 + 50 == Circle(200)
    assert c12 - 25 == Circle(125)
    assert c12 / 50 == Circle(3)

    # Test comparison operators
    assert c11 < c12
    assert c12 > c11
    assert c12 != c11
    c11.radius = 150
    assert c11 == c12

    # Test sorting
    c1 = Circle(10)
    c2 = Circle(20)
    c3 = Circle(30)
    c4 = Circle(40)
    c5 = Circle(50)
    c6 = Circle(60)
    c7 = Circle(70)
    c8 = Circle(80)
    c9 = Circle(90)
    c10 = Circle(100)
    circles = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

    assert circles[0] == c1
    assert circles[-1] == c10

    circles.sort(key=Circle.sort_key, reverse=True)

    assert circles[0] == c10
    assert circles[-1] == c1

    # Test reflection
    assert c6 * 20 == 20 * c6

    # Test augmentation
    assert c11 == Circle(150)
    assert c12 == Circle(150)
    c11 += c12
    assert c11 == Circle(300)
    c11 *= c12
    assert c11 == Circle(45000)

    # Test Sphere subclass additional derived attributes
    s1 = Sphere(10)
    assert int(s1.volume) == 4188
    assert int(s1.area) == 1256  # override Circle area property

    # Test alternate constructor
    s2 = Sphere.from_diameter(20)
    assert s2.radius == 10

    # Test str and repr reflect Sphere subclass
    s1.diameter = 100
    s2.diameter = 200
    assert s1.__str__() == "Sphere(50.0)"
    assert s2.__repr__() == "Sphere(100.0)"
