# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 19:50:20 2019

@author: joejo

Mailroom Part I
"""


donor_db = [('Bill Gates', [4000.32, 35.00, 17899.99]),
            ('Oprah Winfrey', [9999.99, 9999.99]),
            ('Rob Schneider', [400.00, 55.00, 800.00]),
            ('Donald Trump', [0.32, 5.00]),
            ('Denise Richards', [6040.77])]

prompt = "\n".join(("Welcome to the mailroom!",
          "Please choose from below options:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - quit",
          ">>> "))


def thank_you():
    response = 'list'
    while response == 'list':
        response = input('What is the full name of the donor to whom you would like to\
                     send a thank you?\nType "list" for a list of current donors.\n')
        if response == 'list':
            for x, y in donor_db:
                print(x)
        
    name = response
    if not [x for x, y in donor_db if x == name.title()]:
        donor_db.append((name.title(), []))

    amount = input(f'Enter the amount that {name.title()} donated: ')
    
    idx = [x for x, y in donor_db].index(name.title())
    donor_db[idx][1].append(float(amount))



if __name__ == "__main__":
    pass