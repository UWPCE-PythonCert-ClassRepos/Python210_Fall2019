#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 20:41:22 2019
assignment 03: mailroom.py
Class: Python210 fall quater


@author: kenclark
"""

"""
The program part 1: write a small command-lind script.
This script should be executable. The script shoud accomplish the following
goals:
1. It should have a data structure that holds a list of your donors and a
    history of the amount they have donated. This structure should be populated
    at first with at least five donors, with between 1 and 3 donations each.
    You can store that data structure in the global namespase.
2. The script should prompt the user(you) to choose from a menu of 3 actions:
    "send a thank you", "create a report" or "quit".

Mailroom 2 - Update your mailroom program to:

Use dicts where appropriate.
See if you can use a dict to switch between the user’s selections.
Done - Convert your main donor data structure to be a dict.
Try to use a dict and the .format() method to produce the
     letter as one big template, rather than building up a big string that
     produces the letter in parts.

"""


donor_db = {'William Gates III': [653777.32, 12.17],
            'Paul Allen': [633.23, 43.87, 1.32],
            'Jeff': [100.20],
            'Mark Zuckerberg': [1663.23, 4300.87, 10432.0]}


def print_donors():
    # print donor list
    print("Donor list:\n")
    for donor in donor_db:
        print(donor)


def find_donor(name):
    """
    find a donor in the donor db
    """
    for donor in donor_db.keys():
        # do a case-insensitive compare
        if name.strip().lower() == donor[:].lower():
            return donor
    return None


def main_menu_selection():
    """Request user input and prints options"""
    #action = ''
    while True:
        try:
            usr_input = input('''
                Pleaes select one:

                    a - Send a thank you
                    b - Create a report
                    c - Letter to all donors
                    x - Quit
                    > ''')

            menu_dict = {'a': send_thank_you, 'b': print_donor_report,
                         'c': all_donor_letters, 'x': exit}

            selection = menu_dict[usr_input]
            selection()
        except KeyError:
            print("That is not an option. Please select from the"
                  " options above.")


def gen_letter(donor, amount):
    """
    generates donor thank you letter
    and save new letter in txt file.
    """

    letter = ('''
    Dear {}


    Thank you for your very kind donation of ${:.2f}.
    It will be put to very good use helping the youth
    of your nation.

                Sincerely,
                The Youth Council
    ''').format(donor[:], amount)

    print(letter)  # print letter to screen

    # Create letter txt file with donor name
    with open(donor + '_donor_letter.txt', 'w+') as f:
        f.write(letter)


def all_donor_letters():
    # Generates letter and txt file for all donors using sum of donotations.
    for donor in donor_db:
        total_sum = sum(donor_db[donor])
        """
        generates donor thank you letter
            and save new letter in txt file.
        """

        letter = ('''
        Dear {}


        Thank you for your very kind donation of ${:.2f}.
        It will be put to very good use helping the youth
        of your nation.

                    Sincerely,
                    The Youth Council
        ''').format(donor[:], total_sum)

        print(letter)  # print letter to screen

        # Create letter txt file with donor name
        with open(donor + '_donor_letter.txt', 'w+') as f:
            f.write(letter)


def send_thank_you():
    while True:
        name = input("Enter a donor's name"
                     "(or 'search' to see all donors or 'menu' to exit)>")
        if name == "search":
            print_donors()
        elif name == "menu":
            return
        else:
            break

    while True:
        try:
            amount_str = input("Enter a donation amount"
                               "(or 'menu' to exit) > ")
            if amount_str == "menu":
                return
            # Make sure amount is a valid amount before leaving loop
            amount = float(amount_str)
            break
        except ValueError:
            print("That is not a valid entry. Please enter a dollar amount.")

    donor = find_donor(name)
    if donor is None:
        donor_db[name] = [amount]
        print(gen_letter(name, amount))
    else:
        donor_db[donor].append(amount)
        print(gen_letter(donor, amount))


def sort_key(item):
    donor = find_donor(item[0])
    return sum(donor[1])


def print_donor_report():

    """
    Generates report of donors and donation amounts.
    """

    report_rows = []
    for donor in donor_db:
        total_sum = sum(donor_db[donor])
        num_gifts = len(donor_db[donor])
        avg_gift = total_sum / num_gifts
        report_rows.append((donor, total_sum, num_gifts, avg_gift))

    print("\n" + "-" * 66)
    print("{:25s} | {:11s} | {:9s} |{:12s}".format(
            "Donor Name", "Total Given", "Num Gifts", "avg_gift"))
    print("-" * 66)
    for row in report_rows:
        print("{:25s}  {:11.2f}  {:9d} {:12.2f}".format(*row))


if __name__ == "__main__":
    main_menu_selection()