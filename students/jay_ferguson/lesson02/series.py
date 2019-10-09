#!/usr/bin/env python3


def fibonacci(n):
    """Return the nth value of a Fibonacci sequence."""
    fib_list = [0, 1]
    fib_a = 0
    fib_b = 1
    if n == 0 or n == 1:
        return fib_list[n]
    else:
        for i in range(n + 1):
            fib = fib_a + fib_b
            fib_a = fib_b
            fib_b = fib
        return fib

