
def exchange_first_last(seq):
    new_sequence = (seq[-1:len(seq)] + seq[1:-1] + seq[0:1])
    return new_sequence

def remove_every_other(seq):
    new_sequence = seq[0:-1:2]
    return new_sequence


def remove_first_last_four_and_every_other(seq):
    new_sequence = seq[4:-4:2]
    return new_sequence


def reverse_elements(seq):
    return seq[::-1]


def last_first_middle_third(seq):
    third_count = int(len(seq)/3)

    first = seq[0: third_count]
    middle = seq[third_count: (2 * third_count)]
    last = seq[(2 * third_count): len(seq)]

    new_sequence = (last + first + middle)

    return new_sequence



if __name__ == "__main__":
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    a_long_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

    # FOR EVERY OTHER
    assert remove_every_other(a_string) == "ti sasrn"
    assert remove_every_other(a_tuple) == (2, 13, 5)
    
    # FOR FIRST LAST FOUR and EVERY OTHER
    assert remove_first_last_four_and_every_other(a_string) == " sas"
    assert remove_first_last_four_and_every_other(a_long_tuple) == (5, 7, 9, 11, 13, 15)

    # REVERSE ELEMENTS
    assert(reverse_elements(a_string)) == "gnirts a si siht"
    assert(reverse_elements(a_long_tuple)) == (19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)

    # LAST_FIRST_MIDDLE_THIRDS
    assert(last_first_middle_third(a_string)) == "stringthis is a "
    assert(last_first_middle_third(a_long_tuple)) == (13, 14, 15, 16, 17, 18, 19, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

