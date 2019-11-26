# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 19:54:20 2019

@author: joejo

class example of OO Mailroom
"""

class donor:
    
    def __init__(self, name, initial_donations = None):
        self.name = name
        self.donations = initial_donations

    def add_donation(self, donation):
        if type(self.donations) != 'list':
            self.donations = []
        self.donations.append(donation)

    def avg_donation(self):
        return sum(self.donations)/len(self.donations)
    
    def send_thank_you(self):
        print('thanks ' + self.name + '! we really like getting money! you sent ' + self.donations[-1] + '!')


class charity:
    def __init__(self, name):
        self.CharityName = name
        self.Donors = {}
    
    def add_donor(self, donorname, donations):
        self.Donors[donorname] = donor(donorname, donations).donations