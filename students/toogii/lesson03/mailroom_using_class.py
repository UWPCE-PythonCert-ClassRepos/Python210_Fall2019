#!/usr/bin/env python3
from time import sleep
from mailroom import create_table

default_donor_dict = {'TOOGII DASHDAVAA': {"donation": 3, "donation_amnt": 30000},'MARK ZACHERBERG': {"donation": 1, "donation_amnt": 1000}, 'JEFF BEZOS': {"donation": 3, "donation_amnt": 15000}, 'BILL GATES': {"donation": 1, "donation_amnt": 500}, 'LARRY PAGE': {"donation": 2, "donation_amnt": 10000}}
choices = ('Send a Thank You', 'Create Report')
donations = {}
donators_obj_list = []
donators_name_list = []

class create_donor:
    def __init__(self, name: str, donation_amnt: int, donation: int=1):
        self.name = name
        self.donation = donation
        self.donation_amnt = donation_amnt


    def add_donor(self, donation_amnt):
        self.donation_amnt = self.donation_amnt + donation_amnt
        self.donation = self.donation + 1


    def email_composer(self,donation_amnt):
        self.email = f"Dear {self.name}, \n\nThank you for your generous gift of $ {donation_amnt} to our organization. We are thrilled to have your support.\nThrough your donation we have been able to accomplish our charity work around the world.\n  \nThank you"
        print("\n\n")
        print("="*30)
        print(self.email)
        print("="*30)
        print("\n\n")


def create_donor_object(name, donation_amnt, donation=1, default=False):
    # If the donor is new, will create new object,
    if name not in donators_name_list:
        donators_name_list.append(name)
        if default == True: # Checks if the donor is default/called from main(), if yes we have to update donation
            donators_obj_list.append(create_donor(name, donation_amnt, donation))
        else:
            donators_obj_list.append(create_donor(name, donation_amnt))
    else:
        donators_obj_list[donators_name_list.index(name)].add_donor(donation_amnt) # If donor already exist in the list, update donation amount


def create_report(donators_obj_list):
    # Preparing data for the report table
    for obj in donators_obj_list:
        donations.update({obj.name: [obj.donation, obj.donation_amnt, int(obj.donation_amnt/obj.donation)]})
    column = ['Donor Name', 'Num Gifts', 'Total Given', 'Average Gift']

    create_table(column,donations) # Call this function to create table. Pass column and list nested dict


def send_a_thank_you():
    # Prompting for the donor name and amount of donations
    while True:
        name = str(input("Enter the name of the Donor:   "))
        if name.upper() == "QUIT":
            return None
        if name.upper() == "LIST":
            for donor in donators_name_list:
                print(donor)
            continue
        donation_amnt = int(input("Enter the donation amount for the {}:  ".format(name))) # asking for donation amount
        create_donor_object(name, donation_amnt) # Creating donor object
        donators_obj_list[donators_name_list.index(name)].email_composer(donation_amnt) # Sending an appreciation email to the Donor
        return None


def main():
    # Add default donors:
    for name in default_donor_dict:
        create_donor_object(name, default_donor_dict[name]["donation_amnt"], default_donor_dict[name]["donation"], default=True)
    print(donators_obj_list)
    print(donators_obj_list[0].name, donators_obj_list[0].donation_amnt,donators_obj_list[0].donation)
    while True:
        # Welcome screen with prompt:
        print('\n\n\n\t Welcome to Donations!\n\n')
        print('\t1.   {}\n\t2.   {}'.format(*choices))
        choice = input("\n\nPlease Enter Your choice(1 or 2):   ")
        sleep(1)
        if choice == '1':
            print("\nYour choice was {}\n".format(choices[0]))
            send_a_thank_you()
        elif choice == '2':
            print("\nYour choice was {}\n".format(choices[1]))
            create_report(donators_obj_list)
        else:
            print("Please enter a valid choice!")



if __name__ == '__main__':
    main()
