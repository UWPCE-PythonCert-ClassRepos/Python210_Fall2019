# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 15:11:41 2019

@author: bclas
"""
"""
This file is the class structure for the mailroom OOP. It contains the
donor class and all functions/methods/properties associated 
with creation of new donors or donations.
"""

class Donor:
    """
    All methods here in are attributes attached to a specific donor.
    i.e. How much money has this specific donor given, or how many donations
    has said donor made. etc.
    
    Any code that only accesses information about a single donor
    should be part of this class.
    """
    def __init__(self, name, donation = None):
        """Initializes a donor with a name and a starting donation value of None"""
        self.name = name
        self.donation = [donation]
        
    def __repr__(self):
        pass
    
    def add_donation_to_donor(self, donation):
        """Appends a new donation to a single donor"""
        self.donation.append(self.donation)
        
    def avg_donation(self):
        """returns a given donors average donation"""
        return sum(self.donation)/len(self.donation)
    
    def total_num_of_donations(self):
        """Grabs the number of values in a given donor dict. returning the total number of donations for a single donor"""
        return len(self.donation)
    
    def donations_total(self):
        return sum(self.donation)
    
    def create_new_file(self):
        """This fucntion creates a new .TXT file with a given donor name"""
        file = open(self.name + ".txt", "w")
        file.write(self.build_email())
        file.close()
    
    def build_email(self):
        """Constructs a thank you letter to a specifc donor."""
        amount = self.donations_total()
        return (
          """  
            {}
           
            Thank you for your wonderful donation of ${:.2f}!
            As you know, dismantaling the structures of global capitalism is
            quite expensive, with your help we are one step closer to our goals!
           
            Many thanks!
           
            Center for the prolonged excistence of literally any life on planet earth.
           
            """.format(self.name, amount))
    
class DonorCollection:
    """
    This class will hold all of the donor objects, as well as methods to
    add a new donor, search for a given donor, etc. If you want a way to
    save and re-load your data, this class would hold that method, too.
    
    """
    def __init__(self):
        """Initialize Donor Collection with donor class object"""
        self.Donors = {}
    
    def add_donor(self, name, donation):
        """Add a new donor to the charity's dictionary of donors"""
        self.Donors[name] = Donor(name, donation)
    
    def list_donors(self):
        """This function prints a list of all current donors"""
        formatted = "List of current donors: \n"
        for Donor in self.Donors.keys():
            formatted += (Donor + ' \n')
        return formatted
        
    def create_report(self):
        """This function generates a formated report of all donors and some
        information regarding their donations"""
        donor_name = "Donor Name"
        total_donation = "Total of donations"
        num_donations = "Number of donations"
        avg_donation = "Average of donations"
        report_header = f"{donor_name:<15}|{total_donation:>15}|{num_donations:>15}|{avg_donation:>15}\n"
        report = report_header
        report += len(report) * "_"
        report += "\n"
        for key, amount in self.Donors.items():
            total_donation = sum(amount)
            num_donations = len(amount)
            avg_donation = total_donation / num_donations
            formated_total_donation = ("{:.2f}".format(total_donation))
            formated_avg_donation = ("{:.2f}".format(avg_donation))
            report += (f"{key:<15} ${formated_total_donation:>17} {num_donations:>19} ${formated_avg_donation:>19}\n")
        return report   
    
    def send_letter_to_all_donors(self):
        """Iterates through the donors dict and calls the build_email() function
        from the Donor class to generate a string Thank you letter to each Donor
        This function also calls the create_new_file() function"""
        for donor in self.Donors.keys():
            donor.create_new_file()
        
        