# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 19:43:56 2019

@author: bclas
"""
def grid_print(x,y):
    """Fuction takes a two arguments x, for the size of the cells and y for how
    many cells tall/wide the grid should be. and prints said grid.
    """
    height = y
    width = x
    row_width = ("+" + "-" * width) * width + "+"
    column_width = ("|" + " " * width) * width + "|"
    grid_printed = [row_width, column_width]
    
    for i in range(height):
        print(grid_printed[0])
        for a in range(height - 1):
            print(grid_printed[1])
    print(grid_printed[0])
    
if __name__ == "__main__":
    grid_print(4,4)