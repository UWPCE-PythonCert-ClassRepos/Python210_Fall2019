# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""Write a program that prints the numbers from 1 to 100 inclusive.
But for multiples of three print “Fizz” instead of the number.
For the multiples of five print “Buzz” instead of the number.
For numbers which are multiples of both three and five print “FizzBuzz” instead."""

def fizzbuzz()
    """ Module Counts up from 1 to 100, for multiples of 5 it prints Buzz
    For multiples of 3 it prints Fizz, For multiples of both 3 and 5 it prints
    FizzBuzz"""    

    for num in range(1,100):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
 
    
if __name__ == "__main__":
"""    
for i in range(1,101):
    fb = ''
    if i%3 == 0:
        fb +="Fizz"
    if i%5 == 0:
        fb +="Buzz"
    if fb:
        print(fb)
    else:
        print(i)
"""