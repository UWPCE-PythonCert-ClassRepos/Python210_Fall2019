import unittest
from .circle import *


class MyTestCase(unittest.TestCase):

    def test_radius(self):
        c = Circle(4)
        self.assertEqual( c.radius, 4)

    def test_diameter(self):
        c = Circle(4)
        self.assertEqual(c.diameter, 8)
        c.diameter = 2
        self.assertEqual(c.diameter, 2)
        self.assertEqual( c.radius, 1)

    def test_area(self):
        c = Circle(2)
        self.assertEqual(c.area, 12.566370)

        with self.assertRaises(AttributeError):
            c.area = 42

    def test_from_diameter(self):
        c = Circle.from_diameter(8)
        self.assertEqual(c.diameter, 8)
        self.assertEqual(c.radius, 4)


    def test_print(self):
        c = Circle(4)
        self.assertEqual(str(c), "Circle with radius: 4")
        self.assertEqual(repr(c), "Circle(4)")
        print(c.__repr__())


    def test_add(self):
        c1 = Circle(2)
        c2 = Circle(4)
        c3 = c1 + c2
        self.assertEqual(c3.radius, 6)


if __name__ == '__main__':
    unittest.main()
