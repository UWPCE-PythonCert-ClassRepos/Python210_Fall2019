#!/usr/bin/env python3
##this program outputs fibonacci and lucas series

def fibonacci(n):
    return sum_series(n)

def lucas(n):
    return sum_series(n, x=2, y=1)


def sum_series(n, x=0, y=1):
    if x == 0 and y == 1:  # for Fibonacci
        if n == 0:
            return 0
        elif n == 1:
            return 1
    else:
        if x == 2 and y == 1:  # for Lucas
            if n == 0:
                return 2
            elif n == 1:
                return 1
    return sum_series(n-2, x, y) + sum_series(n-1, x, y)

if __name__ == "__main__":
    # run some tests
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    assert lucas(0) == 2
    assert lucas(1) == 1

    assert lucas(4) == 7

    # test that sum_series matches fibonacci
    assert sum_series(5) == fibonacci(5)
    assert sum_series(7, 0, 1) == fibonacci(7)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    # test if sum_series works for arbitrary initial values
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19

    print("tests passed")

