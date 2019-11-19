#!/usr/bin/env python
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']


def series1(fruits):
    print("\n SERIES 1 : \n")
    s1fruits = fruits.copy()
    print(s1fruits)
    response = input("Enter to add another fruit to the list > ")
    s1fruits.append(response)
    print(s1fruits)
    response = input(f"Enter an index number 1 - {len(s1fruits)} >")
    print(f" That index = {s1fruits[int(response) - 1]}")

    response = input("Enter a Second fruit to the list > ")
    s1fruits = [response] + s1fruits
    print(s1fruits)

    response = input("Enter Third  fruit to the list > ")
    s1fruits.insert(0, response)
    print(s1fruits)
    pfruits = [fruit for fruit in s1fruits if fruit[0] in ("p", "P")]
    # or
    # pfruits = list(filter(lambda x : x[0] in ("p", "P"), fruits))
    # or
    '''
    pfruit = []
    for fruit in fruits:
        if fruit[0] == "P" or fruit[0] =="p":
            pfruit.append(fruit)
        # or    
        if fruit[0] in ("p", "P"):
            pfruit.append(fruit)
    '''
    print(f"Fruits starting with P {pfruits}")


def series2(fruits):
    print("\n SERIES 2 : \n")
    s2fruits = fruits.copy()
    print(f"Using {s2fruits}")
    removed_fruits = s2fruits.pop()
    print(f"Removed last fruit {s2fruits}")
    response = input("Select a Fruit to delete from list > ")
    s2fruits.remove(response)
    new_fruit_list = s2fruits * 2
    print(new_fruit_list)
    length = len(new_fruit_list)
    found = False
    while found == False:
        response = input("Select a Fruit From to delete,> ")
        remaining_fruits = [x for x in new_fruit_list if x != response]
        if len(remaining_fruits) < length:
            found = True
    print(remaining_fruits)


def series3(fruits):
    print("\n SERIES 3 : \n")
    s3fruits = []
    for f in fruits:
        s3fruits.append(f.lower())
    possable_fruits = s3fruits.copy()
    for fruit in possable_fruits:
        response = input(f"Do you like {fruit}? > ")
        while response not in ('yes', 'no'):
            response = input(f"Please answer only yes or no > ")
        if response == "no":
            s3fruits.remove(fruit)
    print(s3fruits)


def series4(fruits):
    print("\n SERIES 4 : \n")
    s4fruits = fruits.copy()
    new_list = []
    for i in fruits:
        new_list += [i[::-1]]
    s4fruits.pop(-1)
    print(s4fruits)
    print(new_list)


def main(fruits):

    series1(fruits)
    series2(fruits)
    series3(fruits)
    series4(fruits)

if __name__ == '__main__':
        main(fruits)
