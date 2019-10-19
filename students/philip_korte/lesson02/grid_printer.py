#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
grid_printer.py

@author: philipkorte
"""

PLUS = '+'
MIN = '-'
BAR = '|'



# Part 1

def grid_function_1():
    """Print a 2x2 square grid."""
    grid = range(11)    

    for i in grid:
        if i % 5 == 0:
            for x in grid:
                if x % 5 == 0:
                    print(PLUS, end=' ')
                else:
                    print(MIN, end=' ')
            print('\n', end='')
        else:
            for y in grid:
                if y % 5 == 0:
                    print(BAR, end=' ')
                else:
                    print(' ', end=' ')
            print('\n', end='')


# Part 2
def print_grid(n):
    """
    Print a 2x2 square grid.
    param n: The size of grid. Even numbers are incrimented to the next
             whole number.
    """
    # since even numbers don't form a clean grid, incriment to next whole
    # number
    if n % 2 == 0:
        n += 1
        
    grid = range(n + 2)
    divisor = (n + 1)/2
    
    for i in grid:
        if i % divisor == 0:
            for x in grid:
                if x % divisor == 0:
                    print(PLUS, end=' ')
                else:
                    print(MIN, end=' ')
            print('\n', end='')
        else:
            for y in grid:
                if y % divisor == 0:
                    print(BAR, end=' ')
                else:
                    print(' ', end=' ')
            print('\n', end='')


# Part 3
def print_grid2(cells=3, size=3):
    """
    Print a square grid.
    :param cells: The number of cells in the grid.
    :param size: The size of each cell in the grid.
    """
    
    grid = cells * (size + 1) + 1
    grid = range(grid)
    
    for i in grid:
        if i % (size + 1) == 0:
            for x in grid:
                if x % (size + 1) == 0:
                    print(PLUS, end=' ')
                else:
                    print(MIN, end=' ')
            print('\n', end='')
        else:
            for y in grid:
                if y % (size + 1) == 0:
                    print(BAR, end=' ')
                else:
                    print(' ', end=' ')   
            print('\n', end='')


grid_function_1()
print_grid(5)
print_grid2(3, 4)
