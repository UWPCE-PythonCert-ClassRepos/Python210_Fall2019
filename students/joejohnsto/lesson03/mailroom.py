# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 19:50:20 2019

@author: joejo

Mailroom Part I
"""

import sys

donor_db = [('Bill Gates', [4000.32, 35.00, 17899.99]),
            ('Oprah Winfrey', [9999.99, 9999.99]),
            ('Rob Schneider', [400.00, 55.00, 800.00]),
            ('Donald Trump', [0.32, 5.00]),
            ('Denise Richards', [6040.77])]

prompt = "\n".join(("\nWelcome to the mailroom!",
          "Please choose from below options:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - quit",
          ">>> "))


def sort_key(donor):
    return sum(donor[1])


def thank_you():
    """Add a new donation to the database and print a thank you email for the donor"""
    
    response = 'list'
    # get donor name from user, display donor list if asked
    while response == 'list':
        response = input('\nWhat is the full name of the donor to whom you would like to ' + \
                     'send a thank you?\nType "list" for a list of current donors ' + \
                     'or "q" to quit back to main menu.\n>>> ')
        if response == 'list':
            for x, y in donor_db:
                print(x)
        elif response == 'q':
            main()
        else:
            check = input(f'Is "{response.title()}" the correct donor name?\n' + \
                          'Please respond "y", "n", or "q" to quit back to main menu: ')
            if check == 'q':
                main()
            elif check != 'y':
                response = 'list'  
    name = response.title()
    # get donation amount
    amount = input(f'Enter the amount that {name} donated or type "q" to quit back to the main menu: ')
    if amount == 'q':
        main()
    # add donor and new donation to database under donor name
    if not [x for x, y in donor_db if x == name]:
        donor_db.append((name, []))
    idx = [x for x, y in donor_db].index(name)
    donor_db[idx][1].append(float(amount))
    #format an email thank you and print to the terminal
    ty_note = 'Dear Mr/Mrs {},\n\n' + \
                'Thank you so much for your donation of ${:.2f}!\n' + \
                'We here at RLC (Random Local Charity) really appreciate it!\n\n' + \
                'Sincerely,\n\nBob Saget, CEO of RLC\n'
    print(ty_note.format(name, float(amount)))


def create_report():
    """Print donor database, sorted by total donation amount"""
    
    sorted_db = sorted(donor_db, key=sort_key, reverse=True)
    # build header line for report
    header = 'Donor Name          | Total Given | Num Gifts | Average Gift'
    separator = '-'*len(header)
    bodyline = '{:20} ${:11.2f}   {:9d}  ${:12.2f}'
    # build the body of the report; a list of donors and info about their gifts
    body = ['']*len(sorted_db)
    for i in range(len(sorted_db)):
        body[i] = bodyline.format(sorted_db[i][0],sum(sorted_db[i][1]),
            len(sorted_db[i][1]),sum(sorted_db[i][1])/len(sorted_db[i][1]))
    # print out the report
    print(header, separator, sep='\n')
    for i in range(len(sorted_db)):
        print(body[i])
    
    
def main():
    """Prompt user to choose next action"""
    
    while True:
        response = input(prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        if response == "1":
            thank_you()
        elif response == "2":
            create_report()
        elif response == "3":
            sys.exit()
        else:
            print("Not a valid option!")


if __name__ == "__main__":
    main()