#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##############################
# Assignement: PrintedGrid.py
# Dev: Kenneth Clark
# Date: 10-13-19
# Class: Python210A Winter
#############################

"""
Write a function that draws a grid using the '+' and '-' signs.
Then save assignement on git hub for instructor review.
1. Grid using simmple string miniupulation
2. Grid function using variable to determine size
3. Grid function that draws a similar grid with specified number of rows
    and columns and with each cell a given size.
"""

# 1. grid using simple string minupulation

"""
def grid_function():
    print("+" + "-" * 4 + "+" + "-" * 4 + "+")
    print("|" + " " * 4 + "|" + " " * 4 + "|")
    print("|" + " " * 4 + "|" + " " * 4 + "|")
    print("|" + " " * 4 + "|" + " " * 4 + "|")
    print("+" + "-" * 4 + "+" + "-" * 4 + "+")
    print("|" + " " * 4 + "|" + " " * 4 + "|")
    print("|" + " " * 4 + "|" + " " * 4 + "|")
    print("|" + " " * 4 + "|" + " " * 4 + "|")
    print("+" + "-" * 4 + "+" + "-" * 4 + "+")
    
grid_function()
"""

# 2. grid function using variable to determine size
"""
def grid_function(n):
    print("+" + "-" * n + "+" + "-" * n + "+")
    for i in range(n):
        print("|" + " " * n + "|"  + " " * n + "|")
    print("+" + "-" * n + "+" + "-" * n + "+")
    for i in range(n):
        print("|" + " " * n + "|" + " " * n + "|")
    print("+" + "-" * n + "+" + "-" * n + "+")
    
grid_function(n)
"""

# 3. Write a function that draws a similar grid with a specified 
#   number of rows and columns, and with each cell a given size.

def grid_function(colrow, n):
    
    for i in range(colrow):
        print((colrow // 2) * ("+" + "-" * n + "+" + "-" * n) + "+")
        for i in range(n):
            print((colrow // 2) * ("|" + " " * n + "|"  + " " * n) + "|")
        #print("+" + "-" * n + "+" + "-" * n + "+")
        for i in range(n):
            print((colrow // 2) * ("|" + " " * n + "|" + " " * n) + "|")
    print((colrow // 2) * ("+" + "-" * n + "+" + "-" * n) + "+")
    
    

grid_function(8, 6)


