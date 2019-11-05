#!/usr/bin/env python3


def fibonacci(n: int) -> int:
    """Returns nth value from the fibonacci series"""
    if n <= 1:
        return n
    return (fibonacci(n-1) + fibonacci(n-2))


def lucas(n):
    """Returns nth value from lucas numbers"""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    return (lucas(n-1) + lucas(n-2))


def sum_series(n, n1=0, n2=1):
    """
    This function generates fibonacci series and lucas numbers
    Without positional arguments, function will work as Fibonacci function
    With n1=2 and n2=1, function will work as lucas function.
    sum_series(n, 0, 1) = fibonacci(n)
    sum_series(n, 2, 1) = lucas(n)
    sum_series(n, n1, n2) = sum_series(n, n1, n2)
    """
    if n1 == 0 and n2 == 1:
        return fibonacci(n)
    elif n1 == 2 and n2 == 1:
        return lucas(n)
    else:
        if n == 0:
            return n1
        elif n == 1:
            return n2
        return (sum_series((n-1), n1, n2) + sum_series((n-2), n1, n2))

if __name__ == '__main__':
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5

    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7
    assert lucas(5) == 11

    assert sum_series(5) == 5
    assert sum_series(5,2,1) == 11
    assert sum_series(5,3,4) == 29
    print("test passed")
