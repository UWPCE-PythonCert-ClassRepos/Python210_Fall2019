#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 05:47:35 2019

@author: kenclark
Class: Python 210A-Fall
Teacher: David Pokrajac, PhD
Assignment -
"""

"""
Object Oriented Mailroom

It should have a data structure that holds a list of your donors and a history
of the amounts they have donated.
This structure should be populated at first with at least five donors,
with between 1 and 3 donations each.
You can store that data structure in the global namespace.
The script should prompt the user (you) to choose from a menu of
3 actions: “Send a Thank You”, “Create a Report” or “quit”.
"""


class Donor:
    donor_db = []

    def __init__(self, name, donation):
        self.name = name
        self.donation = donation
        self.donor_db += [(self.name, self.donation)]

    def donor_letter(self):
        """generates donor thank you letter"""
        return ('''
                Dear {}

                Thank you for your very kind donation of ${:.2f}.
                It will be put to very good use helping the youth
                of your nation.

                            Sincerely,
                            The Youth Council
                ''').format(self.name, self.donation)

    # def donor_letter_1(donor):
    #     """generates donor thank you letter"""
    #     return ('''
    #             Dear {}

    #             Thank you for your very kind donation of ${:.2f}.
    #             It will be put to very good use helping the youth
    #             of your nation.

    #                         Sincerely,
    #                         The Youth Council
    #             ''').format([donor])


class DonorCollection(Donor):

    def print_donor_report():
        """
        Generates report of donors and donation amounts.
        """
        report_rows = []
        for (name, gifts) in Donor.donor_db:
            total_gifts = sum(gifts)
            num_gifts = len(gifts)
            avg_gift = total_gifts / num_gifts
            report_rows.append((name, total_gifts, num_gifts, avg_gift))

        # sort the report data
        # report_rows.sort(key=sort_key, reverse=True) # TODO Broken
        # print it out with a nice format.
        print("{:25s} | {:11s} | {:9s} |{:12s}".format(
                "Donor Name", "Total Given", "Num Gifts", "avg_gift"))
        print("-" * 66)
        for row in report_rows:
            print("{:25s}  {:11.2f}  {:9d} {:12.2f}".format(*row))


donor_1 = Donor('William Gates III', [10000, 2000])
donor_2 = Donor('Jeff Bezos', [600000])
donor_3 = Donor('Paul Allen', [300000])
