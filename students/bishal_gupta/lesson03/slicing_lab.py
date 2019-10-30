#!/usr/bin/env python3
"""
Created on Tue Oct 29 15:38:52 2019

@author: Bishal.Gupta
"""



def exchange_first_last(seq):
    if type(seq) == tuple:
        new_seq = seq[::-1]
        return new_seq
    elif type(seq) == list:
        new_seq = seq.reverse()
        return new_seq
    else:
        return seq
  
res = exchange_first_last(seq)
print(res)
    
    
        