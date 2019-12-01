'''
Script: mailroom04
Date: 11/24/2019
Dev: Kory Shaffer
'''

import sys
import io
import os.path
from mailroomclasses import Charity
from mailroomclasses import Donor

def main():

    input = "".join(open("mailroominput.txt", "r").readlines())
    sys.stdin = io.StringIO(input)

    local_charity = Charity('Local Charity')
    local_charity.AddDonor('William Gates, III', [60000.00, 50000.00])
    local_charity.AddDonor('Mark Zuckerberg', [10000.00, 60000.00, 396.10])
    local_charity.AddDonor('Jeff Bezos', [877.33, ])

    user_input(local_charity)

    #Unit Tests
    test_name = 'Kyle Clark'
    amount = 1000.56
    test_send_thank_you(local_charity, test_name, amount)
    test_send_all_thank_yous(local_charity)


def user_input(local_charity):
    selection = ''
    while selection != '4':
        selection = input('\nPlease select type one of following commands: \n' 
                          '1 : Send a single Thank You\n' 
                          '2 : Create a Report\n'
                          '3 : Send letters to all donors\n'
                          '4 : QUIT\n ')
        if selection == '1':
            name = input('\n What is the Donors Name\n')
            amount = None
            while not amount:
                try:
                    amount = float(input('\n How much did they donate?\n'))
                except ValueError:
                    print('\nplease enter a valid dollar amount\n')

            local_charity.send_thank_you(name, amount)
        elif selection == '2':
            local_charity.create_report()
        elif selection == '3':
            local_charity.send_all_thank_yous()
        elif selection == '4':
            print('QUITTING')
        else:
            print('INVALID SELECTION')

def test_send_thank_you(local_charity, test_name, amount):
    local_charity.send_thank_you(test_name, amount)
    assert(local_charity.Donors[test_name].TotalDonations() == 1000.56)
    assert(local_charity.Donors[test_name].DonationCount() == 1)
    local_charity.send_thank_you(test_name, amount)
    assert (local_charity.Donors[test_name].TotalDonations() == 2001.12)
    assert (local_charity.Donors[test_name].DonationCount() == 2)
    assert (local_charity.Donors[test_name].AverageDonation() == 1000.56)
    local_charity.Donors[test_name].AddDonation(amount)
    assert (local_charity.Donors[test_name].TotalDonations() == 3001.68)
    assert (local_charity.Donors[test_name].DonationCount() == 3)
    assert (local_charity.Donors[test_name].AverageDonation() == 1000.56)
    print('\n test_send_thank_you passed\n')

def test_send_all_thank_yous(local_charity):
    local_charity.send_all_thank_yous()
    for donor in local_charity.Donors:
        assert (os.path.exists('./' + donor + '_letter.txt'))
    print('\n test_send_all_thank_yous passed\n')

if __name__ == '__main__':
    main()