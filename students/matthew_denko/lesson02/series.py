#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 21:18:43 2019

@author: matt.denko
"""

# Step 1-----------------------------------------------------------------------

"""Create a new module series.py in the lesson02 folder in your student folder.
In it, add a function called fibonacci.
The function should have one parameter n.
The function should return the nth value in the fibonacci series (starting with zero index).
Ensure that your function has a well-formed docstring"""

def fibonacci(n):
    """ function to return the nth value in the fibonacci series"""
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==0:
        return 0
    elif n==1: 
        return 1
    # Second Fibonacci number is 1 
    elif n==2: 
        return 1
    else: 
        return fibonacci(n-1)+fibonacci(n-2)
    pass

# Step 2 ----------------------------------------------------------------------

"""In your series.py module, add a new function lucas that returns the nth value 
in the lucas numbers series (starting with zero index).Ensure that your function has a well-formed docstring"""

    
def lucas(n) : 
    """function to return the nth value in the lucas series""" 
    # Base cases  
    if (n == 0) : 
        return 2
    if (n == 1) : 
        return 1
  
    # recurrence relation  
    return lucas(n - 1) + lucas(n - 2) 
    pass 

# Step 3-----------------------------------------------------------------------


def sum_series(n, n0=0, n1=1):
    """
    compute the nth value of a summation series.

    :param n0=0: value of zeroth element in the series
    :param n1=1: value of first element in the series

    This function should generalize the fibonacci() and the lucas(),
    so that this function works for any first two numbers for a sum series.
    Once generalized that way, sum_series(n, 0, 1) should be equivalent to fibonacci(n).
    And sum_series(n, 2, 1) should be equivalent to lucas(n).

    sum_series(n, 3, 2) should generate antoehr series with no specific name

    The defaults are set to 0, 1, so if you don't pass in any values, you'll
    get the fibonacci sercies
    """
    if n0 == 0 :
        return fibonacci(n)
    elif n1 == 0:
        return lucas(n)
    elif n0 == 2:
        return lucas(n)
    else:
        return fibonacci(n)
    pass

sum_series(4,0,1)


# Step 4-----------------------------------------------------------------------


# run some tests
assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(4) == 3
assert fibonacci(5) == 5
assert fibonacci(6) == 8
assert fibonacci(7) == 13

# test lucas
assert lucas(0) == 2
assert lucas(1) == 1
assert lucas(4) == 7

# test that sum_series matches fibonacci
assert sum_series(5) == fibonacci(5)
assert sum_series(7, 0, 1) == fibonacci(7)

# test if sum_series matched lucas
assert sum_series(5, 2, 1) == lucas(5)

print('tests passed')