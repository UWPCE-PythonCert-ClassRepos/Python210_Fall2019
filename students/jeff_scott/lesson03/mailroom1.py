#!/usr/bin/env python3
import sys

# Global Variables

#donor_db = [('Robert Bigelow', [65300020.00, 10000000.00]),
#            ('Jeff Bezos', [1500000.00]),
#            ('Paul Allen', [4000000000.99, 20000000.00, 1.32]),
#            ('Elon Musk', [2000000.00, 1000000.00, 10432.0]),
#            ('Richard Branson', [2000000.00, 1000000.00, 10432.0])],


donor_db = {
            'Robert Bigelow':   [65300020.00, 10000000.00],
            'Jeff Bezos':       [1500000.00],
            'Paul Allen':       [4000000000.99, 20000000.00],
            'Elon Musk':        [2000000.00, 1000000.00],
            'Richard Branson':  [2000000.00, 1000000.00],
            }

menu = "\n".join(("\nWelcome to the donors program",
                  "Please choose from below options:",
                  "1 - Send a Thank You",
                  "2 - Create a Report",
                  "3 - Exit",
                  "###> "))


def sort_key(donor):
    return donor[1]


def main():
    while True:
        response = input(menu)
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
    """Print a list of donors"""
    print("\nList of all {} donors: ".format(len(donor_db)), '\n', '-' * 25)
    for donor in donor_db:
        print(f" ", donor)
    print('-' * 25)


def thank_you_email(response, donated):
    """Thank you email"""
    print(
        """Dear {},
        Thank you for donating to the billionaires space race charity. Your generous donation will go a long ways
        towards bringing space travel to the masses. 
        
        Thanks,
        BSRC
        """ .format(response, donated))


def send_thank_you():
    """Send thank you e-mails to donors"""
    while True:
        response = input("Enter the name of the donor you would like to send a thank you e-mail to "
                         "\nType 'list' to see a all our donors: ")
        if response == 'quit':
            break
        if response == "list":
            list_donors()
        elif response in donor_db:
            donation = input("Enter donation amount: ")
            if donation == 'quit':
                break
            donated = float(donation)
            donor_db[response].append(donated)
            thank_you_email(response, donated)
        else:
            donation = input("{} is not a donor, adding to donor db, enter donation amount: ".format(response))
            donated = float(donation)
            [response] = [donated]
            thank_you_email(response, donated)


def create_report():
    sort_db = sorted(donor_db.items(), key=sort_key, reverse=True)
    header_donor_name = "Donor Name"
    header_total_given = "Total Given"
    header_num_gifts = "Num Gifts"
    header_average_gift = "Average Gift"

    header = f"{header_donor_name:<25} | {header_total_given:>17} | {header_num_gifts:>10} | {header_average_gift:>15}"

    print(header)
    print(len(header) * '-')

    for key, value in sort_db:
        total_given = sum(value)
        num_gifts = len(value)
        average_gift = total_given / num_gifts
        total_given_formatted = ("{:.2f}".format(total_given))
        average_gift_formatted = ("{:.2f}".format(average_gift))
        print(f"{key:<25} | $ {total_given_formatted:>15} | {num_gifts:>10} | $ {average_gift_formatted:>10}")


def exit_program():
    print("Bye!")
    sys.exit()


if __name__ == "__main__":
    main()
