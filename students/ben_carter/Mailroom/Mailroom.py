# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 08:47:12 2019

@author: bclas
"""


import sys

"""
This code is for the Mailroom assignment, The code should be include a list of
donors and how much they have donated. It should prompt the user to chose from 
three options 1) send a thank you email, 2) Generate a report, 3)Exit the program
"""

"""
1) Build a dictionary with multiple donors to pull from
2) prompt the user to select 1, 2, or 3
3) in a function construct while loop
"""



donors = {
        "Bernie Sanders": [65234.82, 143.25],
        "Freddie Mercury": [72134.41]
        "Bob Dylan": [540, 9000, 344.23, 231.15, 877]
        "Winston Churchhill":[1874, 1965]
        "Carl Segan": [3245.42, 1996, 1934]
        }


prompt = "\n".join(("\nMailroom Script, Welcome!",
                    "Please Enter 1, 2, or 3 to select an option",
                    "1 ) Send a thank you",
                    "2 ) Generate a donations report",
                    "3 ) Exit the script",
                    " "))

def mailroom():
    """This function will contain the meat of the script which will inform the
    script what function to call based on the users input at the first prompt"""

def build_email():
    """This function generates a thank you email """
    
def Send_thank_you():
    """This function is called when the user inputs option 1. its than askes
    the user for a donors name or takes the list input to display the names
    of all the donors. it does with with a while loop until
    user inputs q to exit"""
    
def report():
    """This function generates a formated report of all donors and some
    information regarding their donations"""
    
def exit_program():
    """This function closes the program"""
    print("Thank you for using the mailroom")
    sys.exit()  
    

if __name__ == "__main__":
    main()