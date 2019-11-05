# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:41:42 2019

@author: tdietz
"""
def printFizzBuzz():
    for x in range(1,101):
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)
            
            
