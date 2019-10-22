# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 17:37:54 2019

@author: bclas
"""
"""
if the var n is zero return a 0 and exit the function(return exits the function
If the var n is 1 return a 1 and exit the fibonacci function
if n is not 0 or 1 than process through the fibonacci equation
"""
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)
    
"""
this does the same thing as the fibonacci function but it starts at 2.
"""   
def lucas(n):
    if n == 0: 
        return 2
    elif n == 1:   
        return 1
    else:
        return lucas(n-2) + lucas(n-1)

"""takes var n and gives a fibonacci sequence number, If optional variables a and b are defined gives a lucas numberit """

def sum_series(n, a=0, b=1):
    if n == 0:
        if a == 2:
            return 2
        else: 
            return 0
    elif n == 1:
        return 1
    else:     
        return sum_series(n-2,a,b) + sum_series(n-1,a,b)
    
    
"""tests for fibonacci"""
assert sum_series(0) == 0
assert sum_series(1) == 1
assert sum_series(2) == 1
assert sum_series(3) == 2
assert sum_series(4) == 3
assert sum_series(5) == 5
assert sum_series(6) == 8
assert sum_series(7) == 13
"""tests for lucas"""
assert sum_series(0,2,1) == 2
assert sum_series(1,2,1) == 1
assert sum_series(2,2,1) == 3
assert sum_series(3,2,1) == 4
assert sum_series(4,2,1) == 7
assert sum_series(5,2,1) == 11
assert sum_series(6,2,1) == 18
assert sum_series(7,2,1) == 29




    