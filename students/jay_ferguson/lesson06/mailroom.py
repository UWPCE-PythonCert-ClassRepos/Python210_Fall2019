#!/usr/bin/env python3

import os
import json
import re

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

    def datetime_encoder(self, o):
        """
        Encoder function to parse datetime object to json serializable string.
        :return: string in format '2019-11-25 17:39:33.608858'
        """
        if isinstance(o, datetime.datetime):
            return str(o)

        return o

    def datetime_decoder(self, obj):
        """
        Decoder function to convert iso timestamp to datetime object
        :param obj: JSON object
        :return: datetime object
        """
        p = re.compile("\d\d\d\d-[0-1][0-9]-[0-3][0-9] [0-6]\d:[0-5]\d:[0-5]\d\.\d\d\d\d\d\d")

        if 'date' in obj.keys():
            if isinstance(p.match(obj['date']), re.Match):
                obj['date'] = datetime.strptime(obj['date'], "%Y-%m-%d %H:%M:%S.%f")
                return obj
            else:
                return obj
        return obj


    def read_donors(self):
        """
        Open donors.json to load donors data.
        :return: Dictionary of donors
        """
        with open(self.donors_file, 'r') as f:
            return json.load(f, object_hook=self.datetime_decoder)

    def save_donors(self):
        """
        Save donors dict to file
        :return: None
        """
        with open(self.donors_file, 'w+') as f:
            json.dump(f, default=self.datetime_encoder)



    def add_donor(self, donor):
        """
        Add a new donor to the donor dict
        :param donor: Donor object
        :return: None
        """

        self.donors[donor.name] = donor.donations

    def sort_donors(self, ):


