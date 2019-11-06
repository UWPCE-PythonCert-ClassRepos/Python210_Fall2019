# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 17:51:52 2019

@author: bclas
"""

preformat = ( 2, 123.4567, 10000, 12345.67)

def format_tuple():
    """This function reformats the items in a provided tuple"""
    first = "file_00{},".format(preformat[0])
    second = "  {r:1.3f}".format(r=preformat[1])
    third = format(preformat[2], '10.2e')
    fourth = format(preformat[3], '10.2e')
    return first+second+third+fourth
