#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 06:34:53 2019

@author: matt.denko
"""
# pt 2 description ------------------------------------------------------------

"""Update your mailroom program to:

Use dicts where appropriate.
See if you can use a dict to switch between the user’s selections.
see Using a Dictionary to switch for what this means.
Convert your main donor data structure to be a dict.
Try to use a dict and the .format() method to produce the letter as one big template, 
rather than building up a big string that produces the letter in parts."""

"""File Writing:
    
In the first version of mailroom, you generated a letter to a donor who had 
just made a new donation, and printed it to the screen.

In this version of your program, add a function (and a menu item to 
invoke it), that goes through all the donors in your donor data structure, 
generates a thank you letter for each donor,
 and writes each letter to disk as a text file."""

# importing packages ----------------------------------------------------------
 
import sys
import os

# Creating donor list----------------------------------------------------------

donors = dict()
"Convert main donor data structure to be a dict"

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
    "fixing from pt 1 - actually exiting :)"
    sys.exit()

# Creating home screen text ---------------------------------------------------
    
home_screen_text = ("\nWelcome to the home screen please select one of option 1 through 3:\n"
"1: Make a Thank You\n"
"2: Make a Report\n"
"3: Make a letter\n"
"4: Exit\n")

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
        
# letter prompt ---------------------------------------------------------------

def letter_prompt():
    "function to create letter prompt for custom donor letters"
    line1 = 'To my dearest and special friend {name},\n\n' \
          + 'Thank you for your awe inspiring donation of ${last:.2f}!'
    line2 = 'With this latest personal sacrifice your lifetime donations total is ${total:.2f}!!!!!! ' \
          + 'Best Wishes,\n\nMatthew Denko, Decider of Things\n'
    lp = '\n'.join([line1, line2])
    "returning joined prompt"
    return lp

# writing letters -------------------------------------------------------------
        
def make_letter():
    "function to create custom letter files for each donor"
    try:
        "creating a new folder in the current working directory named thank_you_notes"
        os.mkdir(os.getcwd() + '/donationletters')
        new_folder_string = str(os.getcwd()) + '/donationletters'
    except FileExistsError:
        "exception in case file is already there"
        new_folder_string = str(os.getcwd()) + '/donationletters'
    "loop to create note"
    for i in donors:
        donors2 = donors[i]
        letter_details = {'name': i, 
                   'last': donors2['donation_avg'],
                   'total': donors2['donation_total']}
        file = new_folder_string + '/' + letter_details['name'].replace(' ', '_') + '.txt'
        with open(file, 'w') as letter:
            "using .format() method to produce the letter as one big template"
            letter_note = letter_prompt()
            letter.write(letter_note.format(**letter_details))
        
# home screen summary ---------------------------------------------------------

"See if you can use a dict to switch between the user’s selections"
home_screen_summary = {"1": make_thank_you, "2":make_report, "3":make_letter, "4":exit_program}

# if _name_ == '_main_' block -------------------------------------------------

if __name__ == '__main__':
    "If this is the main file then execute these functions"
    create_donors()
    "create donors function generates donor list"
    home_screen(home_screen_summary)
    """home screen function prints home_screen_summary which contains functions
    for all of the menu prompts"""