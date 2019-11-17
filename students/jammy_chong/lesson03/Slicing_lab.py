def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]

def every_other_item(seq):
    return seq[::2]

def remove_first_last_four_every_other(seq):
    return seq[4:-4:2]

def reversed_sequence(seq):
    return seq[::-1]

def thirds_sequence(seq):
    first_third = int(len(seq)/3)
    last_third = int(len(seq)/3*2)
    new_sequence = seq[last_third:] + seq[:first_third] + seq[first_third:last_third]
    return new_sequence

a_string = "this is a string"
a_tuple = (2,54,13,12,5,32)
a_list = [3,6,9,21,43,65,2]

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32,54,13,12,5,2)
assert exchange_first_last(a_list) == [2,6,9,21,43,65,3]

assert every_other_item(a_string) == "ti sasrn"
assert every_other_item(a_tuple) == (2,13,5)
assert every_other_item(a_list) == [3,9,43,2]

another_string = "This is a third"
another_tuple = (2,54,13,12,5,32,35,23,10,27,11,43)
another_list = [3,6,9,21,43,65,2,8,27,48,13,1]

assert remove_first_last_four_every_other(a_string) == " sas"
assert remove_first_last_four_every_other(another_tuple) == (5,35)
assert remove_first_last_four_every_other(another_list) == [43,2]

assert reversed_sequence(a_string) == "gnirts a si siht"
assert reversed_sequence(a_tuple) == (32,5,12,13,54,2)
assert reversed_sequence(a_list) == [2,65,43,21,9,6,3]

assert thirds_sequence(another_string) == "thirdThis is a "
assert thirds_sequence(another_tuple) == (10,27,11,43,2,54,13,12,5,32,35,23)
assert thirds_sequence(another_list) == [27,48,13,1,3,6,9,21,43,65,2,8]
