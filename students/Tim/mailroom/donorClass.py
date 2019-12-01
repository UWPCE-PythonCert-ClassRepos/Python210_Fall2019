# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 19:38:59 2019

@author: TimLaptop
"""
class Charity:
    def __init__(self,Name):
        self.CharityName=Name
        self.Donors = {}
    def AddDonor(self,DonorName, ListDonations):
        self.Donors[DonorName]=Donor(DonorName, ListDonations)
    def PrintTotalDonations(self):
        String = ''
        for key,value in self.Donors.items():
            String += key, ': total amount is',self.value.TotalNumberOfDonations(), '\n'
        print(String)
    
class Donor:
    def __init__(self, n, listOfDonations=None):
        self.Name = n
        self.Donations = listOfDonations
    def AddDonation(self,Amount):
        self.Donation.append(Amount)
    def totalNumberOfDonations(self):
        return len(self.Donations)            
    def AverageDonation(self):
        return sum(self.Donations)/len(self.Donations)
    def SendEmailLatest(self):
        print('Dear Donor', self.Name,'the last donation is', self.Donations[-1])
        
