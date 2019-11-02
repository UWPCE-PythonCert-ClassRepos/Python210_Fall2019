#!/usr/bin/env python3
"""
Created on Mon Oct 28 18:25:04 2019

@author: Bishal.Gupta
"""

#Series 1
fruitlist = ['Apples','Pears','Oranges','Peaches']
print("The list has following fruit", len(fruitlist), "fruits:", fruitlist)

new_fruit = input("What fruit would you like to add? ")

fruitlist.append(new_fruit)

print("The list has following fruit", len(fruitlist), "fruits:", fruitlist)

new_number = input("What number order of fruit would you like to see? ")

new_number = int(new_number)

print("The", new_number, "nd or nth fruits is:", fruitlist[new_number])

fruitlist2 = ['Orange']

fruitlist = fruitlist2 + fruitlist

print("The list has following fruit", len(fruitlist), "fruits:", fruitlist)

fruitlist.insert(0,'Banana')

print("The list has following fruit", len(fruitlist), "fruits:", fruitlist)

for f in fruitlist:
    if 'P' in f:
        print(f)
        
#Series 2        
print("The list has following fruit", len(fruitlist), "fruits:", fruitlist)

fruitlist.pop(-1)

print("The list has following fruit", len(fruitlist), "fruits:", fruitlist)

delete_fruit = input("What fruit would you like to delete? ")

fruitlist.remove(delete_fruit)

print("The list has following fruit", len(fruitlist), "fruits:", fruitlist)

#Series3
fruitlist = ['Apples','Pears','Oranges','Peaches']
print("The list has following fruit", len(fruitlist), "fruits:", fruitlist)

lowercase_fruit = input("Do you like apples? ")
fruit1 = fruitlist[0]
fruit1 = fruit1.lower()
fruitlist = [fruit1,'Pears','Oranges','Peaches']

lowercase_fruit = input("Do you like Pears? ")
fruit2 = fruitlist[1]
fruit2 = fruit2.lower()
fruitlist = [fruit1,fruit2,'Oranges','Peaches']

lowercase_fruit = input("Do you like Oranges? ")
fruit3 = fruitlist[3]
fruit3 = fruit2.lower()
fruitlist = [fruit1,fruit2,fruit3,'Peaches']

lowercase_fruit = input("Do you like Peaches? ")
fruit4 = fruitlist[0]
fruit4 = fruit4.lower()
fruitlist = [fruit1,fruit2,fruit3,fruit4]

print("The list has following fruit", len(fruitlist), "fruits:", fruitlist)


        
        



