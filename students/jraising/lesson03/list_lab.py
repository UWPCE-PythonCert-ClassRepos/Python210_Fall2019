#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 00:52:46 2019

@author: jraising
"""

def series1(fruit):
    print(fruit)
    
    newFruit = input("Which other fruit you want to add?")
    
    fruit.append(newFruit)
    
    print(fruit)
    
    number = int(input("Give a number to see the fruit you will get back: "))
    
    print(fruit[number -1])
    
    new_fruit_list = ['Plum']
    
    print(new_fruit_list + fruit)
    
    (fruit.insert(0, 'Pomo'))
    print(fruit)
    
    return fruit
    
result = series1(['Apples', 'Pears', 'Oranges', 'Peaches'])
print (result)

def series2(fruit):
    print(fruit)
    fruit.pop()
    print(fruit)
    
    delete_fruit = input("Which fruit you want to delete? ")
    fruit.remove(delete_fruit)
    print(fruit)
    
    
    
    



def series3(fruit):
    for i in fruit[:]:
        
        like_fruit = input("Do you like {} ?".format(i)).strip().lower()
            
        while like_fruit not in ("yes","no"):
            print("Enter a valid input")
            like_fruit = input("Do you like {} ?".format(i))
            
        if like_fruit.lower() == "no":   
            fruit.remove(i)
           
    print(fruit)
            




def series4(fruit):
    rev_fruit = []
    for i in fruit:
        rev_fruit.append(i[::-1])
    print(rev_fruit)
    fruit.pop()
    print(fruit)    
    
    
    
series4(['Apples', 'Pears', 'Oranges', 'Peaches'])
