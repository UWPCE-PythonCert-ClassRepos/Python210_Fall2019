# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 19:32:34 2019

@author: bclas
"""
#import Mailroom 
""" 
def test_build_email_output_string():
    assert type(build_email("BEN", 100)) == str
    pass
        
def test_build_email_output_contains_name():
    assert "BEN" in (build_email("BEN", 100))  
    pass    

def test_build_email_output_contains_number():
    assert "100" in (build_email("BEN", 100))
    pass
  
def test_list_donors_type():
    assert type(list_donors()) == list
    
def test_list_donors_contains_donors():
    for donor in donors:
        assert donor in (list_donors())
        
def test_send_thank_you():
    
    pass
  
def test_all_donors():
    all_donors()
    for donor in donors:
        file = os.path.basename("\Users\bclas\{donor}.txt")
        assert file


    
def test_create_new_file():
    
    pass   
def test_exit_program():
    pass

    pass
def test_create_report_output_string():
    assert type(create_report()) == str

def test_create_report_output_contains_name():
    for donor in donors:
        assert donor in (create_report())

    pass   
def test_create_report_output_contains_all_donations():
    output = create_report();
    for donation in donors.values():
        #print(sum(donation), output)
        assert sum(donation) in (output) 
"""