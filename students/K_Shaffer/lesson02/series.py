'''
Series
Dev: K. Shaffer
Date: 10/20/18
'''


def fibonacci(n):
    valCounter = 2
    fibNum = 0
    # Returns first two hardcoded sequence values and zeroith term used in reccursion
    if n == 1 or n == 0:
        fibNum = 0
    if n == 2 or n == 3:
        fibNum = 1

    # Reccursive call to step through the series until requested value is reached
    else:
        while valCounter < n:
            valCounter += 1
            currentVal = fibonacci(n-2) + fibonacci(n-1)
            fibNum = currentVal

    # Returns requested series number both internal to recurrsion and function call result
    return fibNum


def lucas(n):
    valCounter = 2
    lucNum = 0
    # Returns first two hardcoded sequence values and zeroith term used in reccursion
    if n == 1:
        lucNum = 2
    if n == 2:
        lucNum = 1

    # Reccursive call to step through the series until requested value is reached
    else:
        while valCounter < n:
            valCounter += 1
            currentVal = lucas(n-2) + lucas(n-1)
            lucNum = currentVal

    # Returns requested series number both internal to recurrsion and function call result
    return lucNum


def sum_series(n, a = 0, b= 1):
    valCounter = 2
    seriesNum = 0

    # Returns first two hardcoded sequence values and zeroith term used in reccursion for both series types
    if n == 1 and a == 0:
        seriesNum = 0
    if n == 2 and b == 1:
        seriesNum = 1
    if n == 1 and a == 2:
        seriesNum = 2
    if n == 2 and b == 1:
        seriesNum = 1

    # Reccursive call to step through the series until requested value is reached
    else:
        while valCounter < n:
            valCounter += 1
            currentVal = sum_series(n-2, a, b) + sum_series(n-1, a, b)
            seriesNum = currentVal

    # Returns requested series number both internal to recurrsion and function call result
    return seriesNum


# ---Test Block---
# Assert hard coded and recursion values return expected values and then test print of the first 8 values in sequence
print("Test prnt fibonacci:")
assert fibonacci(1) == 0
assert fibonacci(2) == 1
assert fibonacci(3) == 1
assert fibonacci(4) == 2
assert fibonacci(5) == 3

for i in range(1, 9):
    fib = fibonacci(i)
    print(fib)

# Assert hard coded and recursion values return expected values and then test print of the first 8 values in sequence
print("Testing print lucas:")
assert lucas(1) == 2
assert lucas(2) == 1
assert lucas(3) == 3
assert lucas(4) == 4
assert lucas(5) == 7

for i in range(1, 9):
    luc = lucas(i)
    print(luc)

# Test explicit parameter inputs as well as default assert values returned are expected
print("Testing sum_series:")
x = sum_series(3)
assert x == 1
print(x)

y = sum_series(3, 0, 1)
assert y == 1
print(y)

z = sum_series(3, 2, 1)
assert z == 3
print(z)