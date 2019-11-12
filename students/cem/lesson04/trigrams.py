#!/usr/bin/env python3
import random


FILE_LOCATION = "sherlock.txt"
# FILE_LOCATION = "/Users/csalih/Code/python/uw/Python210_Fall2019/students/cem/lesson04/sherlock.txt"  # For PyCharm.


def file_reader():
    with open(FILE_LOCATION, 'r') as story_file:
        stored_data = story_file.read()
        # story_file.close()    # Using Context Manager so do not need to close.
    return stored_data


def split_file(file_read):
    return file_read.split()


def build_trigrams(file_read):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """

    # build up the dict here!
    d = {}
    for i in range(len(file_read) - 2):
        pair = tuple(file_read[i:i + 2])
        # print(f"Pair 1: ", pair[0])
        # print(f"Pair 2: ", pair[1])
        # print(f"Pair: ", pair)
        follower = file_read[i + 2]

        # cleaning str
        cleaned_pair = (
            ''.join([i for i in pair[0] if i.isalpha()]),
            ''.join([i for i in pair[1] if i.isalpha()]),
        )
        cleaned_follower = ''.join([i for i in follower if i.isalpha()])
        if cleaned_pair in d:
            d[cleaned_pair].append(cleaned_follower)
        else:
            d[cleaned_pair] = [cleaned_follower]

    # print(f"Just the dict:  ", d)
    return d


def build_text(word_pairs):
    selected_first_random = random.choice(list(word_pairs.keys()))

    # Start of program
    list_of_words = []
    sentence_length = 100
    for word in selected_first_random:
        list_of_words.append(word)
    list_of_words.append(word_pairs[selected_first_random][0])

    for index in range(sentence_length):
        new_word_pair = (list_of_words[-2], list_of_words[-1])
        next_word = word_pairs[new_word_pair][0]
        list_of_words.append(next_word)
        joined_list = (" ".join(list_of_words))
    return joined_list


if __name__ == "__main__":
    file_read = file_reader()
    split = split_file(file_read)
    word_pairs = build_trigrams(split)
    new_text = build_text(word_pairs)

print(new_text)
