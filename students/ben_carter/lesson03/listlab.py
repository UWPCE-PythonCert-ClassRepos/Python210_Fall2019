#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 17:48:39 2019

@author: bclas
"""

#series 1

#This line creates the list we will be playing with
fruits = ["apples","pears","oranges","peaches"]

#these lines prompt for a new fruit and add it via the .extend() method to the fruits list
print(fruits)
newfruit = input ("please type in a fruit:")
fruits.extend([newfruit])
print(fruits)

#this line prompts for a indexed position in the list and prints the fruit in that location to the console
fruit_index = int(input ("please provide an index number:"))
print(fruits[fruit_index - 1])

#this line adds a fruit to the list via the +
print(["pineapple"] + fruits)

#This code adds guava to the index position 0 (the beginning) of the list
fruits.insert(0,"guava")
print(fruits)

#This code displays all fruits that begin with 'p'
p_fruits = []
for word in fruits:
    if word.startswith('p'):
       p_fruits.append(word)

print(p_fruits)


#series 2

#This code displays the list, removes the last item from the list, and displays it again.
print(fruits)
del fruits[-1::]
print(fruits)

#This code prompys for a fruit in the list to delete and removes it from the list. 
delete_fruit = input("please type a fruit to delete from the list:")
fruits.remove(delete_fruit) 
print(fruits)


#series 3 

#This for loop asks the user if they like each fruit in the list. If a 'No' answer is received it deletes that item
like_fruits = fruits
for x in like_fruits:
    answer = input("Do you like {}?\n".format(x))
    while answer != 'No' and answer != 'Yes':
        answer = input("Please respond with 'Yes' or 'No'.\n")
    if answer == 'No':
        fruits.remove(x)
    elif answer == 'Yes':
        continue
print(like_fruits)

#series 4
"""Make a new list with the contents of the original, but with all the letters in each item reversed.
Delete the last item of the original list. Display the original list and the copy."""


#these first two lines create a new list and populate it with the contents of the original list
reversed_fruits = []
new_fruits = fruits
#This for loop takes each item in the list 'x' and reverses the string and appends it to the new list 'reversed_fruits'
for x in new_fruits:
    x = x[::-1]
    reversed_fruits.append(x)

#this line removes the last item from the original list,
#the .pop function defaults to the last position in the list, thus needs no arguments in this case.
fruits.pop()
print(fruits)
print(reversed_fruits)







