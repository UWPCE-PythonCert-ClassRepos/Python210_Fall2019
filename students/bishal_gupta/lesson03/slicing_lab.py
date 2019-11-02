#!/usr/bin/env python3
"""
Created on Tue Oct 29 15:38:52 2019

@author: Bishal.Gupta
"""


#with the first and last items exchanged.
def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[0:1]

#with every other item removed.
def remove_every_other_word(seq):
    return seq[::2]

#with the first 4 and the last 4 items removed, and then every other item in the remaining sequence
def remove_first4_last4_and_every_other_item(seq):
    return seq[4:-4][::2]

#with the elements reversed (just with slicing).
def reverse_elements(seq):
    return seq[::-1]

#with the last third, then first third, then the middle third in the new order.
def last3_first3_middle3_Neworder(seq):
    return seq[-3:] + seq[:3] + seq[3:-3]

if __name__ ==  "__main__":
    assert exchange_first_last('John Smith') == 'hohn SmitJ'
    assert remove_every_other_word('John Smith') == 'Jh mt'
    assert remove_first4_last4_and_every_other_item('First4Last4') == 'tL'
    assert reverse_elements('John Smith') == 'htimS nhoJ'
    assert last3_first3_middle3_Neworder('Last3First3MiddleOrder') == 'derLast3First3MiddleOr'
    
        