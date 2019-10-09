#!/usr/bin/env python3

def fibonacci(n):
    """Return the nth value of a Fibonacci sequence."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1 )


if __name__ == '__main__':
    n = int(input("n : "))
    print(fibonacci(n))


