'''
Script: cli_main.py
Date: 11/24/2019
Dev: Kory Shaffer
'''

import sys
import io
import os.path
from donor_models import Charity
from donor_models import Donor

def main():

    input = "".join(open("mailroominput.txt", "r").readlines())
    sys.stdin = io.StringIO(input)

    local_charity = Charity('Local Charity')
    local_charity.AddDonor('William Gates, III')
    local_charity.Donors['William Gates, III'].AddDonation(60000.00)
    local_charity.Donors['William Gates, III'].AddDonation(50000.00)
    local_charity.AddDonor('Mark Zuckerberg')
    local_charity.Donors['Mark Zuckerberg'].AddDonation(10000.00)
    local_charity.Donors['Mark Zuckerberg'].AddDonation(60000.00)
    local_charity.Donors['Mark Zuckerberg'].AddDonation(396.10)
    local_charity.AddDonor('Jeff Bezos')
    local_charity.Donors['Jeff Bezos'].AddDonation(877.33)

    user_input(local_charity)

def user_input(local_charity):
    selection = ''
    while selection != '5':
        selection = input('\nPlease select type one of following commands: \n' 
                          '1 : Add a Donor\n'
                          '2 : Send Donation Thank You\n' 
                          '3 : Create a Report\n'
                          '4 : Send letters to all donors\n'
                          '5 : QUIT\n ')
        if selection == '1':
            name = input('\n What is the Donors Name\n')
            local_charity.AddDonor(name)
            print('\n {:s} has been added to the donor list\n'.format(name))

        elif selection == '2':
            name = input('\n What is the Donors Name\n')
            amount = None
            while not amount:
                try:
                    amount = float(input('\n How much did they donate?\n'))
                except ValueError:
                    print('\nplease enter a valid dollar amount\n')
            try:
                local_charity.Donors[name].send_thank_you(amount)
            except KeyError:
                print('\n Please try again with a valid donor name or add your requested donor to the database')

            print('\n A thank you has been made for {:s} in the ammount of {:.2f}\n'.format(name, amount))

        elif selection == '3':
            local_charity.create_report()
        elif selection == '4':
            local_charity.send_all_thank_yous()
        elif selection == '5':
            print('QUITTING')
        else:
            print('INVALID SELECTION')

if __name__ == '__main__':
    main()