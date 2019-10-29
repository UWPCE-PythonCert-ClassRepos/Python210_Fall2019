#!/usr/bin/env python3
"""
Created on Tue Oct 29 15:38:52 2019

@author: Bishal.Gupta
"""

new_seq = ''
seq = ''

def exchange_first_last(seq):
    if type(seq) == tuple:
        new_seq = seq[::-1]
    elif type(seq) == list:
        seq.reverse()
        print(new_seq)
    else:
        print('nothing')
        
        
exchange_first_last(seq)

if __name__ == "__main__":
    a_tuple = (2, 54, 13, 12, 5, 32)
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    
    
        