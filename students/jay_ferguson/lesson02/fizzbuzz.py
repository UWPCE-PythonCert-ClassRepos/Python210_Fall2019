#!/usr/bin/env python3

def fizz_buzz():
    """Print numbers 1-100, inclusive. Output 'fiZz!' for multiples of 3.
    Output 'BuZz!' for multiples of 5. Output 'fiZzBuZz' for multiples of both."""

    for i in range(1, 101):

        if i % 3 == 0 and i % 5 == 0:
            print('fiZzBuZz!')
        elif i % 3 == 0:
            print("fiZz!")
        elif i % 5 == 0:
            print("BuZz!")
        else:
            print(i)

if __name__ == '__main__':

    fizz_buzz()