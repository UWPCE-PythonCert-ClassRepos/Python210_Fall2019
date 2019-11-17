# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 16:17:40 2019

@author: TimLaptop
"""

def exchange_first_last(seq):
    new_seq = seq[-1] + seq[1:len(seq)-1] + seq[:1]
    return new_seq

def remove_every_other_item(seq):
    new_seq = seq[0::2]
    return new_seq

def remove_firstFour_lastFour_everyOther(seq):
    if(len(seq) > 8):
        splicedSeq = seq[4:-4]
        new_seq = splicedSeq[::2]
        return new_seq
    else:
        print("String is not long enough")

def reverse_order(seq):
    new_seq = seq[len(seq)::-1]
    return new_seq

def lastThird_FirstThird_middleThird(seq):
    first_third = seq[:int(len(seq)/3)]
    last_third = seq[int(-len(seq)/3):]
    middle_third = seq[int(len(seq)/3):int(-len(seq)/3)]
    return last_third + first_third + middle_third

if __name__ == "__main__":    
    a_string = "this is a string"
    a_thirdTest = "FstMidLst"
    a_tuple = (2, 54, 13, 12, 5, 32)
    
    assert exchange_first_last(a_string) == "ghis is a strint"
    assert lastThird_FirstThird_middleThird(a_thirdTest) == "LstFstMid"
    assert remove_every_other_item(a_tuple) == (2,13,5)
    assert reverse_order(a_string) == "gnirts a si siht"
    assert reverse_order(a_tuple) == (32, 5, 12, 13, 54, 2)
    assert remove_firstFour_lastFour_everyOther(a_string) == " sas"
    assert lastThird_FirstThird_middleThird(a_tuple) == (5,32,2,54,13,12)
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)