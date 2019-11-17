#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
trigrams.py

created by philip korte
"""
import string
import random


def build_trigrams(words):
    trigrams = {}

    for i in range(len(words) - 2):
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        # if pair does not exist in trigrams dict, then add it
        # append follower to the list value
        trigrams.setdefault(pair, []).append(follower)

    return trigrams


def trigram_proj(trigrams):
    story = list(random.choice(list(trigrams)))
    key = tuple(story[-2:])
    sl = 0

    while sl < 200:
        # if pair is not in trigrams dictionary, remove last word and try again
        while key not in trigrams:
            story.pop()
            key = tuple(story[-2:])

        word_list = trigrams[key]

        # choose from that list at random, a single word
        next_word = random.choice(word_list)

        story.append(next_word)
        # select the last two words in the list as the key for the next letter
        key = tuple(story[-2:])
        sl += 1

    text = " ".join(story)
    print('...' + text + '...')


def get_text(file_name):
    # get the text from the file and convert it to a list of lines
    with open(file_name, 'r') as f:
        my_text = f.read()

    # strip out punctuation
    punctuation = string.punctuation

    for letter in my_text:
        if letter in punctuation:
            my_text = my_text.replace(letter, ' ')

    # split words into a list
    words_list = my_text.split()

    return words_list


if __name__ == "__main__":
    words = get_text('Sherlock1.txt')
    trigrams = build_trigrams(words)
    trigram_proj(trigrams)
