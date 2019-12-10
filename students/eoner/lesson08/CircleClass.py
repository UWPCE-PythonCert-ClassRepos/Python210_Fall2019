
# Compute the circle’s area.
# Print the circle and get something nice.
# Be able to add two circles together.
# Be able to compare two circles to see which is bigger.
# Be able to compare to see if they are are equal.
# (follows from above) be able to put them in a list and sort them.

from math import pi
import turtle


class Circle:

    def __init__(self, radius):
        # requires radius greater > 0
        if radius > 0:
            self.radius = radius
        else:
            raise ValueError(f'{self.__class__.__name__} radius can only be a positive number')

    @property
    def diameter(self):
        # diameter r*2
        return self.radius * 2

    @diameter.setter
    #should be able to set only ptoeprty (radius) from this setter
    def diameter(self, d):
        self.radius = d / 2

    @classmethod
    # constructor method to build circle from Diameter
    def from_diameter(cls, d):
        r = d/2
        return cls(r)

    @property
    def area(self):
        # can now calculate area
        return pi * self.radius ** 2.0

    def draw(self):
        # draw a represantation of a circle??? try turtle - this is causes python to crash when launched in ipython
        t = turtle.Turtle()
        t.circle(self.radius)
        turtle.done()

    def __add__(self, other):
        # override "+" add another circle's radius or another number to itself and return a new object
        if hasattr(other, 'radius'):
            other = other.radius
        #self.class should return current or subclass object
        return self.__class__(self.radius+other)
    
    __radd__ = __add__

    def __sub__(self, other):
        # override "-" subtract another circle's radius or another number from itself and return a new object
        if hasattr(other, 'radius'):
            other = other.radius
        return self.__class__(self.radius-other)
            
    __rsub__ = __sub__

    def __mul__(self, other):
        if hasattr(other, 'radius'):
            other = other.radius
        return self.__class__(self.radius*other)

   #so you can make reverse method like this... 
    __rmul__ = __mul__

    def __eq__(self, other):
        # override equal "=="
        return self.radius == other.radius

    def __lt__(self, other):
        # override ">"
        return self.radius < other.radius

    def __str__(self):
        # return readable info about object
        # using __class__ we don't need to write this
        return f'{self.__class__.__name__},radius: {self.radius}'

    def __repr__(self):
        # return some represantaion
        return f'{self.__class__.__name__}({self.radius})'


class Sphere(Circle):
    @property
    def area(self):
        # area for spehere A=4πr2
        return 4 * pi * self.radius ** 2

    @property
    def volume(self):
        # volume
        return ((pi/3)*4) * self.radius ** 3





if __name__ == "__main__":
    print("Running Tests...")
    
    # create using class methods
    c1 = Circle(4)
    c2 = Circle(40)
    c3 = Circle(40)
    c4 = Circle.from_diameter(50)
    s1 = Sphere(5)
    s2 = Sphere(50)
    s3 = Sphere(50)
    s4 = Sphere.from_diameter(50)
    cl= [Circle(40),Circle(4),Circle(400),Circle(4000)]
    
    #test create and verify class attributes
    assert c1.radius == 4
    assert c1.diameter == 8
    #this is a dumb way to make sure this will run on 32 bit or 128 bit system
    assert str(c1.area)[:8] == "50.26548"
    assert c4.radius == 25
    assert s1.radius == 5
    assert s1.diameter == 10
    assert str(s1.area)[:8] == "314.1592"
    assert str(s1.volume)[:8] == "523.5987"

    #test Equality/Less than
    #circle
    assert c2==c3
    assert c2!=c1
    assert c1<c2
    assert c4>c1
    #sphere
    assert s2==s3
    assert s2!=s1
    assert s1<s2
    assert s4>s1

    #test sorting
    cl.sort(key = None, reverse = True)
    assert cl == [Circle(4000), Circle(400), Circle(40), Circle(4)]

    #test addition with same obj type, integer, reverse, circle+sphere
    assert c2+c1 == Circle(44)
    assert c1+c2 == Circle(44)
    assert c1+10 == Circle(14)
    assert 10+c1 == Circle(14)
    assert c1+s1 == Circle(9)
    assert s1+c1 == Sphere(9)

    #test changing class attributes
    c1.radius = 8
    assert c1.radius == 8
    assert c1.diameter == 16
    c1.diameter = 8
    assert c1.diameter == 8
    assert c1.radius == 4

    #test string method
    assert str(c3) == 'Circle,radius: 40'
    assert str(s2) == 'Sphere,radius: 50'