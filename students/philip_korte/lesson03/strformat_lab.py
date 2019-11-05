#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
strformat_lab.py

@author: philipkorte
"""

# Task One
my_tuple = (2, 123.4567, 10000, 12345.67)

print(f'file_{my_tuple[0]:03d} : {my_tuple[1]: 8.2f}, {my_tuple[2]:.2e}, \
{my_tuple[3]:.3e}')

# Task Two
print('file_{:03d} : {: 8.2f}, {:.2e}, {:.3e}'.format(*my_tuple))

# Task Three
def formatter(t):
    l = len(t)

    print(("the {} numbers are: " + ', '.join(['{:d}'] * l)).format(l, *t))
    
formatter((1,2,3,4,5))

# Task Four
new_tuple = (4, 30, 2017, 2, 27)

print('{3:02d} {4:d} {2:d} {0:02d} {1:d}'.format(*new_tuple))

# Task Five
my_list = ['oranges', 1.3, 'lemons', 1.1]
fruit1 = my_list[0][:-1]
fruit2 = my_list[2][:-1]

message = f'The weight of an {fruit1:s} is {my_list[1]:2.1f} ' \
          f'and the weight of a {fruit2:s} is {my_list[3]:2.1f}'

print(message)

# Task Six
persons = [['Bugs Bunny', 30, 1000.00],
           ['Daffy Duck', 32, 88.09],
           ['Porky Pig', 40, 125.40],
           ['Pepé Le Pew', 27, 260.75],
           ['Tweety', 17, 509.34],
           ['Wile E. Coyote', 37, 600.90]]
           

header = f'{"Name":20}|{"Age":>9}|{"Cost":>9}|'
print(header)
print('-'*len(header))
for person in persons:
    print('{:20s}|{:9d}|{:9.2f}|'.format(*person))
    
# Extra Task
this_tuple = tuple(range(10))

print(('{:5}'* len(this_tuple)).format(*this_tuple))