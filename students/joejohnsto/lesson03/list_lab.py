# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 17:48:34 2019

@author: jjohnston
"""


#IDEA makes each list a function, then have list4 call list3(optionally), list3 call list2, etc

def list1():
    """Build and return a list of fruits"""
    
    fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
    print('Your list is:\n', fruits)
    
    newfruit = input('What fruit would you like to add to the list?\n')
    fruits.append(newfruit.capitalize())
    
    idx = input('Give me a number between 1 and {}:\n'.format(len(fruits)))
    print(int(idx), fruits[int(idx)-1])
    
    fruits = ['Bananas'] + fruits
    print('Your list is:\n', fruits)
    
    fruits.insert(0,'Pineapples')
    print('Your list is:\n', fruits)
    
    for _ in fruits:
        if _[0] == 'P':
            print(_)
    
    return fruits


def list2(fruitlist):
    """Return the input list with some items removed"""
    
    print(fruitlist)
    
    fruitlist = fruitlist[:-1]
    print(fruitlist)
    
    #Next two lines ask for a fruit to remove and remove it
    #badfruit = input('Which fruit in the list should be removed?\n')
    #fruitlist.remove(badfruit.capitalize())
    
    #Next lines are updated from above to continue asking until given a fruit in the list
    #also the fruitlist is doubled for no reason and then both instances of badfruit are removed
    fruitlist = fruitlist*2
    badfruit = ''
    while badfruit.capitalize() not in fruitlist:
        badfruit = input('What fruit sucks?\n')
    while badfruit.capitalize() in fruitlist:
        fruitlist.remove(badfruit.capitalize())
        
    return fruitlist


def list3(fruits):
    """Remove fruits from the list that the user dislikes"""
    
    templist = fruits[:]
    for _ in fruits:
        ans = input('Do you like {}?\n'.format(_.lower()))
        while ans.lower() != 'yes' and ans.lower() != 'no':
            ans = input('Please respond "yes" or "no".\n')
        if ans.lower() == 'no':
            templist.remove(_.capitalize())
        elif ans.lower() == 'yes':
            continue
    fruits = templist
    print(fruits)
    
    return fruits


def list4(fruits):
    """Reverse the spelling of each fruit in the list"""
    
    reverse_fruits = fruits[:]
    for i, f in enumerate(fruits):
        reverse_fruits[i] = f[::-1]
    fruits.pop(-1)
    print(fruits, reverse_fruits, sep='\n')
    


# Code below calls the functions in order so this file will run like a script
fruits = list1()
list2(fruits)
list3(fruits)
list4(fruits)


if __name__ == "__main__":
    pass