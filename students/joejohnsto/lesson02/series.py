# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:28:09 2019

@author: jjohnston
"""

def fibonacci(n):
    """Return the nth number in the fibonacci series."""
    if n <= 0:
        print("Index must be positive!")
        return
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib = fibonacci(n-2) + fibonacci(n-1)
        return fib


def lucas(n):
    """Return the nth number in the lucas series."""
    if n <= 0:
        print("Index must be positive!")
        return
    elif n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        luc = lucas(n-2) + lucas(n-1)
        return luc


def sum_series(n, first = 0, second = 1):
    """
    Return the nth number in any sumation series, like lucas or fibonacci, given the first two numbers.
    :param n:       the index in the series which will be returned
    :param first:   the first number in the series (optional)
    :param second:  the second number in the series (optional)
    
    if param first and second are not supplied the fucntion will return the fibonacci series
    
    """
    if n <= 0:
        print("Index must be positive!")
        return
    elif n == 1:
        return first
    elif n == 2:
        return second
    else:
        sum = sum_series(n-2,first,second) + sum_series(n-1,first,second)
        return sum


if __name__ == "__main__":
    # run some tests
    assert fibonacci(1) == 0
    assert fibonacci(2) == 1
    assert fibonacci(3) == 1
    assert fibonacci(4) == 2
    assert fibonacci(5) == 3
    assert fibonacci(6) == 5
    assert fibonacci(7) == 8

    assert lucas(1) == 2
    assert lucas(2) == 1

    assert lucas(5) == 7

    # test that sum_series matches fibonacci
    assert sum_series(5) == fibonacci(5)
    assert sum_series(7, 0, 1) == fibonacci(7)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    # test if sum_series works for arbitrary initial values
    assert sum_series(1, 3, 2) == 3
    assert sum_series(2, 3, 2) == 2
    assert sum_series(3, 3, 2) == 5
    assert sum_series(4, 3, 2) == 7
    assert sum_series(5, 3, 2) == 12
    assert sum_series(6, 3, 2) == 19

    print("tests passed")