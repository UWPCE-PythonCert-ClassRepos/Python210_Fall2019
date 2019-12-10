# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 15:10:44 2019

@author: bclas
"""
"""
this module is effectively the main mailroom structure it handles 
the program flow, it takes inputs and calls all functions/properties/methods
from the other mailroom files
"""


def mailroom():
    """This function will contain the meat of the script which will inform the
    script what function to call based on the users input at the first prompt"""
    #this will need refactoring to mate with new class structure. 
    while True:
        user = input(prompt)
        if user == "1":
            print(send_thank_you())
        elif user == "2":
            print(create_report())
        elif user == "3":
            print(all_donors())
        elif user == "4":
            exit_program()
        else:
            print("The input received was not valid. Please input 1, 2, or 3.")    

def send_thank_you():
    """This function is called when the user inputs option 1. its than asks
    the user for a donors name or takes the list input to display the names
    of all the donors. it does with with a while loop until
    user inputs q to exit
   
    this function also contains the list_donors() function which will build a
    list of current donors once the users inputs 1 and than requests the 'list'
    option
    """
    #
    while True:
        try:
            user = input("Enter the full name of the donor you want to email, "
                         "\nor type 'list' to see a list of current donors"
                         "\nor type 'q' to return to previous menu:")
            if user == "q":
                break
            elif user == "list":
                return list_donors()
            elif user in donors:
                donation = input("Enter the donation amount or 'q' to exit: ")
                if donation == "q":
                    break
                else:
                    return build_email(user, add_donation_to_donor(user, donation))      
            else:
                donation = input("{} not found in donors, Adding donor, enter a donation amount: ".format(user))
                return build_email(user, add_donation_to_donor(user, donation))
        except ValueError:
            #print("Value Error: The donation amount must be a integer, enter a donation amount (e.g. 100 or 25.50):")
            donation = input("Value Error: The donation amount must be a integer, enter a donation amount (e.g. 100 or 25.50):")
            return build_email(user, add_donation_to_donor(user, donation))

def exit_program():
    """This function closes the program"""
    print("Thank you for using the mailroom")
    sys.exit()  
   