### Author - Tommy Aguilu
### Version 1.0
### Class - Python 210A
import sys, random

###opens file from input
import random

def open_source():
    choice = input("please specify the file you would like to read")
    with open(choice, "r") as f:
        opened_file = f.read()
        f.close()
        return opened_file

def output_split(f):
    return f.split()

def build_trigrams(words):
    trigrams = {}
    for i in range(len(words)-2):
        pair = tuple(words[i:i+2])
        follow = words[i+2]

        #scrub output

        clean_pair = ("".join([i for i in pair[0] if i.isalpha()]), "".join([i for i in pair[1] if i.isalpha()]))
        clean_follow = "".join([i for i in follow if i.isalpha()])

        if clean_pair in trigrams:
            trigrams[clean_pair] += [clean_follow]
        else:
            trigrams[clean_pair] = [clean_follow]
    return trigrams

def build_new(text_words):
    output_list = []
    for k in text_words:
        random_key = random.randint(0,1)
        random_value = random.randint(0,1)
        output_list.append(k[random_key])
        output_list.append(k[random_value])

    for i in range(len(output_list)):
        x = (" ".join(output_list))
    return x


if __name__ == "__main__":
    (build_new(build_trigrams((open_source().split()))))