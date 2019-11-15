# -*- coding: utf-8 -*-
"""
Created on Nov 15

@author: joejo

Mailroom Part IV
"""

import sys
import os

donor_db = {'Bill Gates': [4000.32, 35.00, 17899.99],
            'Oprah Winfrey': [9999.99, 9999.99],
            'Rob Schneider': [400.00, 55.00, 800.00],
            'Donald Trump': [0.32, 5.00],
            'Denise Richards': [6040.77]
            }

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
            for _ in donor_db.keys():
                print(_)
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


def build_ty(k, v):
    """Build and format an email thank you letter"""
    ty_info = {'name': k, 'last': v[-1], 'total': sum(v)}
    ty_note = '\n'.join(('Dear Mr/Mrs {name},\n',
                         'Thank you so much for your donation of ${last:.2f}!',
                         'This brings your total lifetime donations to ${total:.2f}!',
                         'We here at RLC (Random Local Charity) really appreciate it!\n',
                         'Sincerely,\n\nBob Saget, CEO of RLC\n'))
    return ty_note.format(**ty_info)


def add_donor(name, amount):
    """Add donor and new donation to database under donor name"""
    if name in donor_db.keys():
        donor_db[name].append(amount)
    else:
        donor_db.update({name: [amount]})


def thank_you():
    """Add a new donation to the database and print a thank you email for the donor"""
    name = get_donor()
    amount = get_amount(name)
    add_donor(name, amount)
    ty_note = build_ty(name, donor_db[name])
    print('\n' + ty_note)


def create_report():
    """Print donor database, sorted by total donation amount"""
    sorted_db = sorted(donor_db.items(), key=lambda x: sum(x[1]), reverse=True)
    # build header line for report
    header = 'Donor Name          | Total Given | Num Gifts | Average Gift'
    separator = '-'*len(header)
    bodyline = '{:20} ${:11.2f}   {:9d}  ${:12.2f}'
    # build the body of the report; a list of donors and info about their gifts
    body = [bodyline.format(sorted_db[i][0], sum(sorted_db[i][1]),
                            len(sorted_db[i][1]),
                            sum(sorted_db[i][1])/len(sorted_db[i][1]))
            for i in range(len(sorted_db))]
    report = (header, separator, *body)
    return report


def print_report():
    """Print the report to the terminal"""
    report = create_report()
    print('\n' + '\n'.join(report))


def write_letters():
    # make directory for letters
    try:
        folder = os.mkdir(os.getcwd() + '\\letters')
    except FileExistsError:
        pass
    folder = os.getcwd() + '\\letters'
    for k,v in donor_db.items():
        ty_note = build_ty(k, v)
        filename = folder + '\\' + k.replace(' ', '_') + '.txt'
        with open(filename, 'w') as letter:
            letter.write(ty_note)


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
