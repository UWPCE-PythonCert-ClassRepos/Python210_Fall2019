# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:14:00 2019

@author: joejo

Object Oriented Mailroom: tests
"""


import donor_models as dm
import os
import shutil


# Set up a donor and charity to use for testing
bob = dm.donor('Bob', [500])
RLC = dm.charity('RLC')
RLC.add_donor('Bob', bob.donations)


# Tests for donor class
def test_add_donation():
    print(bob.donations)
    bob.add_donation(300)
    assert len(bob.donations) == 2
    assert bob.donations[1] == 300


def test_avg_donation():
    assert bob.avg_donation() == 400


def test_tot_donation():
    assert bob.total_donation() == 800


def test_send_ty():
    ty = bob.send_thank_you().split('\n')
    assert ty[0] == 'Dear Mr/Mrs Bob,'
    assert ty[2] == 'Thank you so much for your donation of $300.00!'


# Tests for Charity class
def test_add_donor():
    """Test adding a new donor and donation to the database"""
    name = 'Sam'
    amount = 200
    RLC.add_donor(name, [amount])
    assert 'Sam' in RLC.list_donors()
    assert RLC.Donors['Sam'].donations == [200]


def test_list_donors():
    assert type(RLC.list_donors()) == str
    assert 'Bob' in RLC.list_donors()


def test_create_report():
    report = RLC.create_report()
    assert report[0] == 'Donor Name          | Total Given | Num Gifts | Average Gift'
    assert report[2] == 'Bob                  $     800.00           2  $      400.00'
    assert len(report) == 4


def test_write_letters():
    RLC.write_letters()
    assert os.path.isdir(os.getcwd() + '\\letters')
    assert os.path.isfile(os.getcwd() + '\\letters\\Bob.txt')
    shutil.rmtree(os.getcwd() + '\\letters')
