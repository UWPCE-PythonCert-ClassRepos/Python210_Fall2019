"""
-----------------------------------------------------------------------
    Programmer: Eric Gosnell
    Lesson 02: Fibonacci, Lucas, summation series with recursion
    Created program 10.17.2019
-----------------------------------------------------------------------
"""


def fibonacci(n):
    """Compute the nth value of the fibonacci sequence."""
    return sum_series(n)


def lucas(n):
    """Compute the nth value of the Lucas sequence."""
    return sum_series(n, a=2, b=1)


def sum_series(n, a=0, b=1):
    """Compute the nth value of a summation series.
    If seed values are 0 and 1, series if Fibonacci.
    If seed values are 2 and 1, series is Lucas.
    Other values are generic mathematical summation series."""

    if a == 0 and b == 1:  # Fibonacci
        if n == 0:
            return 0
        elif n == 1:
            return 1
    else:
        if n == 0:
            return a
        elif n == 1:
            return b
    return sum_series(n - 2, a, b) + sum_series(n - 1, a, b)


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
