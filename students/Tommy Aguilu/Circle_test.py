import Circle as C
def tests():
    x = []
    FirstCircle = C.C(20)
    SecondCircle = C.C(10)
    Circle_List = [C.C(1).Radius, C.C(5).Radius, C.C(3).Radius, C.C(8).Radius, C.C(48).Radius, C.C(15).Radius,
                   C.C(10).Radius]
    Circle_list_sorted = [C.C(1).Radius, C.C(3).Radius, C.C(5).Radius, C.C(8).Radius,C.C(10).Radius,
                          C.C(15).Radius,C.C(48).Radius]
    (Circle_List.sort())
    # test of constructors
    assert FirstCircle.Radius == 20
    assert SecondCircle.Radius == 10
    # test with assigned variables/inherited class
    assert C.Circle_Math.addition(FirstCircle.Area(), SecondCircle.Area()) == 13612.07184107664
    assert C.Circle_Math.compare(FirstCircle.Area(), SecondCircle.Area()) == False
    # test of comparison and addition functions
    assert C.Circle_Math.addition((C.C(20).Area()), C.C(10).Area()) == 13612.07184107664
    assert C.Circle_Math.compare((C.C(20).Area()), C.C(10).Area()) == False
    # test with sorted circle objects
    assert Circle_List == Circle_list_sorted
    print("tests pass")

tests()