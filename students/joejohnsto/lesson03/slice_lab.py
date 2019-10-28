# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 18:17:53 2019

@author: joejo
"""

def switch_first_last(seq):
    """Return the given sequence with the fist and last items switched"""
    i = seq[:1]
    j = seq[-1:]
    newseq = j + seq[1:-1] + i
    return newseq

def remove_every_other(seq):
    """Return the given sequence with every other item removed"""
    return seq[::2]

def drop_4_everyother(seq):
    """
    Return the given sequence minus the first and last 4 elements, 
    and only return every other remaining element
    """
    return seq[4:-4:2]

def reverse(seq):
    """Return the given sequence in reverse"""
    return seq[::-1]

def thirds(seq):
    """Return the given sequence in the order: last third, first third, middle third"""
    first = seq[:int(len(seq)/3)]
    last = seq[-int(len(seq)/3):]
    mid = seq[int(len(seq)/3):-int(len(seq)/3)]
    return last + first + mid

if __name__ == "__main__":
    # run some tests
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)

    assert switch_first_last(a_string) == "ghis is a strint"
    assert switch_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    
    assert remove_every_other(a_string) == "ti sasrn"
    assert remove_every_other(a_tuple) == (2, 13, 5)
    
    a_long_string = "this is a significantly longer string"
    a_long_tuple = (2, 54, 13, 12, 5, 32, 43, 3, 6, 55, 2, 22, 27, 8)

    assert drop_4_everyother(a_long_string) == " sasgiiatylne t"
    assert drop_4_everyother(a_long_tuple) == (5, 43, 6)

    assert reverse(a_string) == 'gnirts a si siht'
    assert reverse(a_tuple) == (32, 5, 12, 13, 54, 2)

    assert thirds(a_string) == 'tringthis is a s'
    assert thirds(a_tuple) == (5, 32, 2, 54, 13, 12)
    
    print('Tests passed!')