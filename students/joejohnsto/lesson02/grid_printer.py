# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 18:37:25 2019

@author: joejo
"""
# simple grid
topline = ('+ ' + '- '*4)
topline = (topline*2 + '+')
print(topline)

midline = ('|' + ' '*9)
midline = (midline * 2 + '|')
print(midline)
print(midline)
print(midline)
print(midline)

print(topline)

print(midline)
print(midline)
print(midline)
print(midline)

print(topline)

# print grid function with 1 input

def print_grid(size):
    topline = ('+ ' + '- ' * size)
    topline = (topline * 2 + '+')
    print(topline)

    midline = ('| ' + '  ' * size)
    midline = (midline * 2 + '|')
    for i in range(size):
        print(midline)

    print(topline)
    
    for i in range(size):
        print(midline)

    print(topline)

# print grid function with 2 inputs

def print_grid2(cells,size):
    topline = ('+ ' + '- ' * size)
    topline = (topline * cells + '+')
    print(topline)

    midline = ('| ' + '  ' * size)
    midline = (midline * cells + '|')
    
    for j in range(cells):
        for i in range(size):
            print(midline)
        print(topline)
