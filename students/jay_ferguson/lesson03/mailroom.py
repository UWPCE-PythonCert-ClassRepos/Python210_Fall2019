#!/usr/bin/env python3

from cli import CLI

cli = CLI()

donors = [
    {
        'Donor Name': 'William Gates, III',
        'Total Given': 653784.49,
        'Num Gifts' : 2
    },
    {
        'Donor Name': 'Mark Zuckerberg',
        'Total Given': 16396.10,
        'Num Gifts':  3
    },
    {
        'Donor Name': 'Jeff Bezos',
        'Total Given':  877.33,
        'Num Gifts': 1
    },
    {
        'Donor Name': 'Paul Allen',
        'Total Given': 708.42,
        'Num Gifts': 3
    },
    {
        'Donor Name': 'Jay Ferguson',
        'Total Given': 21.12,
        'Num Gifts': 2
    }
]

@cli.add_option
def send_thank_you():
    """
    If the user types list show them a list of the donor names and re-prompt.
    If the user types a name not in the list, add that name to the data structure and use it.
    If the user types a name in the list, use it.
    This function makes the dubious assertion that first names will be first when entered.
    :return: None
    """

    #TODO: Most of the nested structures here should be discrete functions.

    message = """Dear {first_name},
    
    Thank you for your generous donation!
     
     Best Regards,
     
     The UW Python Program"""

    # Generate a list of current donor names to compare against
    donor_names = [i['Donor Name'] for i in donors]

    prompt = True  # Set to false to stop prompting and exit.
    while prompt:
        try:
            user_input = input('Please enter donor name: ')
        except KeyboardInterrupt:
            print('\n')
            return None

        if user_input == 'list':
            for name in donor_names: print(name)
            print('\n')

        else:
            #Find whether the name is in the list:

            found = False  # Set to True to skip data input

            for name in donor_names:
                if user_input.lower() in name.lower():
                    print (message.format(first_name=name.split(' ')[0]))
                    print('\n')
                    prompt = False
                    found = True
                    return None
                else:
                    donor_name = user_input.title()

            if not found: # Start prompting for data and write it to the donors global.
                total_given = input('Donation Amount: ')
                #Sanitize our input a bit
                total_given = round(float(total_given.replace('$', '')), ndigits=2)
                num_gifts = 1

                new_donor = {
                    'Donor Name': donor_name,
                    'Total Given': total_given,
                    'Num Gifts': num_gifts
                }

                donors.append(new_donor)

                print (message.format(first_name=donor_name.split(' ')[0]))
                print('\n')
                prompt = False


@cli.add_option
def generate_report():
    """
    Generate a report. And print it.
    :return: None
    """
    sorted_donors = sorted(donors, key=lambda i: i['Total Given'], reverse=True)  # Hooray lambda fuctions!
    spacing = 20  # Blank space to pad rows with
    header_keys = list(donors[0].keys())
    header_keys.append('Average Gift')

    # Calculate average donation and append it to the sorted_donors dicts
    for i in sorted_donors:
        average_donation = round(i['Total Given'] / i['Num Gifts'], ndigits=2)
        i['Average Gift'] = average_donation

    header = '\n' + ('|  {:<20}' * len(header_keys))
    formatted_header = header.format(*header_keys)
    row_template = '|  {:<20}|  ${:<20}|  {:<20}|   ${:<20}'
    print(formatted_header)
    divider = '-'* len(formatted_header)
    print(divider)

    for i in sorted_donors:
        row = []
        for key in header_keys:
            row.append(i[key])
        print(row_template.format(*row))

    print('')

if __name__ == '__main__':

    cli.run_cli()