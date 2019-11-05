a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
nstring = "1234"


def main():
    print("python main function")

'''with the first and last items exchanged.
with every other item removed.
with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
with the elements reversed (just with slicing).
with the last third, then first third, then the middle third in the new order.
'''

def exchange_first_last(seq):
    """
    with the first and last items exchanged.
    :param seq:
    :return:
    """
    first = seq[:1]
    middle = seq[1:-1]
    last = seq[-1:]
    return last + middle + first

def ever_other(seq):
    return seq[::2]

def ever_other_middle(seq):
    middle = seq[5:-4]
    return ever_other(middle)

def reverse_order(seq):
    return seq[::-1]

def third(seq):
    thr = len(seq)/3
    thr = int(round(thr))
    first = seq[:thr]
    middle = seq[thr:thr*2]
    last = seq[thr*2:]
    return last + first + middle



if __name__ == '__main__':
    main()
    assert exchange_first_last(a_string) == "ghis is a strint"

    assert ever_other(a_string) == "ti sasrn"

    assert ever_other_middle(a_string) == "i  t"

    assert reverse_order(a_string) == "gnirts a si siht"

    assert third(a_string) == "stringthis is a "
