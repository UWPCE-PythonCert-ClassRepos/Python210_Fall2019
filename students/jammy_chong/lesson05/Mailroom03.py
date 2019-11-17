import os
import pathlib
from datetime import datetime

donor_list = dict()

def main_menu(dispatch_dict):
    while True:
        print(main_prompt)
        action = input("")
        if action in dispatch_dict:
            dispatch_dict[action]()
            if action == "q":
                break

def add_donor(name, donations=[]):
    if name not in donor_list: donor_list[name] = donations

def create_donor_list():
    add_donor("Paul Allen", [250.00, 433.49, 413.45])
    add_donor("Mark Zuckerberg", [3422.12, 5877.13, 4323.65])
    add_donor("Jeff Bezos", [877.33])
    add_donor("William Gates, III", [45523.16, 212333.12])
    add_donor("Jammy Chong", [13233.45, 8233.12])

def create_letter(name):
    total_given = sum(donor_list[name])
    last_donation = donor_list[name][-1]
    number_donations = len(donor_list[name])
    letter = (f"Dear {name},\n\n\tThank you for your very kind donation of " + \
             f"${last_donation:.2f}.\n\n\tYou have donated {number_donations}" + \
             f" times with an average of ${(total_given/number_donations):.2f}" + \
             f" per donation.\n\n\tThe total amount you donated is " + \
             f"{total_given:.2f}.\n\n\tIt will be put to very good use.\n\n" + \
             f"\t\t\tSincerely,\n\t\t\t\t-The Team.")
    return letter

# Menu Actions:

def send_thank_you():
    donor_input = ""
    donation_amount = ""
    thank_you_prompt = "For main menu enter 'q' at any time.\n"+ \
            "Enter a donor's Full Name or enter 'list' to see the donors list :"
    dontation_prompt = "Please enter donation amount: "
    while donor_input != "q":
        donor_input = input(thank_you_prompt)

        #Donors list and exiting options
        while donor_input == "list":
            print("-"*30)
            for name in donor_list:
                print(name)
            print("-"*30)
            donor_input = input(thank_you_prompt)
        if donor_input == "q":
            break

        while type(donation_amount) != float:
            if donation_amount == "q":
                break
            donation_amount = input(dontation_prompt)
            try:
                donation_amount = float(donation_amount)
            except ValueError:
                donation_amount = input(dontation_prompt)

        #Assigning donor values
        if donor_input not in donor_list:
            add_donor(donor_input, [donation_amount])
        else:
            donor_list[donor_input].append(donation_amount)

        print(create_letter(donor_input))
        donor_input = "q"

def create_report():
    #Using lambda to access values from list of dictionaries
    sorted_list = sorted(donor_list.items(),
                  key = lambda e: sum(e[1]), reverse=True)
    print("Donor Name"," "*14,"| Total Given | Num Gifts | Average Gift")
    print("-"*66)
    for name in sorted_list:
        print("{:25}  ${:>11.2f}{:>12d}  ${:>12.2f}".format(name[0],
        sum(name[1]), len(name[1]), sum(name[1])/len(name[1])))

def send_thank_you_all():
    folder = input("Enter the folder to save the letters: ")
    path = pathlib.Path('./'+folder)
    if not path.is_dir(): os.mkdir("./"+folder)

    date = str(datetime.now())[:-16]

    for name in donor_list:
        string_letter = create_letter(name)
        #print (string_letter)
        with open('./'+folder+'/'+name+'_'+date+'.txt', 'w') as f:
            f.write(string_letter)
            f.close()

def quit():
    print("Thank you for using Mailroom.\nExiting Program\n")

main_prompt = ("\nYou are in the main menu, Choose an action to perform:\n"
               "1: Send a Thank You to a single donor.\n"
               "2: Create a Report.\n"
               "3: Send letters to all donors.\n"
               "q: Quit\n")

main_dispatch = {"1": send_thank_you,
                "2":create_report,
                "3":send_thank_you_all,
                "q":quit}

if __name__ == '__main__':
    create_donor_list()
    main_menu(main_dispatch)
