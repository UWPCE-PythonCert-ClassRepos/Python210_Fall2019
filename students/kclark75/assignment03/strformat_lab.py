#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:58:14 2019
author: kenclark
assignment 03: strformat_lab.py
class: Py210 Introduction to Python
"""

"""
Task one
Write a format string that will take the following four element tuple:
( 2, 123.4567, 10000, 12345.67)
and produce:
'file_002 :   123.46, 1.00e+04, 1.23e+04'

Task Three
Dynamically Building up format strings
Rewrite:
"the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
to take an arbitrary number of values.

Task Four
Given a 5 element tuple:
( 4, 30, 2017, 2, 27)
use string formating to print:
'02 27 2017 04 30'

Task Five
f-strings are new to Python (version 3.6), but are very powerful and efficient. 
    This means they are worth understanding and using. And this is made easier
    than it might be because they use the same, familiar formatting language that 
    is conventionally used in Python (in .format()).
    
Task Six
Write some Python code to print a table of several rows, each with a name, 
    an age and a cost. Make sure some of the costs are in the hundreds and 
    thousands to test your alignment specifiers.
"""

fnames = ['file1', 'file2', 'file10', 'file11']
task_one = (2, 123.456, 10000, 12345.67)
in_tuple = ((2,3,5,8,9,10))
in_tuple01 = (4, 30,2017, 2,27)

"""Test script"""
def pad_zeros(fnames):
    """Example of how to get padding format"""
    length = len(fnames) 
    i = 0
    name = ''
    # Iterating using while loop 
    while i < length: 
        name = fnames[i]
        print(name[:4] + "_" + name[4:].zfill(3))
        i += 1


"""Task one"""        
def change_list(task_one):
    """Given string format per example in title"""
    name = str(task_one[0])
    file_name = ("'" + "file" + "_" + name[:].zfill(3) + " " + ":")
    
    flt_number = str(round(task_one[1],2))
    
    sci_notation = '{:.2e}'.format(task_one[2])
    
    sci_notation1 = '{:.2e}'.format(task_one[3])
        
    print(file_name + "  " + flt_number + "," + " " + sci_notation + "," + " " + sci_notation1 + "'")
    

"""Task Two"""
"""TBD"""


"""Task Three"""
def dyn_fstring(in_tuple):
    """Given a tuple use dynamic formating to format any length tuple
    into requested format"""
    l = len(in_tuple)
    form_string = "The" + " {:d}".format(l) + " numbers are:" + (" {:d}, "*l).format(*in_tuple)
    print(form_string.format(*in_tuple))
    
    
"""Task four"""
def dyn_fstring01(in_tuple01):
    form_string = ("{:d}, {:d}, {:d}, {:d}, {:d}").format(in_tuple01[3], in_tuple01[4], in_tuple01[2], in_tuple01[0], in_tuple01[1])
    print(form_string)    

"""Task Five"""
def f_string():
    str_list = ['oranges', 1.3, 'lemons', 1.1]
    print(f"The weight of an {str_list[0]} is {str_list[1]} and the weight of a {str_list[2]} is {str_list[3]}.")


"""Task Six"""
def data_test():
    line01 = ['Ken',25,'$100.00']
    line02 = ['Stan', 32, '$1100.00']
    line03 = ['Brad', 45, '$21,000.34']
    line01 = '{:5},{:15},{:30}'.format(*line01)
    line02 = '{:10},{:15},{:10}'.format(*line02)
    line03 = '{:10},{:15},{:10}'.format(*line03)
    print(line01)
    print(line02)
    print(line03)
    
"""Sample script"""    
#pad_zeros(fnames)
    
"""Task One"""
#change_list(task_one)  

"""Task Three"""   
#dyn_fstring(in_tuple)
 
"""Task Four""""
#dyn_fstring01(in_tuple01)

"""Task five"""
#f_string()

"""Task Six"""
data_test()
