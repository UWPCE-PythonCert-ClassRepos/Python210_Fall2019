#!/usr/bin/env python3

# Series-1

"""Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”."""
fruit = ["Apples", "Pears", "Oranges", "Peaches"]

"""Display the list"""
print("My list contains,", fruit)

"""Ask the user for another fruit and add it to the end of the list."""
response = input("Please provide a fruit to add to the list: ")
fruit.extend([response])

"""Display the list"""
print("My list now contains", fruit)


"""Ask the user for a number and display the number back to the user and the fruit
corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, 
so you will need to correct"""

index = input("Please state an index number: ")
index = (int(index) - 1)
name = fruit[index]
print(name)

"""Add another fruit to the beginning of the list using “+” and display the list."""

fruit = (["Strawberries"] + fruit)
print(fruit)

"""Add another fruit to the beginning of the list using insert() and display the list."""

fruit.insert(0, "Grapes")
print(fruit)

"""Display all the fruits that begin with “P”, using a for loop."""

for fruits in fruit:
    if fruits.startswith('P'):
        print(fruits)






