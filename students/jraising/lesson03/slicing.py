# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
def switch_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[0:1]


def every_other_item_removed(seq):
    return seq[::2]


def first_last_4_removed(seq):
    return seq[4:-4:2]


def elements_reversed(seq):
    return seq[::-1]

def last_first_middle_third(seq):
    length = len(seq)
    third_length = math.floor(length/3)
    return seq[third_length * 2:] + seq[:third_length * 2]

print(switch_first_last('123456789'))

print(every_other_item_removed('123456789'))

print(first_last_4_removed('123456789'))

print(elements_reversed('123456789'))

print(last_first_middle_third('123456789'))


if __name__=="__main__":
    assert (switch_first_last('123456789')) == '923456781'
    
    assert (every_other_item_removed('123456789')) == '13579'
    
    assert (first_last_4_removed('123456789')) == '5'
    
    assert (elements_reversed('123456789')) == '987654321'
    
    assert (last_first_middle_third('123456789')) == '789123456'
    
    print("Tests passed")
    