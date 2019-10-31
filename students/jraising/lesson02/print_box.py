#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 17:50:26 2019

@author: jraising
"""

def grid(cell,size):
    for i in range(cell):
        print(cell * ('+'+ size * '-') + '+') 
        for i in range(size):
            print(cell * ('|' + ' ' * size) + '|')
    
    print(cell * ('+'+ size * '-') + '+') 
grid (4,2)