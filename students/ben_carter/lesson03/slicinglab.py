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
tupleofnum = 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20

def exchange_first_last(seq):
    """This function swaps the first and last items in a sequence"""
    copy_list = seq
    copy_list.append(copy_list.pop(0))    
    copy_list.insert(0, copy_list.pop(-2))
    return copy_list

listofpets = ["lizard","dog","cat","bird","snake","spider","ferret","monkey","hippo","rock"]
assert exchange_first_last(listofpets) == ["rock","dog","cat","bird","snake","spider","ferret","monkey","hippo","lizard"]

def remove_every_other(seq):
    """This function removes every other item in a sequence"""
    every_other = seq[0::2]
    return every_other

listofpets = ["lizard","dog","cat","bird","snake","spider","ferret","monkey","hippo","rock"]    
assert remove_every_other(listofpets) == ['lizard', 'cat', 'snake', 'ferret', 'hippo']

def remove_first_four_last_four_every_other(seq):
    """This function removes the first four items in a sequence, the
    last four items in a sequence, and than every other item of what remains"""
    copy_list = seq
    return copy_list[4:-4:2]

listofpets = ["lizard","dog","cat","bird","snake","spider","ferret","monkey","hippo","rock"]    
assert remove_first_four_last_four_every_other(listofpets) == ["snake"]
    
def reverse_order(seq):
    """This function flips the sequence so all items are backwards"""
    copy_list = seq
    return copy_list[::-1]

listofpets = ["lizard","dog","cat","bird","snake","spider","ferret","monkey","hippo","rock"]    
assert reverse_order(listofpets) == ['rock','hippo','monkey','ferret','spider','snake','bird','cat','dog','lizard']    

def chop_reorder(seq):
    """This function chops the sequence into thirds and reorders them"""
    seq_length = len(seq)
    x = int((seq_length) / 3)
    original_first = seq[:x:]
    original_second = seq[x:-x:]
    original_third = seq[-x::]
    return original_third + original_first + original_second
    
assert chop_reorder(tupleofnum) == (15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



