# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 09:04:48 2019

@author: tdietz
"""

#task1
t = (4, 123.4567, 10000, 12345.67)
def task1(t):
    formatString = "file_{:03d}: {:.2f}, {:.2E}, {:.2E}".format(*t)
    print(formatString)
#task2 using F strings
def task2(t):
    print(f'file_{t[0]:03d}: {t[1]:.2f}, {t[2]:.2E}, {t[3]:.2E}')

#task3 dynamically building up format strings
def formatter(t):
    l = len(t)
    return "The {} numbers are: ".format(l) + ",".join(["{}"]*l).format(*t)

#task4 five element tuple
def task4(t):
    print(f'{t[3]:02d}, {t[4]:02d}, {t[2]:d}, {t[0]:02d}, {t[1]:02d}')
    
#task5 
def task5():
    fruits = ['oranges', 1.3, 'lemons', 1.1]
    print(f"The weight of an {fruits[0][:-1]} is {fruits[1]} and the weight of a {fruits[2][:-1]} is {fruits[3]}")
    
#task6
def task6():
    table = [["Fortnite", 123, 4000], ["Call of Duty", 560, 40290], ["Super Smash Bros", 709, 60298], ["Sim City", 270, 19280]]
    for a in range(len(table)):
        print("{:>20}{:>10}{:>10}".format(*table[a]))

def extraTask():
    randomInts = (1,2,3,4,5,6,7,8,9)
    for a in range(len(randomInts)):
        print("{:5}".format(*randomInts), end="")
    
    