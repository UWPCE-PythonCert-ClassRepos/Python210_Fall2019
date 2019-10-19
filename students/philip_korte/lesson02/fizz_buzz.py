#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fizz_buzz.py
@author: philipkorte
"""
# including the integer just for clarity
for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, 'FizzBuzz')
    elif i % 5 == 0:
        print(i, 'Buzz')
    else:
        print(i)
