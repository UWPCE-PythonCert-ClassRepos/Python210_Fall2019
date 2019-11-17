#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##############################
# Assignement03: list_lab.py
# Dev: Kenneth Clark
# Date: 10-25-19
# Class: Python210A Winter
#############################


"""
Series 1
Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
Display the list (plain old print() is fine…).
Ask the user for another fruit and add it to the end of the list.
Display the list.
Ask the user for a number and display the number back to the user and
    the fruit corresponding to that number (on a 1-is-first basis). 
    Remember that Python uses zero-based indexing, so you will need to correct.
Add another fruit to the beginning of the list using “+” and display the list.
Add another fruit to the beginning of the list using insert() and
    display the list.
Display all the fruits that begin with “P”, using a for loop.

Series 2
Using the list created in series 1 above:
Display the list.
Remove the last fruit from the list.
Display the list.
Ask the user for a fruit to delete, find it and delete it.
(Bonus: Multiply the list times two. Keep asking until a match is found.
     Once found, delete all occurrences.)

Series 3
Again, using the list from series 1:
Ask the user for input displaying a line like “Do you like apples?” 
    for each fruit in the list (making the fruit all lowercase).
For each “no”, delete that fruit from the list.
For any answer that is not “yes” or “no”, prompt the user to answer with 
    one of those two values (a while loop is good here)
Display the list.

Series 4
Once more, using the list from series 1:
Make a new list with the contents of the original, 
    but with all the letters in each item reversed.
Delete the last item of the original list. 
    Display the original list and the copy.
"""    


currentInv = ["Apples", "Pears", "Oranges", "Peaches"]

def mainMenu():
    """User selects number corrosponging to initiat next action"""
    
    usrChoice = str
    
    while usrChoice != ("0"):
        print("#" * 45)
        print(
            "Please select one of the following options:\n"
            "0. To exit\n"
          "1. Print Current inventory\n"
          "2. Add item to inventory\n" 
          "3. Select Number and return item in inventory\n"
          "4. Select letter and return inventory item\t starting with letter\n"
          "5. Remove last item from list\n"
          "6. Select item to remove from inventory\n"
          "7. Do you like item?\n"
          "8. Reverse letters of inventory item\n"
          "9. Remove last item from list(Same as number 6)\n"
          )
        print("#" * 45)
        usrChoice = input("Please select an action: ")
        if usrChoice == ("1"):
            printInventory(currentInv)
        elif usrChoice ==("2"):
            addInventory(currentInv)
        elif usrChoice ==("3"):
            invItem(currentInv)
        elif usrChoice ==("4"):
            searchInv(currentInv)
        elif usrChoice ==("5"):
            rmvLast(currentInv)    
        elif usrChoice ==("6"):
            rmvItem(currentInv)
        elif usrChoice ==("7"):
            askYn(currentInv)
        elif usrChoice ==("8"):
            letReverse(currentInv)
        elif usrChoice ==("9"):
            rmvLast2(currentInv)
        elif usrChoice ==("0"):
            print("Thank You Good Bye!!")


"""Series 1"""        
def printInventory(currentInv):
    """1. Returns current inventory"""
    print("Your current inventory is: ")
    for i in currentInv:
        print(i)
    print("\n")


def addInventory(currentInv):
    """2. Add another item to the beginning of the list"""
    print("You have requested to add an item to your inventory\n")
    usrInput = input("Please input another fruit: ")
    newList = [usrInput] + currentInv
    currentInv.insert(0,usrInput)
    print("Using + to add item: \n", currentInv)
    print("Using .insert to add item: \n ", newList)
    print("\n")

    
def invItem(currentInv):
    """3. Returns number of items in inventory.  User then selects number, function
    then returns item in list based on user input"""
    print("You have", len(currentInv), "items in your inventory")
    item = (int(input("Plese select an item number: ")))
    print(currentInv[item])
    print("\n")

def searchInv(currentInv):
    """4. Displays item that begins with user intered letter"""
    print("Displays fruit that begins with user input") 
    item = input("Please choose a letter: ")
    for i in currentInv:
        if i[0] == item:
            print(i)
    print("\n")
            

"""Series 2"""
def rmvLast(currentInv):
    """5. Removes last inventory item from list"""
    item = currentInv[-1]
    print("Current inventory is: \n", currentInv, "\n")
    print("Removing last item on inventory list: \n")
    currentInv.remove(item)
    print(item, "was removed from inventory.\n Current inventory is:\n ")
    print(currentInv, "\n")
    

def rmvItem(currentInv):
    """6. Removes user intered item from list"""
    print(currentInv)
    usrInput = input("Please enter item you would like removed from list: ")
    currentInv.remove(usrInput)
    deletedItem = currentInv
    print(usrInput, "where removed from inventory. Current inventory is:\n ")
    print(deletedItem, "\n")

    
"""Series 3"""
def askYn(currentInv):
    """7. Ask user if he likes inventory item. If yes keeps item, if no
    removes item from inventory"""
    a = 0
    x = len(currentInv)
    while a < x:
        item = (currentInv[a])
        usrInput = input("Do you like " + item + "?")
        if usrInput == "y":
            print("Nice")
            a += 1
            #print(a, x)        #For debugging counting method
        elif usrInput == "n":
            currentInv.remove(item)
            print("Sorry to hear that!!\n")
            print("Current inventory is:\n", currentInv)
            x -= 1
        elif usrInput != "y" or "n":
            print("Please answer 'y' or 'n':\n")
    print("\n", "Thank you for you input!")
    

"""Series 4"""
def letReverse(currentInv):
    """8. Reverses letters in inventory"""
    a = len(currentInv)
    b = 0
    while b < a:
        item = currentInv[b]
        print(item[::-1])
        b += 1
        

def rmvLast2(currentInv):
    """9. Remove last item and print original (same as number 6)"""
    item = currentInv[-1]
    print("Current inventory is: \n", currentInv, "\n")
    print("Removing last item on inventory list: \n")
    currentInv.remove(item)
    print(item, "was removed from inventory.\n Current inventory is:\n ")
    print(currentInv, "\n")
    
        
    
    
mainMenu()

print("End Program")



