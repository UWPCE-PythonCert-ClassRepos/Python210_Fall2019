### Author - Tommy Aguilu
### Version 1.0
### Class - Python 210A
import sys, random

###opens file from input
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
        pair = words[i:i+2]
        pair = tuple(pair)
        follow = words[i+2]
        print(follow)
        if pair in trigrams:
            trigrams[pair] += [follow]
        else:
            trigrams[pair] = [follow]
    return trigrams



if __name__ == "__main__":
    words = (open_source().split())
    print(words)
    print(build_trigrams(words))