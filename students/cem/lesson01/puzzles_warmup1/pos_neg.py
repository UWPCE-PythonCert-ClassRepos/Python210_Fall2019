"""
Given 2 int values, return True if one is negative and one is positive.
Except if the parameter "negative" is True, then return True only if both are negative.
"""


def pos_neg(a, b, negative):
    if a < 0 or b < 0:
        return True
    else:
        return (False, negative)


one_positive_one_negative_number = pos_neg(-3, 3, negative=False)
positive_number = pos_neg(10, 10, negative=False)
one_positive_one_negative_number_negative = pos_neg(-3, 3, negative=True)

print("1 Number is positive, 1 is negative should equal True ==", one_positive_one_negative_number)
print("Both numbers are positive, return False ==", positive_number)
print("One positive, One negative, Negative, return False ==", one_positive_one_negative_number_negative)