#!/usr/bin/env python3

donors = {'William Gates': [65784.49, 1000.50], 'Mark Zuckerberg': [163.10, 30000, 20000.30], 'Jeff B': [
    877.33], 'Paul Allen': [767.42, 780, 444.20], 'Shantanu Narayen': [1000, 500.33, 3434,34]}

# ex append donors['Mark Z'].append(2435353.23)
# len(donors['Mark Z'])
# first donation on the list donors['Mark Z'][0]

def create_report(donors):
    header = f'{"Donor Name":25}{"| Total Given":15}{"| Num Gifts":>15}{ "| Average Gift":>20}'
    print(header)
    print("_"*len(header))
    for k, v in donors.items(): #use keys?
        # print(k,v,len(v),sum(v), (sum(v)/len(v)))
        # Need to sort!!!!!
        # Add $ symbol!
        name, total, numGifts, AvgGift = (k, sum(v), len(v), (sum(v)/len(v)))
        print(f'{name:20} {total:{17}.2f} {numGifts:15} {AvgGift:{20}.2f}')
    entry_menu()


def entry_menu():
    top_menu = input(
        "Type (1) to Send a Thank You, (2) to Create a Report or (q) to quit: ")
    if top_menu == "1":
        thanks()
    elif top_menu == "2":
        print("reports selected")
        create_report(donors)
    elif top_menu == "q":
        return exit
    else:
        print("please enter a valid input")
        entry_menu()


# If the user (you) selects “Send a Thank You” option, prompt for a Full Name.
# If the user types list show them a list of the donor names and re-prompt.
# If the user types a name not in the list, add that name to the data structure and use it.
# If the user types a name in the list, use it.
# Once a name has been selected, prompt for a donation amount.
# Convert the amount into a number; it is OK at this point for the program to crash if someone types a bogus amount.
# Add that amount to the donation history of the selected user.
# Finally, use string formatting to compose an email thanking the donor for their generous donation. Print the email to the terminal and return to the original prompt.

def thanks():
    thanks_input = input(
        "Type the donors full name, type (list) for all donors or (x) to get back to main menu: ")
    if thanks_input == "list":
        for k, v in donors.items():
            print(k)
        thanks()
    elif thanks_input == "x":
        entry_menu()
    elif thanks_input in donors:
        donation = input("Found " + thanks_input + " please enter donation amount: ")
        donors[thanks_input].append(int(donation))
        thanks()
    elif thanks_input not in donors:
        # donors.keys
        donation = input(thanks_input + " is a new donor, please enter donation amount: ")
        donors.update({thanks_input: [int(donation)]})
        thanks()
    else:
        print("else")
        thanks()


entry_menu()
