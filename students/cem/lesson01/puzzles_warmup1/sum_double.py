"""
sum_double @ https://codingbat.com/prob/p141905
Given two int values, return their sum. Unless the two values are the same, then return double their sum.
"""


def sum_double(a, b):
    sum = a + b

    if a == b:
        sum = sum * 2
    return sum


different_values = sum_double(5, 10)
same_values = sum_double(10, 10)

print('Summing two values that are the different:', different_values)
print('Summing two values that are the same:', same_values)
