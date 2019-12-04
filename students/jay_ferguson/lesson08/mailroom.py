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

    def thank_donor(self):
        """
        Send a nice thankyou note to a donor.
        :return: Multi-line string
        """

        message = """Dear {},

            Thank you for your generous contribution of ${}!

             Best Regards,

             The UW Python Program"""

        return message.format(self.name, self.most_recent_donation()[0])


    def most_recent_donation(self):
        """
        Sort donations and return the most recent
        :return: tuple - (amount, datetime obj)
        """

        sorted_donations = sorted(self.donations, key=lambda i: i['date'] , reverse=True)
        return sorted_donations[0]['amount'], sorted_donations[0]['date']


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
        Save donors to file
        :return: None
        """

        donors_dict = {}

        for donor in self._donors:
            donors_dict[donor.name] = donor.donations

        with open(self.donors_file, 'w+') as fp:
            json.dump(donors_dict, fp, default=self._datetime_encoder)



    def add_donor(self, donor):
        """
        Add a new donor to the donor collection
        :param donor: Donor object
        :return: None
        """
        self._donors.append(donor)

    def sort(self, **kwargs):

        self._donors.sort(**kwargs)

    def get_donor_by_name(self, name):
        """
        Return Donor whose name property matches input
        :return:
        """

        for donor in self._donors:
            if name in donor.name:
                return donor

        raise ValueError('Name not found in DonorCollection')

    def generate_report(self, reverse=True):
        """
        Generate a report.
        :return: A report - multiline string
        """

        report = ""

        if reverse is False:

            self.sort(reverse=False)

        else:

            header_keys = ['Donor Name', 'Total Given', 'Number Gifts', 'Average Gift']
            header = '\n' + ('|  {:<20}' * len(header_keys))
            formatted_header = header.format(*header_keys)
            row_template = '\n|  {:<20}|  ${:<20}|  {:<20}|   ${:<20}'
            # print(formatted_header)
            report += '\n' + formatted_header
            divider = '-' * len(formatted_header)
            # print(divider)
            report += '\n' + divider

            for donor in self._donors:
                row = []
                row.append(donor.name)
                # Calculate average donation and append it to the sorted_donors dicts
                row.append(donor.total_donation)
                row.append(len(donor.donations))
                row.append(donor.average_donation)
                report += (row_template.format(*row))

            report += '\n'

        return report


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

