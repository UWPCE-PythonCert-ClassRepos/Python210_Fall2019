#!/usr/bin/env python3


def first_and_last_item_exchanged(seq):
    if type(seq) == list:
        seq[0],seq[-1] = seq[-1],seq[0]
        return seq
    elif type(seq) == str:
        return seq[-1] + seq[1:-1] + seq[0]
    elif type(seq) == tuple:
        return tuple((seq[-1],)) + tuple(seq[1:-1],) + tuple((seq[0],))


def every_other_item_removed(seq):
    def every_other_item_removed_list(seq_copy):
        seq_copy_copy = []
        for index in range(0, len(seq_copy), 2):
            seq_copy_copy.append(seq_copy[index]) 
        return seq_copy_copy
    if type(seq) == list:
        return every_other_item_removed_list(seq)
    elif type(seq) == str:
        return ''.join(every_other_item_removed_list(list(seq)))
    elif type(seq) == tuple:
        return tuple(every_other_item_removed_list(list(seq)))


def reversed(seq):
    return seq[::-1]
    

def last_third_first_third_middle_third_order(seq):
    def last_third_first_third_middle_third_order_list(seq):
        return seq[0:3] + seq[-3:] + seq[int(len(seq)/2 - 1): int(len(seq)/2)+2 ]
    if len(seq) < 9: 
        return seq
    if type(seq) == list:
        return last_third_first_third_middle_third_order_list(seq)
    elif type(seq) == str:
        return ''.join(last_third_first_third_middle_third_order_list(list(seq)))
    elif type(seq) == tuple:
        return tuple(last_third_first_third_middle_third_order_list(list(seq)))


def first_4_last_4_removed(seq):
    return seq[4:-4]


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
    
    assert last_third_first_third_middle_third_order('appLEJUice') == 'appiceEJU'
    assert last_third_first_third_middle_third_order(['one','two','three','four','five','six','seven', 'eight','nine','ten','eleven']) == ['one', 'two', 'three', 'nine', 'ten', 'eleven', 'five', 'six', 'seven']
    assert last_third_first_third_middle_third_order(('one','two','three','four','five','six','seven', 'eight','nine','ten','eleven')) == ('one', 'two', 'three', 'nine', 'ten', 'eleven', 'five', 'six', 'seven')
  
    assert first_4_last_4_removed('appLEJUice') == 'EJ'
    assert first_4_last_4_removed([1,2,3,4,5,6,7,8,9]) == [5]
    assert first_4_last_4_removed((1,2,3,4,5,6,7,8,9)) == (5,)


    print('Test Succeeded!')

