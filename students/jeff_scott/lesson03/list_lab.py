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


# Series-2

"""Display the list from Series-1."""

print(fruit)

"""Remove the last fruit from the list."""

fruit.pop()

"""Display the list."""

print(fruit)

"""Ask the user for a fruit to delete, find it and delete it."""

fruit = input("Which fruit would you like to delete? \
Input the name of the fruit: ")
if fruits in fruit:
    fruit.remove(fruits)
    print(fruit), "has been deleted"

# Series-3

"""Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list 
(making the fruit all lowercase)."""


"""For each “no”, delete that fruit from the list."""

"""For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values 
(a while loop is good here)"""

"""Display the list."""

# Series-4

"""Make a new list with the contents of the original, but with all the letters in each item reversed."""

"""Delete the last item of the original list. Display the original list and the copy."""
