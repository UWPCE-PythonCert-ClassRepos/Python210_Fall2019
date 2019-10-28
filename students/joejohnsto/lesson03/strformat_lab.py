# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 14:42:34 2019

@author: jjohnston
"""


# Task One

t = (2, 123.4567, 10000, 12345.67)
s = 'file_{:0=3d} :  {:.2f}, {:.2e}, {:.2e}'

s.format(*t)


# Task Two
# redo task one using f-string
s = f'file_{t[0]:03} :  {t[1]:.2f}, {t[2]:.2e}, {t[3]:.2e}'


# Task Three

t = (1,2,3,4)

def formatter(t: tuple):
    s = 'The {} numbers are: ' + '{}, '*(len(t)-1) + '{}'
    return s.format(len(t),*t)


# Task Four
    
t = ( 4, 30, 2017, 2, 27)
s = f'{t[3]:02} {t[4]} {t[2]} {t[0]:02} {t[1]}'


# Task Five

l = ['oranges', 1.3, 'lemons', 1.1]
s = f'The weight of an {l[0][:-1]} is {l[1]} and the weight of a {l[2][:-1]} is {l[3]}'
s2 = f'The weight of an {l[0][:-1].upper()} is {l[1]*1.2} and the weight of a {l[2][:-1].upper()} is {l[3]*1.2}'


# Task Six
wines = ('Cabernet', 'Syrah', 'Malbec', 'Chardonay')
ages = (24, 13, 8, 3)
prices = [4560, 125, 89, 9]

for i, j in enumerate(prices):
    prices[i] = f'${j:,.2f}'

for i in range(len(wines)):
    print(f'{wines[i]:12}{ages[i]:>5}{prices[i]:>15}')
# tuple with 10 consecutive numbers, printed in columns of width 5
t2 = (1,2,3,4,5,6,7,8,9,10)
print('{0:5}{1:5}{2:5}{3:5}{4:5}{5:5}{6:5}{7:5}{8:5}{9:5}'.format(*t2))
