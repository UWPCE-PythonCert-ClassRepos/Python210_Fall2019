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

#
#from decimal import Decimal
#import math
#
#t = ( 2, 123.4567, 10000, 12345.67)
#
#
#def func0(i):
#    
#   print('file_+{:03d}'.format(i))
#func1(2)  
    
    
    
    
    
#def func1(i):
#    formatter = f'{i:.02f}'
#    print(formatter)
#    
#   
#func1(123.4567)
#        
    
    
    
#def func2(i):
#    return '%.2e' % Decimal(i)
#    
#    
#def func3(i): 
#    return '%.2e' % Decimal(i)
    
#print(func2(10000))
#print(func3(12345.67))


"""Task 4
Given a 5 element tuple:

( 4, 30, 2017, 2, 27)

use string formating to print:

'02 27 2017 04 30'

Hint: use index numbers to specify positions."""

#
#tup = ( 4, 30, 2017, 2, 27)
#
#def formatter(i):
#    print(f'{tup[3]:02d}'+ ' ' + f'{tup[4]:02d}' + ' ' + f'{tup[2]:04d}' + ' ' + f'{tup[0]:02d}' + ' ' + f'{tup[1]:02d}')
#formatter(tup)




"""Task 5
Here’s a task for you: Given the following four element list:

['oranges', 1.3, 'lemons', 1.1]
Write an f-string that will display:
The weight of an orange is 1.3 and the weight of a lemon is 1.1

Now see if you can change the f-string so that it displays the names 
of the fruit in upper case, and the weight 20% higher (that is 1.2 times higher).
"""
#weight = ['oranges', 1.3, 'lemons', 1.1]
#def formatter(i):
#    print(f'The weight of an {weight[0][0:-1].upper()} is {weight[1]*1.2} and the weight of a {weight[2][0:-1].upper()} is {weight[3]*1.2}')
#
#formatter(weight)



"""Task Six

Write some Python code to print a table of several rows, 
each with a name, an age and a cost. Make sure some of the 
costs are in the hundreds and thousands to test your alignment specifiers.
"""

whiskey = [["Black","12 years", "$40"], ["Chevas", "15 years", "$180"], ["special Edition", "30 years", "$1000.50"]]
def table(l):
    for i in range(len(l)):
        print(i)
        print(f'{l[i][0]:25}{l[i][1]:20}{l[i][2]:>8}')
        
table(whiskey)

