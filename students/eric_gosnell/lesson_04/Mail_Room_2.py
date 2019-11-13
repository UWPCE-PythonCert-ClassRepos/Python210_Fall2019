"""
Eric Gosnell
Lesson 4 - Mail Room - Part 2
11.12.2019
"""

from sys import exit

# Data structure converted to dictionary

donor_db = {"Brent Golden": [750.00, 250.00, 250.00],
            "Regan Kirk": [300.00, 300.00],
            "Shiloh Gardner": [100.00, 100.00, 100.00, 100.00],
            "Alanna Newton": [200.00, 50.00, 100.00, 75.00],
            "Marcel Torres": [25.00, 25.00, 25.00, 25.00, 25.00, 25.00]}

# Prompts used in functions

thank_you_message = ("Thank you {}.\n"
                     "We greatly appreciate your donation of ${:.2f}.\n"
                     "It will be put to good use.\n"
                     "\t\t\tSincerely,\n"
                     "\t\t\t\t-The Team\n")

donor_error_message = ("ERROR! Donor name not found!\n"
                       "You must first add donor and then "
                       "add donation to donor before sending letter!\n")

donation_error_message = ("ERROR! Donor name not found!\n"
                          "You must first add donor before adding donation!\n")

main_prompt = ("\n"
               "       Main Menu\n"
               "------------------------\n"
               "1:  Send a 'Thank You' letter to single donor.\n"
               "2:  Send letters to all donors.\n"
               "3:  Print summary report.\n"
               "0:  Exit.\n\n"
               "Your choice >")

thank_you_prompt = ("\n"
                    "     Thank You Options\n"
                    "---------------------------\n"
                    "1:  Type 'list' or press 1 to see existing donors.\n"
                    "2:  Add donor.\n"
                    "3:  Write 'thank you' letter to single donor.\n"
                    "4:  Return to main menu.\n"
                    "0:  Exit the program.\n\n"
                    "Your choice > ")

NAME_PROMPT = "Enter donor name >"
DONATION_PROMPT = "Enter new donation amount >"
DONOR_FOUND_MESSAGE = "{} found."
DONOR_NOT_FOUND_MESSAGE = "{} not in database."
DONOR_SUCCESS_MESSAGE = "{} successfully added to database."
DONOR_EXISTS_MESSAGE = "{} already in database!  Returning to menu..."
DONATION_SUCCESS_MESSAGE = "Donation of {:.2f} for {} successfully added."
INVALID_SELECTION_MESSAGE = "Invalid selection!"


def header_rows():
    """ Returns multi-row formatted report header string """

    col_head = ["Donor Name", "Total Given", "Number Donations", "Average Donation"]
    report_title = ["*" * 11, "Donation Summary Report", "*" * 11]
    rows = ("\n{:>15s}{:^40s}{:<20s}\n".format(*report_title)
            + "\n{:<18s}|{:>14s} | {:>18s} | {:>18s}".format(*col_head)
            + "\n" + "-" * 78)
    return rows


def exit_func():
    print("\nExiting the program.")
    exit()


def task_complete_prompt():
    response = input("\nExit program? y or n >")
    if response == "y":
        exit_func()


def show_donor_list():
    print("\nExisting donor list:\n" + "-" * 20, sep="")
    for donor in donor_db:
        print(donor)


def add_donor():
    name = input("\n" + NAME_PROMPT)
    if name not in donor_db:
        donor_db[name] = []
        print("\n" + DONOR_SUCCESS_MESSAGE.format(name))
    else:
        print("\n" + DONOR_EXISTS_MESSAGE.format(name))


def single_donor_letter():
    """ Verify donor exists, add donation, write thank you to file and screen """
    name = input("\n" + NAME_PROMPT)
    if name not in donor_db:
        print("\n" + DONOR_NOT_FOUND_MESSAGE.format(name))
        print("103")
    else:
        print("\n" + DONOR_FOUND_MESSAGE.format(name))
        donation = float(input("\n" + DONATION_PROMPT))
        donor_db[name].append(donation)
        print("\n" + DONATION_SUCCESS_MESSAGE.format(donation, name))
        file_name = name + ".txt"
        try:
            with open(file_name, "w") as file:
                file.write(thank_you_message.format(name, donation))
                print("\nThe following was saved to disk as a file...\n")
                print(thank_you_message.format(name, donation))
        except Exception as e:
            print("Error:", str(e))


def all_donors_letter():
    """ Write multiple thank you files and print to screen - uses most recent donation """
    for donor in donor_db:
        try:
            with open(donor + ".txt", "w") as file:
                file.write(thank_you_message.format(donor, donor_db[donor][-1]))
                print("\nThe following was saved to disk as a file...\n")
                print(thank_you_message.format(donor, donor_db[donor][-1]))
        except Exception as e:
            print("Error:", str(e))


# Report operations


def sort_key(donor):
    """Returns summed donation list values"""
    return sum(donor_db[donor])


def print_report():
    """ Prints formatted report using derived calculations """
    print(header_rows())

    sorted_db = sorted(donor_db, key=sort_key, reverse=True)

    for donor in sorted_db:
        total_donations = sum(donor_db[donor])
        qty_donations = len(donor_db[donor])
        if qty_donations != 0:
            average_donation = total_donations / qty_donations
        else:
            average_donation = 0
        dollar_format_total = "${:.2f}".format(total_donations)
        dollar_format_average = "${:.2f}".format(average_donation)
        print(f"{donor:<18s}{dollar_format_total:>15s}"
              f"{len(donor_db[donor]):>21d}{dollar_format_average:>21s}")


# Menu operations


def menu_selection(prompt, switch):
    """ Multi-use menu selection function """
    while True:
        choice = input(prompt)
        if choice.isdigit():
            choice = int(choice)
            if choice in switch:
                switch.get(choice)()
            else:
                print("\n" + INVALID_SELECTION_MESSAGE)
        else:
            if choice.lower() == "list":
                choice = 1
                switch.get(choice)()
            else:
                print("\n" + INVALID_SELECTION_MESSAGE)


def main_menu():
    menu_selection(main_prompt, main_switch)


def thank_you_sub_menu():
    menu_selection(thank_you_prompt, thank_you_switch)


thank_you_switch = {1: show_donor_list,
                    2: add_donor,
                    3: single_donor_letter,
                    4: main_menu,
                    0: exit_func}


main_switch = {1: thank_you_sub_menu,
               2: all_donors_letter,
               3: print_report,
               0: exit_func}


if __name__ == "__main__":
    menu_selection(main_prompt, main_switch)
