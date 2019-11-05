"""
Given a string, return a new string made of every other char
starting with the first, so "Hello" yields "Hlo".
"""

def string_bits(str):
    new_str = ""
    for n in range(0, len(str), 2):
        new_str = new_str + str[n]

    return new_str
