#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 12:16:04 2019

@author: matt.denko
"""

# List Lab

"""Series 1
Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
Display the list (plain old print() is fine…).
Ask the user for another fruit and add it to the end of the list.
Display the list.
Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
Add another fruit to the beginning of the list using “+” and display the list.
Add another fruit to the beginning of the list using insert() and display the list.
Display all the fruits that begin with “P”, using a for loop."""

# Create a list that contains Apples, Pears, Oranges and Peaches

fruit_list = ["Apples","Pears","Oranges","Peaches"]

# Display the list

print(fruit_list)

# Ask the user for another fruit and add it to the end of the list

response = input("Hey user!!! What fruit do you want to add? > ")
fruit_list.append(response)

#Display the list

print(fruit_list)

# Ask the user for a number and display the number back to the user and 
# the fruit corresponding to that number (on a 1-is-first basis). 
# Remember that Python uses zero-based indexing, so you will need to correct.

response2 = input("Hey bozo! Give me a number from 1 to 5 ! > ")
print("your number is ",response2, "and the fruit for the number is ",fruit_list[int(response2) - 1])

# Add another fruit to the beginning of the list using “+” and display the list.

new_item = ['Huckleberries']
fruit_list = new_item + fruit_list
print(fruit_list)

# Add another fruit to the beginning of the list using insert() and display the list.

fruit_list.insert(0,'Rasberries')
print(fruit_list)

# Display all the fruits that begin with “P”, using a for loop.

i = 0
for i in range(0,len(fruit_list)):
    p = fruit_list[i]
    if p.startswith("P") == True:
        print(p)
    i = i + 1

"""Series 2
Using the list created in series 1 above:

Display the list.
Remove the last fruit from the list.
Display the list.
Ask the user for a fruit to delete, find it and delete it."""

# Display the list.

print(fruit_list)

# Remove the last fruit from the list.

fruit_list = fruit_list[0:6]

# Display the list.

print(fruit_list)

# Ask the user for a fruit to delete, find it and delete it

response2 = input("Yo! Give me the number of the fruit you want to delete from 1 to 6 > ")

fruit_list.remove(fruit_list[int(response2) - 1])

print(fruit_list)

"""Series 3
Again, using the list from series 1:

Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
For each “no”, delete that fruit from the list.
For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
Display the list."""

i = 0
for i in range(0,len(fruit_list)):
    try:
        p = fruit_list[i].lower()
        p = "Do you like " + str(p) + " ? >"
        response = input(p)
        if response == "no":
            fruit_list.remove(fruit_list[int(i)])
        elif response == "yes":
            pass
        else:
            while response not in ["yes","no"]:
                p = fruit_list[i].lower()
                p = "Do you like " + str(p) + " ? >"
                response = input(p)
    except IndexError as exception:
        print(fruit_list)
        pass
    print(fruit_list)
                
            
            
"""Series 4
Once more, using the list from series 1:

Make a new list with the contents of the original, but with all the letters in each item reversed.
Delete the last item of the original list. Display the original list and the copy."""

def reversed_string(a_string):
    return a_string[::-1]

fruit_list_copy = []
a = 0
for a in range(0,len(fruit_list)-1):
    b = fruit_list[a]
    fruit_list_copy.append(reversed_string(b))
    
fruit_list.remove(fruit_list[len(fruit_list)-1])

print(fruit_list)
print(fruit_list_copy)

# test ------------------------------------------------------------------------