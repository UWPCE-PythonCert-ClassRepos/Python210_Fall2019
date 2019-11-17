#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 15:08:38 2019

@author: matt.denko
"""

"""Write some functions that take a sequence as an argument, and return a copy of that sequence:

with the first and last items exchanged.
with every other item removed.
with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
with the elements reversed (just with slicing).
with the last third, then first third, then the middle third in the new order."""

# with the first and last items exchanged

sequence = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def exchange_first_last(seq):
    f = seq[0]
    l = seq[-1]
    seq[0]= l
    seq[-1] = f
    return print(seq)

exchange_first_last(sequence)

# with every other item removed.

def every_other_removed(seq):
    f = seq[0]
    l = seq[-1]
    seq = []
    seq.append(l)
    seq.append(f)
    return print(seq)

every_other_removed(sequence)

# with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.

sequence = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def keep_the_middle(seq):
    del seq[0:4]
    del seq[-4:]
    return print(seq)

keep_the_middle(sequence)

# with the elements reversed (just with slicing).

sequence = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def elements_reversed(seq):
    seq[::-1]
    return print(sequence)

elements_reversed(sequence)

# with the last third, then first third, then the middle third in the new order

sequence = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def thirds_switched(seq):
    first = seq[-5:]
    second = seq[0:5]
    third = seq[5:10]
    seq = []
    seq = first + second + third
    return print(seq)

thirds_switched(sequence)

