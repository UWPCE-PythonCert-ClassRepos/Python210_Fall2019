#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 19:26:27 2019

@author: matt.denko
"""

# part 1 ----------------------------------------------------------------------

print('+','- - - - ','+',' - - - - ', '+')
print('|          |           |')
print('|          |           |')
print('|          |           |')
print('|          |           |')
print('+','- - - - ','+',' - - - - ', '+')
print('|          |           |')
print('|          |           |')
print('|          |           |')
print('|          |           |')
print('+','- - - - ','+',' - - - - ', '+')


# part 2 ----------------------------------------------------------------------


def print_grid(x):
    if  x % 2 == 0:
        y = int(x/2)
        print("+ " + ("- " * y) + "+ " + ("- " * y) + "+")
        for _ in range(y):
            print("| " + ("  " * y) + "| " + ("  " * y) + "|")
        print("+ " + ("- " * y) + "+ " + ("- " * y) + "+")
        for _ in range(y):
            print("| " + ("  " * y) + "| " + ("  " * y) + "|")
        print("+ " + ("- " * y) + "+ " + ("- " * y) + "+")
    elif x % 2 != 0:
        y = int((x - 1)/2)
        print("+ " + ("- " * y) + "+ " + ("- " * y) + "+")
        for _ in range(y):
            print("| " + ("  " * y) + "| " + ("  " * y) + "|")
        print("+ " + ("- " * y) + "+ " + ("- " * y) + "+")
        for _ in range(y):
            print("| " + ("  " * y) + "| " + ("  " * y) + "|")
        print("+ " + ("- " * y) + "+ " + ("- " * y) + "+")
 
print_grid(4)
print_grid(15)

# part 3 ----------------------------------------------------------------------

def print_grid2(x, y):
    for _ in range(x):
        print(("+" + "- " * y) * x + "+")
        for _ in range(y):
            print(("|" + "  " * y) * x + "|")
    print(("+" + "- " * y) * x + "+")
    
print_grid2(2,2)
print_grid2(5,3)