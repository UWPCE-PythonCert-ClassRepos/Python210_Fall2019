#!/usr/bin/env python3

import os
import json

from datetime import datetime
from cli import CLI

# Set default file path as the current working directory
os.environ['DONOR_DIR'] = os.getcwd() + '/'

# Name of our donors file. Default is 'donors.json'.
DONORS_FILE = 'donors.json'

cli = CLI()

# Pre-check if our file is here


def check_for_donors():
    if not os.path.isfile(os.environ['DONOR_DIR'] + DONORS_FILE):
        print("""donors.json not found in this directory. We'll use sample data, 
or you can choose a different directory.\n""")


class Donor():

    def __init__(self, name, donations=[]):
        """
        Instantiate a new donor.
        :param name: Name of donor, ex. 'Bill Murray'
        :param donations: list of (donation, datetime.datetime) tuples
        """

        donations = list(donations)

        for donation in donations:
            if (type(donation) is not dict
                    or type(donation['amount']) is not float
                    or isinstance(donation['date'], datetime) is False):
                raise TypeError("'donation' parameter must be dict of {'amount': float, 'date': datetime.datetime obj)")

        if type(name) is not str:
            raise TypeError("'name' parameter must be of type str")

        self.name = name.strip().title()
        self.donations = donations

    def add_donation(self, donation):
        """
        Add a new donation.
        :param donation: type float
        :return: None
        """

        if type(donation) is not float:
            raise TypeError("donation value not of type 'float'")

        donation = (donation, datetime.now())

        self.donations.append(donation)

    def average_donation(self):
        """
        Calculate average donation
        :return: Average donation amount - float
        """

        donations = [donation['amount'] for donation in self.donations]
        return sum(donations) / len(donations)


class Donors():

    def __init__(self, donors_file='{}/donors.json'.format(os.getcwd()), donors_dict={}):
        """
        Instantiate a new donors object.
        :param donors_file: Full path of donors file to load and save data
        :param donors_dict: Dictionary of donors to use
        """
        self.donors_file = donors_file

        if donors_dict == {}:
            self.donors = self.read_donors()

        else:
            self.donors = donors_dict

    def read_donors(self):
        """
        Open donors.json to load donors data.
        :return: Dictionary of donors
        """
        with open(self.donors_file, 'r') as f:
            return json.load(f)


class Charity():
    pass


