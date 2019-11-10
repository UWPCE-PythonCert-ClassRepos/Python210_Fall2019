"""
Eric Gosnell
Lesson 4 - Trigrams
11.7.2019
"""

from re import sub
from string import punctuation
from random import choice

file_name = "Sherlock1.txt"


def read_file(file):
    with open(file, "r") as f:
        return f.read()


def prep_text(text):
    translation = str.maketrans("\n\t", "  ", punctuation)
    translation[45] = 32
    text = text.translate(translation)
    text = sub(r"\s+", " ", text)
    list_of_words = text.split(" ")
    return list_of_words


def get_trigrams(words):
    trigrams = {}
    for i in range(len(words) - 2):
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        trigrams.setdefault(pair, []).append(follower)
    return trigrams


def build_new(data):
    new_words_list = []
    rand_start_key = choice(list(data.keys()))
    new_words_list.append(rand_start_key[0])
    new_words_list.append(rand_start_key[1])
    new_words_list.append(choice(data[rand_start_key]))  # Random if more than one value
    for i in range(100):
        new_pair = (new_words_list[-2], new_words_list[-1])
        new_follower = choice(data[new_pair])
        new_words_list.append(new_follower)
    return new_words_list


def print_new(seq):
    print("\nNew trigram story...\n")
    line_length = 0
    for word in seq:
        line_length += len(word)
        if line_length < 60:
            print(word + " ", end="")
        else:
            print(word + " ")
            line_length = 0
    print()


if __name__ == "__main__":
    in_text = read_file(file_name)
    word_list = prep_text(in_text)
    tri_data = get_trigrams(word_list)
    out_data = build_new(tri_data)
    print_new(out_data)
