#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 15:10:08 2019
Lesson 06
Assignment: mailroom04 unit testing

@author: kenclark
class: Beginning python 210A

"""


donor_db = {'William Gates III': [653777.32, 12.17],
            'Paul Allen': [633.23, 43.87, 1.32],
            'Jeff': [100.20],
            'Mark Zuckerberg': [1663.23, 4300.87, 10432.0]}


def list_donor():
    """
    Generate donor list.
    """
    for donor in donor_db:
        return donor


def num_donors():
    """
    Generate donor list length
    """
    x = len(donor_db)
    return x


def gen_letter(donor, amount):
    """
    generates donor thank you letter.
    """

    letter = ('''
    Dear {}


    Thank you for your very kind donation of ${:.2f}.
    It will be put to very good use helping the youth
    of your nation.

                Sincerely,
                The Youth Council
    ''').format(donor[:], amount)

    print(letter)  # print letter to screen
    return(letter)

    # Create letter txt file with donor name
    with open(donor + '_donor_letter.txt', 'w+') as f:
        f.write(letter)
    print(letter)


gen_letter('william Gates', 1000)
