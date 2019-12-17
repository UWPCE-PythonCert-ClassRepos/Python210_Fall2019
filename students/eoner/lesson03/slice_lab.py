# with the first and last items exchanged.
# with every other item removed.
# with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
# with the elements reversed (just with slicing).
# with the last third, then first third, then the middle third in the new order.

# with the first and last items exchanged.
def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[0:1]

# with every other item removed.
def remove_every_other(seq):
    return seq[::2]

# with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
def first_last_four_and_other(seq):
    return seq[4:-4:2] 

# with the elements reversed (just with slicing).
def reverse_elements(seq):
    return seq[::-1] 

# with the last third, then first third, then the middle third in the new order.
def last_first_middle_third(seq):
    #find the third and if not a whole number use int to make it so... 
    x=int(len(seq)/3)
    #you could just find the last 3rd, first and middle is just (all of sequence - last 3rd)
    #commenting below code out but leaving it incase... going to it simple way
    #return seq[-x:]+ seq[:x] + seq[x:-x:]
    return seq[-x:]+ seq[:-x:]

if __name__ == "__main__":
    #each func tests in order:
    #a string
    #a tuple
    #a list

    assert exchange_first_last("string") == "gtrins"
    assert exchange_first_last((2, 54, 13, 12, 5, 32)) == (32, 54, 13, 12, 5, 2)
    assert exchange_first_last([2, 54, 13, 12, 5, 32]) == [32, 54, 13, 12, 5, 2]

    assert remove_every_other("abababab") == "aaaa"
    assert remove_every_other((1, 2, 3, 4, 5, 6, 7, 8, 9)) == (1,3,5,7,9)
    assert remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1,3,5,7,9]

    assert first_last_four_and_other("qwertyuiopasdfghjkl") == "tuoadg"
    assert first_last_four_and_other((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)) == (5, 7, 9, 11)
    assert first_last_four_and_other([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) == [5, 7, 9, 11]

    assert reverse_elements("abcde") == "edcba"
    assert reverse_elements((1,2,3,4,5)) == (5, 4, 3, 2, 1)
    assert reverse_elements([1,2,3,4,5]) == [5, 4, 3, 2, 1]

    assert last_first_middle_third("abcdefghjkl") == "jklabcdefgh"
    assert last_first_middle_third((1,2,3,4,5,6,7,8,9,10)) == (8, 9, 10, 1, 2, 3, 4, 5, 6, 7)
    assert last_first_middle_third([1,2,3,4,5,6,7,8,9,10]) == [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]

    print("Tests Passed!!!")