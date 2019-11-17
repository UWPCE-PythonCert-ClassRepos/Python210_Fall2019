#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 19:26:44 2019

@author: kenclark
"""

import sys
import random

words = "sip the juice cuz i got enough to go around and the thought takes place uptown I grew up on the sidewalk where i learned street talk and then taught how to hawk new york".split()

"""
def get_book():
    
    print("\nReading the newly created file.")
    infilename = open("rat_in_skull.txt", "r")
    #print(infilename.read())
    #text_file.close()
    
    return infilename
"""

def make_words(text):
    

    replace_punc = [('-', ' '),
                    (',', ''),
                    (',', ''),
                    ('.', ''),
                    (')', ''),
                    ('(', ''),
                    ('"', '')]

    table = {}
    for orig, replace in replace_punc:
        table[ord(orig)] = replace
  
    text = text.translate(table)
    
    # lower-case everthing
    text = text.lower()
    
    # split into words
    words = text.split()
    
    
    # remove the bare single quotes
    # captilize "i"
    
    words2 = []
    for word in words: 
        if word != "'": 
            words2.append("I" if word == 'i' else word)
    #print(words2) # for testing remove       
    return words2
    
# read in words from file



def read_in_data(infilename):
    """
    get txt from file
    """
    
    with open("rat_in_skull.txt", 'r') as infile:
        for i in range(61):
            infile.readline()
            
        full_text = []
        for line in infile:
            if line.startswith("End of the Prohect Gutenberg EBook"):
                break
            full_text.append(line)
            
        return " ".join(full_text)


# build trigrams out of dictionary
def build_trigrams(words2):
    """
    build trigrams dict from the list of words
    returns a dict with:
        keys: word pairs
        values: list of followers
    """
    
    word_pairs = {}
   
    # build up the dict here!
    for i in range(len(words2) - 2):
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
    
        word_pairs.setdefault(pair, []).append(follower)
        #trigrams[pair] = [follower]
   
    #print(trigrams)  #Keep for testing  
    
    return word_pairs



# Build word pairs
def build_text(word_pairs):
    """Build txt from trigrams"""
    
    new_text = []
    for i in range(20):
        sentence = list(random.choice(list(word_pairs.keys())))
        
        for j in range(random.randint(2, 10)):
            pair = tuple(sentence[-2:])
            sentence.append(random.choice(word_pairs[pair]))
            
            
        sentence[0] = sentence[0].capitalize()
        
        sentence[-1] += "."
        new_text.extend(sentence)
        
    new_text = " ".join(new_text)
        
    return new_text




# main function of program
if __name__ == "__main__":
    # get the filename form the command line
    
    #infilename = get_book()
    in_data = read_in_data(infilename)
    words2 = make_words(in_data)
    word_pairs = build_trigrams(words2)
    #new_text = build_text(trigrams)
    
    
    #print(new_text)
    
    
    
    
    