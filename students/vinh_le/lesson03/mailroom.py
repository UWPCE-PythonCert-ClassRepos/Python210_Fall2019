
fred_donations = [100, 1000, 10000]
bob_donations = [200, 2000, 20000]
todd_donations = [300, 3000, 30000]
sally_donations = [400, 4000, 40000]
becky_donations = [500, 5000, 50000]

donor_dict = {
    "Fred": fred_donations,
    "Bob": bob_donations,
    "Todd": todd_donations,
    "Sally": sally_donations,
    "Becky": becky_donations
}


def send_thank_you():
    print("Sending TY...")
    while True:
        response_1 = input('Please enter donors full name')
        if response_1 == 'list':
            print(donor_dict)
            continue

        # If the user types a name not in the list, add that name to the data structure and use it.
        if response_1 not in donor_dict:
            donor_dict[response_1] = []
            curr_donor_list = donor_dict[response_1]
        else:
            curr_donor_list = donor_dict.get(response_1)


        response_2 = input("Enter donation amount:")

        # Exits the program if the the string is an integer,
        # and if the donation amount is above 1,000,000,000,000(Due to char limit of report)
        try:
            if int(response_2) >= 1000000000000:
                print("Amount entered was above 1,000,000,000,000")
                return quit_program()
        except ValueError:
            print("Amount entered was not a proper number")
            return quit_program()

        else:
            curr_donor_list.append(int(response_2))
            print(f"Thank You {response_1} for your donation of {response_2}.")
            break


def create_report():
    table_title_format = "{:<26}{:14}{:12}{:>14}"
    table_entry_format = "{:<26} ${:>12}{:11}  ${:>12}"

    print(table_title_format.format("Donor Name", "| Total Given ", "| Num Gifts ", "| Average Gift"))
    print(table_title_format.format("-" * 26, "-" * 14, "-" * 12, "-" * 14))

    for donor in donor_dict:
        print(table_entry_format.format(donor,
                                        get_total_given(donor_dict[donor]),
                                        get_num_gifts(donor_dict[donor]),
                                        get_average_gift_amount(donor_dict[donor])))


def quit_program():
    return "quit"


def get_total_given(donations_list):
    total_donation = 0

    for amount in donations_list:
        total_donation += amount
    return total_donation


def get_num_gifts(donations_list):
    num_of_gifts = 0

    for amount in donations_list:
        num_of_gifts += 1
    return num_of_gifts


def get_average_gift_amount(donations_list):
    return get_total_given(donations_list) / get_num_gifts(donations_list)


# Dictionary dispatch for mailroom menu with values as function calls
mailroom_menu_dispatch = {
    "send a thank you": send_thank_you,
    "create a report": create_report,
    "quit": quit_program
}

main_menu_prompt = ('\nWhat would you like to do?\n'
                    'Type one of the following\n'
                    '-Send a Thank You\n'
                    '-Create a Report\n'
                    '-quit\n'
                    'INPUT:')


def menu_selection(prompt, dispatch_dict):

    while True:
        response = input(prompt)

        # If input is not within dispatch, it will return an "invalid"
        dict_value = dispatch_dict.get(response.lower(), "invalid")
        if dict_value == "invalid":
            # Checks for invalid input
            print("Invalid input, please try again.\n")
            continue
        if dict_value() == "quit":
            print("Exited")
            break


if __name__ == "__main__":
    menu_selection(main_menu_prompt, mailroom_menu_dispatch)
