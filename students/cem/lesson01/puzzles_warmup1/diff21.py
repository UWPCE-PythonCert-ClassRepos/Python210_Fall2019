"""
diff_21 @ https://codingbat.com/prob/p197466
Given an int n, return the absolute difference between n and 21,
except return double the absolute difference if n is over 21.
"""


def diff21(n):
    if n <= 21:
        return 21 - n
    else:
        return (n - 21) * 2


number_is_21 = diff21(21)
number_under_21 = diff21(10)
number_over_21 = diff21(24)

print("n = 21, absolute difference between n and 21 is:", number_is_21)
print("n = under 21, absolute difference between n and 21 is:", number_under_21)
print("n = over 21, double the absolute difference:", number_over_21)


