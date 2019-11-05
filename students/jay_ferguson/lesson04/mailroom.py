#!/usr/bin/env python3

import os
import json

from datetime import datetime
from cli import CLI

# Set default file path as the current working directory
os.environ['DONOR_DIR'] = os.getcwd() + '/'

cli = CLI()

DONORS_FILE = 'donors.json'

# Pre-check if our file is here

def check_for_donors():
    if not os.path.isfile(os.environ['DONOR_DIR'] + DONORS_FILE):
        print("""donors.json not found in this directory. We'll use sample data, 
or you can choose a different directory.\n""")


def read_donors():
    """
    Read data from donors.json
    :return: donors dict
    """

    try:
        with open(os.environ['DONOR_DIR'] + DONORS_FILE, 'r') as f:
            donors = json.load(f)

    except FileNotFoundError:  # Use our pre-populated list for now
        donors = {
            'William Gates': [653784.49],
            'Mark Zuckerberg': [1600.10, 300.34],
            'Jeff Bezos': [877.33],
            'Paul Allen': [405, 678.23, 200.12],
            'Jay Ferguson': [21.12]
        }

    return donors


def save_donors(donors):

    """
    Save donors dict to file. Overwrites current file or creates a new
    file if not found in donors directory.
    """

    with open(os.environ['DONOR_DIR'] + DONORS_FILE, 'w') as f:
        json.dump(donors, f)

sub_prompt = CLI()


@cli.add_option
def send_thank_you_to_a_donor():
    """
    If the user types list show them a list of the donor names and re-prompt.
    If the user types a name not in the list, add that name to the data structure and use it.
    If the user types a name in the list, use it.
    This function makes the dubious assertion that first names will be first when entered.
    :return: None
    """

    # TODO: Most of the nested structures here should be discrete functions or a dict mapping of functions.

    message = """Dear {first_name},
    
    Thank you for your generous contribution!
     
     Best Regards,
     
     The UW Python Program"""

    donors = read_donors()

    prompt = True  # Set to false to stop prompting and exit.
    while prompt:
        try:
            user_input = input('Please enter donor name: ')
        except KeyboardInterrupt:
            print('\n')
            return None

        if user_input.lower() == 'list':
            for name in donors.keys():
                print(name)
            print('\n')

        else:
            # Find whether the name is in the list:

            found = False  # Set to True to skip data input

            if user_input.title() in donors.keys():
                donation_amount = input('Donation Amount: ')
                # Sanitize input a bit
                donation_amount = round(float(donation_amount.replace('$', '').replace(',', '')), ndigits=2)
                donors[user_input].append(donation_amount)

                print(message.format(first_name=user_input.title().split(' ')[0]))
                print('\n')
                save_donors(donors)
                return None
            else:
                donor_name = user_input.title()

            if not found:  # Start prompting for data and write it to the donors global.
                donation_amount = input('Donation Amount: ')
                # Sanitize our input a bit
                donation_amount = round(float(donation_amount.replace('$', '').replace(',', '')), ndigits=2)

                donors[user_input] = [donation_amount]

                print(message.format(first_name=donor_name.split(' ')[0]))
                print('\n')
                prompt = False
                save_donors(donors)


@cli.add_option
def send_letters_to_all_donors():
    """
    Generate a letter for every donor. Save the letter to a file under 'DONOR_DIR' env var path.
    """

    donors = read_donors()

    message = """Dear {first_name},

    Thank you for your generous contribution!

     Best Regards,

     The UW Python Program"""

    for donor in donors.keys():
        message = message.format(first_name=donor.split(' ')[0])
        # Strip commas and spaces
        file_name_prefix = donor.replace(' ', '').replace(',' , '')
        filename = file_name_prefix + '_' +  datetime.now().strftime("%b%d%YT%H%M%S") + '.txt'

        with open(os.environ['DONOR_DIR'] + filename, 'w') as f:
            f.write(message)

    print('\nSaved {} letters to {}\n'.format(len(donors.keys()), os.environ['DONOR_DIR']))









@cli.add_option
def generate_report():
    """
    Generate a report. And print it.
    :return: None
    """

    donors = read_donors()
    sorted_donors = sorted(donors, key=lambda i: sum(donors[i]), reverse=True)  # Hooray lambda fuctions!
    header_keys = ['Donor Name', 'Total Given', 'Number Gifts', 'Average Gift']
    header = '\n' + ('|  {:<20}' * len(header_keys))
    formatted_header = header.format(*header_keys)
    row_template = '|  {:<20}|  ${:<20}|  {:<20}|   ${:<20}'
    print(formatted_header)
    divider = '-' * len(formatted_header)
    print(divider)

    for i in sorted_donors:
        row = []
        row.append(i)
        # Calculate average donation and append it to the sorted_donors dicts
        total_donation = sum(donors[i])
        average_donation = total_donation / len(donors[i])
        row.append(round(total_donation, ndigits=2))
        row.append(len(donors[i]))
        row.append(round(average_donation, ndigits=2))
        print(row_template.format(*row))

    print('')


@cli.add_option
def set_donors_file_directory():
    """
    Prompt for and set the base directory for donor files.
    Defaults to current working directory as set in environment variable.
    """

    donor_directory = input('Directory to read and save donor files: ')

    # Sanitize input to match expected format

    if donor_directory[-1:] != '/':
        donor_directory += '/'

    if '~' in donor_directory:
        donor_directory = os.path.expanduser(donor_directory)

    if os.path.exists(donor_directory):
        os.environ['DONOR_DIR'] = donor_directory

        print('\nSuccessfully updated base directory.\n')

        check_for_donors()

    else:
        user_input = input('Directory does not exist. Create directory [Y/N]? ')

        if user_input.lower() in ['yes', 'y']:
            os.makedirs(donor_directory)
            os.environ['DONOR_DIR'] = donor_directory
            print('\nSuccessfully updated base directory\n.')

        else:
            print('Aborting and returning to main menu.\n')


if __name__ == '__main__':
    cli.run_cli()
