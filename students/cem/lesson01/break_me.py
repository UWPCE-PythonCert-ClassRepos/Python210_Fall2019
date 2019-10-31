#!/usr/bin/env python3

# Exceptions

"""This will generate a NameError
The interpreter does not recognise a local or global object name
that has been provided in the Python source code
Change x to i to fix"""
for i in "word":
    print(x)

# '''This will generate a TypeError
# Raised when a function or operation is applied to an object of an incorrect type
# You cannot add a string and a number
# '''
# '2'+2

# '''SyntaxError - Did not add " " in between the printed string'''
# for i in range(5):
#     print(The number is: , i)

# """AttributeError
# Attempting to access an attribute on an object that does not exist"""
# word = "hello"
# word.append = "world"

# list = ['words', 'are']
# list.append('fun')
# print(list)

# ''' IndexError '''
# try:
#     transportation = ["car", "bike", "bus"]
#     print(transportation[4])
# except IndexError as e:
#     print("The value in the list you are trying does not exist, please try a smaller ID number.")
