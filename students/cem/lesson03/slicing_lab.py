#!/usr/bin/env python3

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
a_longer_tuple = (44, 66, 98, 22, 7, 9, 2, 'apple', 'pear', 'orange', 'london', 88)


def exchange_first_last(seq):
    first_item = seq[:1]
    last_item = seq[-1:]
    middle_item = seq[1:-1]
    first_item_last_item = last_item + middle_item + first_item
    return first_item_last_item


def remove_every_other_item(seq):
    every_other_item_removed = seq[::2]
    return every_other_item_removed


def exchange_first_4_last_4(seq):
    middle_item = seq[4:-4]
    return middle_item


def elements_reversed(seq):
    reverse_element = seq[::-1]
    return reverse_element


def thirds_new_order(seq):
    first_third = seq[:4]
    middle_third = seq[4:8]
    last_third = seq[-4:]
    new_order = last_third + first_third + middle_third
    return new_order


print(f"Exchange first and last letter: ", exchange_first_last(a_string))
print(f"Exchange first and last index: ", exchange_first_last(a_tuple))

if __name__ == '__main__':
    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert remove_every_other_item(a_string) == "ti sasrn"
    assert remove_every_other_item(a_tuple) == (2, 13, 5)
    assert exchange_first_4_last_4(a_string) == " is a st"
    assert exchange_first_4_last_4(a_longer_tuple) == (7, 9, 2, 'apple')
    assert elements_reversed(a_string) == "gnirts a si siht"
    assert elements_reversed(a_tuple) == (32, 5, 12, 13, 54, 2)
    assert thirds_new_order(a_longer_tuple) == ('pear', 'orange', 'london', 88, 44, 66, 98, 22, 7, 9, 2, 'apple')
    print("Tests Passed")
