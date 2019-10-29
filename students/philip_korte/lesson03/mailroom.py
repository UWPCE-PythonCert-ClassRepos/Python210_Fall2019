#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mailroom.py

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


def list_donors():
    print('\nList of Donors:')
    for key, value in donors.items():
        print(' ',key.title())
        
def write_letter(person, donation):

    thank_you = f"""
    Dear {person.title()},
    
    On behalf of all of us here at Warner Bros. we would like to
    thank you for your generous donation of ${donation:.2f}. Your
    contribution will ensure that our services here will continue
    to thrive. 
    
    Wishing you the best,
    The Warners
    """
    
    print(thank_you) 
        
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
    sorted_donors = dict(sorted(donors.items(), key=lambda e: sum(e[1]), reverse=True))

    # create data summary for each person
    for key, value in sorted_donors.items():
        donor_name = key.title()
        total = sum(value)
        num = len(value)
        avg = total/num
        print(f'{donor_name:25s} | ${total:11.2f} | {num:12d} | ${avg:11.2f} |')

def send_thanks():
    while True:
        person = input("Who do you wish to send a thank you note to? "+
                       "(Type 'list' for the list of donors). ").lower()
        # quit by typing in q
        if person == 'q':
            break
        elif person == 'list':
            list_donors()
            continue
        else:
            if person not in donors:
                donors[person] = []
        
        donation = input(f'How much did {person.title()} donate? ').lower()
    
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
                

def main():
    while True:
        print(
        '''
    Mailroom Program - Menu of Options
    
        1) Send a Thank You
        2) Create a Report
        3) Quit
        ''')
        choice = input('Which option would you like to choose? ')
        
        # choice 1: send a thank you note
        if choice.strip() == '1':
            send_thanks()
            
        # choice 2: create a report
        elif choice.strip() == '2':
            create_report()
        
        # choice 3: exit program
        elif choice.strip() == '3':
            print('Good-bye')
            break
    
        # invalid choice
        else:
            print("That was not a valid choice.")


# main
main()