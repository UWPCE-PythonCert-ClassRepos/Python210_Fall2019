#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 15:37:54 2019

@author: kenclark
Class: Python 210A
Lesson 6 
Assignement: mailroom04.py
File to test donors mailroom script. 
"""

import mailroom04

import pytest


def test_list_donor():
    """
    Test the first donors name in list"
    """
    result = mailroom04.list_donor().strip()
    assert result.startswith('William')
    assert result.endswith('III')


def test_num_donors():
    """
    Functiont to test number of total donors.
    """
    assert mailroom04.num_donors() == 4


def test_gen_letter():
    """
    Function to test donor letter output.
    """
    result = mailroom04.gen_letter('William Gates', 1000).strip()
    assert result.startswith('Dear')
    assert result.endswith('Youth Council')


if __name__ == '__main__':
    pytest.main()
