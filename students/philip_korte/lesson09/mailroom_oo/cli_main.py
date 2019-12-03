#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 11:39:25 2019

@author: philipkorte
"""
import donor_models

initial_donors = {'bugs bunny': [50, 50, 75],
                  'daffy duck': [25, 25],
                  'porky pig': [75],
                  'elmor fudd': [50, 25, 25],
                  'sylvester': [25, 35],
                  'marvin the martian': [100, 100, 80],
                  'tweety': [15, 10, 10],
                  'yosemite sam': [50]}

# load charity
my_charity = Charity('Warner Bros Inc')


# load initial_donors into charity
for donor, donations in initial_donors.items():
    my_charity.add_donor(donor, donations)

def menu_selection(prompt, switch_dict):
    while True:
        response = input(prompt).lower()
        if prompt == main_prompt:
            try:
                if switch_dict[response]() == 'exit':
                    break
            except KeyError:
                print('Please select a valid response.')
                continue
        # when sub-prompt is asked, if response is not either 'list' or 'q'
        # then make that response a donor name
        elif response not in switch_dict:
            send_thanks(response)
        elif switch_dict[response]() == 'exit':
            break

def send_thanks(donor=None):
    if donor is None:
        menu_selection(sub_prompt, sub_options)
    elif donor not in my_charity.donors:
        response = input(f'{donor.title()} has not yet been added to the charity. \nDo you wish to add them? ')
        while True:
            if response[0] == 'y':
                new_donation = float(input(f'How much did {donor.title()} donate? '))
                my_charity.add_donor(donor, [new_donation])
                print(f'{donor.title()} has been added.')
                break
            elif response[0] == 'n':
                print(f'{donor.title()} was not added.')
                menu_selection(sub_prompt, sub_options)
                break
            else:
                print('\nThat was not a valid response.', end='')
                response = input('Do you wish to add them? ')
                continue

    else:
        letter = my_charity.donors[donor].write_thank_you()
        save_letter(donor, letter)
        print(letter)

def save_letter(donor, letter):
    from datetime import datetime

    # get date for unique file name
    today = str(datetime.now())[:-7].replace(':', '')

    # create file name
    file_name = (donor.lower() + '_' + today).replace(' ', '_') + '.txt'
    print(file_name, "has been created")

    with open(file_name, 'w') as f:
        f.write(letter)

def list_donors():
    my_list = my_charity.list_donors()
    print('\n')
    for donor in my_list:
        print(donor.title())

def create_report():
    my_report = my_charity.create_report()
    for line in my_report:
        print(line)

def send_thanks_all():
    for key, value in my_charity.donors.items():
        letter = value.write_thank_you()
        save_letter(key, letter)
        print(letter)
        print('\n\n')

def quit_menu():
    return ("exit")



main_prompt = '''
    Mailroom Program - Menu of Options

        1) Send a thank you to a single donor
        2) Create a report
        3) Send letters to all donors
        4) Quit
>>> '''

main_options = {'1': send_thanks,
                '2': create_report,
                '3': send_thanks_all,
                '4': quit_menu}

sub_prompt = "Who do you wish to send a thank you note to? \
(Type 'list' for list of donors, 'q' to return to main menu): "

sub_options = {'q': quit_menu,
               'list': list_donors}

menu_selection(main_prompt, main_options)