

"""this function exchanges the first and last object in a series and if a tuple or int list breaks them apart to form
a single tuple instead of tuples in tuples"""
def exchange_first_last(seq):
    x=seq
    a=x[0]
    g=len(x)-1
    c=x[1:g]
    b = x[g]
    if type(seq)==type(()):
        d=(b, *c, a)
        return d
    else:
        return b+c+a

"""this exchanges every other letter """
def exchange_every_other(seq):
    x=seq
    a=x[0]
    g=len(x)-1
    c=x[2:g:2]
    b = x[g]
    if type(seq)==type(()):
        d=(a, *c,)
        return d
    else:
        return a+c

def exchange_four_and_every_other(seq):
    x=seq
    a=x[0:4]
    g=len(x)-8
    h=len(x)-4
    c=x[4:h]
    b = x[h:]
    if type(seq)==type(()):
        d=(*b, *c, *a)
        return d
    else:
        return b+c+a

def reversi(seq):
    a=seq[::-1]
    return a

def thirds(seq):
    a=seq
    length=len(a)
    div= length//3
    first=a[0:div]
    last=a[-div:]
    lengthlast=length-div
    middle=a[div:lengthlast]
    if type(seq) == type(()):
        d = (*middle, *last,*first)
        return d
    else:
        return middle+last+first
# TESTS OUT THE FUNCTIONS FOR THIS LAB
if __name__ == '__main__':
    print(thirds("the beginning of the end"))
    print(thirds((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)))
    print(reversi("the beginning of the end"))
    print(reversi((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)))
    print(exchange_every_other("the beginning of the end"))
    print(exchange_every_other((1, 2, 3, 4, 5, 6, 7, 8)))
    print(exchange_first_last("the beginning of the end"))
    print(exchange_first_last((1, 2, 3, 4, 5, 6, 7, 8)))
    print(exchange_four_and_every_other("the beginning of the end"))
    print(exchange_four_and_every_other((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)))
