#!/usr/bin/env python3

import os
from datetime import datetime

from cli import CLI
from mailroom import Donor, DonorCollection

# Set default file path as the current working directory
os.environ['OUTPUT_DIR'] = os.getcwd() + '/'

cli = CLI()

DONORS_FILE = 'donors.json'

donors = DonorCollection(DONORS_FILE)



# Pre-check if our file is here


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
    try:
        prompt = True  # Set to false to stop prompting and exit.
        while prompt:
            try:
                user_input = input('Please enter donor name: ')
                donor_name = user_input.strip().title()
            except KeyboardInterrupt:
                print('\n')
                return None

            if user_input.lower() == 'list':
                for donor in donors:
                    print(donor.name)
                print('\n')

            else:
                # Find whether the name is in the list:

                try:

                    donor = donors.get_donor_by_name(donor_name)
                    donation_amount = input('Donation Amount: ')
                    # Sanitize input a bit
                    donation_amount = round(float(donation_amount.replace('$', '').replace(',', '')), ndigits=2)
                    donor.add_donation(donation_amount)
                    donors.save_donors()
                    print(donor.thank_donor())
                    print('\n')
                    donors.save_donors()

                except ValueError:
                    donation_amount = input('Donation Amount: ')
                    # Sanitize our input a bit
                    donation_amount = round(float(donation_amount.replace('$', '').replace(',', '')), ndigits=2)
                    donor = Donor(donor_name, [{'amount':donation_amount, 'date': datetime.now()}])
                    donors.add_donor(donor)
                    print(donor.thank_donor())
                    print('\n')
                    donors.save_donors()

    except KeyboardInterrupt:
        return None


@cli.add_option
def send_letters_to_all_donors():
    """
    Generate a letter for every donor. Save the letter to a file under 'OUTPUT_DIR' env var path.
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

        filename = file_name_prefix + '_' + datetime.now().strftime("%b%d%YT%H%M%S") + '.txt'

        with open(os.environ['OUTPUT_DIR'] + filename, 'w') as f:
            f.write(message)

    print('\nSaved {} letters to {}\n'.format(len(donors.keys()), os.environ['OUTPUT_DIR']))


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
        os.environ['OUTPUT_DIR'] = donor_directory

        print('\nSuccessfully updated base directory.\n')

        check_for_donors()

    else:
        user_input = input('Directory does not exist. Create directory [Y/N]? ')

        if user_input.lower() in ['yes', 'y']:
            os.makedirs(donor_directory)
            os.environ['OUTPUT_DIR'] = donor_directory
            print('\nSuccessfully updated base directory\n.')

        else:
            print('Aborting and returning to main menu.\n')


if __name__ == '__main__':
    cli.run_cli()
