import random
import sys

def read_in_data(filename):
    with open(filename, 'r') as f:
        read_data = f.read()
        f.close()
    return read_data

#print(read_data.split())
def make_words(in_data):
    return in_data.split()

def build_trigrams(words):
    trigrams = {}
    for i in range(len(words)-2):
        pair = (words[i],words[i+1])
        follower = words[i+2]
        if pair in trigrams:
            trigrams[pair]+= [follower]
        else:
            trigrams[pair] = [follower]
        #print(f"pair: {pair}, follower: {follower}")

    return trigrams

def build_text(trigrams):
    a_list = list()
    for pair in trigrams:
        a_list.append(pair)
    #current_pair = random.choice(a_list)
    current_pair = a_list[0]
    #current_pair = ('I', 'may')
    text = [current_pair[0],current_pair[1]]
    while current_pair:
        if current_pair in trigrams:
            text.append(random.choice(trigrams[current_pair]))
            current_pair = (text[-2],text[-1])
        else:
            break

    #inserting line breaks
    for x in range(int(len(text)/9)):
        text.insert(x*10, '\n')

    return " ".join(text)

if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass a filename")
        sys.exit(1)

    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigrams(words)
    new_text = build_text(word_pairs)

    print(new_text)
