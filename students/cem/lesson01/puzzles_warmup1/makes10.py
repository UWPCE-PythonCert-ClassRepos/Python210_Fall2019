"""
makes10 @ https://codingbat.com/prob/p124984
Given 2 ints, a and b, return True if one of them is 10 or if their sum is 10.
"""


def makes10(a, b):
    if a == 10 or b == 10 or a+b == 10:
        return True
    else:
        return False


one_number_is_10 = makes10(10, 2)
one_number_is_not_10 = makes10(9, 9)
sum_equals_10 = makes10(5, 5)
sum_equals_more_than_10 = makes10(10, 2)

print("This should be True ==", one_number_is_10)
print("This should be False ==", one_number_is_not_10)
print("This should be True ==", sum_equals_10)
print("This should be True ==", sum_equals_more_than_10)
