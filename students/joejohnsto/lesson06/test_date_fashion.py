# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 17:52:27 2019

@author: joejo

from codingbat

You and your date are trying to get a table at a restaurant. The parameter
"you" is the stylishness of your clothes, in the range 0..10, and "date" is the
stylishness of your date's clothes. The result getting the table is encoded as
an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or
more, then the result is 2 (yes). With the exception that if either of you has
style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).
"""


from date_fashion import date_fashion


def test1():
    assert date_fashion(5, 10) == 2


def test2():
    assert date_fashion(5, 2) == 0


def test3():
    assert date_fashion(5, 5) == 1


def test4():
    assert date_fashion(3, 3) == 1


def test5():
    assert date_fashion(10, 2) == 0


def test6():
    assert date_fashion(2, 9) == 0


def test7():
    assert date_fashion(9, 9) == 2


def test8():
    assert date_fashion(10, 5) == 2