#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:09:09 2019

@author: jraising
"""

def fibo(n):
    fib = [0,1]
    for i in range(n-1):
        fib.append(fib[i] + fib[i+1])    
    return (fib[n])

ans = fibo(5)
print (ans)

def lucas(n):
    luc = [2,1]
    for i in range(n-1):
        luc.append(luc[i] + luc[i+1])
    print(luc)
    return (luc[n])
    
    
luca = lucas(6)
print(luca)

"""
This function has one required parameter and two optional parameters. The required parameter will determine which element in the series to print. The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced.

Calling this function with no optional parameters will produce numbers from the fibo series (because 0 and 1 are the defaults).

Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers.

Other values for the optional parameters will produce other series.

Note: While you could check the input arguments, and then call one of the functions you wrote, the idea of this exercise is to make a general function, rather than one specialized. So you should re-implement the code in this function.
"""
def sumseries(n, first = 0, second = 1):
    series =[first, second]
    for i in range(n):
        series.append(series[i] + series[i+1])
    return series[n]
    
result = sumseries(6,2,1)
print(result)
    

if __name__ == "__main__":
    # run some tests
    assert fibo(0) == 0
    assert fibo(1) == 1
    assert fibo(2) == 1
    assert fibo(3) == 2
    assert fibo(4) == 3
    assert fibo(5) == 5
    assert fibo(6) == 8
    assert fibo(7) == 13

    assert lucas(0) == 2
    assert lucas(1) == 1

    assert lucas(4) == 7

    # test that sumseries matches fibo
    assert sumseries(5) == fibo(5)
    assert sumseries(7, 0, 1) == fibo(7)

    # test if sumseries matched lucas
    assert sumseries(5, 2, 1) == lucas(5)

    # test if sumseries works for arbitrary initial values
    assert sumseries(0, 3, 2) == 3
    assert sumseries(1, 3, 2) == 2
    assert sumseries(2, 3, 2) == 5
    assert sumseries(3, 3, 2) == 7
    assert sumseries(4, 3, 2) == 12
    assert sumseries(5, 3, 2) == 19

    print("tests passed")