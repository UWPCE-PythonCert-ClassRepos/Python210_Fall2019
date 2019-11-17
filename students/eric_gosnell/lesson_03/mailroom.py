"""**************************************
# Author: Eric Gosnell
# Lesson: 3
# Assignment: Mail Room, Part One
**************************************
"""

import sys

#   List object for donors with starter values, declared in global namespace.

donor_db=[
(("Golden", "Brent"), 750.00, 250.00, 250.00),
(("Kirk", "Raegan"), 300.00, 300.00),
(("Gardner", "Shiloh"), 100.00, 100.00, 100.00, 100.00),
(("Newton", "Alanna"), 200.00, 50.00, 100.00, 75.00),
(("Torres", "Marcel"), 25.00, 25.00, 25.00, 25.00, 25.00, 25.00)
]


def exit_func():
    """ Clean exit function. """

    print("\nExiting the program.")
    sys.exit()


def sort_key(row):
    """ Key for use in the donor_db reporting function."""

    return sum(row[1:])


def show_donor_list():
    """ Show existing donor list. Read only. """

    print("""
Existing donor list:
--------------------""")
    for donor in donor_db:
        print(donor[0][1], donor[0][0])


def existing_donor(name):
    """ Check to see if donor exists before trying to add new donor. """

    name_exists = False
    first_name, last_name = name.split(" ")
    new_donor = (last_name, first_name),
    for donor in donor_db:
        if new_donor[0] == donor[0]:
            name_exists = True
            break
        else:
            continue
    return bool(name_exists)


def task_complete_prompt():
    """ Short prompt at end of tasks to give user option to exit. """

    response = input("\nExit program? y or n >")
    if response == "y":
        exit_func()
    else:
        return None


def print_thanks(name, donation):
    """ Print an *email* saying thank you to screen."""

    print("\nCopy of email...")
    print(f"Dear {name}.  Thank you so very much for your generous donation of ${donation:.2f}.")


def add_new_donor(name):
    """ Add new donors to the database.
        Takes in string argument 'name' that includes a space.
        Splits the string up into two values: last name and first name.
        A new tuple is created from these values and appended to the donor list. """

    first_name, last_name = name.split(" ")
    new_donor = (last_name, first_name),
    donor_db.append(new_donor)
    print("\n", name, " successfully added to list.", sep="")


def add_new_donation(name):
    """ One argument passed in: name.  This is the donor name for
        which donations will be added.  Name gets cleaned up for
        comparison finding in donor_db list.  The record with name and
        amounts is stored as tuple.  Tuple converted to list for updating.
        User is prompted for donation amount.  Donation amount added to
        list. Record converted to tuple.  Old record deleted. New record
        appended to donor list."""

    donation = float(input("Enter new donation amount. >"))
    first_name, last_name = name.split(" ")
    donor_name = (last_name, first_name)

    for donor in donor_db:
        if donor_name == donor[0]:
            existing_donor_record = list(donor[:])
            existing_donor_record.append(donation)
            updated_donor_record = tuple(existing_donor_record)
            donor_db.remove(donor)
            donor_db.append(updated_donor_record)

    print(f"\nDonation of ${donation:.2f} added to record for {name}.")
    print_thanks(name, donation)


def report():
    """ Creates a copy list from the global donor_db list.
        Sorts the copy list using a custom function that sums the
        donation values for a given donor.  Prints to the screen
        derived calculations for totals and averages.  Final report
        is printed in descending order by total donations."""

    # Print formatted header to terminal.
    print("\n{:>15s}{:^40s}{:<20s}\n".format("*" * 10, "Donation Summary Report", "*" * 10))
    col_head = ["Donor Name", "Total Given", "Number Donations", "Average Donation"]
    print(f"{col_head[0]:<18s}|{col_head[1]:>14s} | {col_head[2]:>18s} | {col_head[3]:>18s}")
    print("-" * 78)

    # Sorted copy of master donor_db list.
    sorted_list = sorted(donor_db, key=sort_key, reverse=True)

    # Print report rows.
    for donor in sorted_list:
        donations = donor[1:]
        total_donations = sum(donations)
        count_donations = len(donations)
        average_donation = total_donations / count_donations
        dollar_format_total = "${:.2f}".format(total_donations)
        dollar_format_average = "${:.2f}".format(average_donation)
        name = donor[0][1] + " " + donor[0][0]
        print(f"{name:<18s}{dollar_format_total:>15s}"
              f"{count_donations:>21d}{dollar_format_average:>21s}")


def thank_you_menu():
    """ Menu of options for completing thank you tasks.
        Basic if/else logic to steer user choices. """

    while True:
        response = input("""
    Thank You Options
------------------------
1:  Type 'list' or press 1 to see existing donors.
2:  Enter new donor.
3:  Add donation.
4:  Return to main menu.
0:  Exit the program.

Your choice > """)

        if response == "list" or int(response) == 1:
            show_donor_list()
            task_complete_prompt()
        elif response == "2":
            name = input("\nEnter new donor first and last name > ")
            if existing_donor(name):
                print("\nDonor already in database!")
                choice = input("\nAdd new donation to donor? y or n? > ")
                if choice == "n":
                    task_complete_prompt()
                else:
                    add_new_donation(name)
                    task_complete_prompt()
            else:
                add_new_donor(name)
                choice = input("\nAdd new donation to donor? y or n? > ")
                if choice == "n":
                    task_complete_prompt()
                else:
                    add_new_donation(name)
                    task_complete_prompt()
        elif response == "3":
            name = input("\nEnter donor first and last name >")
            if existing_donor(name):
                add_new_donation(name)
                task_complete_prompt()
            else:
                choice = input("Donor not found! Add donor to the list? y or n >")
                if choice == "n":
                    task_complete_prompt()
                elif choice == "y":
                    add_new_donor(name)
                    choice = input("\nAdd new donation to donor? y or n? > ")
                    if choice == "n":
                        task_complete_prompt()
                    else:
                        add_new_donation(name)
                        task_complete_prompt()
        elif response == "4":
            main_menu()
        elif response == "0":
            exit_func()
        else:
            exit_func()


def main_menu():
    """ Top level menu.  Choices here launch sub-menus. """

    while True:
        choice = int(input('''
      Main Menu
------------------------
1:  Send a thank you.
2:  Create a report.
0:  Exit.

Your choice > '''))

        if choice == 1:
            thank_you_menu()
        elif choice == 2:
            report()
            task_complete_prompt()
        elif choice == 0:
            exit_func()
        else:
            exit_func()


if __name__ == "__main__":
    main_menu()
