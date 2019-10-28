### Author - Tommy Aguilu
### Version 1.0
### Class - Python 210A

def first_last(flippy):
    first = flippy[0]
    last = flippy[-1]
    middle = flippy[1:(len(flippy)-1)]
    if flippy == str(flippy):
        final_output = last + middle + first
    elif flippy == tuple(flippy):
        final_output = []
        final_output.append(last)
        final_output.append(middle)
        final_output.append(first)
    return final_output

def every_other(other):
    output = other[0:len(other):2]
    return output

def four_by_four(four):
    middle_inputs = four[3:-4:2]
    return middle_inputs

def reverse(reversed):
   output = reversed[len(reversed)::-1]
   return output

def thirds(thirds):
    len_calc = (len(thirds)/3)
    first_third = thirds[:(int(len_calc))]
    middle_third = thirds[(int(len_calc)):(int(len_calc)*-1)]
    last_third = thirds[(int(len_calc)*-1):]

    return last_third, first_third, middle_third


values_string = ("this is a string")
values_tuple = (2, 54, 13, 12, 5, 32, 8, 47, 78, 99, 56)
if __name__ == "__main__":
    assert (first_last(values_string)) == "ghis is a strint"
    assert (first_last(values_tuple)) == [56, (54, 13, 12, 5, 32, 8, 47, 78, 99), 2]
    assert (every_other(values_string)) == "ti sasrn"
    assert (every_other(values_tuple)) == (2, 13, 5, 8, 78, 56)
    assert (four_by_four(values_string)) == "si  t"
    assert (four_by_four(values_tuple)) == (12, 32)
    assert (reverse(values_string)) == "gnirts a si siht"
    assert (reverse(values_tuple)) == (56, 99, 78, 47, 8, 32, 5, 12, 13, 54, 2)
    assert (thirds(values_string)) == ('tring', 'this ', 'is a s')
    assert (thirds(values_tuple)) == ((78, 99, 56), (2, 54, 13), (12, 5, 32, 8, 47))
    print("tests pass")