#!/usr/bin/env python3
from time import sleep


choices = ('Send a Thank You', 'Create Report')
donations = {'TOOGII DASHDAVAA': {"donation": 3, "donation_amnt": 30000},'MARK ZACHERBERG': {"donation": 1, "donation_amnt": 1000}, 'JEFF BEZOS': {"donation": 3, "donation_amnt": 15000}, 'BILL GATES': {"donation": 1, "donation_amnt": 500}, 'LARRY PAGE': {"donation": 2, "donation_amnt": 10000}}

def email_compose(name: str, donation: int, donation_amnt: int):
    
    email_letter = f"Dear {name}, \nThank you for your generous gift of $ {donation_amnt} to our organization. We are thrilled to have your support.\nThrough your donation we have been able to accomplish our charity work around the world.\n  \nThank you"
    print("\n\nGenerating an appreciation email for {}!\n\n" .format(name))
    sleep(1)
    print("\n{}".format(email_letter))

def update_donation(donor, donation_amnt):
    if donor in donations:
        donations[donor]["donation"] = donations[donor]["donation"] + 1
        donations[donor]["donation_amnt"] = donations[donor]["donation_amnt"] + donation_amnt
    else:
        donations.update({donor: {"donation": 1,"donation_amnt": donation_amnt }})
    sleep(1)
    print(donations)
    sleep(1)
    email_compose(donor, donations[donor]["donation"], donations[donor]["donation_amnt"])


def list_all_donors():
    for donors, donation in donations.items():
        print(donors)


def choose_the_donor():
    while True:
        donor = str(input("\nEnter the full name of the Donor or type list to list all existing Donors:  \n"))
        print("\nYour choice was {} \n\n" .format(donor.upper()))
        sleep(1)
        if donor.upper() == "LIST":
            list_all_donors()
            continue
        return donor.upper()


def send_a_thank_you():
    full_name = choose_the_donor().upper()
    donation_amount = int(input('Please enter the donation amount of {} ?:  \n\n'.format(full_name)))
    sleep(1)
    update_donation(full_name,donation_amount)

def create_table(column, data: dict):
    # Find the longest name in the cell 
    temp_list = list()
    for donor in data:
        temp_list.append(len(donor))
    longest_space = sorted(temp_list)[-1] + 3

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
    column = ['Donor Name', 'Num Gifts', 'Total Given', 'Average Gift']
    data = dict()
    lst = []
    for donor in donations:
        data.update({donor: []})
        for k, v in donations[donor].items():
            data[donor].append(v)
        data[donor].append("$ " + str(data[donor][-1]/data[donor][-2]))
    print(data)
    create_table(column,data)



def detect_choice(choice):
    if int(choice) == 1:
        send_a_thank_you()
    elif int(choice) == 2:
        create_report()
    return None



def main():
    while True:
        print('\n\n\n\t Welcome to Donations!\n\n')
        print('\t1.   {}\n\t2.   {}'.format(*choices))
        choice = input("\n\nPlease Enter Your choice(1 or 2): ")
        sleep(1)
        if choice == '1' or choice == '2':
            detect_choice(choice)
        else:
            print("Please enter the valid choice!") 



if __name__ == '__main__':
    main()     
