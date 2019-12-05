import os
import sys
import time
from donor import Donation, Donor, Charity



def send_thank_you(charity):
    while True:
        response_1 = input("Please enter donors full name")

        if response_1 == "list":
            print(charity.get_donation_list())
            continue

        if response_1 not in charity.donors_dict:
            charity.add_donor(response_1)
            print("{} was added as a donor.".format(response_1))

        response_2 = input("Enter donation amount: ")

        # Exits the program if the the string is an integer,
        # and if the donation amount is above 1,000,000,000,000(Due to char limit of report)
        try:
            if int(response_2) >= 1000000000000:
                print("Amount entered was above 1,000,000,000,000")
                return quit_program()
            elif int(response_2) < 0:
                print("Amount entered was a negative amount")
                return quit_program()
        except ValueError:
            print("Amount entered was not a proper number")
            return quit_program()

        else:
            charity.donors_dict[response_1].add_donation(response_2)
            print(f"Thank You {response_1} for your donation of {response_2}.")
            break


def create_report(charity):
    charity.create_report()

def send_letter_to_all_donors(charity):
    charity.send_letter_to_all_donors()

# Added param due to menu functionality, not used though
def quit_program(charity=None):
    return "quit"

# Dictionary dispatch for mailroom menu with values as function calls
mailroom_menu_dispatch = {
    "1": send_thank_you,
    "2": create_report,
    "3": send_letter_to_all_donors,
    "4": quit_program
}

main_menu_prompt = ('\nWhat would you like to do?\n'
                    'Enter "1", "2", or "3"\n'
                    '1 - Send a Thank You\n'
                    '2 - Create a Report\n'
                    '3 - Send Letter To All Donors\n'
                    '4 - quit\n'
                    'INPUT:')


def menu_selection(prompt, dispatch_dict, charity):
    while True:
        response = input(prompt)

        try:
            dict_value = dispatch_dict[response]
        except KeyError:
            print("Invalid input, please try again.\n")
        else:
            if dict_value(charity) == 'quit':
                sys.exit()




if __name__ == '__main__':

    # TEST DATA
    new_donor1 = Donor("Fred")
    new_donor1.add_donation(100)
    new_donor1.add_donation(1000)
    new_donor1.add_donation(10000)

    new_donor2 = Donor("Bob")
    new_donor2.add_donation(200)
    new_donor2.add_donation(2000)
    new_donor2.add_donation(20000)

    new_donor3 = Donor("Todd")
    new_donor3.add_donation(300)
    new_donor3.add_donation(3000)
    new_donor3.add_donation(30000)

    new_donor4 = Donor("Sally")
    new_donor4.add_donation(400)
    new_donor4.add_donation(4000)
    new_donor4.add_donation(40000)

    new_donor5 = Donor("Becky")
    new_donor5.add_donation(500)
    new_donor5.add_donation(5000)
    new_donor5.add_donation(50000)

    new_charity = Charity("Foundation")
    new_charity.add_donor(new_donor1.donor_name, new_donor1.donations_list)
    new_charity.add_donor(new_donor2.donor_name, new_donor2.donations_list)
    new_charity.add_donor(new_donor3.donor_name, new_donor3.donations_list)
    new_charity.add_donor(new_donor4.donor_name, new_donor4.donations_list)
    new_charity.add_donor(new_donor5.donor_name, new_donor5.donations_list)
    #new_charity.print_total_donations()


    menu_selection(main_menu_prompt, mailroom_menu_dispatch, new_charity)