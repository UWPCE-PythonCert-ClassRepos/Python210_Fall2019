# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 18:01:11 2019

@author: joejo
"""
import random


def build_trigrams(words):
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


def build_text(wordpairs):
    """Build new text output from a dictionary of trigrams"""
    
    wordkey = random.choice(list(wordpairs.keys()))
    wordlist = [wordkey[0].capitalize(), wordkey[1], random.choice(wordpairs[wordkey])]
    for i in range(50):
        try:
            wordkey = tuple(wordlist[-2:])
            wordlist.append(random.choice(wordpairs[wordkey]))
        except KeyError:
            wordkey = random.choice(list(wordpairs.keys()))
            wordlist.append(random.choice(wordpairs[wordkey]))
    eos = 0
    while eos < len(wordlist) - 10:
        eos = eos + random.randint(3,10)
        wordlist[eos] += '.'
        wordlist[eos + 1] = wordlist[eos + 1].capitalize()
    new_text = ' '.join(wordlist) + '.'
    
    return new_text

if __name__ == "__main__":
    words = "I wish I may I wish I might".split()
    wordpairs = build_trigrams(words)
    new_text = build_text(wordpairs)
    print(new_text)
    
#    try:
#        filename = sys.argv[1]
#    except IndexError:
#        print("You must pass in a filename")
#        sys.exit(1)
#
#    in_data = read_in_data(filename)
#    words = make_words(in_data)
#    word_pairs = build_trigram(words)
#    new_text = build_text(word_pairs)

#    print(new_text)