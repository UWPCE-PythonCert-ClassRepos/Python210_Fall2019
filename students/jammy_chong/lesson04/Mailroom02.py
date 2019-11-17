import os
import pathlib
import datetime

donor_list = dict()

def main_menu(dispatch_dict):
    while True:
        print(main_prompt)
        action = input("")
        if action in dispatch_dict:
            dispatch_dict[action]()
            if action == "q":
                break

def add_donor(name, total=0, gifts=0, average=0):
    if name not in donor_list:
        if gifts > 0:
            average = round(total/gifts, 2)
        donor_list[name] = {'total_given': round(total, 2),
                            'num_gifts':int(gifts),
                            'average_gift':average}

def create_donor_list():
    add_donor("Paul Allen", 708.42, 3)
    add_donor("Mark Zuckerberg", 16396.10, 3)
    add_donor("Jeff Bezos", 877.33, 1)
    add_donor("William Gates, III", 653784.49, 2)
    add_donor("Jammy Chong", 25433.12,2)

def create_letter(name,amount,gifts,average):
    letter = (f"Dear {name},\n\n\tThank you for your very kind donation of ${amount}.\n\n\
             \tYou have donated {gifts} times with an average of ${average} per donation.\n\n\
             \tIt will be put to very good use.\n\n\t\t\tSincerely,\n\t\t\t\t-The Team.")
    return letter

# Menu Actions:

def send_thank_you():
    donor_input = ""
    thank_you_prompt = "For main menu enter 'q' at any time.\nEnter a donor's Full Name or enter 'list' to see the donors list :"
    while donor_input != "q":
        donor_input = input(thank_you_prompt)

        #Donors list and exiting options
        while donor_input == "list":
            for name in donor_list:
                print(name)
            donor_input = input(thank_you_prompt)
        if donor_input == "q":
            break
        donation_amount = input("Please enter donation amount: ")
        if donation_amount == "q":
            break

        #Assigning donor values
        if donor_input not in donor_list:
            new_donor = add_donor(donor_input)
        donor_list[donor_input]['total_given'] += float(donation_amount)
        donor_list[donor_input]['num_gifts'] += 1
        donor_list[donor_input]['average_gift'] = donor_list[donor_input]['total_given']/donor_list[donor_input]['num_gifts']

        print(create_letter(donor_input,donation_amount,donor_list[donor_input]['num_gifts'],\
        donor_list[donor_input]['average_gift']))
        donor_input = "q"

def create_report():
    #Using lambda to access values from list of dictionaries
    sorted_list = sorted(donor_list.items(), key = lambda e: e[1]['total_given'], reverse=True)
    print("Donor Name"," "*14,"| Total Given | Num Gifts | Average Gift")
    print("-"*66)
    for item in sorted_list:
        print("{:25}  ${total_given:>11.2f}{num_gifts:>12d}  ${average_gift:>12.2f}".format(item[0], \
        **item[1]))

def send_thank_you_all():
    folder = input("Enter the folder to save the letters: ")
    path = pathlib.Path('./'+folder)
    if not path.is_dir():
        os.mkdir("./"+folder)
    for name in donor_list:
        string_letter = create_letter(name,donor_list[name]['total_given'],\
        donor_list[name]['num_gifts'],donor_list[name]['average_gift'])
        print (string_letter)
        with open('./'+folder+'/'+name+'.txt', 'w') as f:
            f.write(string_letter)
            f.close()

def quit():
    print("Thank you for using Mailroom.\nExiting Program\n")

main_prompt = ("\nYou are in the main menu, Choose an action to perform:\n"
               "1: Send a Thank You to a single donor.\n"
               "2: Create a Report.\n"
               "3: Send letters to all donors.\n"
               "q: Quit\n")

main_dispatch = {"1": send_thank_you,
                "2":create_report,
                "3":send_thank_you_all,
                "q":quit}

if __name__ == '__main__':
    create_donor_list()
    main_menu(main_dispatch)
