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
1) Build a dictionary (as Key=donor name value as donated amount)
with multiple donors to pull from

2) receive user input as 1, 2, or 3

3) contain the following functions within a Main Mailroom function.
this will be a while loop which uses if and elifs based on the users input
can end with an else for inproper input from user

4) send a thank you function called when user inputs 1, (while loop, with
inbedded if elifs) prompts user for a donor or takes 'list' as input and 
displays a list of donors. if donor name given is not in dictionary, add and 
prompt for donation amount, then calls build_email function which will
assemble the thank you message with the donors name and amount of donation

5) generate a report that is cleanly formated when user inputs 2. 
Can use {____:>14} method of string length formating. uses for loop to 
assemble report much like grid printer exercise.

for key, value in dictionary
print {____:>14}

6) exit program input uses sys.exit to close mailroom

"""



donors = {
        "Bernie Sanders": [65234.82, 143.25],
        "Freddie Mercury": [72134.41],
        "Bob Dylan": [540, 9000, 344.23, 231.15, 877],
        "Winston Churchhill":[1874, 1965],
        "Carl Segan": [3245.42, 1996, 1934],
        "Marc Marquez": [120.25, 200, 525, .75]
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
    while True:
        user = input(prompt)
        if user == "1":
            send_thank_you()
        elif user == "2":
            create_report()
        elif user == "3"
            exit_program()
        else:
            print("The input received was not valid. Please input 1, 2, or 3.")    

def build_email(user, donated):
    """This function generates a thank you email """
    
def send_thank_you():
    """This function is called when the user inputs option 1. its than askes
    the user for a donors name or takes the list input to display the names
    of all the donors. it does with with a while loop until
    user inputs q to exit
    
    this function also contains the list_donors() function which will build a 
    list of current donors once the users inputs 1 and than requests the 'list'
    option
    """
    while true:
        user = input("Enter the full name of the donor you want to email, "
                     "\nor type 'list' to see a list of current donors"
                     "\nor type 'q' to return to previous menu:")
        if user == "q":
            break
        elif user == "list":
            list_donors()
        elif user in donors:
            donation = input("Enter the donation amount or 'q' to exit: ") 
            if donation == "q":
                break
            donated = float(donation)
            donors[user].append(donated)
            build_email(user, donated)
        else:
            donation = input("{} not found in donors, Adding donor, enter a donation amount: ".format(user))
            donated = float(donation)
            donors[user] = [donated]
            build_email(user, donated)
    
    
    
    def list_donors():
        """This function prints a list of all current donors"""
        print("\nList of current donors: ".format(len(donors)), '\n', '_'* 20)
        for donor in donors.keys():
            print(f" ", donor)
        print("_" * 20)
    
def create_report():
    """This function generates a formated report of all donors and some
    information regarding their donations"""
    
def exit_program():
    """This function closes the program"""
    print("Thank you for using the mailroom")
    sys.exit()  
    

if __name__ == "__main__":
    main()