# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 19:28:36 2019

@author: joejo
"""

for i in range(1,101):
    if i%3==0 and i%5==0:
        print('FizzBuzz')
    elif i%5==0:
        print('Buzz')
    elif i%3==0:
        print('Fizz')
    else:
        print(i)