#!/usr/bin/env python3
import random

def read_in_data(file):
    words = []
    for line in open(file):
        words += line.split()
    return words

def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}

    # build up the dict here!
    for index in range(len(words) -2):
        key =(words[index], words[index + 1])
        if key in trigrams:
            trigrams[key].append(words[index +2])
        else:
            trigrams[key] = [words[index +2]]

    return trigrams

def build_text(trigrams, rounds = 10):
    start = random.choice(list(trigrams.keys()))
    loop_text = [start[0],start[1]]
    current_tuple = start
    for i in range(rounds):
        if current_tuple not in trigrams:
            continue
        loop_text.append(random.choice(trigrams[current_tuple]))
        current_tuple = (loop_text[-2],loop_text[-1])
        separator = " "
        text = separator.join(loop_text)
    return text


if __name__ == "__main__":
    filename = 'sherlock_small.txt'
    new_text_depth = 75
    words = read_in_data(filename)
    word_pairs = build_trigrams(words)
    new_text = build_text(word_pairs, new_text_depth)
    print(new_text)