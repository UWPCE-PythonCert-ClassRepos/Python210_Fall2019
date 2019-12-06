#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 18:23:05 2019

@author: matthewdenko
"""
# mailroom OOO description ----------------------------------------------------

"""Goal: Refactor the mailroom program using classes to help organize the code.

The functionality is the same as the earlier mailroom:

Mailroom Part 1

But this time, we want to use an OO approach to better structure the code to 
make it more extensible.

It was quite reasonable to build the simple mailroom program using a single 
module, a simple data structure, and functions that manipulate that data 
structure. In fact, you’ve already done that :-)

But if one were to expand the program with additional functionality, it 
would start to get a bit unwieldy and hard to maintain. So it’s a pretty good 
candidate for an object-oriented approach."""

# importing packages-----------------------------------------------------------

from donor_models import *

# mock data for testing -------------------------------------------------------

test_name = "Matthew Denko"
test_donations = [1]
test_list = Main_Donor_Class(test_name, test_donations)

# creating tests for each function --------------------------------------------

def assert_new_donor():
    "function to test new donor function"
    assert test_list.donor_name == "Matthew Denko"
    assert test_list.donations == [1]

def assert_add_donation():
    "function to test adding new donation"
    test_list.add_new_donation(2)
    assert test_list.donation_list == [1, 2]

def assert_sum_donations():
    "function to test sum donation function"
    assert test_list.donation_total == 3

def assert_count_donations():
    "function to test count donation function"
    assert test_list.donation_quantity == 2

def assert_avg_donations():
    "function to test average donation function"
    assert test_list.donation_average == 1.5

def test_list_donors():
    "function to test list function"
    test_list = test_list.print_donors()
    assert test_list == ['Matthew Denko']
