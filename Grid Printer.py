"""this function will allow you to create an X by X grid of any size Y"""
def print_grid2(x, y):
    n = x
    text = ''
    while n > 0:
        b = y
        topConcat(x, y)
        while b > 0:
            sideWalls(x,y)
            b = b - 1
        n = n - 1
    topConcat(x, y)
    print(text)
    return

"""this function will allow you to create a line running horizontally"""
def topConcat(size, voids):
    b = voids
    n = size
    text = ''
    while n > 0:
        text += "+ " + b * ('- ')
        n = n - 1
    text += '+'
    print(text)
    return

"""this function will allow you to create a line of | walls"""
def sideWalls(size, voids):
    b = voids
    m = voids
    while m > 0:
        n = size
        text = ''
        while n > 0:
            text += "| " + b * ('  ')
            n = n - 1
        text += '|'
        m = m - 1
    print(text)
    return


size = int(input('What x by x dimension would you like your grid to be?: '))
voids = int(input('How Large would you like your squares (whole numbers please)?: '))
print_grid2(size, voids)