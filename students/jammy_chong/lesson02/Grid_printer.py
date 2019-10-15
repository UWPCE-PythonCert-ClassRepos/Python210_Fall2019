#Part 1
def grid_printer():
    horizontal_line = '+ - - - - + - - - - +'
    vertical_line = '|         |         |'

    print(horizontal_line)
    print(vertical_line)
    print(vertical_line)
    print(vertical_line)
    print(horizontal_line)
    print(vertical_line)
    print(vertical_line)
    print(vertical_line)
    print(horizontal_line)

#Part 2
def print_grid(n):

    #repetition factor considering even integer
    f = int(n/2)

    dash = '- '*f
    empty_str = ' '*f*2

    def horizontal_line():
        for x in range(2):
            print('+ ', end='')
            print(dash, end='')
        print('+')

    def vertical_lines():
        for y in range(f):
            for x in range(2):
                print('| ', end='')
                print(empty_str, end='')
            print('|')

    for z in range(2):
        horizontal_line()
        vertical_lines()

    #last horizontal dash line
    horizontal_line()

#Part 3
def print_grid2(grid,n):

    g = round(grid)
    n = round(n)

    dash = '- '*n
    empty_str = '  '*n

    def horizontal_line():
        for x in range(grid):
            print('+ ', end='')
            print(dash, end='')
        print('+')

    def vertical_lines():
        for y in range(n):
            for x in range(grid):
                print('| ', end='')
                print(empty_str, end='')
            print('|')

    for z in range(grid):
        horizontal_line()
        vertical_lines()

    #last horizontal dash line
    horizontal_line()


grid_printer()
print_grid(3)
print_grid(9)
print_grid(8)
print_grid2(3,4)
print_grid2(5,3)
