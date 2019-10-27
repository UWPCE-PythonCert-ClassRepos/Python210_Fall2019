#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 17:48:39 2019

@author: bclas
"""

fruits = ["apples","pears","oranges","peaches"]

print(fruits)
newfruit = input ("please type in a fruit:")
fruits.extend([newfruit])
print(fruits)

fruit_index = int(input ("please provide an index number:"))
print(fruits[fruit_index - 1])

print(["pineapple"] + fruits)

fruits.insert(0,"guava")
print (fruits)

p_fruits = []
for word in fruits:
    if word.startswith('p'):
       p_fruits.append(word)

print(p_fruits)
