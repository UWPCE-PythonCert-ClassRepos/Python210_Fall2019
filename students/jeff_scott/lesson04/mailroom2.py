#!/usr/bin/env python3
import datetime

charity = "BSRC"
today = datetime.date.today()

donor_db = {
    'Robert Bigelow': [65300020.00, 10000000.00],
    'Jeff Bezos': [1500000.00],
    'Paul Allen': [4000000000.99, 20000000.00],
    'Elon Musk': [2000000.00, 1000000.00],
    'Richard Branson': [2000000.00, 1000000.00],
}

menu = "\n".join(("\nWelcome to the donors program",
                  "Please choose from below options:",
                  "1 - Send a Thank You",
                  "2 - Create a Report",
                  "3 - Send letter to all donors",
                  "q - Quit",
                  "###> "))

main_prompt = menu


def sort_key(donor):
    return donor[1]


def list_donors():
    """Print a list of donors"""
    print("\nList of all {} donors: ".format(len(donor_db)), '\n', '-' * 25)
    for donor in donor_db:
        print(f" ", donor)
    print('-' * 25)


def thank_you_email(response, donated):
    letter = (
        f"""
        Dear {response},
        Thank you for donating to the billionaires space race charity. Your generous donation of ${donated:.2f}! will go
        a long ways towards bringing space travel to the masses. 

        Thanks,
        {charity}
        """.format(**donor_db))
    print("Writing files to current working directory")
    return letter


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


def thank_you_email_all():
    for donor, donated in donor_db.items():
        with open(f'{donor}_{today}.txt', 'w') as file:
            file.write(f""" 
        Dear {donor},
        Thank you for donating to the billionaires space race charity. Your generous donation of ${sum(donated)} will go
        a long ways towards bringing space travel to the masses. 

        Thanks,
        {charity}
        """.format(**donor_db))
        break


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


def quit():
    print("Quitting")
    return "exit menu"


main_dispatch = {
            "1": send_thank_you,
            "2": create_report,
            "3": thank_you_email_all,
            "q": quit
        }


def menu_selection(prompt, dispatch_dict):
    while True:
        response = input(prompt)
        if dispatch_dict[response]() == "exit menu":
            break


# make executable


if __name__ == "__main__":
    menu_selection(main_prompt, main_dispatch)
