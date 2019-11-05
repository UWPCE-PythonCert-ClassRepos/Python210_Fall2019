"""**************************************
# Author: Eric Gosnell
# Lesson: 3
# Assignment: Slicing lab exercise
**************************************
"""

# Declare sequence variables for use in functions.

a_string = "This is a test string"
a_tuple = 2, 54, 13, 12, 5, 32, 75, 93, 100, 2048, 531, 779
a_list = ["item0", 1, "item2", 3, "item4", 5,
          "item6", 7, "item8", 9, "item10", 11]


def exchange_first_last(seq):
    if isinstance(seq, str):    # String specific due to immutability of argument.
        str_first = seq[0]
        str_middle = seq[1:-1]
        str_last = seq[-1]
        return str_last + str_middle + str_first
    elif isinstance(seq, tuple):    # Tuple specific due to immutability of argument.
        tmp_list = list(seq)
        new_list = tmp_list[:]
        new_list[0] = tmp_list[-1]
        new_list[1:-1] = tmp_list[1:-1]
        new_list[-1] = tmp_list[0]
        return tuple(new_list)
    else:   # Lists - mutable.
        new_list = seq[:]
        new_list[0] = seq[-1]
        new_list[1:-1] = seq[1:-1]
        new_list[-1] = seq[0]
        return new_list


def remove_every_other(seq):
    if isinstance(seq, str):
        new_str = seq[::2]
        return new_str
    elif isinstance(seq, tuple):
        new_list = list(seq[::2])
        return tuple(new_list)
    else:
        new_list = list(seq[::2])
        return new_list


def fours_remove_first_last(seq):
    if isinstance(seq, str):
        return seq[4:-4]
    elif isinstance(seq, tuple):
        new_list = list(seq[4:-4])
        return tuple(new_list)
    else:
        return list(seq[4:-4])


def reversed_elements(seq):
    if isinstance(seq, str):
        return seq[::-1]
    elif isinstance(seq, tuple):
        new_list = list(seq[::-1])
        return tuple(new_list)
    else:
        return list(seq[::-1])


def last_third_first(seq):
    if isinstance(seq, str):
        i = (len(seq) // 3)
        str_first = seq[:-i]
        str_last = seq[-i:]
        return str_last + str_first
    elif isinstance(seq, tuple):
        i = (len(seq) // 3)
        list_first = seq[:-i]
        list_last = seq[-i:]
        return tuple(list_last + list_first)
    else:
        i = (len(seq) // 3)
        list_first = seq[:-i]
        list_last = seq[-i:]
        return list_last + list_first


if __name__ == "__main__":
    assert exchange_first_last(a_string) == "ghis is a test strinT"
    assert exchange_first_last(a_tuple) == (779, 54, 13, 12, 5, 32, 75, 93, 100, 2048, 531, 2)
    assert exchange_first_last(a_list) == [11, 1, 'item2', 3, 'item4', 5, 'item6', 7, 'item8', 9, 'item10', 'item0']

    assert remove_every_other(a_string) == "Ti sats tig"
    assert remove_every_other(a_tuple) == (2, 13, 5, 75, 100, 531)
    assert remove_every_other(a_list) == ['item0', 'item2', 'item4', 'item6', 'item8', 'item10']

    assert fours_remove_first_last(a_string) == " is a test st"
    assert fours_remove_first_last(a_tuple) == (5, 32, 75, 93)
    assert fours_remove_first_last(a_list) == ['item4', 5, 'item6', 7]

    assert reversed_elements(a_string) == "gnirts tset a si sihT"
    assert reversed_elements(a_tuple) == (779, 531, 2048, 100, 93, 75, 32, 5, 12, 13, 54, 2)
    assert reversed_elements(a_list) == [11, 'item10', 9, 'item8', 7, 'item6', 5, 'item4', 3, 'item2', 1, 'item0']

    assert last_third_first(a_string) == " stringThis is a test"
    assert last_third_first(a_tuple) == (100, 2048, 531, 779, 2, 54, 13, 12, 5, 32, 75, 93)
    assert last_third_first(a_list) == ['item8', 9, 'item10', 11, 'item0', 1, 'item2', 3, 'item4', 5, 'item6', 7]

print("All tests passed!")
