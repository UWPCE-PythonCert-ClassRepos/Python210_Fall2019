# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 20:07:30 2019

@author: mdenko
"""

# mairoom OOO description -------------------------------------------------------

"""Goal: Refactor the mailroom program using classes to help organize the code.

The functionality is the same as the earlier mailroom:

Mailroom Part 1

But this time, we want to use an OO approach to better structure the code to 
make it more extensible.

It was quite reasonable to build the simple mailroom program using a single 
module, a simple data structure, and functions that manipulate that data 
structure. In fact, you’ve already done that :-)

But if one were to expand the program with additional functionality, it 
would start to get a bit unwieldy and hard to maintain. So it’s a pretty good 
candidate for an object-oriented approach."""

# Defining main donor class ---------------------------------------------------

class Main_Donor_Class:
    "Main class to define functionality of program"

    def __init__(self, donorname, amount=None):
        "Creating _init_ to specify the name of donor and the amount of donation"
        self.donorname = donorname.title()
        self.donation_list = []
        "If the donor is donating a non zero amount, add it, else dont"
        if amount is not None:
            for i in amount:
                self.donation_list.append(i)
    
    def __str__(self):
        "defining string to print when new donation occurs"
        return f'Donor("{self.donorname}") has donated ${self.donation_total:.2f}'
    
    def __repr__(self):
        "defining the donor name"
        return f"Donor('{self.donorname}')"

    def add_new_donation(self, amount):
        "defining how to add a new donation"
        if type(amount) == int or type(amount) == float:
            "if donationa amount is not a number, then add it"
            self.donation_list.append(amount)
        return self.donation_list
        "return the donation list as the final output"

    @property
    def donation_quantity(self):
        "Will return the total count of donations"
        return len(self.donation_list)

    @property
    def donation_total(self):
        "Will return the total amount in $$$ of the donation"
        return sum(self.donation_list)

    @property
    def donation_average(self):
        "Will return the average amount in $$$ of all donations"
        return self.donation_total / self.donation_quantity

    def create_thank_you_letter(self):
        "Creating a custom thank you letter for each donater"

        self.letter = """
        Yo {},
        Thanks for your awesome donation of ${:.2f}. Your gift will keep
        the North Pole fully operating this christmas - 
        thanks again""".format(self.donorname, self.donation_list[-1])
        return self.letter

# - Defining Donor Sub Class --------------------------------------------------
        
class Donor_Sub_Class:
    def __init__(self, donor_group):
        "Creating _init_ to specify self and donor group - donor group makes up donor list"
        self.donor_group = donor_group
        "Creating empty list for donor list"
        self.donor_list = {}

    def __repr__(self):
        return f"Donor_Sub_Class('{self.donor_group}')"

    def create_donor(self, donorname, donation_list):
        "defining how to create a new donor to the donor group"
        new_donor = Main_Donor_Class(donorname, donation_list)
        "if donor already exisits in list then only add a new amount"
        if donorname.lower() in self.donor_list.keys():
            [self.donor_list[donorname.lower()].add_new_donation(amount) for amount in donation_list]
        else:
            "If a donor does not already exit then add it to donor list"
            self.donor_list.setdefault(donorname.lower(), new_donor)
        self.sort_donor_list()
        "return modified donor list"
        return self.donor_list

    def sort_donor_list(self):
        "sorting donor list on donation total using lambda function"
        self.donor_list = dict(sorted(self.donor_list.items(), key=lambda e: e[1].donation_total, reverse=True))
        "returning sorted donor_list"
        return self.donor_list
    
    def print_donors(self):
        "printing list of donors"
        self.print_donors = list(self.donor_list.keys())
        "returns the list of donors"
        return self.print_donors

    def create_report(self):
        "defining how to create a custom report for each donor"
        header = (f'{"Donor Name":25s} | '
              f'{"Total Given":>12s} | '
              f'{"Num Gifts":>12s} | '
              f'{"Average Gift":>12s} |')
        body = []
        for key, value in self.donor_list.items():
            line = (f'{self.donor_list[key].donorname:25s} | '
              f'${self.donor_list[key].donation_total:11.2f} | '
              f'{self.donor_list[key].donation_quantity:12d} | '
              f'${self.donor_list[key].donation_average:11.2f} |')
            body.append(line)
        "creating blank report"
        report = []
        "appending column titles"
        report.append(header)
        report.append('-' * len(header))
        report += body
        "returning final report"
        return report
