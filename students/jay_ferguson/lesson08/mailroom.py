#!/usr/bin/env python3

import os
import json
import re
from datetime import datetime
from functools import total_ordering

from cli import CLI

# Name of our donors file. Default is 'donors.json'.

DONORS_FILE = 'donors.json'

@total_ordering
class Donor():
    """
    A donor object. Contains donor name and donation history as a list.
    """

    def __init__(self, name, donations=[]):
        """
        Instantiate a new donor.
        :param name: Name of donor, ex. 'Bill Murray'
        :param donations: list of {'amount':float, 'date': datetime.datetime} dicts
        """

        donations = list(donations)

        for donation in donations:
            if type(donation) is not dict:
                raise TypeError("'donation' must be a list.")

            if type(donation['amount']) is not float:
                raise TypeError("'donation' parameter must be dict of {'amount': float, 'date': datetime.datetime obj)")

            if isinstance(donation['date'], datetime) is False:
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

        donation = {'amount': donation, 'date': datetime.now()}

        self.donations.append(donation)


    def __str__(self):

        return f'Donor({self.name}, {round(self.total_donation, ndigits=2)})'


    def __repr__(self):

        return self.__str__()


    def __eq__(self, other):

        return self.total_donation == other.total_donation


    def __lt__(self, other):

        return self.total_donation < other.total_donation


    @property
    def average_donation(self):
        """
        Calculate average donation
        :return: Average donation amount - float
        """

        return self.total_donation / len(self.donations)


    @property
    def total_donation(self):
        """Calculate total donation from donor"""

        donations = [donation['amount'] for donation in self.donations]
        return sum(donations)


class DonorCollection():

    def __init__(self, donors_file=DONORS_FILE, donors=[]):
        """
        Instantiate a new donors object.
        :param donors_file: Full path of donors file to load and save data
        :param donors: list of donors objects to use
        """
        self.donors_file = donors_file

        if donors == []:
            donors = self.read_donors()

            donor_collection = []

            for key in donors.keys():
                donor = Donor(key, donors[key])
                donor_collection.append(donor)

        else:
            donor_collection = donors

        self._donors = donor_collection

        self._index = 0

    @classmethod
    def from_dict(cls, donors_dict):
        """
        Instantiate class using dictionary parameter. Same input as Donor.
        :param donors_dict
        """

        donor_collection = []

        for key in donors_dict.keys():
            donor = Donor(key, donors_dict[key])
            donor_collection.append(donor)

        return cls(donors=donor_collection)


    @staticmethod
    def _datetime_encoder(o):
        """
        Encoder function to parse datetime object to json serializable string.
        :return: string in format '2019-11-25 17:39:33.608858'
        """
        if isinstance(o, datetime):
            return str(o)

        return o

    @staticmethod
    def _datetime_decoder(obj):
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
            return json.load(f, object_hook=self._datetime_decoder)

    def save_donors(self):
        """
        Save donors dict to file
        :return: None
        """
        with open(self.donors_file, 'w+') as f:
            json.dump(f, default=self._datetime_encoder)



    def add_donor(self, donor):
        """
        Add a new donor to the donor collection
        :param donor: Donor object
        :return: None
        """
        self._donors.append(donor)

    def sort(self, **kwargs):

        self._donors.sort(**kwargs)


    def __str__(self):

        return str(self._donors)


    def __repr__(self):

        return self.__str__()


    def __iter__(self):

        self._index = 0
        return self


    def __next__(self):

        if self._index >= len(self._donors):
            self._index = 0
            raise StopIteration

        else:
            self._index += 1
            return self._donors[self._index - 1]

