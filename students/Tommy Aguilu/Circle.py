import math

class C:
    def __init__(self,r):
        self.Radius=r
    def Circumference(self):
        return self.Radius*math.pi
    def Area(self):
        return self.Radius**math.pi
    def Diameter(self):
        return self.Radius*2
class Sphere(C):
    def Volume(self):
        return ((4/3)*math.pi)(self.Radius**3)
    def S_Area(self):
        return 4*math.pi*(self.Radius**2)

class Circle_Math:
    def __init__(self,Second_Circle):
        self.Second_Circle = Second_Circle
    def addition(self,a):
        return self.__add__(a)
    def compare(self,a):
        return self.__lt__(a)
