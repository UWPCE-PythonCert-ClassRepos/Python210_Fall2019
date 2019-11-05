# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 18:54:44 2019

@author: bclas
"""

import sys

"""
This code is for the Mailroom assignment, The code should be include a list of
donors and how much they have donated. It should prompt the user to chose from 
three options 1) send a thank you email, 2) Generate a report, 3)Exit the program
"""
#The inital donor data structure 
donors = {
        "Bernie Sanders": [65234.82, 143.25],
        "Bill Gates": [72134.41]
        "Paul Allen": [540, 9000, 344.23, 231.15, 877]
        "Winston Churchhill":[1874, 1965]
        "Carl Segan": [3245.42, 1996, 1934]
        }


prompt = "\n".join(("\nMailroom Script, Welcome!",
                    "Please Enter 1, 2, or 3 to select an option",
                    "1 ) Send a thank you",
                    "2 ) Generate a donations report",
                    "3 ) Exit the script",
                    " "))

def email():
    """This function generates a thank you email with two arguments"""
    
def report():
    """This function generates a formated report of all donors and some information regarding their donations"""
    
def exit_program():
    """This function closes the program"""
    print("Thank you for using the mailroom")
    sys.exit()  
    

if __name__ == "__main__":
    main()