# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 13:58:54 2019

@author: bclas
"""
"""
write a function that exchanges the first and last items in a list

write a function that removes every other item in the list

write a function that removes the first 4 and last 4 items 
and then every other item in the sequence

write a function that reverses the items

write a function that chops the sequence into thirds and puts the last
third first, and the first in the middle and the middle at the end. 
"""
listofpets = ["lizard","dog","cat","bird","snake","spider","ferret","monkey","hippo","rock"]
tupleofnum = 31, 4, 5, 19, 29, 12, 54, 17, 83, 56, 92, 154

def exchange_first_last(seq):
    """This function swaps the first and last items in a sequence"""
    copy_list = seq
    copy_list.append(copy_list.pop(0))    
    copy_list.insert(0, copy_list.pop(-2))
    return copy_list

assert exchange_first_last(listofpets) == ["rock","dog","cat","bird","snake","spider","ferret","monkey","hippo","lizard"]


def remove_every_other(seq):
    """This function removes every other item in a sequence"""
    
def remove_first_four_last_four_every_other(seq):
    """This function removes the first four items in a sequence, the
    last four items in a sequence, and than every other item of what remains"""
    
def reverse_order(seq):
    """This function flips the sequence so all items are backwards"""
    
def chop_reorder(seq):
    """This function chops the sequence into thirds and reorders them"""