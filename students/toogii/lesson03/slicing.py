#!/usr/bin/env python3


def first_and_last_item_exchanged(seq):
    return seq[-1:] + seq[1:-1] + seq[0:1]


def every_other_item_removed(seq):
    return seq[::2]


def reversed(seq):
    return seq[::-1]


def last_third_first_third_middle_third_order(seq):
    return seq[int(len(seq)*2/3+1):] + seq[:int(len(seq)/3+1)] + seq[int(len(seq)/3+1): int(len(seq)*2/3)+1 ]


def first_4_last_4_removed(seq):
    return seq[4:-4][::2]


if __name__ == '__main__':
    assert first_and_last_item_exchanged('testing') == 'gestint'
    assert first_and_last_item_exchanged(['apple', 'orange', 'banana']) == ['banana', 'orange', 'apple']
    assert first_and_last_item_exchanged(('apple', 'orange', 'banana')) == ('banana', 'orange', 'apple')

    assert every_other_item_removed('testing') == 'tsig'
    assert every_other_item_removed(['apple', 'orange', 'banana']) == ['apple', 'banana']
    assert every_other_item_removed(('apple', 'orange', 'banana')) == ('apple', 'banana')

    assert reversed('testing') == 'gnitset'
    assert reversed(['apple', 'orange', 'banana']) == ['banana', 'orange', 'apple']
    assert reversed(('apple', 'orange', 'banana')) == ('banana', 'orange', 'apple')

    assert last_third_first_third_middle_third_order('abcdefghjklmno') == 'lmnoabcdefghjk'
    assert last_third_first_third_middle_third_order(['one','two','three','four','five','six','seven', 'eight','nine','ten','eleven']) == ['nine', 'ten', 'eleven', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']
    assert last_third_first_third_middle_third_order(('one','two','three','four','five','six','seven', 'eight','nine','ten','eleven')) == ('nine', 'ten', 'eleven', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight')

    assert first_4_last_4_removed('appL012345678Uice') == '02468'
    assert first_4_last_4_removed([1,2,3,4,5,1,5,1,5,1,6,7,8,9]) == [5,5,5]
    assert first_4_last_4_removed((1,2,3,4,5,1,5,1,5,1,6,7,8,9)) == (5,5,5)


    print('Test Succeeded!')
