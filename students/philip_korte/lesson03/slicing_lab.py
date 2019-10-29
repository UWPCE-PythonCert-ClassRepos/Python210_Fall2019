#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
slicing_lab.py

@author: philipkorte
"""

# Create a copy
def copy_seq(seq):
    return seq[:]

# Swap the first and last items
def swap_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]

# Remove every other item
def remove_every_other(seq):
    return seq[::2]

# Remove first and last four items and then every other item
def four_by_four(seq):
    return seq[4:-4:2]
    
# Reverse each element
def reverse_seq(seq):
    return seq[::-1]

# Change the order to last third, first third, middle third
def triple_shuffle(seq):
    length = round(len(seq) / 3)
    return seq[-length:] + seq[:-length]


my_seq = list(range(20))
my_string = 'This is a string'
 
# check if copy works
assert copy_seq(my_seq) == my_seq

# check if swap works
assert swap_first_last(my_seq) == [19, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                                   11, 12, 13, 14, 15, 16, 17, 18, 0]
assert swap_first_last(my_string) == 'ghis is a strinT'

# check if remove every other item works
assert remove_every_other(my_seq) == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
assert remove_every_other(my_string) == 'Ti sasrn'

# check if four by four works
assert four_by_four(my_seq) == [4, 6, 8, 10, 12, 14]
assert four_by_four(my_string) == ' sas'

# check if reversing works
assert reverse_seq(my_seq) == [19, 18, 17, 16, 15, 14, 13, 12, 11,
                               10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
assert reverse_seq(my_string) == 'gnirts a si sihT'

# check that shuffling works
assert triple_shuffle(my_seq) == [13, 14, 15, 16, 17, 18, 19, 
                                   0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
assert triple_shuffle(my_string) == 'tring' 'This is a s'
