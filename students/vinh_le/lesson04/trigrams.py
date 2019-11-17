import random
import sys

def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}

    for i in range(len(words) - 2):  # Ends loop 2 indexes prior to the end of the list of words.
        pair = words[i:i + 2]
        follower = words[i + 2]

        # If not in dict, add to dict, and the if follower not in list, append to that key's value list with follower
        if tuple(pair) not in trigrams:
            trigrams[tuple(pair)] = []
        if follower not in trigrams[tuple(pair)]:
            trigrams[tuple(pair)].append(follower)

    return trigrams


def build_text(word_pairs):

    first_pair = random.choice(list(word_pairs.keys()))
    print(f"First Pair: {first_pair}")
    first_follower = word_pairs.get(first_pair)

    # Initial word list to start
    text_list = []
    text_list.append(first_pair[0])  # Tuple item
    text_list.append(first_pair[1])  # Tuple item
    text_list.append(first_follower[0])  # list item

    curr_index = 3  # Third item of list, which is the first follower item

    while curr_index < 1000:
        word_pair_key = tuple(text_list[curr_index - 2: curr_index])

        # Checks if current word pair is in the word pair dictionary, exits system if it does not exists
        # and returns the text string
        if word_pair_key not in word_pairs.keys():
            print(f"Word pair {word_pair_key} does not exist. {curr_index} words were generated.")
            return ' '.join(text_list)
            #sys.exit(1)

        word_pair_value_list = word_pairs.get(word_pair_key)

        value_len = len(word_pair_value_list)

        # Finds a random index of the value_list
        # For selecting a random word from the value list received from a word pair key of the dictionary
        if value_len >= 1:
            value_len -= 1
        random_index_in_list = random.randint(0, value_len)

        text_list.append(word_pair_value_list[random_index_in_list])
        curr_index += 1

    print(f"{curr_index} words were generated.")
    return ' '.join(text_list)


def read_in_data(filename):
    """Reads in file data, filters out ),),,,.,-, characters in each line.
    Then appends words into a list"""

    filtered_word_list = []

    #ASCII values for translation, translate into a space
    translation = {34: 32,  # '"'
                   40: 32,  # '('
                   41: 32,  # ')'
                   44: 32,  # ','
                   45: 32,  # '-'
                   46: 32}  # '.'
                            # 32 = Space

    with open(filename, 'r') as f:
        # Every line is translated(removed of special character)
        # then words are split into a list and then concatenated to a total word list
        for line in f.readlines():
            new_word_list = line.translate(translation).split()
            filtered_word_list = filtered_word_list + new_word_list

        return filtered_word_list


if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    in_data = read_in_data(filename)
    word_pairs = build_trigrams(in_data)
    print(build_text(word_pairs))



