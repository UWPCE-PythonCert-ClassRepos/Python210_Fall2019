#!/usr/bin/env python3

# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
# Display the list (plain old print() is fine…).
# Ask the user for another fruit and add it to the end of the list.
# Display the list.
# Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
# Add another fruit to the beginning of the list using “+” and display the list.
# Add another fruit to the beginning of the list using insert() and display the list.
# Display all the fruits that begin with “P”, using a for loop.

# series1
lst1 = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(lst1)
another_fruit = input("Enter another fruit, ya fruit: ")
lst1.append(another_fruit)
print("new list: " + str(lst1))
# need to convert to integer explicitly
fruit_no = int(input("enter fruit location 1-" + str(len(lst1))+": "))
print("number "+str(fruit_no)+": " + str(lst1[fruit_no-1]))
# add fruit to beginning w/ + then insert()
lst1 = ['Watermelons'] + lst1
print("Added Watermelons to the beginning of the list: ")
print(lst1)
# I don't know my fruits
lst1.insert(0, "Pancakes",)
print("Added Pancakes to the begining of list: ")
print(lst1)
print("Fruits that start with P: ")
for i in lst1:
    if i[0] == 'P':
        print(i)

# series2
# Display the list.
# Remove the last fruit from the list.
# Display the list.
# Ask the user for a fruit to delete, find it and delete it.
# (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)

print(lst1)
print("remove last item from list: ")
# remove last
lst1.pop(-1)
print(lst1)
del_fruit = input("Enter a fruit to remove: ")
lst1.remove(del_fruit)
print(del_fruit + " removed, new list: ")
print(lst1)
# Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences
lst1 *= 2
print("Multipled list by 2: ")
print(lst1)
# Never Iterate over a list where you are removing items.
# The Python documents say that it is safer to create a new list
del_fruit = input("Enter a fruit to remove: ")
print("Remove all instances of " + del_fruit + " in the list")
lst2 = []
# Iterate over list and add the element that does not match to a new list
for i in lst1:
    if i != del_fruit:
        lst2.append(i)
lst1 = lst2
print(lst1)

# series3
# Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
# For each “no”, delete that fruit from the list.
# For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
# Display the list.
lst1 = ['Apples', 'Pears', 'Oranges', 'Peaches'] 

for i in lst1[:]:

    ans = input("Do you like {}? ".format(i.lower()))

    while ans not in ("yes", "no"):
        print("yes or no!")
        ans = input("Do you like {}? ".format(i.lower()))
    
    if ans.lower == "no":
        lst1.remove(i)

lst1 = ['Apples', 'Pears', 'Oranges', 'Peaches'] 

#series4    
# Make a new list with the contents of the original, but with all the letters in each item reversed.
# Delete the last item of the original list. Display the original list and the copy.

reverse_lst=[]
for i in lst1:
    reverse_lst.append(i[::-1])
print("Reversed list: " + ", ".join(reverse_lst))
del lst1[-1] 
print("Original list: " + ", ".join(lst1))   