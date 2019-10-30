"""
Title: slicing_lab
Date: 10/25/2019
Dev: K.Shaffer

"""


# Swaps first and last entry
def exchange_First_last(sequence):
    first = sequence[0]
    last = sequence[-1]

    if type(sequence) == str:
        sequence = last + sequence[1:-1] + first

    if type(sequence) == tuple:
        sequence = (last,) + sequence[1:-1] + (first,)

    return sequence
# Removes every other entry
def remove_Every_Other(sequence):
    sequence = sequence[1::2]
    return sequence

# Swaps first 4 and last 4 entries
def first_Four_Last_Four(sequence):
    first4 = sequence[0:4]
    last4 = sequence[-4:]
    sequence = last4 + sequence[4:-4] +first4
    return sequence

# Reverses all entries
def reverse(sequence):
    sequence = sequence[::-1]
    return sequence

# Slices sequence in thirds and reorders them
def thirds(sequence):
    length = int(len(sequence) / 3)
    first = sequence[:length]
    second = sequence[length:-length]
    third = sequence[-length:]
    sequence = second + third + first
    return sequence


# Tests

s = "this is a string"
s1 = "ThrTwoOne"
t = (2, 54, 13, 12, 5, 32)
t1 = (1, 2, 3, 4, 5, 6, 7, 8)

assert exchange_First_last(s) == "ghis is a strint"
assert exchange_First_last(t) == (32, 54, 13, 12, 5, 2)
assert remove_Every_Other(s) == "hsi  tig"
assert remove_Every_Other(t) == (54, 12, 32)
assert first_Four_Last_Four(s) == "ring is a stthis"
assert first_Four_Last_Four(t1) == (5, 6, 7, 8, 1, 2, 3, 4)
assert reverse(s) == "gnirts a si siht"
assert reverse(t) == (32, 5, 12, 13, 54, 2)
assert thirds(s1) == "TwoOneThr"
assert thirds(t) == (13, 12, 5, 32, 2, 54)
