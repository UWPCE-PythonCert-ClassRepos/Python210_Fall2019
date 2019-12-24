
from datetime import date, datetime

class donor():
    """Class that contains donor name and donations """
    def __init__(self, name, initial_donations=None):
        """Initialize classs with name and list of dantons"""
        self.name = name
        self.donations = initial_donations

    def add_donation():
        """append to donation list"""
        if type(self.donations) is not list:
            self.donations = []
        self.donations.append(donation)
    
    def average_doantion():
        """calculates average donations"""