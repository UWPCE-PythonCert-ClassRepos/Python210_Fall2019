#!/usr/bin/env python3

from cli import CLI

cli = CLI()

# TODO: Keep a record of donation amounts. Donations:[]
# TODO: Refactor logic to account for this.

donors = {
    'William Gates': [653784.49],
    'Mark Zuckerberg': [1600.10, 300.34],
    'Jeff Bezos': [877.33],
    'Paul Allen': [405, 678.23, 200.12],
    'Jay Ferguson': [21.12]
}



@cli.add_option
def send_thank_you():
    """
    If the user types list show them a list of the donor names and re-prompt.
    If the user types a name not in the list, add that name to the data structure and use it.
    If the user types a name in the list, use it.
    This function makes the dubious assertion that first names will be first when entered.
    :return: None
    """

    # TODO: Most of the nested structures here should be discrete functions or a dict mapping of functions.

    message = """Dear {first_name},
    
    Thank you for your generous donation!
     
     Best Regards,
     
     The UW Python Program"""

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
                prompt = False
                found = True
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


@cli.add_option
def generate_report():
    """
    Generate a report. And print it.
    :return: None
    """
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


if __name__ == '__main__':
    cli.run_cli()
