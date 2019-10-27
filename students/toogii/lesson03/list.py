#!/usr/bin/env python3
from copy import copy
from time import sleep

#Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
print("\nTask-1: Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.")

sleep(1)

fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']

sleep(1)

# Display the list (plain old print() is fine…).

print("\nTask-2: Display the list (plain old print() is fine…).\n")

sleep(1)

print(fruits)

sleep(1)

#Ask the user for another fruit and add it to the end of the list.

print("\nTask-3: Ask the user for another fruit and add it to the end of the list.\n")
fruit = str(input("Enter the fruit name: "))
fruits.append(fruit)

sleep(1)

#Display the list.

print("\nTask-4: Display the list.\n")

sleep(1)

print(fruits)

sleep(1)

# Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.

print("\nTask-5: Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.\n")

while True:
    number = int(input("What is the number?: "))
    if number <= 0 or number > len(fruits): 
        print("Number is not valid")
        continue
    break

sleep(1)

print(number, "  ---  ", fruits[number-1])

sleep(1)

# Add another fruit to the beginning of the list using “+” and display the list.
print("\nTask-6: Add another fruit to the beginning of the list using “+” and display the list.\n")

fruits = ['Kiwi'] + fruits
print(fruits)

sleep(1)

# Add another fruit to the beginning of the list using insert() and display the list.
print("\nTask-7: Add another fruit to the beginning of the list using insert() and display the list.\n")

fruits.insert(0,'Blueberry') 

"""
Display all the fruits that begin with “P”, using a for loop.:
"""

print("\nTask-8: Display all the fruits that begin with “P”, using a for loop.:\n")

sleep(1)

for fruit in fruits:
    if fruit[0] != 'P':
        continue
    print(fruit)


# Series-2: 

print("\nDisplay the list.\n")
print(fruits)

sleep(1)

print("\nRemove the last fruit from the list.\n")
fruits.remove(fruits[-1])

sleep(1)

print("\nDisplay the list.\n")
print(fruits)

sleep(1)

print("\nAsk the user for a fruit to delete, find it and delete it.\n")

sleep(1)

fruits_multiplied = copy(fruits*2)

sleep(1)

while True:
    fruit = input("Enter the fruit to delete(Case sensitive): ")

    if fruit in fruits_multiplied:
        fruits_multiplied.remove(fruit)
        fruits.remove(fruit)
        break
    else: 
        print("There is no such fruit, try again: ")

sleep(1)

print(fruits_multiplied, "\n")
print(fruits, "\n")

# Series-3:

print("Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).")

sleep(1)

fruits_copy = copy(fruits)
    
for fruit in fruits:
    while True:
        answer = input("Do you like {} ?:  ".format(fruit.lower()))
        if answer.upper() == "YES":
            break
        elif answer.upper() == "NO":
            fruits_copy.remove(fruit)
            break
        else: 
            print("Please answer Yes or No")

sleep(1)     

print("\nDisplay the list\n")

sleep(1)

print(fruits_copy)

sleep(1)

#Series-4

print("Make a new list with the contents of the original, but with all the letters in each item reversed.")

sleep(1)

fruit_copy_copy = []

for item in fruits_copy:
    fruit_copy_copy.append(item[::-1])

sleep(1)

print("\nDelete the last item of the original list. Display the original list and the copy.\n")

fruit_copy_copy.remove(fruit_copy_copy[-1])

sleep(1)

print("Original List:  \n", fruits_copy) 
print("Copy: \n", fruit_copy_copy)
