# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 08:11:25 2019

@author: joejo

Pytests for Mailroom Part IV
"""


#import pytest
import mailroom4 as m4
import os
import shutil


def test_build_ty():
    ty = m4.build_ty('Bob', [500])
    ty = ty.split('\n')
    assert ty[0] == 'Dear Mr/Mrs Bob,'
    assert ty[2] == 'Thank you so much for your donation of $500.00!'


def test_create_report():
    report = m4.create_report()
    assert report[0] == 'Donor Name          | Total Given | Num Gifts | Average Gift'
    assert report[2] == 'Bill Gates           $   21935.31           3  $     7311.77'
    assert len(report) == 7


def test_add_donor1():
    """Test adding a donation to a donor who is already in the database"""
    name = 'Donald Trump'
    amount = 200
    m4.add_donor(name, amount)
    #assert list(m4.donor_db.keys())[0] == 'Bob'
    assert m4.donor_db['Donald Trump'] == [0.32, 5, 200]


def test_add_donor2():
    """Test addind a new donor and donation to the database"""
    #donor_db = {'Bob': [500]}
    name = 'Sam'
    amount = 200
    m4.add_donor(name, amount)
    assert 'Sam' in list(m4.donor_db.keys())
    assert m4.donor_db['Sam'] == [200]


def test_write_letters():
    m4.write_letters()
    assert os.path.isdir(os.getcwd() + '\\letters')
    assert os.path.isfile(os.getcwd() + '\\letters\\Bill_Gates.txt')
    shutil.rmtree(os.getcwd() + '\\letters')
    