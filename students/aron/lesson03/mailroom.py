#!/usr/bin/env python
from statistics import mean

donors = {"William Gates, II":[12300,55000,75600],"Mark Zuckerberg":[4500,1900,12],"Jeff Bezos":[2000,4000,8500], \
         "Paul Allen":[2600,140000],"Donald Trump":[100,50,12]}
actions = ('Send a Thank You', 'Create a Report', 'Quit')

#helper functions
def sort_key(donor):
    return donor[1]


def get_add_donor():
    """
    If the user (you) selects “Send a Thank You” option, prompt for a Full Name.
    If the user types list show them a list of the donor names and re-prompt.
    If the user types a name not in the list, add that name to the data structure and use it.
    If the user types a name in the list, use it.
    :return:
    """
    list = False
    while list == False:
        response = input(f"Whats the donor full name?\nTo see a list of donors type List:")
        possable_donors = []
        for k in donors.keys():
            possable_donors.append(k)
        if response.lower() == "list":
            for donor in possable_donors:
                print(donor)
        elif response not in possable_donors:
            donors[response]= []
            print(f"Adding a new Donor named: {response}")
            return response

        else:
            i = possable_donors.index(response.lower())
            print(f"INDEX IS {i}")
            print(possable_donors[i])
            return possable_donors[i]
            list = True

def send_ty_email(donor, donation):
    print(f"THIS IS YOUR THANK YOU EMAIL {donor} for the ammount of {donation}")

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
    main_response = ""
    while main_response.lower() != "quit":
        valad_response = False
        while valad_response != True:
            main_response = input(f"Enter an action: {actions} > ")
            if main_response.lower() in [x.lower() for x in actions]:
                valad_response = True


            if main_response.lower() == "send a thank you":
                donor_name = get_add_donor()
                donation = int(input(f"What was {donor_name}'s donation amount? > "))
                print(f"Adding a {donation} donation for {donor_name}")
                donors[donor_name].append(donation)
                send_ty_email(donor_name, donation)

            if main_response.lower() == "create a report":  #generate_report():
                generate_report()
    print("THANK YOU FOR QUITING")






if __name__ == '__main__':
    main()

