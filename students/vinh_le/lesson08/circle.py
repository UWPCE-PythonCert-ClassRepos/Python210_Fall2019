import math

from functools import total_ordering


@total_ordering
class Circle:
    def __init__(self, radius):
        self.radius = radius


    @property
    def diameter(self):
        return self.radius*2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter/2

    @property
    def area(self):
        return math.pi*self.radius**2

    @classmethod
    def from_diameter(cls, diameter):
        if isinstance(diameter, int) or isinstance(diameter, float):
            return cls(diameter/2)

    def __str__(self):
        return "Circle with Radius: {} Diameter: {} Area: {}".format(self.radius, self.diameter, self.area)

    def __repr__(self):
        return "Circle(" + str(self.radius) + ")"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        elif isinstance(other, int) or isinstance(other, float):
            return Circle(self.radius + other)

    def __radd__(self, other):
        return Circle(other + self.radius)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Circle(self.radius * other)

    def __rmul__(self, other):
        return Circle(other * self.radius)

    def __eq__(self, other):
        return self.radius == other.radius

    def __gt__(self, other):
        return self.radius > other.radius
    #
    # def __lt__(self, other):
    #     return self.radius < other.radius


class Sphere(Circle):

    @property
    def area(self):
        return 4*math.pi*self.radius**2

    @property
    def volume(self):
        return (4/3)*math.pi*self.radius**3

    def __str__(self):
        return "Sphere with Radius: {} Diameter: {} Area: {} Volume: {}".format(self.radius, self.diameter,
                                                                                self.area, self.volume)

    def __repr__(self):
        return "Sphere(" + str(self.radius) + ")"



if __name__ == "__main__":
    circ1 = Circle(10)

    print(circ1.radius)
    print(circ1.diameter)
    circ1.diameter = 4
    print(circ1.radius)
    print(circ1.area)

    c2 = Circle.from_diameter(20)

    print(c2.radius)


