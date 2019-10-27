#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##############################
# Assignement: PrintedGrid.py
# Dev: Kenneth Clark
# Date: 10-13-19
# Class: Python210A Winter
#############################

def exchange_first_last(seq):
    a_new_sequence = ''
    last_let = seq[-1]
    first_let = seq[0]
    middle = seq[1:-1]
    for i in seq:
        a_new_sequence = last_let + middle + first_let
    
    print(a_new_sequence)


def every_other(seq):
    for i in seq:
        a = (seq[0::2])
    print(a)
        
  
def remove_four(seq):
    print(seq[4:-4:2])
    

def reverse(seq):
    print(seq[::-1])
    
    
def thirds(l):
    n = len(l)//3
    i = n + n
    a = l[:n]
    b = l[n:i]
    c = l[n: + n]
    for i in range(0, len(l), n):
        e = c + b + a
        #print(l[i:i + n])
        #print(a)
        #print(b)
    print(e)
    
      
exchange_first_last("this is a string")

every_other("this is a string")

remove_four("1234576789123456789")

reverse("1234576789123456789")

thirds("123456789123456789")