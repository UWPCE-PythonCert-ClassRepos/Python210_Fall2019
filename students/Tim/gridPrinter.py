# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 10:41:48 2019

@author: tdietz
"""
#printing columns where n is the cellSize and cols is the tablesize
def buildColumns(n,cols):
    plus = '+'
    minus = '-'
    print(plus, end=' ')
    for columns in range(cols):
        for b in range(n):
            print(minus, end=' ')
        if columns == cols - 1:
            print(plus)
        else:
            print(plus, end=' ')
#printing rows where n is the cellSize and cols is the tablesize           
def buildRows(n, cols):
    bar = '|'
    space = ' '   
    for rows in range(n):
        print(bar, end=' ')
        for columns in range(cols):
            for a in range(n):
                print(space, end=' ')
            if columns == cols - 1:
                print(bar)
            else:
                print(bar, end=' ')
#prints grid layout of 2x2 with specified gridsize
def print_grid(gridSize):
    if(gridSize % 2 == 0):
        cellSize = int(gridSize/2)
    else:
        cellSize = int((gridSize - 1)/2)
    for a in range(2):
        buildColumns(cellSize, 2)
        buildRows(cellSize, 2)
    buildColumns(cellSize, 2)
#prints grid layout with specified table size and cell size    
def print_grid2(tableSize, cellSize):
    for a in range(tableSize):
        buildColumns(cellSize, tableSize)
        buildRows(cellSize, tableSize)
    buildColumns(cellSize, tableSize)
                
    
    
    
    
    
    