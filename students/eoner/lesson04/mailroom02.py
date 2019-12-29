#!/usr/bin/env python3
import sys
import os

donors = {'William Gates': [65784.49, 1000.50], 'Mark Zuckerberg': [163.10, 30000, 20000.30], 'Jeff B': [
    877.33], 'Paul Allen': [767.42, 780, 444.20], 'Shantanu Narayen': [1000, 500.33, 3434,34]}

# ex append donors['Mark Z'].append(2435353.23)
# len(donors['Mark Z'])
# first donation on the list donors['Mark Z'][0]

def create_report():
    header = f'{"Donor Name":25}{"| Total Given":15}{"| Num Gifts":>15}{ "| Average Gift":>20}'
    print(header)
    print("_"*len(header))
    
    for k, v in donors.items(): #use keys?
        # print(k,v,len(v),sum(v), (sum(v)/len(v)))
        # Need to sort!!!!!
        # Add $ symbol!
        name, total, numGifts, AvgGift = (k, sum(v), len(v), (sum(v)/len(v)))
        print(f'{name:20} {total:{17}.2f} {numGifts:15} {AvgGift:{20}.2f}')
    print("\n")
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
        create_thankYou(str(thanks_input),int(donation))
        thanks()
    
    elif thanks_input not in donors:
        # donors.keys
        donation = input(thanks_input + " is a new donor, please enter donation amount or (x) to go back: ")
        print("new donor added")
        if donation == "x":
            pass
        
        else:
            donors.update({thanks_input:[int(donation)]})
            create_thankYou(str(thanks_input),int(donation))
        
        thanks()
    else:
        print("else")
        thanks()

#call each donor in dictionary then send thank you letter with last donation
def thanks_all():
    for k, v in donors.items():
        create_thankYou(k,v[-1])
    print('\n')    
    entry_menu()


def create_thankYou(name, last_Donation):
    #create letter
    output = TY_LETTER.format(name,last_Donation)
    file_name = name+"_thank_you_letter.txt"
    file_path = os.getcwd() + "/TY_LETTERS"
    file_fullPath = file_path + "/" + file_name

    if not os.path.exists(file_path):
        os.mkdir(file_path)
    with open(file_fullPath, 'w') as outfile:
        outfile.write(output)
        print("file: " +file_fullPath + " created")
    


#try to have both prompt and selections inside a single dictionary
MAIN_MENU_DISPATCH = {
    "Menu_prompt":("Type (1) to send a Thank You to single donor, (2) to send a Thank You to all donors, (3) to Create a Report or (q) to quit"),
    "accessory_dic":donors,
    "1":thanks,
    "2":thanks_all,
    "3":create_report,
    "q":sys.exit

}

TY_LETTER = ("Dear {},\n \n Thanks for the ${:.2f} sucker.\n\n                          -Your Fave Charity")

#Create a function that can call another function from a dictionary
def menu_driver(d):
    #store local copy so we can pop the "Menu Prompt" if it exists and print
    prompt = d
    if "Menu_prompt" in prompt:
        print(prompt["Menu_prompt"])
        #prompt.pop("Menu_prompt", None)
        # print("pop")
    
    while True:
        response = input()
        print(response + " selected")
        
        try:
            prompt[response]()
        
        except KeyError:
            print("Please enter a valid input")
            menu_driver(d)           
        
        else:
            break

def entry_menu():
    menu_driver(MAIN_MENU_DISPATCH)

#start the app
entry_menu()


