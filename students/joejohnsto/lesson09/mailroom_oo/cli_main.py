# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:13:37 2019

@author: joejo

Object Oriented Mailroom: Command Line Interface (cli)
"""

import sys
import donor_models as dm


# Initialize charity with first donor set
charity = dm.charity('RLC')
donor_db = {'Bill Gates': [4000.32, 35.00, 17899.99],
            'Oprah Winfrey': [9999.99, 9999.99],
            'Rob Schneider': [400.00, 55.00, 800.00],
            'Donald Trump': [0.32, 5.00],
            'Denise Richards': [6040.77]
            }
for k, v in donor_db.items():
    charity.add_donor(k, v)

prompt = "\n".join(("\nWelcome to the mailroom!",
                    "Please choose from below options:",
                    "1 - Enter a new donation and send a thank you",
                    "2 - Create a Report",
                    "3 - Send Thank Yous to All Donors",
                    "4 - quit",
                    ">>> "))


def get_amount(name):
    """Get and return user input donation amount"""
    amount = input(f'Enter the amount that {name} donated or type "q" to quit back to the main menu: ')
    if amount == 'q':
        main()
    try:
        amount = float(amount)
    except ValueError:
        print("You must enter either 'q' or a number!")
        get_amount(name)
    return amount


def get_donor():
    """Get and return user input donor name"""
    response = 'list'
    # get donor name from user, display donor list if asked
    while response == 'list':
        response = input('\nWhat is the full name of the donor to whom you '
                         + 'would like to send a thank you?\nAlternatively, '
                         + 'type "list" for a list of current donors '
                         + 'or "q" to quit back to main menu.\n>>> ')
        if response == 'list':
            print(charity.list_donors())
        elif response == 'q':
            main()
        else:
            check = input(f'Is "{response.title()}" the correct donor name?\n'
                          + 'Please respond "y", "n", or "q" to quit back to main menu: ')
            if check == 'q':
                main()
            elif check != 'y':
                response = 'list'
    return response.title()


def thank_you():
    """Add a new donation to the database and print a thank you email for the donor"""
    name = get_donor()
    amount = get_amount(name)
    if name in charity.Donors.keys():
        charity.Donors[name].add_donation(amount)
    else:
        charity.add_donor(name, [amount])
    ty_note = charity.Donors[name].thank_you_note()
    print('\n' + ty_note)


def print_report():
    """Print the report to the terminal"""
    report = charity.create_report()
    print('\n' + '\n'.join(report))


def write_letters():
    """Write a thank you to every donor and save it to file"""
    charity.write_letters()


def main():
    """Prompt user to choose next action"""

    while True:
        response = input(prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        user_select = {'1': thank_you, '2': print_report, '3': write_letters,
                       '4': sys.exit}
        selection = user_select.get(response, 'Not a valid option!')
        try:
            selection()
        except TypeError:
            print(selection)
            continue


if __name__ == "__main__":
    main()
