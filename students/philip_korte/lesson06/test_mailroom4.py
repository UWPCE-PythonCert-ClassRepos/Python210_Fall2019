#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 15:20:24 2019

@author: philipkorte
"""

from mailroom4 import write_letter, sort_donors

# test Send a thank you (add new donor or updates exisiting donor info)
def test_write_letter():
    assert write_letter('Paul Bunyon', 33) == """
    Dear Paul Bunyon,

    On behalf of all of us here at Warner Bros. we would like to
    thank you for your generous donation of $33.00. Your
    contribution will ensure that our services here will continue
    to thrive.

    Wishing you the best,
    The Warners
    """



# test create report
def test_sort_donors():
    sorted_donors_list = ['marvin the martian', 'bugs bunny', 'elmor fudd',
                     'porky pig', 'sylvester', 'daffy duck', 'yosemite sam',
                     'tweety']
    sorted_donors = sort_donors()
    assert list(sorted_donors.keys()) == sorted_donors_list

# test send letters (created files)



