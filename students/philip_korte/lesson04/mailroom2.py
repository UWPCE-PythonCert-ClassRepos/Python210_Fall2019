#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mailroom2.py

@author: philipkorte
"""

donors = {'bugs bunny': [50, 50, 75],
          'daffy duck': [25, 25],
          'porky pig': [75],
          'elmor fudd': [50, 25, 25],
          'sylvester': [25, 35],
          'marvin the martian': [100, 100, 80],
          'tweety': [15, 10, 10],
          'yosemite sam': [50]}


def menu_selection(prompt, switch_dict):
    while True:
        response = input(prompt).lower()
        # make sure they can only choose from 4 options of main menu
        if prompt == main_prompt and response not in switch_dict:
            print("Please select a valid option.")
            continue
        elif prompt == sub_prompt and response not in switch_dict:
            send_thanks(response)
        elif switch_dict[response]() == 'exit':
            break


def send_thanks(person='none'):
    if person == 'none':
        menu_selection(sub_prompt, sub_options)
    else:
        if person not in donors:
            donors[person] = []
        donation = input(f'How much did {person.title()} donate? ').lower()

        while True:
            # quit by typing in q
            if donation == 'q':
                # remove new person from donor list before quiting
                if donors[person] == []:
                    del donors[person]
                break
            else:
                donation = float(donation)

                # add amount to donation history of person
                donors[person].append(donation)
                # write a nice thank you note (use function)
                write_letter(person, donation)
                break


def list_donors():
    print('\nList of Donors')
    for key in donors:
        print(' ', key.title())


def write_letter(person, donation, ignore = False):
    thank_you = """
    Dear {},

    On behalf of all of us here at Warner Bros. we would like to
    thank you for your generous donation of ${:.2f}. Your
    contribution will ensure that our services here will continue
    to thrive.

    Wishing you the best,
    The Warners
    """.format(person.title(), donation)
    if not ignore:
        print(thank_you)
    save_letter(person, thank_you)


def save_letter(person, letter):
    from datetime import datetime

    # get date for unique file name
    today = str(datetime.now())[:-7].replace(':', '')

    # create file name
    file_name = (person.lower() + '_' + today).replace(' ', '_') + '.txt'
    print(file_name, "has been created")

    with open(file_name, 'w') as f:
        f.write(letter)


def create_report():
    # create header row
    header = (f'{"Donor Name":25s} | '
              f'{"Total Given":>12s} | '
              f'{"Num Gifts":>12s} | '
              f'{"Average Gift":>12s} |')
    l = len(header)
    print(header)
    print('-' * l)

    # sort the dictionary into a new dictionary
    sorted_donors = dict(sorted(donors.items(), key=lambda e: sum(e[1]),
                                reverse=True))

    # create data summary for each person
    for key, value in sorted_donors.items():
        donor_name = key.title()
        total = sum(value)
        num = len(value)
        avg = total/num
        print(f'{donor_name:25s} | '
              f'${total:11.2f} | '
              f'{num:12d} | '
              f'${avg:11.2f} |')


def send_thanks_all():
    for person, donation in donors.items():
        write_letter(person, sum(donation), True)

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
#save_letter('Bugs Bunny', 'this is an empty file')