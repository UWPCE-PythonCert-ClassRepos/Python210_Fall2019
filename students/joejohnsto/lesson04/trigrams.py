# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 18:01:11 2019

@author: joejo
"""
import random
import string
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def read_data(filename):
    """
    Return a string from a Project Gutenberg book .txt file
    
    Inputs
    filename: expects a .txt file from Project Gutenberg
    Output
    data: a string of the book text, with header and footer removed
    """
    header_string = '*** START OF THIS PROJECT GUTENBERG EBOOK'
    footer_string = '*** END OF THIS PROJECT GUTENBERG EBOOK'
    data = ''
    with open(filename, 'r') as infile:
        line = infile.readline()
        # while loop to get through header
        while header_string not in line:
            line = infile.readline()
        while True:
            line = infile.readline()
            # Stop when footer is reached
            if footer_string in line:
                break
            data += line
    data = data.replace('\n', ' ')
    data = data.rstrip()
    return data


def make_words(data: str):
    """Return a list of words from a given input string"""
#    for _ in string.punctuation:
#        data = data.replace(_, '')
    words = data.split()
    return words


def build_trigrams(words: list):
    """
    Build a dictionary of trigrams from the list of words
    
    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}
    for i in range(len(words)-2):
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        trigrams.setdefault(pair, [])
        trigrams[pair].append(follower)
    
    return trigrams


def build_text(wordpairs: dict):
    """Build new text output from a dictionary of trigrams"""
    
    wordkey = random.choice(list(wordpairs.keys()))
    # Make sure the output starts with a capital letter
    i = 0
    while wordkey[0][i] in string.punctuation:
        i += 1
    firstword = wordkey[0][:i] + wordkey[0][i:].capitalize()
    wordlist = [firstword, wordkey[1], random.choice(wordpairs[wordkey])]
    for i in range(200):
        try:
            wordkey = tuple(wordlist[-2:])
            wordlist.append(random.choice(wordpairs[wordkey]))
        except KeyError:
            wordlist[-1] += '.\n'
            wordkey = random.choice(list(wordpairs.keys()))
            wordlist.append([wordkey[0].capitalize, wordkey[1]])
# These next lines originally added periods at random intervals to give the output some sentence structure
# I have commented this out as I found that with a large enough file leaving the punctuation in allows the
# trigram to include the punctuation and automatically create sentances/quotes/etc
#    eos = 0
#    while eos < len(wordlist) - 10:
#        eos = eos + random.randint(3,10)
#        wordlist[eos] += '.'
#        wordlist[eos + 1] = wordlist[eos + 1].capitalize()
    new_text = ' '.join(wordlist)
    # Make sure the output ends in a period
    for _ in string.punctuation:
        if new_text.endswith(_):
            new_text = new_text[:-1]
    new_text += "."
    
    return new_text


if __name__ == "__main__":
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    data = read_data(filename)
    words = make_words(data)
    wordpairs = build_trigrams(words)
    new_text = build_text(wordpairs)
    print(new_text)
