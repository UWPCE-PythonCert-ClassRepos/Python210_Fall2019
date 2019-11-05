#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 23:36:32 2019

@author: jraising

Write a format string that will take the following four element tuple:

( 2, 123.4567, 10000, 12345.67)

and produce:

'file_002 :   123.46, 1.00e+04, 1.23e+04'
"""


from decimal import Decimal
import math

t = ( 2, 123.4567, 10000, 12345.67)


#def func0(i):
    
    
    
    
    
    
    
def func1(i):
   
    print('file_+{:043d}'.format(i))
func1(2)
        
    
    
    
#def func2(i):
#    return '%.2e' % Decimal(i)
#    
#    
#def func3(i): 
#    return '%.2e' % Decimal(i)
    
#print(func2(10000))
#print(func3(12345.67))
