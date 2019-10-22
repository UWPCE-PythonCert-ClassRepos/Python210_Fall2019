# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 17:37:54 2019

@author: bclas
"""
"""
create a function that starts at zero and takes an input (a number) and adds
that number to the 
"""
def fibonacci(n):
    if n == 0:    """If the var n is zero return a 0 and exit the function(return exits the function"""
        return 0
    elif n == 1:   """If the var n is 1 return a 1 and exit the fibonacci function"""
        return 1
    else:     """if n is not 0 or 1 than process through the fibonacci equation"""
        return fibonacci(n-2) + fibonacci(n-1)
    
def lucas(n):
    if n == 0:  """if the var n is zero retur a 2 and exit the function"""
        return 2
    elif n == 1:   """if the var n is 1 retur a 1 and exit the function"""
        return 1
    else:
        return lucas(n-2) + lucas(n-1)
