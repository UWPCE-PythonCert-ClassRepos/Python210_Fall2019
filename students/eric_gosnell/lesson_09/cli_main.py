"""
Eric Gosnell
Lesson 9 - Object Oriented Mailroom
12.10.2019

        ****    Main execution module   ****
"""

from donor_models import Donor, Charity
from datetime import datetime
from io import StringIO

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
DONATION_DATE = "\nEnter donation date >"
CONTINUE_PROMPT = "\nPress enter to continue..."
DONOR_FOUND = "\n{} found."
DONOR_NOT_FOUND = "\n{} not in database."
DONOR_SUCCESS = "\n{} successfully added to database."
DONOR_EXISTS = "\n{} already in database!"
DONATION_SUCCESS = "\nDonation of ${:,.2f} on {} for {} successfully added."
INVALID_SELECTION = "\nInvalid selection!"
INVALID_DONATION = "\nInvalid input! Enter numbers only."
NEGATIVE_DONATION = "\nInvalid input! Enter number greater than zero."
INVALID_NAME = "\nInvalid input! Enter text only."


def exit_func(charity):
    print(f"\nClosing charity '{charity.name}'. Exiting the program.")
    exit()


def get_date():
    d = datetime.today()
    date_time = f'{d.month}_{d.day}_{d.year}'
    return date_time

    # ----------    Input validation functions     ----------- #


def get_valid_name():
    while True:
        name = input(NAME_PROMPT).strip()
        try:
            first, last = name.split()
        except:
            print("Input error! Name cannot be just one word. "
                  "Correct format: First Last (with a space between).")
            continue
        try:
            # User entered numeric data instead of name?
            name = float(name.strip())
            print(INVALID_NAME)
            continue
        except ValueError:
            return name.strip()


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
            return float(donation)

    # ----------    Working with classes     ----------- #


def add_donor(charity):
    name = get_valid_name()
    for donor in charity.donor_list:
        if donor.name.upper() == name.upper():
            print(DONOR_EXISTS.format(donor.name))
            break
    else:
        charity.add_donor(Donor(name))
        print(DONOR_SUCCESS.format(name))


def single_donor_letter(charity):
    name = get_valid_name()
    for donor in charity.donor_list:
        if donor.name.upper() == name.upper():
            print(DONOR_FOUND.format(donor.name))
            donation = get_valid_donation()
            date = get_date()
            donor.add_donation(date, donation)  # string, float
            print(DONATION_SUCCESS.format(donation, date, donor.name))
            write_email(donor)
            break
    else:
        print(DONOR_NOT_FOUND.format(name))

    # ----------    Working with files    ----------- #


def write_email(donor):
    """ Someday this code to be replaced with real email function"""
    f = StringIO()
    message = donor.thank_you_email
    f.write(message)
    print("\nThe following message was saved to file... \n\n"
          f"{f.getvalue()}")


def all_donors_letter(charity):
    """ Write multiple thank you files and print to screen - uses most recent donation """
    for donor in charity.donor_list:
        write_email(donor)

# ----------    Formatted output to terminal    ----------- #


def header_rows():
    """ Returns multi-row formatted report header string """
    report_title = ["*" * 11, "Donation Summary Report", "*" * 11]
    col_head = ["Donor Name", "Total Given", "Number Donations", "Average Donation"]
    rows = ("\n{:>15s}{:^40s}{:<20s}\n".format(*report_title)
            + "\n{:<18s}|{:>14s} | {:>18s} | {:>18s}".format(*col_head)
            + "\n" + "-" * 78)
    return rows


def show_donor_list(charity):
    print("\nExisting donor list:\n" + "-" * 20, sep="")
    for donor in charity.donor_list:
        first, last = donor.name.split()
        print(f"{first} {last}")


def sort_key(donor):
    return donor.sum_donations


def print_report(charity):
    print(header_rows())
    donor_list = sorted(charity.donor_list, key=sort_key, reverse=True)
    for donor in donor_list:
        dollar_format_average = f"${donor.avg_donation:,.2f}"
        dollar_format_total = f"${donor.sum_donations:,.2f}"
        print(f"{donor.name:<18s}{dollar_format_total:>15s}"
              f"{donor.qty_donations:>21n}{dollar_format_average:>21s}")

# ----------    Menu functions    ----------- #


def menu_selection(prompt, switch, charity):
    """ Multi-use menu selection function """
    while True:
        choice = input(prompt)
        try:
            choice = int(choice)
            if choice in switch:
                switch.get(choice)(charity)
            else:
                print(INVALID_SELECTION)
                continue
        except ValueError:
            # User has entered a word or text, not a number, is it 'list'?
            if choice in switch:
                switch.get(choice)(charity)
            else:
                print(INVALID_SELECTION)
                continue
        input(CONTINUE_PROMPT)


def main_menu(charity):
    menu_selection(MAIN_PROMPT, main_switch, charity)


def thank_you_sub_menu(charity):
    menu_selection(THANK_YOU_PROMPT, thank_you_switch, charity)


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

    # ----------     Build initial donor list     ----------- #

    brent_golden = Donor("Brent Golden", [{'12_13_2019': 750.00},
                                          {'12_12_2019': 250.00},
                                          {'12_11_2019': 250.00}])
    regan_kirk = Donor("Regan Kirk", [{'12_10_2019': 300.00},
                                      {'12_09_2019': 300.00}])
    shiloh_gardner = Donor("Shiloh Gardner", [{'12_08_2019': 100.00},
                                              {'12_07_2019': 100.00},
                                              {'12_06_2019': 100.00},
                                              {'12_05_2019': 100.00}])
    alanna_newton = Donor("Alanna Newton", [{'12_04_2019': 200.00},
                                            {'12_03_2019': 50.00},
                                            {'12_02_2019': 100.00},
                                            {'12_01_2019': 75.00}])
    marcel_torres = Donor("Marcel Torres", [{'11_30_2019': 25.00},
                                            {'11_29_2019': 25.00},
                                            {'11_28_2019': 25.00},
                                            {'11_27_2019': 25.00},
                                            {'11_26_2019': 25.00},
                                            {'11_25_2019': 25.00}])

    help_for_students = Charity("Help for Students")
    help_for_students.add_donor(brent_golden)
    help_for_students.add_donor(regan_kirk)
    help_for_students.add_donor(shiloh_gardner)
    help_for_students.add_donor(alanna_newton)
    help_for_students.add_donor(marcel_torres)

    # ----------    Main menu with Charity object passed in ----------- #

    menu_selection(MAIN_PROMPT, main_switch, help_for_students)
