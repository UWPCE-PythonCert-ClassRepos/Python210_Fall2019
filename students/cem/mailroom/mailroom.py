#!/usr/bin/env python3
import sys

"""
The script prompts the user (you) to choose from a menu of 
3 actions: “Send a Thank You”, “Create a Report” or “quit”.
"list" will bring up up donors list.
"q" will quit the application.
"""

# Set as global ENV so when my charity gets acquired I can change here and it will change everywhere referenced.
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
                    "1 - Send a Thank You",
                    "2 - Create a Report",
                    "3 - Exit",
                    ">>> "))


def main():
    while True:
        response = input(prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        if response == "list":
            list_donors()
        elif response == "1":
            send_thank_you()
        elif response == "2":
            create_report()
        elif response == "3":
            exit_program()
        else:
            print("Not a valid option!")


def list_donors():
    """Prints a list of all donors in list"""
    print("\nList of all {} donors: ".format(len(donors)), '\n', '-' * 25)
    for donor in donors.keys():
        print(f" ", donor)
    print('-' * 25)


def thank_you_email(response, donated):
    """Prints out thank you letter"""
    print(
        """
        Dear {}, 
        
        Thank you for your amazingly generous donation of ${:.2f}! 
        We, at {}, greatly appreciate your donation, and your sacrifice. 
        
        Your support helps to further our mission.
        
        Regards,
        Cem
        """.format(response, donated, CHARITY_NAME))


def send_thank_you():
    """Send thank you e-mails to existing or new donors"""
    while True:
        response = input("Enter the name of who you would like to send a thank you e-mail to "
                         "\nType 'list' to see a all our donors: ")
        if response == 'q':
            break
        if response == "list":
            list_donors()
        elif response in donors:
            donation = input("Enter donation amount: ")
            if donation == 'q':
                break
            donated = float(donation)
            donors[response].append(donated)
            # print("\n", donors)   # Good for testing, shows donor appended to list.
            thank_you_email(response, donated)
        else:
            donation = input("{} is not an existing donor, adding to db, enter donation amount: ".format(response))
            donated = float(donation)
            donors[response] = [donated]
            # print("\n", donors) # Good for testing, shows donor appended to list.
            thank_you_email(response, donated)


def create_report():
    header_donor_name = "Donor Name"
    header_total_given = "Total Given"
    header_num_gifts = "Num Gifts"
    header_average_gift = "Average Gift"

    header = f"{header_donor_name:<25} | {header_total_given:>10} | {header_num_gifts:>10} | {header_average_gift:>10}"

    print(header)
    print(len(header)*'-')

    for key, value in donors.items():
        total_given = sum(value)
        num_gifts = len(value)
        average_gift = total_given / num_gifts
        total_given_formatted = ("{:.2f}".format(total_given))
        average_gift_formatted = ("{:.2f}".format(average_gift))
        print(f"{key:<25} | $ {total_given_formatted:>10} | {num_gifts:>9} | $ {average_gift_formatted:>10}")


def exit_program():
    print("Bye!")
    sys.exit()


# make executable
if __name__ == "__main__":
    main()
