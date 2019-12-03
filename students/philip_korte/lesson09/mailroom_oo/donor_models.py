#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 18:57:02 2019

@author: philipkorte
"""



class Donor:
    """An object that contains a donor name and their list of donations"""

    def __init__(self, donor_name, donation=None):
        """Initialize donor with name and donation list"""
        self.donor_name = donor_name.title()
        self.donations = []
        if donation is not None:
            for i in donation:
                self.donations.append(i)

    def __repr__(self):
        return f"Donor('{self.donor_name}')"

    def __str__(self):
        return f'Donor("{self.donor_name}") has donated ${self.sum_donations:.2f}'

    def add_new_donation(self, donation):
        if type(donation) == int or type(donation) == float:
            self.donations.append(donation)
        return self.donations

    @property
    def sum_donations(self):
        """Returns the total donations from the list of donations"""
        return sum(self.donations)

    @property
    def count_donations(self):
        """Returns the total donations from the list of donations"""
        return len(self.donations)

    @property
    def avg_donations(self):
        """Returns the average donation from the list of donations"""
        return self.sum_donations / self.count_donations

    def write_thank_you(self):
        """Returns a thank you letter as a string"""

        self.letter = """
        Dear {},

        On behalf of all of us here at Warner Bros. we would like to
        thank you for your generous donation of ${:.2f}. Your
        contribution will ensure that our services here will continue
        to thrive.

        Wishing you the best,
        The Warners""".format(self.donor_name, self.donations[-1])
        return self.letter


class Charity:
    def __init__(self, charity_name):
        self.charity_name = charity_name
        self.donors = {}

    def __repr__(self):
        return f"Charity('{self.charity_name}')"

    def add_donor(self, donor_name, donations):
        new_donor = Donor(donor_name, donations)
        if donor_name.lower() in self.donors.keys():
            [self.donors[donor_name.lower()].add_new_donation(donation) for donation in donations]
        else:
            self.donors.setdefault(donor_name.lower(), new_donor)
        self.sort_donors()
        return self.donors

    def sort_donors(self):
        self.donors = dict(sorted(self.donors.items(), key=lambda e: e[1].sum_donations, reverse=True))
        return self.donors

    def list_donors(self):
        self.donor_list = list(self.donors.keys())
        return self.donor_list

    def create_report(self):
        header = (f'{"Donor Name":25s} | '
              f'{"Total Given":>12s} | '
              f'{"Num Gifts":>12s} | '
              f'{"Average Gift":>12s} |')
        body = []
        for key, value in self.donors.items():
            line = (f'{self.donors[key].donor_name:25s} | '
              f'${self.donors[key].sum_donations:11.2f} | '
              f'{self.donors[key].count_donations:12d} | '
              f'${self.donors[key].avg_donations:11.2f} |')
            body.append(line)

        report = []
        report.append(header)
        report.append('-' * len(header))
        report += body
        return report

if __name__ == "__main__":
    c = Charity('Toys for Tots')
    c.add_donor('philip', [500])
    c.add_donor('jackie', [333, 444])
    c.add_donor('jim', [5000, 4000, 600])
    c.add_donor('vita', [4000, 300])



