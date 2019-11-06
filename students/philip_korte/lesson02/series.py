#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 14:30:07 2019

@author: philipkorte
series.py
"""

def fibinacci(n):
    """Return the nth value in a fibinacci sequence."""
#    if n == 0:
#        return 0
#    elif n == 1:
#        return 1
#    else:
#        return fibinacci(n-2) + fibinacci(n-1)
    return sum_series(n)
    
        
def lucas(n):
    """Return the nth value in a lucas numbers series."""
#    if n == 0:
#        return 2
#    elif n == 1:
#        return 1
#    else:
#        return lucas(n-2) + lucas(n-1)   
    return sum_series(n, 2, 1)
 
    
def sum_series(number, first=0, second=1):
    """
    Return the nth value in a a summation series
    
    :param number: required, the nth value in the series
    :param first: optional, value of the 0th element in the series
    :param second: optional, value of the 1st element in the series
    
    This function calculates the nth value in any summation series. The default
    first and second value are 0 and 1 so if you don't pass in any values, 
    you'll get the fibinacci series.
    """

    if number == 0:
        return first
    elif number == 1:
        return second
    else:
        return sum_series(number-2, first, second) + \
               sum_series(number-1, first, second)


if __name__ == "__main__":
    # check if fibinacci works
    assert fibinacci(0) == 0
    assert fibinacci(1) == 1
    assert fibinacci(2) == 1
    assert fibinacci(3) == 2
    assert fibinacci(4) == 3
    assert fibinacci(5) == 5
    assert fibinacci(6) == 8
    assert fibinacci(7) == 13
    
    # check if lucas works
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7
    assert lucas(5) == 11
    assert lucas(6) == 18
    assert lucas(7) == 29
    
    # check if sum_series works
    assert sum_series(0) == 0
    assert sum_series(1) == 1
    assert sum_series(2) == 1
    assert sum_series(3) == 2
    assert sum_series(4) == 3
    assert sum_series(5) == 5
    assert sum_series(6) == 8
    assert sum_series(7) == 13
    
    # check if sum_series works with arbitrary initial values
    assert sum_series(0, 3, 4) == 3
    assert sum_series(1, 3, 4) == 4
    assert sum_series(2, 3, 4) == 7
    assert sum_series(3, 3, 4) == 11
    assert sum_series(4, 3, 4) == 18
    assert sum_series(5, 3, 4) == 29
    
    print("tests passed")
    
    
