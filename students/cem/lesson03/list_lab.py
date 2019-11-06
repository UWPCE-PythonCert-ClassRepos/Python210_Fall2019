#!/usr/bin/env python3

fruit = ["Apples", "Pears", "Oranges", "Peaches"]


# Series 1
def fruit_selector(fruit):
    print(fruit)
    fruit.append(input("Add a new fruit to the list: "))
    print(fruit)
    entered_num = input("Enter a number and i'll give you the fruit associated: ")
    entered_num = int(entered_num)-1
    index_of_fruit = fruit[entered_num]
    print(index_of_fruit)
    # Add another fruit to the beginning of the list using “+” and display the list.
    fruit.insert(0, input("Add a new fruit to the beginning of the list: "))
    print(fruit)

    # Display all the fruits that begin with “P”, using a for loop.
    for i in fruit:
        if "P" in i:
            print(i)

    return fruit


fruit_selector(fruit)


# Series 2
def exercise2(fruit):
    print(fruit)
    del fruit[-1]
    print(fruit)
    # Ask the user for a fruit to delete, find it and delete it.
    response = input("Pick a fruit to delete: ")
    fruit.remove(response)
    print(fruit)


exercise2(fruit)


# Series 3
def exercise3(fruit):
    for i in fruit:
        response  = print(input("Do you like {}? ".format(i.lower())))
        if response == "no":
            fruit.remove(fruit)


exercise3(fruit)

