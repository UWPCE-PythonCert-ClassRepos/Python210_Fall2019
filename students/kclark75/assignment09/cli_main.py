#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 06:42:27 2019

@author: kenclark
Class: Python 210A-Fall
Teacher: David Pokrajac, PhD
Assignment -
"""

import OO_mailroom


def main_menu_selection():
    """Request user input and prints options"""
    action = input('''
        Pleaes select one:

            a - Send a thank you
            b - Create a report
            c - Quit
            >''')

    return action.strip()


def print_donors():
    print("Donor list:\n")
    for donor in OO_mailroom.Donor.donor_db:
        print(donor[0])


def find_donor(name):
    """
    find a donor in the donor db
    """
    for donor in OO_mailroom.Donor.donor_db:
        # do a case-insensitive compare
        if name.strip().lower() == donor[0].lower():
            return donor

    return None


def send_thank_you():
    while True:
        name = input("Enter a donor's name "
                     "(or 'list' to see all donors or "
                     "'menu' to exit)> ").title()
        print(name)
        if name == "List":
            print_donors()
        elif name == "menu":
            return
        else:
            break

    while True:
        amount_str = input("Enter a donation amount (or 'menu' to exit) > ")
        if amount_str == "menu":
            return
        # Make sure amount is a valid amount before leaving loop
        amount = int(amount_str)
        break

    donor = find_donor(name)
    if donor is None:
        donor = (name, [])
        OO_mailroom.Donor.donor_db.append(donor)

    donor[1].append(amount)
    print(donor)
    donation = sum(donor[1])

    print(donor_letter_1(donor, donation))


def donor_letter_1(donor, donation):
    """generates donor thank you letter"""
    return ('''
            Dear {}

            Thank you for your very kind donation of ${:.2f}.
            It will be put to very good use helping the youth
            of your nation.

                        Sincerely,
                        The Youth Council
            ''').format(donor[0], donation)


if __name__ == "__main__":
    # main script
    running = True
    while running:
        selection = main_menu_selection()
        if selection == "a":
            send_thank_you()
        elif selection == "b":
            OO_mailroom.DonorCollection.print_donor_report()
        elif selection == "c":
            break
        else:
            print("Error: menu selection is invalid!")
