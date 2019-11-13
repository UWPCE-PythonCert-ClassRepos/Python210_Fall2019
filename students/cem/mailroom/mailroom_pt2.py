#!/usr/bin/env python3
import sys
import datetime
import os

"""
The script prompts the user (you) to choose from a menu of 
3 actions: “Send a Thank You”, “Create a Report” or “quit”.
"list" will bring up up donors list.
"q" will quit the application.
"""

CHARITY_NAME = "Cem's Charity"

donors = {
    "Bill Gates": [653772.32, 12.17],
    "Jeff Bezos": [877.33],
    "Paul Allen": [663.23, 43.87, 1.32],
    "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
    "Thierry Henry": [6777.00, 8750.00],
    "The Rock": [90000.00, 5550.00],
    }

prompt = "\n".join(("\nWelcome to the Mailbox!",
                    "Please choose from below options:",
                    "1 - Send a Thank You to a single donor",
                    "2 - Create a Report",
                    "3 - Send letters to all donors",
                    "q - Quit",
                    ">>> "))


def list_donors():
    """Prints a list of all donors in list"""
    print("\nList of all {} donors: ".format(len(donors)), '\n', '-' * 25)
    for donor in donors.keys():
        print(f" ", donor)
    print('-' * 25)


def thank_you_email(response, donated):
    """Prints out thank you letter"""
    # for donor, value in donors.items():
    letter = (
        f"""
        Dear {response}, 

        Thank you for your amazingly generous donation of ${donated:.2f}! 
        We, at {CHARITY_NAME}, greatly appreciate your donation, and your sacrifice. 

        Your support helps to further our mission.

        Regards,
        Cem
        """.format(**donors))
    return letter


def thank_you_email_all():
    path = input(
        f"\nEnter a dir name to create folder here in this pwd, full path or go back directories with '../'"
        f"\nYour pwd now is {os.getcwd()}: ")
    full_dir = os.path.join(os.getcwd() + "/" + path)
    while True:
        if path == 'q':
            print("Quitting.")
            break
        else:
            print(full_dir)
            try:
                os.mkdir(path)
            except OSError:
                print(f"Folder already exists, so saving to this directory.")
            else:
                print(f"Directory created successfully at {full_dir}, letters written to this folder!")

            for donor, donated in donors.items():
                compose = thank_you_email(donor, sum(donated))
                with open(full_dir + "/" + "{}_{}.txt".format(donor, datetime.date.today()).replace(" ", "_"),
                          'w+') as thanks_file:
                    thanks_file.write(compose)
        break


def send_thank_you():
    """Send thank you e-mails to existing or new donors"""
    while True:
        response = input("Enter the name of who you would like to send a thank you e-mail to "
                         "\nType 'list' to see a all our donors"
                         "\nType 'q' to go back to the main menu: ")
        if response == 'q':
            break
        if response == 'list':
            list_donors()
        elif response in donors:
            donation = input("Enter donation amount: ")
            if donation == 'q':
                break
            donated = float(donation)
            donors[response].append(donated)
            # print("\n", donors)   # Good for testing, shows donor appended to list.
            thank_you_email(response, donated)
            print(thank_you_email(response, donated))
            return response, donated
        else:
            donation = input("{} is not an existing donor, adding to db, enter donation amount: ".format(response))
            donated = float(donation)
            donors[response] = [donated]
            # print("\n", donors) # Good for testing, shows donor appended to list.
            thank_you_email(response, donated)
            print(thank_you_email(response, donated))


def sort_key(donor):
    return donor[1]


def create_report():
    header_donor_name = "Donor Name"
    header_total_given = "Total Given"
    header_num_gifts = "Num Gifts"
    header_average_gift = "Average Gift"

    sorted_total = sorted(donors.items(), key=sort_key, reverse=True)

    header = f"{header_donor_name:<25} | {header_total_given:>10} | {header_num_gifts:>10} | {header_average_gift:>10}"

    print(header)
    print(len(header)*'-')

    for key, value in sorted_total:
        total_given = sum(value)
        num_gifts = len(value)
        average_gift = total_given / num_gifts
        total_given_formatted = ("{:.2f}".format(total_given))
        average_gift_formatted = ("{:.2f}".format(average_gift))
        print(f"{key:<25} | $ {total_given_formatted:>10} | {num_gifts:>9} | $ {average_gift_formatted:>10}")


def exit_program():
    print("Bye!")
    sys.exit()


def select_menu_option(prompt, dispatch_dict):
    while True:
        response = input(prompt)
        if dispatch_dict[response]() == "exit menu":
            break


switcher_menu = {
            "1": send_thank_you,
            "2": create_report,
            "3": thank_you_email_all,
            "q": exit_program
        }

# make executable
if __name__ == "__main__":
    select_menu_option(prompt, switcher_menu)

