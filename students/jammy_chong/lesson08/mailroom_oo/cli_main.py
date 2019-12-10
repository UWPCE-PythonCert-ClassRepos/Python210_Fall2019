from donor_models import Donor, Charity
import os
import pathlib
from datetime import datetime


def main_menu(dispatch_dict):
    while True:
        print(main_prompt)
        action = input("")
        if action in dispatch_dict:
            dispatch_dict[action]()
            if action == "q":
                break
        else:
            print('Please choose an option from the menu')

def add_donation():
    donor_input = ""
    confirm_input = ""
    donation_amount = ""
    thank_you_prompt = "For main menu enter 'q' at any time.\n" + \
                       "Enter a donor's Full Name or enter 'list' to see " + \
                       "the donors list :"
    dontation_prompt = "Please enter donation amount: "

    while (donor_input != "q"):
        donor_input = input(thank_you_prompt)

        # Donors list and exiting options
        while donor_input == "list":
            print(Charity.GetDonorList())
            donor_input = input(thank_you_prompt)
        if donor_input == "q":
            break

        while confirm_input.lower() not in ("y","n","q"):
            confirm_input = input(f"Is {donor_input} the donor's name? (y/n): ")
        if confirm_input.lower() == "q":
            break
        elif confirm_input.lower() == "n":
            donor_input = ""
            continue

        while (type(donation_amount) != float):
            donation_amount = input(dontation_prompt)
            if donation_amount == "q":
                break
            try:
                donation_amount = float(donation_amount)
                if donation_amount < 0:
                    donation_amount = ""
                    print('Please enter a positive number')
            except ValueError:
                print('Please enter a number')


        if donation_amount == "q":
            break

        # Assigning donor values
        if donor_input not in Charity.DonorList:
            Charity.AddDonor(donor_input, [donation_amount])
        else:
            Charity.DonorList[donor_input].AddDonation(donation_amount)

        print(Charity.DonorList[donor_input].LatestDonation())
        donor_input = "q"


def create_report():
    print(Charity.GetReport())

def create_folder(folder):
    path = pathlib.Path('./'+folder)
    if not path.is_dir(): os.mkdir("./"+folder)
    folder_path = './' + folder +'./'
    date = str(datetime.now())[:-16]
    return folder_path, date

def send_thank_you():
    donor_name = ""
    print(Charity.GetDonorList())

    while (donor_name not in Charity.DonorList):
        donor_name = input("Enter a donor name from the list: ")
        if donor_name == "q":
            break
        if donor_name not in Charity.DonorList:
            print(f"{donor_name} is not in the list")

    if donor_name != "q":
        folder_name = input("Enter the folder to save the letter: ")
        folder = create_folder(folder_name)
        Charity.DonorList[donor_name].TextFile(folder[0], folder[1])


def send_thank_you_all():
    folder_name = input("Enter the folder to save the letters: ")
    folder = create_folder(folder_name)

    for name in Charity.DonorList:
        Charity.DonorList[name].TextFile(folder[0], folder[1])


def quit():
    print("Thank you for using Mailroom.\nExiting Program\n")


main_prompt = ("\nYou are in the main menu, Choose an action to perform:\n" +
               "1: Add a Donation.\n" +
               "2: Create a Report.\n" +
               "3: Send Thank You letter to a single donor.\n"
               "4: Send Thank You letters to all donors.\n" +
               "q: Quit\n")

main_dispatch = {"1": add_donation,
                 "2": create_report,
                 "3": send_thank_you,
                 "4": send_thank_you_all,
                 "q": quit}


if __name__ == '__main__':
    Charity = Charity("Red Cross")
    Charity.AddDonor("Paul Allen", [250.00, 433.49, 413.45])
    Charity.AddDonor("Mark Zuckerberg", [3422.12, 5877.13, 4323.65])
    Charity.AddDonor("Jeff Bezos", [877.33])
    Charity.AddDonor("William Gates, III", [45523.16, 212333.12])
    main_menu(main_dispatch)
