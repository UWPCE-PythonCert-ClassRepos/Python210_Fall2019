#!/usr/bin/env python3

def fibonacci(n):
    """Return the nth value of a Fibonacci sequence."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1 )

def lucas(n):
    """Return the nth value of a Lucas sequence."""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    return lucas(n - 2) + lucas(n - 1)


def sum_series(n, pos_1=0, pos_2=1):
    """Return the nth value of a Fibonacci sequence if pos_1=0 and pos_2=1.
    Else, return the nth value of a Lucas sequence."""

    if pos_1 == 0 and pos_2 == 1:
        if n == 0:
            return 0
        elif n == 1:
            return 1
    elif pos_1 == 2 and pos_2 == 1:
        if n == 0:
            return 2
        elif n == 1:
            return 1
    return sum_series(n - 2, pos_1, pos_2) + sum_series(n - 1, pos_1, pos_2)


if __name__ == '__main__':
    print(sum_series(3, 2, 1))


