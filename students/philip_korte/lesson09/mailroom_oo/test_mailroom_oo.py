#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 17:24:44 2019

@author: philipkorte
"""

from donor_models import *
import pytest
import datetime


test_name = "Tony Soprano"
test_donations = [500, 600, 800]
test_name2 = "Walter White"
test_donations2 = [333, 444]

def test_new_donor():
    d1 = Donor(test_name, test_donations)
    assert d1.donor_name == "Tony Soprano"
    assert d1.donations == [500, 600, 800]
    d2 = Donor(test_name)
    assert d2.donor_name == "Tony Soprano"
    assert d2.donations == []

def test_add_donation():
    d1 = Donor(test_name, test_donations)
    d1.add_new_donation(333)
    assert d1.donations == [500, 600, 800, 333]
    d1.add_new_donation(555.55)
    assert d1.donations == [500, 600, 800, 333, 555.55]
    d1.add_new_donation("five")
    assert d1.donations == [500, 600, 800, 333, 555.55]

def test_sum_donations():
    d1 = Donor(test_name, test_donations)
    assert d1.sum_donations == 1900

def test_count_donations():
    d1 = Donor(test_name, test_donations)
    assert d1.count_donations == 3
    d1.add_new_donation(333)
    assert d1.count_donations == 4

def test_avg_donations():
    d1 = Donor(test_name, test_donations)
    assert d1.avg_donations == (500 + 600 + 800) / 3

def test_write_letter():
    d1 = Donor(test_name, test_donations)
    letter = d1.write_thank_you()
    assert ('Tony Soprano') in letter
    assert ('$800.00') in letter

def test_new_charity():
    c1 = Charity("Toys for Tots")
    assert c1.charity_name == "Toys for Tots"
    assert c1.donors == {}

def test_add_donor():
    c1 = Charity("Toys for Tots")
    c1.add_donor(test_name, test_donations)
    c1.add_donor(test_name2, test_donations2)
    assert 'tony soprano' in c1.donors
    assert 'walter white' in c1.donors
    c1.add_donor(test_name, test_donations)
    assert c1.donors['tony soprano'].donations == [500, 600, 800, 500, 600, 800]

def test_list_donors():
    c1 = Charity("Toys for Tots")
    c1.add_donor(test_name, test_donations)
    c1.add_donor(test_name2, test_donations2)
    test_list = c1.list_donors()
    assert test_list == ['tony soprano', 'walter white']

def test_create_report():
    c1 = Charity("Toys for Tots")
    c1.add_donor(test_name, test_donations)
    c1.add_donor(test_name2, test_donations2)
    test_report = c1.create_report()
    print(test_report)
    assert 'Walter White' in test_report[3]
    assert '777' in test_report[3]
    assert '1900' in test_report[2]

