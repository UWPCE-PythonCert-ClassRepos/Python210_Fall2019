#!/usr/bin/env python3
"""
Created on Sat Nov  2 14:12:38 2019

@author: Bishal.Gupta
"""

import sys  # imports go at the top of the file

donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ("Satya Nadella", [2500.45, 3558.98, 5700.45]),
            ]

prompt = "\n".join(("Welcome to the Mailroom Program!",
          "Please choose from below options:",
          "1 - View Donor List",
          "2 - Send a Thank You",
          "3 - Create a Report",
          "4 - quit",
          ">>> "))

def view_donor_list():
    for a,b in donor_db:
        print(a)        


def send_thank_you():
        donor_name = input("Enter the full name of the donor?").title()
                
        # Check whether name is in the list of tuples and print feedback
        for d in donor_db:
            if donor_name in d:
                # Provide feedback that the donor is already in the list
                print(str(donor_name) + ' found in the donor_db')
            elif donor_name not in d:                
                # Provide feedback        
                print('I don\'t have ' + str(donor_name) + '\'s donation, what is it?')
            
                # Take in a new donation for the associated name
                donation_amount = input()
                donation_amount = int(donation_amount)
            
                # Enter new donor name and amount
                donor_db.insert(0,(donor_name,[donation_amount]))
                print('Thank you ' + str(donor_name) + ' for the donation amount of $' + str(donation_amount))
            else:
                print("Not a valid option!")
            break
                
                
            
def create_report():
    for i,v in donor_db:
        print('Donorname '+ "\n" + i, ' donation amount of $' + str(sum(v)) + ' with total of number gifts: ' + str(len(v)) + ' and average number of gifts: ' + str(sum(v)/len(v)))
      

def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script
        

def main():
    while True:
        response = input(prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        if response == "1":
            view_donor_list()
        elif response == "2":
            send_thank_you()
        elif response == "3":
            create_report()
        elif response == "4":
            exit_program()
        else:
            print("Not a valid option!")    
        
if __name__ ==  "__main__":
    main()
    
        
