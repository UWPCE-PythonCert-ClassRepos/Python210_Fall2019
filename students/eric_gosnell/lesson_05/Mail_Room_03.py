"""
Eric Gosnell
Lesson 4 - Mail Room - Part 2
11.14.2019
"""

from sys import exit

DONOR_DB = {"Brent Golden": [750.00, 250.00, 250.00],
            "Regan Kirk": [300.00, 300.00],
            "Shiloh Gardner": [100.00, 100.00, 100.00, 100.00],
            "Alanna Newton": [200.00, 50.00, 100.00, 75.00],
            "Marcel Torres": [25.00, 25.00, 25.00, 25.00, 25.00, 25.00]}

THANK_YOU_EMAIL = ("Thank you {}.\n"
                   "We greatly appreciate your recent donation of ${:,.2f}.\n"
                   "It will be put to good use.\n"
                   "\t\t\tSincerely,\n"
                   "\t\t\t\t-The Team")

MAIN_PROMPT = ("\n"
               "       Main Menu\n"
               "------------------------\n"
               "1:  Send a 'Thank You' letter to single donor.\n"
               "2:  Send letters to all donors.\n"
               "3:  Print summary report.\n"
               "0:  Exit.\n\n"
               "Your choice >")

THANK_YOU_PROMPT = ("\n"
                    "     Thank You Options\n"
                    "---------------------------\n"
                    "1:  Type 'list' or press 1 to see existing donors.\n"
                    "2:  Add donor.\n"
                    "3:  Write 'thank you' letter to single donor.\n"
                    "4:  Return to main menu.\n"
                    "0:  Exit the program.\n\n"
                    "Your choice > ")

NAME_PROMPT = "\nEnter donor name >"
DONATION_PROMPT = "\nEnter new donation amount >"
CONTINUE_PROMPT = "\nPress enter to continue..."
DONOR_FOUND = "\n{} found."
DONOR_NOT_FOUND = "\n{} not in database."
DONOR_SUCCESS = "\n{} successfully added to database."
DONOR_EXISTS = "\n{} already in database!"
DONATION_SUCCESS = "\nDonation of ${:,.2f} for {} successfully added."
INVALID_SELECTION = "\nInvalid selection!"
INVALID_DONATION = "\nInvalid input! Enter numbers only."
NEGATIVE_DONATION = "\nInvalid input! Enter number greater than zero."
INVALID_NAME = "\nInvalid input! Enter text only."
SAVED_TO_DISK = "\nThe following message was saved to file: '{}'...\n"
IO_ERROR = "\nIOError! Problem with {}: {}."


def header_rows():
    """ Returns multi-row formatted report header string """
    report_title = ["*" * 11, "Donation Summary Report", "*" * 11]
    col_head = ["Donor Name", "Total Given", "Number Donations", "Average Donation"]
    rows = ("\n{:>15s}{:^40s}{:<20s}\n".format(*report_title)
            + "\n{:<18s}|{:>14s} | {:>18s} | {:>18s}".format(*col_head)
            + "\n" + "-" * 78)
    return rows


def exit_func():
    print("\nExiting the program.")
    exit()


def show_donor_list():
    print("\nExisting donor list:\n" + "-" * 20, sep="")
    for donor in DONOR_DB:
        print(donor)


def get_valid_name():
    while True:
        name = input(NAME_PROMPT)
        try:
            # User entered numeric data instead of name?
            name = float(name)
            print(INVALID_NAME)
            continue
        except ValueError:
            return name


def get_valid_donation():
    while True:
        donation = input(DONATION_PROMPT)
        try:
            donation = float(donation)
            if donation <= 0:
                print(NEGATIVE_DONATION)
                continue
        except ValueError:
            print(INVALID_DONATION)
            continue
        else:
            return donation


def add_donor():
    name = get_valid_name()
    if name not in DONOR_DB:
        DONOR_DB[name] = []
        print(DONOR_SUCCESS.format(name))
    else:
        print(DONOR_EXISTS.format(name))


def single_donor_letter():
    """ Verify donor in database, add donation, write thank you to file and screen """
    name = get_valid_name()
    if name in DONOR_DB:
        print(DONOR_FOUND.format(name))
        donation = get_valid_donation()
        DONOR_DB[name].append(donation)
        try:
            file_name = name + ".txt"
            with open(file_name, "w") as file:
                file.write(THANK_YOU_EMAIL.format(name, donation))
        except IOError:
            # Problem writing to file
            print(IO_ERROR)
            exit_func()
        else:
            print(DONATION_SUCCESS.format(donation, name))
            print(SAVED_TO_DISK.format(file_name))
            print(THANK_YOU_EMAIL.format(name, donation))
    else:
        print(DONOR_NOT_FOUND.format(name))


def all_donors_letter():
    """ Write multiple thank you files and print to screen - uses most recent donation """
    for donor in DONOR_DB:
        file_name = donor + ".txt"
        try:
            with open(file_name, "w") as file:
                # Most recent donation
                file.write(THANK_YOU_EMAIL.format(donor, DONOR_DB[donor][-1]))
        except IOError as e:
            print(IO_ERROR.format(file_name, str(e)))
            exit_func()
        else:
            print(SAVED_TO_DISK.format(file_name))
            print(THANK_YOU_EMAIL.format(donor, DONOR_DB[donor][-1]))


# ---------------     Report operations     --------------- #


def sort_key(donor):
    """Returns summed donation list values"""
    return sum(DONOR_DB[donor])


def print_report():
    """ Prints formatted report using derived calculations """
    print(header_rows())

    sorted_db = sorted(DONOR_DB, key=sort_key, reverse=True)

    for donor in sorted_db:
        total_donations = sum(DONOR_DB[donor])
        qty_donations = len(DONOR_DB[donor])
        try:
            average_donation = total_donations / qty_donations
        except ZeroDivisionError:
            average_donation = 0
        finally:
            dollar_format_total = "${:,.2f}".format(total_donations)
            dollar_format_average = "${:,.2f}".format(average_donation)
            print(f"{donor:<18s}{dollar_format_total:>15s}"
                  f"{len(DONOR_DB[donor]):>21d}{dollar_format_average:>21s}")


# ---------------     Menu operations     --------------- #

def menu_selection(prompt, switch):
    """ Multi-use menu selection function """
    while True:
        choice = input(prompt)
        try:
            choice = int(choice)
            if choice in switch:
                switch.get(choice)()
            else:
                print(INVALID_SELECTION)
                continue
        except ValueError:
            # User has entered a word or text, not a number, is it 'list'?
            if choice in switch:
                switch.get(choice)()
            else:
                print(INVALID_SELECTION)
                continue
        input(CONTINUE_PROMPT)


def main_menu():
    menu_selection(MAIN_PROMPT, main_switch)


def thank_you_sub_menu():
    menu_selection(THANK_YOU_PROMPT, thank_you_switch)


thank_you_switch = {1: show_donor_list,
                    2: add_donor,
                    3: single_donor_letter,
                    4: main_menu,
                    0: exit_func,
                    "list": show_donor_list}

main_switch = {1: thank_you_sub_menu,
               2: all_donors_letter,
               3: print_report,
               0: exit_func}

if __name__ == "__main__":
    menu_selection(MAIN_PROMPT, main_switch)
