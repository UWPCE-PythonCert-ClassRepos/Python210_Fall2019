# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 10:49:34 2019

@author: tdietz
"""

#!/usr/bin/env python3
fruitList = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruitList)

#user adds new fruit to list via text input, uses append() to add new fruit
userInput = input("What additional fruit would you like to add: ")
fruitList.append(userInput)
print(fruitList)

#user chooses number between 1 and 5 then display the fruit corresponding to the number
userInputNumber = input("Please choose a number between 1 and 5: ")
print("Fruit: "+userInputNumber+": "+fruitList[int(userInputNumber)-1])

#add a fruit to the beginning of list using '+' and display
fruitList = (["Pineapple"] + fruitList)
print(fruitList)

#add another fruit using insert() and display
fruitList.insert(0,"Grapes")
print(fruitList)

#display fruits that start with 'P'
newList = []
for i in fruitList:
    if i.startswith('P'):
        newList = [i] + newList
print(newList)

"""Task 2"""
#display list
print(fruitList)
#remove last item
fruitList.pop()
print(fruitList)
userDeleteFruit = input("What fruit should be removed?: ")
fruitList.pop(fruitList.index(userDeleteFruit))
print(userDeleteFruit)
print(fruitList)

"""Task 3"""
for fruit in fruitList:
    userInput = input("Do you like "+fruit+"? (yes/no):")
    while userInput not in ("yes", "no"):
        print("Please choose yes or no")
        userInput = input("Do you like "+fruit+"? (yes/no):")
    if userInput.lower() == "no":
        fruitList.remove(fruit)
print(fruitList)
    
    
"""Task 4"""
fruitList = ['Apples', 'Pears', 'Oranges', 'Peaches']
backwardsFruitList = []
for fruit in fruitList:
    backwardsFruitList.append(i[::-1])
fruitList.pop()
print("Original List", end="")
print(fruitList)
print("Reverse List", end="")
print(backwardsFruitList)
    