'''
kata_fourteen
Dev: K. Shaffer
Date: 10/31/19
'''
import sys
import random
import string

def build_trigrams(trigrams, words):
    wordrange = len(words)

    for word in range(wordrange-2):
        word1 = word
        word2 = word + 1
        key = (words[word1], words[word2])
        if key in trigrams:
            trigrams[key] = (trigrams[key] + (words[word2+1],))
        else:
            trigrams[key] = (words[word2+1], )
    return trigrams

def build_story(trigrams, first_pair, length):
    story_list = list(first_pair)
    story_list.append(trigrams[first_pair][0])
    while len(story_list) < 50:
        word = (story_list[-2], story_list[-1])
        if word in trigrams:
            i = random.randint(0, len(trigrams[word])-1)
            story_list.append(trigrams[word][i])
        else:
            story_list.append(random.choice(list(trigrams.keys()))[0])

    story = ' '.join(story_list)
    print(story)


if __name__ == "__main__":
    trigrams = {}
    with open(sys.argv[1]) as f:
        for line in f:
            f.readline()
            words = line.split()
            trigrams = build_trigrams(trigrams, words)

    first_pair = random.choice(list(trigrams.keys()))
    build_story(trigrams, first_pair,sys.argv[2])






