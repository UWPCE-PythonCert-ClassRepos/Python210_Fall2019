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

class Circle_Math:
    def __init__(self,Second_Circle):
        self.Second_Circle = Second_Circle
    def addition(self,a):
        return self.__add__(a)
    def compare(self,a):
        return self.__lt__(a)



print(Circle_Math.addition((C(20).Area()), C(10).Area()))

if __name__ == "__main__":
    FirstCircle = C(20)
    SecondCircle = C(10)
    #test with assigned variables/inherited class
    assert Circle_Math.addition(FirstCircle.Area(), SecondCircle.Area()) == 13612.07184107664
    assert Circle_Math.compare(FirstCircle.Area(), SecondCircle.Area()) == False
    #test with class called directly
    assert Circle_Math.addition((C(20).Area()), C(10).Area()) == 13612.07184107664
    assert Circle_Math.compare((C(20).Area()), C(10).Area()) == False
    print("tests pass")
