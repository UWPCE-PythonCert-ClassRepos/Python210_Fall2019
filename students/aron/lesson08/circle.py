import math



class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls( diameter / 2)

    #Property
    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return round(math.pi * (self.radius ** 2),5)

    def __str__(self):
        return f"Circle with radius: {self.radius}"

    def __repr__(self):
        return F'{self.__class__.__name__}({self.radius})'

    def __add__(self, other):
        return self.__class__(self.radius + other.radius)




# Compute the circle’s area.
# Print the circle and get something nice.
# Be able to add two circles together.
# Be able to compare two circles to see which is bigger.
# Be able to compare to see if they are are equal.
# (follows from above) be able to put them in a list and sort them.



