# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:11:59 2019

@author: joejo

Object Oriented Mailroom: Classes
"""


import os


class donor():
    """An object which contains a donor name and list of donations"""

    def __init__(self, name, initial_donations=None):
        """Initialize donor with name and donation list"""
        self.name = name
        self.donations = initial_donations

    def add_donation(self, donation):
        """Append new donation to donor.donations"""
        if type(self.donations) != list:
            self.donations = []
        self.donations.append(donation)

    def avg_donation(self):
        """Return the average amount donated"""
        return sum(self.donations)/len(self.donations)

    def total_donation(self):
        """Return the total amount donated"""
        return sum(self.donations)

    def thank_you_note(self):
        """Return a string, formatted as a thank you note for the latest donation"""
        ty_info = {'name': self.name, 'last': self.donations[-1],
                   'total': self.total_donation()}
        ty_note = '\n'.join(('Dear Mr/Mrs {name},\n',
                     'Thank you so much for your donation of ${last:.2f}!',
                     'This brings your total lifetime donations to ${total:.2f}!',
                     'We here at RLC (Random Local Charity) really appreciate it!\n',
                     'Sincerely,\n\nBob Saget, CEO of RLC\n'))
        return ty_note.format(**ty_info)


class charity:
    """
    An object which contains a charity name and dictionary of donors.
    Each donor is an oject of class donor
    """

    def __init__(self, name):
        """Initialize charity with name and empty donors dictionary"""
        self.CharityName = name
        self.Donors = {}

    def add_donor(self, donorname, donations):
        """Add a new donor to the charity's dictionary of donors"""
        self.Donors[donorname] = donor(donorname, donations)

    def list_donors(self):
        """Return a string formatted as a list of all donors"""
        donor_list = list(self.Donors.keys())
        return '\n'.join(donor_list)

    def create_report(self):
        """Print donor database, sorted by total donation amount"""
        sorted_db = sorted(self.Donors.items(),
                           key=lambda x: x[1].total_donation(), reverse=True)
        # build header line for report
        header = 'Donor Name          | Total Given | Num Gifts | Average Gift'
        separator = '-'*len(header)
        bodyline = '{:20} ${:11.2f}   {:9d}  ${:12.2f}'
        # build the body of the report; a list of donors and info about their gifts
        body = [bodyline.format(sorted_db[i][0], sorted_db[i][1].total_donation(),
                                len(sorted_db[i][1].donations),
                                sorted_db[i][1].avg_donation())
                for i in range(len(sorted_db))]
        report = (header, separator, *body)
        return report

    def write_letters(self):
        """Write a thank you to each donor and save that note to a txt file"""
        # make directory for letters
        try:
            folder = os.mkdir(os.getcwd() + '\\letters')
        except FileExistsError:
            pass
        folder = os.getcwd() + '\\letters'
        for k, v in self.Donors.items():
            ty_note = v.thank_you_note()
            filename = folder + '\\' + k.replace(' ', '_') + '.txt'
            with open(filename, 'w') as letter:
                letter.write(ty_note)
