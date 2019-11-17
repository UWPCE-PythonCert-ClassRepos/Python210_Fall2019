#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 18:03:24 2019

@author: jraising
"""
import random
#import any given file

def import_file(file):
    with open(file, 'r') as f:
        text = f.read()
    return text

    
text_from_file = import_file("./sherlock_small.txt") #pass relative file path to function
text_from_file = (text_from_file.replace("\n", " ")).replace("--", " ") # we need to get rid of '\n'
print (text_from_file)

# check for anything that is not in the whitelist and move them to extras set
extras = {x for x in text_from_file if x not in ' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'}
print (extras)

# using for loop, remove any elements from text file that are also present in extras
for i in text_from_file:
    if i in extras:
        text_from_file = text_from_file.replace(i,"") 
                
words = text_from_file.split(" ")
#print (words)

def build_trigrams(file):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams_dict = {}
    for i in range(len(file)-2):
        if((file[i], file[i+1]) not in trigrams_dict):
            trigrams_dict[file[i],file[i+1]] = [(file[i+2])]
        else:
            trigrams_dict[file[i],file[i+1]].append(file[i+2])
        
    print(trigrams_dict)
    return trigrams_dict
trigram = build_trigrams(words)

keys_list = list(trigram.keys()) #create a key list

#print(keys_list)

shuffle_keys = (random.choices(keys_list, k=len(keys_list))) # randomly pick keys and add them to list shuffle keys

#print(shuffle_keys)

final_list =[] # create empty list
for i in shuffle_keys:
    final_list.append(i[0]) # append the first item of the key
    final_list.append(i[1]) # append the second item of the key
    final_list.append(random.choice(trigram[(i[0],i[1])])) # append the randomly picked item from the value of the key
    
print(final_list)

fake_text = " ".join(final_list)
print(fake_text)