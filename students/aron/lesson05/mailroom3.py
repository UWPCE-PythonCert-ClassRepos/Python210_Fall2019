#!/usr/bin/env python
from statistics import mean
import os
import time

donors = {"William Gates, II":[12300,55000,75600],"Mark Zuckerberg":[4500,1900,12],"Jeff Bezos":[2000,4000,8500], \
         "Paul Allen":[2600,140000],"Donald Trump":[100,50,12]}

actions = ('Add new donation or new donor.',
           'Create a Report.',
           'Send letters to all donors.',
           'Quit')

cwd = os.getcwd()
folder = cwd + '/outgoing'

#helper functions
def sort_key(donor):
    return donor[1]

def build_menu(actions):
    options = ""
    for action in actions:
        options += f"{actions.index(action) + 1} - {action}\n"
    menu = f"Choose an action:\n\n{options}"
    return menu

def add_donation(donor_name):
    while True:
        try:
            donation = int(input(f"What was {donor_name}'s donation amount? > "))
            print(f"Adding a {donation} donation for {donor_name}")
            donors[donor_name].append(donation)
            send_ty_email(donor_name, donation)
            return
        except ValueError:
            print(f'Please enter whole dollar amount.')


def get_add_donor():
    """
    """
    while True:
        response =  input(f"Whats the donor full name?\nTo see a list of donors type List:")
        if response.lower() == "list":
            for donor in donors:
                print(donor)
        elif response not in donors:
            donors[response]= []
            print(f"Adding a new Donor named: {response}")
            add_donation(response)
            break
        else:
            possable_donors = [k for k in donors.keys()]
            i = possable_donors.index(response)
            donor = possable_donors[i]
            add_donation(donor)
            break

def send_ty_email(donor, donation):
    print(f"THIS IS YOUR THANK YOU EMAIL {donor} for the ammount of {donation}")

def send_email_to_all():
    create_folder()
    for k, v in donors.items():
        create_email(k, sum(v))

def create_folder():
    if os.path.isdir(folder):
        for root, dirs, files in os.walk(folder):
            print(files)
            for file in files:
                os.remove(folder + "/" + file)
    else:
        os.makedirs(folder, 0o777)

def create_email(donor, donation):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    file_name = donor.replace(" ", "_") + timestr

    email_lines = [
        f"Dear {donor}\n",
        f"\tThank you for your very kind donation of ${donation}\n",
        f"\tIt will be put to very good use.\n",
        f"\n",
        f"\t Sincerely,\n",
        f"\t -The Team",
    ]
    f = open(folder + "/" + file_name, "w")
    for line in email_lines:
        print(line)
        f.write(line)
    f.close()


def generate_report():

    list_donors = [(k, sum(v), len(v), mean(v))for k,v in donors.items() ]
    sorted_donors = sorted(list_donors, key=sort_key, reverse=True)
    header = 'Donor Name          | Total Given | Num Gifts | Average Gift'
    separator = '-' * len(header)
    bodyline = '{:20} ${:11.2f}   {:9d}  ${:12.2f}'
    # build the body of the report; a list of donors and info about their gifts
    body = []
    for donor in sorted_donors:
        print(donor)
        body.append(bodyline.format(donor[0], donor[1], donor[2], donor[3]))
    # print out the report
    print(header, separator, sep='\n')
    for i in range(len(sorted_donors)):
        print(body[i])

def main():
    print(f"Welcome to donor tool what whould you like to do? > ")
    while True:
        try:
            main_response = int(input(build_menu(actions)))
        except ValueError:
            print(f'Please choose a number between 1 and {len(actions)}')
            continue
        if main_response == 1:
            get_add_donor()
        elif main_response == 2:
            generate_report()
        elif main_response == 3:
            send_email_to_all()
        elif main_response == 4:
            print("THANK YOU FOR QUITING")
            break
        else:
            print(f'Please choose a number between 1 and {len(actions)}')





if __name__ == '__main__':
    main()
