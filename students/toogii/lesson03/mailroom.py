#!/usr/bin/env python3
from time import sleep


choices = ('Send a Thank You', 'Create Report')
donations = {'TOOGII DASHDAVAA': {"donation": 3, "donation_amnt": 30000},'MARK ZACHERBERG': {"donation": 1, "donation_amnt": 1000}, 'JEFF BEZOS': {"donation": 3, "donation_amnt": 15000}, 'BILL GATES': {"donation": 1, "donation_amnt": 500}, 'LARRY PAGE': {"donation": 2, "donation_amnt": 10000}}


def email_compose(name: str, donation_amount: int):
    # Generate and print an appreciation email to new Donor.
    email_letter = f"Dear {name}, \n\nThank you for your generous gift of $ {donation_amount} to our organization. We are thrilled to have your support.\nThrough your donation we have been able to accomplish our charity work around the world.\n  \nThank you"
    print("\n\nGenerating an appreciation email for {}!\n\n" .format(name))
    sleep(1)
    print("="*30)
    print("\n{}".format(email_letter))
    print("="*30)
    sleep(1)
    print("\n\nGoing back to main menu\n\n")   

def update_donation(donor, donation_amnt):
    # Update dictionary of donors with new donor information.
    if donor in donations:
        donations[donor]["donation"] = donations[donor]["donation"] + 1
        donations[donor]["donation_amnt"] = donations[donor]["donation_amnt"] + donation_amnt
    else:
        donations.update({donor: {"donation": 1,"donation_amnt": donation_amnt }})


def list_all_donors():
    # Prints all Donors
    for index, donors in enumerate(donations):
        print(str(index + 1) + " -- " + donors)


def get_a_new_donor_info():
    # Get the Donor name and donation amount
    while True:
        donor = str(input("\nEnter the full name of the Donor or type list to list all existing Donors:   "))
        print("\nYour Entered {} \n\n" .format(donor.upper()))
        sleep(1)
        if donor.upper() == "LIST":
            list_all_donors()
            continue
        donation_amount = int(input('Please enter the donation amount of {} ?:  '.format(donor)))
        return donor.upper(), donation_amount


def send_a_thank_you():
    # Gather Information about the new Donor 
    donor,donation_amount = get_a_new_donor_info()
    sleep(1)
    update_donation(donor.upper(),int(donation_amount))
    email_compose(donor, donation_amount)


def create_table(column, data: dict):
    # Find the longest name to make large enough cell 
    temp_list = list()
    for donor in data:
        temp_list.append(len(donor))
    longest_space = sorted(temp_list)[-1] + 3
    print("\n\n\n")
    # Creating the table
    for item in column:
        print(item + (longest_space - len(item))*' ', end = '| ')
    print("\n")
    print("-"*longest_space*len(column))
    for donor in data:
        print(donor + (longest_space - len(donor))*' ', end = '| ')
        for item in data[donor]:
            print(str(item) + (longest_space - len(str(item)))*' ', end = '| ')
        print("\n")


def create_report():
    # Prepare the Data for creating the table
    column = ['Donor Name', 'Num Gifts', 'Total Given ($)', 'Average Gift ($)']
    data = dict()
    # Creating dict-of-list for the table.
    for donor in donations:
        data.update({donor: []})
        for k, v in donations[donor].items():
            data[donor].append(v)
        data[donor].append(str(data[donor][-1]/data[donor][-2]))
    create_table(column,data)  


def main():
    while True:
        print('\n\n\n\t Welcome to Donations!\n\n')
        print('\t1.   {}\n\t2.   {}'.format(*choices))
        choice = input("\n\nPlease Enter Your choice(1 or 2):   ")
        sleep(1)
        if choice == '1':
            print("\nYour choice was {}\n".format(choices[0]))
            send_a_thank_you()
        elif choice == '2':
            print("\nYour choice was {}\n".format(choices[1]))
            create_report()
        else:
            print("Please enter a valid choice!") 



if __name__ == '__main__':
    main()     
