def fibonacci(n):
    """
    The Fibonacci Series is a numeric series starting with the integers 0 and 1.
    The function returns the nth value in the fibonacci series (starting with zero index).
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    """
    The Lucas Series is a numeric series starting with the integers 2 and 1.
    The function returns the nth value in the Lucas series (starting with 2 index).
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)


# """To print sequence"""
# for i in range(10):
#     print(fibonacci(i), ',', end=' ')


def fib(n):
    """
    The Fibonacci Series calling the sum_series function.
    """
    return sum_series(n)


def luca(n):
    """
    The Lucas Series calling the sum_series function.
    """
    return sum_series(n, 2, 1)


def sum_series(n, series_a=0, series_b=1):
    """
    Calling this function with no optional parameters will
    produce numbers from the fibonacci series (because 0 and 1 are the defaults).

    Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers.

    Other values for the optional parameters will produce other series.
    """
    if n == 0:
        return series_a
    elif n == 1:
        return series_b
    else:
        return sum_series(n-1, series_a, series_b) + sum_series(n-2, series_a, series_b)


# # Manual testing
# print(fibonacci(9))
# print(luca(9))
# print(sum_series(12))
# print(f"Printing fibonacci for 9:::", fibonacci(9))
# print(f"Printing Lucas for 9::::", lucas(9))
# print(f"Printing fibonacci in sum:::", sum_series(9))
# print(f"Printing fibonacci in sum:::", sum_series(5, 3, 2))

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


