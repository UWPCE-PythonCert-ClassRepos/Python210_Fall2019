#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 13:46:56 2019

@author: philipkorte
"""

# Python Pushups

"""
The parameter weekday is True if it is a weekday, and the parameter vacation is 
True if we are on vacation. We sleep in if it is not a weekday or we're 
on vacation. Return True if we sleep in.
"""
def sleep_in(weekday, vacation):
    if weekday == False and vacation == False:
        answer = True
    elif weekday == True and vacation == False:
        answer = False
    elif weekday == False and vacation == True:
        answer = True
    elif weekday == True and vacation == True:
        answer = False
    print(answer)

"""
We have two monkeys, a and b, and the parameters a_smile and b_smile indicate 
if each is smiling. We are in trouble if they are both smiling or if neither 
of them is smiling. Return True if we are in trouble.
"""
def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        trouble = True
    elif not a_smile and not b_smile:
        trouble = True
    else:
        trouble = False
    print(trouble)

"""
Given two int values, return their sum. Unless the two values are the same, 
then return double their sum.
"""
def sum_double(a, b):
    if a == b:
        answer = 2 * (a + b)
    else: 
        answer = a + b
    print(answer)

"""
Given an int n, return the absolute difference between n and 21, except 
return double the absolute difference if n is over 21.
"""
def diff21(n):
    if n > 21:
        answer = 2 * abs(21 - n)
    else:
        answer = abs(21 - n)
    print(answer)

"""
We have a loud talking parrot. The "hour" parameter is the current hour time 
in the range 0..23. We are in trouble if the parrot is talking and the hour 
is before 7 or after 20. Return True if we are in trouble.
"""
def parrot_trouble(talking, hour):
    if talking and (hour < 7 or hour > 20):
        trouble = True
    else:
        trouble = False
    print(trouble)
    
"""
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
"""
def makes10(a, b):
    if a == 10 or b == 10:
        answer = True
    elif a + b == 10:
        answer = True
    else:
        answer = False
    print(answer)

"""
Given an int n, return True if it is within 10 of 100 or 200. 
Note: abs(num) computes the absolute value of a number.
"""
def near_hundred(n):
    if abs(100 - n) <= 10 or abs(200 - n) <= 10:
        answer = True
    else:
        answer = False
    print(answer)
    
"""
Given 2 int values, return True if one is negative and one is positive. 
Except if the parameter "negative" is True, then return True only if both 
are negative.
"""
def pos_neg(a, b, negative):
    if negative:
        if a < 0 and b < 0:
            answer = True
        else:
            answer = False
    else:
        if (a < 0 and b > 0) or (a > 0 and b < 0):
            answer = True
        else:
            answer = False
    print(answer)

"""
Given a string, return a new string where "not " has been added to the front. 
However, if the string already begins with "not", return the string unchanged.
"""
def not_strings(str):
    if len(str) >= 3 and str[:3] == 'not':
        answer = str
    else:
        answer = 'not ' + str
    print(answer)

"""
Given a non-empty string and an int n, return a new string where the char 
at index n has been removed. The value of n will be a valid index of a char 
in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
"""
def missing_char(str, n):
    first = str[:n]
    second = str[n+1:]
    answer = first + second
    print(answer)
    
"""
Given a string, return a new string where the first and last chars have been 
exchanged.
"""    
def front_back(str):
    if len(str) <= 1:
        answer = str
    a = str[0]
    b = str[-1]
    c = str[1:-1]
    answer = b + c + a
    print(answer)
    
"""
Given a string, we'll say that the front is the first 3 chars of the string. 
If the string length is less than 3, the front is whatever is there. 
Return a new string which is 3 copies of the front.
"""
def front3(str):
    if len(str) < 3:
        front = str
    else:
        front = str[:3]
    answer = 3*front
    print(answer)

#sleep_in(True, False)
#monkey_trouble(False, False)
#sum_double(4, 5)
#diff21(5)
#parrot_trouble(True, 20)
#makes10(9, 10)
#near_hundred(89)
#pos_neg(-1,-1,True)
#not_strings('candy')
#missing_char('khloe', 2)
#front_back('taco')
front3('morning')