#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 4 18:18:52 2019

@author: matthewdenko
"""
# mailroom OOO description ----------------------------------------------------

"""Goal: Refactor the mailroom program using classes to help organize the code.

The functionality is the same as the earlier mailroom:

Mailroom Part 1

But this time, we want to use an OO approach to better structure the code to 
make it more extensible.

It was quite reasonable to build the simple mailroom program using a single 
module, a simple data structure, and functions that manipulate that data 
structure. In fact, you’ve already done that :-)

But if one were to expand the program with additional functionality, it 
would start to get a bit unwieldy and hard to maintain. So it’s a pretty good 
candidate for an object-oriented approach."""

# importing packages-----------------------------------------------------------

from datetime import datetime
"Here I am loading the Donor Sub Class from the donor_models file"
from donor_models import Donor_Sub_Class

# execute program -------------------------------------------------------------

"generating donor group from donor sub class list"
donor_group = Donor_Sub_Class("Matt's very generous donor group")

"creating initial list of donors"
base_list = {'Santa Claus': [1000000000, 15],
'Rudolf': [15006, 40, 9600000],
'Frosty': [30],
'Grinch': [500],
'Buddy the Elf': [6, 40, 119600000]}

"loading the initial list inside of the donor group"
for donor, donations in base_list.items():
    donor_group.create_donor(donor, donations)

def control_panel(prompt, switch_dict):
    "function for main menu and switching between functions"
    while True:
        "while in menu always prompt an input"
        response = input(prompt).lower()
        if prompt == main_prompt:
            try:
                if switch_dict[response]() == 'exit':
                    break
            except KeyError:
                "Adding error handling in case of incorrect list reference"
                print('Please select a valid response.')
                continue
        elif response not in switch_dict:
            "show sub response in case of use not selecting existing menu option"
            create_thank_you(response)
        elif switch_dict[response]() == 'exit':
            break

def create_thank_you(donor=None):
    "function to create a thank you for an individual donor"
    if donor is None:
        "If you do not eneter a donor - then return to main page"
        control_panel(sub_prompt, sub_options)
    elif donor not in donor_group.donor_list:
        response = input(f'{donor.title()} Has not donated crap. Do you want them to donate yes/no ')
        while True:
            if response[0] == 'yes':
                "If the user responds yes, that they want to add a new donation then ask for how much"
                new_donation = float(input(f'How much did {donor.title()} donate?  '))
                donor_group.create_donor(donor, [new_donation])
                print(f'{donor.title()} has been added.')
                break
            elif response[0] == 'no':
                "If the user does not want to donate then do nothing"
                print(f'{donor.title()} Ok thanks for waisting my time.')
                "return to the main menu"
                control_panel(sub_prompt, sub_options)
                break
            else:
                print('\nThat was not a valid response.', end='')
                response = input('Do you wish to add them? ')
                continue
    else:
        "If donor already exists than create a regular thank you"
        letter = donor_group.donor_list[donor].create_thank_you_letter()
        "save the thank you letter"
        store_thank_you(donor, letter)
        "print the thank you letter"
        print(letter)

def store_thank_you(donor, letter):
    "function to save thank you note in local folder"
    today = str(datetime.now())[:-7].replace(':', '')
    "create the name of the file"
    file_name = (donor.lower() + '_' + today).replace(' ', '_') + '.txt'
    print(file_name, "has been created")
    "opening and writing file to local"
    with open(file_name, 'w') as f:
        f.write(letter)

def print_donors():
    "fucntion to print the list of donors that are in the current list"
    my_list = donor_group.print_donors()
    print('\n')
    for donor in my_list:
        print(donor.title())

def make_report():
    "function to print out the details of each donation for a report"
    my_report = donor_group.create_report()
    "calling create report fuction from Donors class"
    for line in my_report:
        print(line)

def create_thanks_all():
    "function to send a thank you to each donor in group"
    for key, value in donor_group.donor_list.items():
        letter = value.create_thank_you_letter()
        store_thank_you(key, letter)
        print(letter)
        print('\n\n')

def quit_everything():
    "function to quit the program"
    return ("exit")


# Menu prompt -----------------------------------------------------------------

"creating main prompt to be shown in main menu"
main_prompt = '''
    Mailroom Program - Menu
        1) Send thank you - single donor
        2) Create a report
        3) Send thank you - all donors
        4) Quit
>>> '''

"Creating options which line up to functions above"
main_options = {'1': create_thank_you,
                '2': make_report,
                '3': create_thanks_all,
                '4': quit_everything}

"Creating sub prompt for users who do not enter correctly"
sub_prompt = "Who do you wanna make a thank you note for? \
(Please enter 'list' for the group of donors and 'q' to return to main menu): "

sub_options = {'q': quit_everything,
               'list': print_donors}

# if name == main block -------------------------------------------------------

"if name == main block - this code is intended to be the main program to run"
if __name__ == "__main__":
    control_panel(main_prompt, main_options)