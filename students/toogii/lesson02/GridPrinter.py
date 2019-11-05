#!/usr/bin/env python3


def print_grid(n, m):
    for j in range(n):
        print(('+' + '-' * int(m)) * n + '+')
        for i in range(m):
            print(('|' + ' ' * int(m))*n + '|')
    print(('+' + '-' * int(m)) * n + '+')


if __name__ == '__main__':
    print_grid(2,4)
