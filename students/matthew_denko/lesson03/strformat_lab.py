#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:09:33 2019

@author: matt.denko
"""
import pandas as pd

# task 1

"""Write a format string that will take the following four element tuple:

( 2, 123.4567, 10000, 12345.67)

and produce:

'file_002 :   123.46, 1.00e+04, 1.23e+04'"""


print("file_{:03d}:  {:.2f}, {:.2e}, {:.2e} ".format(2, 123.4567, 10000, 12345.67))

# task 2

"""Using your results from Task One, repeat the exercise, but this time using 
an alternate type of format string (hint: think about alternative ways 
to use .format() (keywords anyone?), and also consider f-strings if 
you’ve not used them already)."""

my_tuple = ( 2, 123.4567, 10000, 12345.67)
f_string = "file_{:03d}:  {:.2f}, {:.2e}, {:.2e} "
print(f_string.format(*my_tuple))


# task 3

"""Rewrite:
"the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)

to take an arbitrary number of values."""

t = (1,2,3,4)
f_string = " {:d},"

def formatter(x):
    print(f_string.join(str(x)))
    
formatter(t)

# task 4

"""Given a 5 element tuple: (4, 30, 2017, 2, 27)
use string formating to print: '02 27 2017 04 30'"""

new_tuple = (4, 30, 2017, 2, 27)
print("'{:02d} {:.0f} {:.0f} {:02d} {:.0f}'".format(new_tuple[3],new_tuple[4],new_tuple[2],new_tuple[0],new_tuple[1]))

# task 5

"""Here’s a task for you: Given the following four element list:
['oranges', 1.3, 'lemons', 1.1]
Write an f-string that will display:
The weight of an orange is 1.3 and the weight of a lemon is 1.1"""

elements_list = ('orange', 1.3, 'lemon', 1.1)

f_string = "the weight of an orange is {:.1f} and the weight of a lemon is {:.1f}"

print(f_string.format(elements_list[1], elements_list[3]))

# task 6

"""Write some Python code to print a table of several rows, each with a name,
 an age and a cost. Make sure some of the costs are in the hundreds and thousands
 to test your alignment specifiers."""

cost = []
name = []
age = []
for i in range (0,100):
    age.append(i)
    name.append('Name' + str(i))
    cost.append(i*1000.10)

dataframe = pd.DataFrame()
dataframe.loc[:, 'name'] = name
dataframe.loc[:, 'age'] = age
dataframe.loc[:,'cost']= cost
dataframe = dataframe.iloc[1:]
print(dataframe)
    
 
