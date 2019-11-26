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
    last_amount = donor_list[name][-1]
    number_donations = len(donor_list[name])
    average = total_given/number_donations
    letter = (f"Dear {name},\n\n\tThank you for your very kind donation of " +
              f"${last_amount:.2f}.\n\n\tYou have donated {number_donations}" +
              f" times with an average of ${(average):.2f}" +
              f" per donation.\n\n\tThe total amount you donated is $" +
              f"{total_given:.2f}.\n\n\tIt will be put to very good use.\n\n" +
              f"\t\t\tSincerely,\n\t\t\t\t-The Team.")
    return letter

def display_donor_list():
    display_string = "-"*30 + "\n"
    for name in donor_list:
        display_string += name + "\n"
    display_string += ("-"*30)
    return display_string

# Menu Actions:


def send_thank_you():
    donor_input = ""
    donation_amount = ""
    thank_you_prompt = "For main menu enter 'q' at any time.\n" + "Enter a donor's Full Name or enter 'list' to see " + "the donors list :"
    dontation_prompt = "Please enter donation amount: "

    while donor_input != "q":
        donor_input = input(thank_you_prompt)

        # Donors list and exiting options
        while donor_input == "list":
            print(display_donor_list())
            donor_input = input(thank_you_prompt)
        if donor_input == "q":
            break

        while type(donation_amount) != float:
            donation_amount = input(dontation_prompt)
            if donation_amount == "q":
                break
            try:
                donation_amount = float(donation_amount)
            except ValueError:
                print('Please enter a number')

        if donation_amount == "q":
            break

        # Assigning donor values
        if donor_input not in donor_list:
            add_donor(donor_input, [donation_amount])
        else:
            donor_list[donor_input].append(donation_amount)

        print(create_letter(donor_input))
        donor_input = "q"


def display_report():
    # Using lambda to access values from list of dictionaries
    sorted_list = sorted(donor_list.items(),
                         key=lambda e: sum(e[1]), reverse=True)
    report = "Donor Name" + " "*16 + "| Total Given | Num Gifts | Average Gift\n"
    report += "-"*66 + "\n"
    for name in sorted_list:
        report += ("{:25}  ${:>11.2f}{:>12d}  ${:>12.2f}".format(name[0],
              sum(name[1]), len(name[1]), sum(name[1])/len(name[1])) + "\n")
    return report


def create_report():
    print(display_report())


def create_text_files(path, date):
    for name in donor_list:
        string_letter = create_letter(name)
        with open(path + name + '_' + date + '.txt', 'w') as f:
            f.write(string_letter)
            f.close()


def send_thank_you_all():
    folder = input("Enter the folder to save the letters: ")
    path = pathlib.Path('./'+folder)
    if not path.is_dir(): os.mkdir("./"+folder)
    folder_path = './' + folder_path +'./'
    date = str(datetime.now())[:-16]

    create_text_files(folder_path, date)


def quit():
    print("Thank you for using Mailroom.\nExiting Program\n")


main_prompt = ("\nYou are in the main menu, Choose an action to perform:\n" +
               "1: Send a Thank You to a single donor.\n" +
               "2: Create a Report.\n" +
               "3: Send letters to all donors.\n" +
               "q: Quit\n")

main_dispatch = {"1": send_thank_you,
                 "2": create_report,
                 "3": send_thank_you_all,
                 "q": quit}


if __name__ == '__main__':
    create_donor_list()
    main_menu(main_dispatch)
