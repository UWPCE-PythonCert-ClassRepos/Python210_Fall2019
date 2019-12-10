# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:42:43 2019

@author: bclas
"""

from Mailroom import *
import os.path
from os import path


def test_build_email_output_string():
    assert type(build_email("BEN", 100)) == str
    
def test_build_email_output_contains_name():
    assert "BEN" in (build_email("BEN", 100))  
   
def test_build_email_output_contains_number():
    assert "100" in (build_email("BEN", 100))
    
def test_list_donors_type():
    assert type(list_donors()) == str
    
def test_list_donors_contains_donors():
    for donor in donors:
        assert donor in (list_donors())
        
def test_create_report_output_string():
    assert type(create_report()) == str
    
def test_create_report_output_contains_name():
    for donor in donors:
        assert donor in (create_report())
        
def test_create_report_output_contains_all_donations():
    output = create_report();
    for donation in donors.values():
        assert "".format(sum(donation)) in (output) 

def test_add_donation_to_donor_is_float():
    assert type(add_donation_to_donor("Bob Dylan" , 100)) == float 
    
def test_add_donation_to_donors_new_donor_is_float():
    assert type(add_donation_to_donor("Bob Dylan" , 100)) == float 

def test_add_donation_to_donors_adds_new_donor_to_donors():
    user = "Kat"
    donation = "123"
    assert user not in donors
    add_donation_to_donor(user, donation)
    assert user in donors
    assert float(donation) in donors[user]
 
def test_add_donation_to_donors_adds_donation_to_existing_donor():
    user = "Bob Dylan"
    donation = "1234"
    assert user in donors
    assert float(donation) not in donors[user]
    add_donation_to_donor(user, donation)
    print(float(donation),donors.values)
    assert float(donation) in donors[user]
    

def test_all_donors():
    all_donors()
    for name in donors.keys():
        print(name)
        assert os.path.isfile(name +'.txt')
        assert path.exists(name + '.txt')

def test_create_new_file():
    test = "test"
    text = "This is a test file, created during unit tests of the create_new_file() function in mailroom.py"
    create_new_file(test, text)
    assert path.exists('test.txt')
    
