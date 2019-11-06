"""
Title: list_lab
Date: 10/25/2019
Dev: K.Shaffer

"""
#!/usr/bin/env python3

# Series 1
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruits)
response = input("What fruit would you like to add to the list?")
fruits.append(response)
print("the updated list is:" + str(fruits))
response = input("please provide a number between 1 and " + str(len(fruits)) + ": ")
print("That number is for " + fruits[int(response)-1])
fruits += ("Pinapples",)
print(fruits)
fruits.insert(0, "Plums")
print(fruits)
for fruit in fruits:
    if fruit[0].lower() == 'p':
        print(fruit)

# Series 2
print(fruits)
fruits.pop()
print(fruits)
response = input("What fruit would you like to delete from the list?")
i = 0
for fruit in fruits:
    if fruit.lower() == response.lower():
        fruits.pop(i)
    i += 1
print(fruits)

# Series 3
i = 0
new_fruits = []
for fruit in fruits:
    s = True
    while s:
        response = input("Do you like " + str(fruit) + "? yes/no?")
        if response == "no" or "yes":
            s = False
    if response.lower() == "yes":
        new_fruits.append(fruit)
    i += 1
fruits = new_fruits
print(fruits)

# Series 4
reversed_Fruits = []
for fruit in fruits:
    fruit = fruit[::-1]
    reversed_Fruits.append(fruit)
reversed_Fruits.pop()
print(reversed_Fruits)
