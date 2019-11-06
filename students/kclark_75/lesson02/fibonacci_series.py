#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################
# Assignement: 02
# Name: fizz_buzz.py
# Dev: Kenneth Clark
# Date: 10-13-19
# Class: Python210A Winter
# Instructor: David Pokrajac
#############################

"""
The Fibonacci Series is a numeric series starting with the integers 0 and 1.
In this series, the next integer is determined by summing the previous two
This gives us:
0, 1, 1, 2, 3, 5, 8, 13, ...

We will write a function that computes this series – then generalize it.

The Lucas Numbers are a related series of integers that start with the values 2 and 1 rather than 0 and 1. The resulting series looks like this:
2, 1, 3, 4, 7, 11, 18, 29, ...

1. Fibonacci function
2. Lucas Numbers function
"""

# Function for nth Fibonacci number 


# 1. Fibonacci function
  
def fibonacci(a, b):
    for i in range(0, 10):
        print(a)
        a,b = b, a + b
    print("\n")


# Lucas Number function
def lucas(a, b):
    for i in range(0, 10):
        print(a)
        a,b = b, a + b
    
    
fibonacci(0, 1)

lucas(2, 1)