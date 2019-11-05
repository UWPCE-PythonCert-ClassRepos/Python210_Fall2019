#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
list_lab.py

@author: philipkorte
"""
# create a list of fruit
fruit_list = ['apples', 'pears', 'oranges', 'peaches']

def series1(my_list):
    fruit_list = my_list
    
    print('This is your fruit list:')
    print(fruit_list)
    
    # ask for a new fruit to add to the list
    new_fruit = input('Please add another fruit to your list: ')
    fruit_list.append(new_fruit)
    print('Your list of fruits has been updated.')
    print(fruit_list)
    
    # ask for a number and display that corrisponding fruit
    count = len(fruit_list)
    valid_num = False
    while not valid_num:
        number = int(input(f'Please give me a number between 1 and {count}. '))
        if number < 1 or number > 5:
            print('That was not a valid number.')
        else:
            print(f'You picked number {number}, which is {fruit_list[number-1]}.')
            # included a list of each item
            for i, e in enumerate(fruit_list): 
                print(i + 1, e)
            valid_num = True
    
    # add another fruit to beginning of list using +
    new_fruit = input('Please add another fruit to your list: ')
    fruit_list = [new_fruit] + fruit_list
    print('Your fruit list has been updated:')
    print(fruit_list)
    
    # add another fruit to the beginning of list using insert
    new_fruit = input('Please add another fruit to your list: ')
    fruit_list.insert(0, new_fruit)
    print('Your fruit list has been updated again:')
    print(fruit_list)
    
    # display all fruits that contain the letter p
    print("Here's a list of all fruit with a p in their name:")
    for fruit in fruit_list:
        if 'p' in fruit:
            print(fruit)
    
    # return the list for series2
    return fruit_list


def series2(my_list):
    fruit_list = my_list
    
    # display the list
    print('Here is your list of fruit:')
    print(fruit_list)
    
    # remove the last fruit from the list
    print("\nLet's remove the last fruit from the list:")
    remove_this = fruit_list[-1]
    fruit_list.remove(remove_this)
    print(fruit_list) 
    
    # ask for a fruit to delete. then remove it
    while True:
        del_fruit = input("What fruit do you want to delete? ")
        if del_fruit in fruit_list:
            fruit_list.remove(del_fruit)
            print(f'{del_fruit} has been removed from the list.')
            print(fruit_list)
            break
        else:
            print('That fruit is not in the list.')

    # multiply list several times, then remove a fruit completely
    fruit_list *= 3
    print("The list has been trippled:")
    print(fruit_list)
    
    del_fruit = input("Pick a fruit to remove again. ")
    while del_fruit in fruit_list:
        fruit_list.remove(del_fruit)
    print('This is what remains of your list:')
    print(fruit_list)
    
        
def series3(my_list):
    fruit_list = my_list
    
    for fruit in fruit_list:
        answer = input(f'Do you like {fruit}? ').lower()
        answer = answer[0]
        if answer == 'y':
            print('Cool, it stays')
        else:
            print(f'{fruit.title()} has been removed.')
            fruit_list.remove(fruit)
    print('This is what remains in your list:')
    print(fruit_list)
        
        
def series4(my_list):
    fruit_list = my_list
      
    # make a new list that is the same as the old list 
    # but with its letters reversed for each item
    tsil_tiurf = []
    for fruit in fruit_list:
        l = len(fruit)
        tsil_tiurf.append(fruit[l::-1])
    
    # delete the last item from the original list
    s = fruit_list[-1]
    fruit_list.remove(s)
    
    print(fruit_list)
    print(tsil_tiurf)
    
    
series1(fruit_list)
series2(fruit_list)
series3(fruit_list)
series4(fruit_list)