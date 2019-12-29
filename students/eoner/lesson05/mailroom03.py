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
    
    #more comprehension
    [print(f'{k:20} {sum(v):{17}.2f} {len(v):15} {(sum(v)/len(v)):{20}.2f}') for k,v in donors.items()]
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
        #use comprehnesion to create a new donor name list
        print(*[k for k in donors.keys()], sep='\n')
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
    #more comprehension
    [create_thankYou(k,v[-1]) for k, v in donors.items()]
    
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
        print("Creating new directory: " + str(file_path))
    with open(file_fullPath, 'w') as outfile:
        outfile.write(output)
        print("file: " +file_fullPath + " created")
    


#try to have both prompt and selections inside a single dictionary
MAIN_MENU_DISPATCH = {
    "Menu_prompt":("Type (1) to send a Thank You to single donor, (2) to send a Thank You to all donors, (3) to Create a Report or (q) to quit"),
    "dic_action":"donors",
    "1":thanks,
    "2":thanks_all,
    "3":create_report,
    "q":sys.exit

}

TY_LETTER = ("Dear {},\n \n Thanks for the ${:.2f} sucker.\n\n                          -Your Fave Charity")

#Create a function that can call another function from a dictionary
#optional dictionary for donor dic so that if the input does not exist in the firs dic, check it against optional dic, look up the entry for special call in first dic and call with input
def menu_driver(p,d={}):
    #store local copy so we can pop the "Menu Prompt" if it exists and print
    prompt = p
    accessory_dic = d
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
            if response in d:
                #call the function passed in p
                action=(prompt["dic_action"])
                print(action,response)
                (action)((response))
        print("Please enter a valid input")
        menu_driver(p)
        
def entry_menu():
    menu_driver(MAIN_MENU_DISPATCH, donors)

#start the app
entry_menu()


