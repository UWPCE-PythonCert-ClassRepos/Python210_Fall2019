#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 17:48:39 2019

@author: bclas
"""

#series 1

fruits = ["apples","pears","oranges","peaches"]

print(fruits)
newfruit = input ("please type in a fruit:")
fruits.extend([newfruit])
print(fruits)

fruit_index = int(input ("please provide an index number:"))
print(fruits[fruit_index - 1])

print(["pineapple"] + fruits)

fruits.insert(0,"guava")
print(fruits)

p_fruits = []
for word in fruits:
    if word.startswith('p'):
       p_fruits.append(word)

print(p_fruits)

#series 2
print(fruits)
del fruits[-1::]
print(fruits)

delete_fruit = input("please type a fruit to delete from the list:")
fruits.remove(delete_fruit) 
print(fruits)

#series 3 

for x in fruits:
    answer = input("Do you like {}?\n".format(x))
    while answer != 'No' and answer != 'Yes':
        answer = input("Please respond with 'Yes' or 'No'.\n")
    if answer == 'No':
        fruits.remove(x)
    elif answer == 'Yes':
        continue
print(fruits)

