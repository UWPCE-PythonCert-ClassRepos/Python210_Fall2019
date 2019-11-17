#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################
# Assignement: 02
# Name: fizz_buzz.py
# Dev: Kenneth Clark
# Date: 10-13-19
# Class: Python210A Winter
# Instructor: David Pokrajac
#############################


"""
Write a program that prints the numbers from 1 to 100 inclusive.
But for multiples of three print “Fizz” instead of the number.
For the multiples of five print “Buzz” instead of the number.
For numbers which are multiples of both three and five print “FizzBuzz” instead.
"""


def fizzbuzz():

    num = 0
    while num < 100:
        num += 1 
        if num % 3 == 0 and num % 5 == 0:
            print ("fizzbuzz")
        elif num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print(num)
        
fizzbuzz()