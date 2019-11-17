def print_grid(n):
    h_line = ('+ ' + '- ' * n)
    h_line = (h_line * 2 + '+')
    print(h_line)

    v_line = ('| ' + '  ' * n)
    v_line = (v_line * 2 + '|')
    for i in range(n):
        print(v_line)

    print(h_line)

    for i in range(n):
        print(v_line)

    print(h_line)



def print_grid2(n,size):
    h_line = ('+ ' + '- ' * size)
    h_line = (h_line * n + '+')
    print(h_line)

    v_line = ('| ' + '  ' * size)
    v_line = (v_line * n + '|')

    for j in range(n):
        for i in range(size):
            print(v_line)
        print(h_line)


print_grid(1)

print_grid2(5,2)