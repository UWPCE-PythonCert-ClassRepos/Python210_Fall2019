#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 07:31:39 2019

@author: matt.denko
"""

# Assignment Description ------------------------------------------------------

"""The Program: Part 1

Write a small command-line script called mailroom.py. 
This script should be executable. 
The script should accomplish the following goals:

It should have a data structure that holds a list of your donors and a history 
of the amounts they have donated. This structure should be populated at first 
with at least five donors, with between 1 and 3 donations each. You can store that data structure in the global namespace.
The script should prompt the user (you) to choose from a menu of 3 actions: “Send a Thank You”, “Create a Report” or “quit”."""

"""Send a Thank You
If the user (you) selects “Send a Thank You” option, prompt for a Full Name.
If the user types list show them a list of the donor names and re-prompt.
If the user types a name not in the list, add that name to the data structure and use it.
If the user types a name in the list, use it.
Once a name has been selected, prompt for a donation amount.
Convert the amount into a number; it is OK at this point for the program to crash if someone types a bogus amount.
Add that amount to the donation history of the selected user.
Finally, use string formatting to compose an email thanking the donor for their generous donation. Print the email to the terminal and return to the original prompt.
It is fine (for now) for the program not to store the names of the new donors that had been added, in other words, to forget new donors once the script quits running."""


"""If the user (you) selected “Create a Report,” print a list of your donors, sorted by total historical donation amount.
Include Donor Name, total donated, number of donations, and average donation amount as values in each row. You do not need to print out all of each donor’s donations, just the summary info.
Using string formatting, format the output rows as nicely as possible. The end result should be tabular (values in each column should align with those above and below).
After printing this report, return to the original prompt.
At any point, the user should be able to quit their current task and return to the original prompt.
From the original prompt, the user should be able to quit the script cleanly.
Your report should look something like this:"""

# Creating donor list----------------------------------------------------------

donors = dict()
"donors will be a dictionary"

def new_donor(name, total=0, gifts=0, avg_gift=0):
    "function to add new donor to dictionary - along with average gift, total gift, number of gifts"
    if name not in donors:
        "if donor not in original list then add it to list, if it already exists do nothing"
        if gifts > 0:
            "If gift value is 0 or less do not add - not a valid donation"
            avg_gift = round(total/gifts, 2)
        donors[name] = {'donation_total':round(total, 2), 'donation_ct':int(gifts), 'donation_avg':avg_gift}


def create_donors():
    "function to create donor list, col1 - donor, col2 - average gift, col3 - number of gifts"
    new_donor("Dennis Rodman", 1111, 1)
    new_donor("Suge Knight", 2222.22, 2)
    new_donor("Dumbledore", 33333.33, 3)
    new_donor("Grizzly Adams", 44444, 1)
    new_donor("Bob Evans", 555,2)
    new_donor("Barron Trump", 66.55, 1)

# exit program ----------------------------------------------------------------

def exit_program():
    "Creating a function to exit and stop program at any time"
    print("Now exiting....goodbye\n")

# Creating home screen text ---------------------------------------------------
    
home_screen_text = ("\nWelcome to the home screen please select one of option 1 through 3:\n"
"1: Make a Thank You\n"
"2: Make a Report\n"
"3: Exit\n")

def create_thank_you_note(name,amount):
    "custom thank you note to automatically send the option is chose"
    print(f"\nTo my dearest {name}:\n\n Thank you so much for your giant donation of ${amount}.",\
    "We are extremely thankful for your donation.\n\n.")

# home screen function creation -----------------------------------------------

def home_screen(_):
    "function to print text of home screen - unless an action is chosen"
    while True:
        print(home_screen_text)
        action = input("")
        if action in _:
            _[action]()
            if action == "exit":
                 "if action is exit chosen then break this function"
                 break
# creating custom thank you function ------------------------------------------
                 
donor_new = ()
def make_thank_you():
    """"Function to create custom thank you note for donor, the function also
    prompts user to add a new donor and will add the donor to the existing 
    dictionary if it does not already exist"""
    user_text = ""
    thank_you = """"To go to home screen please enter 'exit'.
    \nType the name of a  donor or type 'donors' to view list of donors\n"""
    while user_text != "exit":
        user_text = input(thank_you)
        while user_text == "donors":
            for name in donors:
                print(name)
            user_text = input(thank_you)
        if user_text == "exit":
            break
        donation_amount = input("Please enter donation amount: ")
        if donation_amount == "exit":
            break
        if user_text not in donors:
           "if the users input is a donor not in the current list then add it"
           donor_new = new_donor(user_text)
        donors[user_text]['donation_total'] += float(donation_amount)
        "total as a float"
        donors[user_text]['donation_ct'] += 1
        "count as an int"
        donors[user_text]['donation_avg'] = donors[user_text]['donation_total']/donors[user_text]['donation_ct']
        "avg will be a float due to dividing by float"
        create_thank_you_note(user_text,donation_amount)
        user_text = "q"

# making report ---------------------------------------------------------------
        
def make_report():
    """Function to create a custom report if the action is choosen by the user.
    The report will contain the donation total, the count of donations, and the
    average donation for each donor"""
    output = sorted(donors.items(), key = lambda e: e[1]['donation_total'], reverse=True)
    print("Donor Name"," Total Given     -      Num Gifts -           Average Gift")
    for item in output:
        print("{:25}  ${:>11.2f}{:>12d}  ${:>12.2f}".format(item[0], 
        item[1]['donation_total'], item[1]['donation_ct'], item[1]['donation_avg']))
        
# home screen summary ---------------------------------------------------------

home_screen_summary = {"1": make_thank_you, "2":make_report, "3":exit_program}

# if _name_ == '_main_' block -------------------------------------------------

if __name__ == '__main__':
    "If this is the main file then execute these functions"
    create_donors()
    "create donors function generates donor list"
    home_screen(home_screen_summary)
    """home screen function prints home_screen_summary which contains functions
    for all of the menu prompts"""