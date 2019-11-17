# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 19:30:50 2019

@author: joejo
"""


# List Comprehension
feast = ['lambs', 'sloths', 'orangutans',
             'breakfast cereals', 'fruit bats']

comprehension = [delicacy.capitalize() for delicacy in feast]

assert comprehension[0] == 'Lambs'
assert comprehension[2] == 'Orangutans'


# Filtering lists
feast = ['spam', 'sloths', 'orangutans', 'breakfast cereals',
            'fruit bats']

comp = [delicacy for delicacy in feast if len(delicacy) > 6]

assert len(feast) == 5
assert len(comp) == 3


# Unpacking tuples
list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]

comprehension = [ skit * number for number, skit in list_of_tuples ]

assert comprehension[0] == 'lumberjack'
assert len(comprehension[2]) == 16


# Double list comprehension
eggs = ['poached egg', 'fried egg']

meats = ['lite spam', 'ham spam', 'fried spam']

comprehension = \
    [ '{0} and {1}'.format(egg, meat) for egg in eggs for meat in meats]

assert len(comprehension) == 6
assert comprehension[0] == 'poached egg and lite spam'


# Set comprehension
comprehension = { c for c in 'aabbbcccc'}

assert comprehension == {'a', 'b', 'c'}


# Dictionary comprehensions
dict_of_weapons = {'first': 'fear',
                       'second': 'surprise',
                       'third':'ruthless efficiency',
                       'forth':'fanatical devotion',
                       'fifth': None}
dict_comprehension = \
    { k.upper(): weapon for k, weapon in dict_of_weapons.items() if weapon}

assert ('first' in dict_comprehension) is False
assert ('FIRST' in dict_comprehension) is True
assert len(dict_of_weapons) == 5
assert len(dict_comprehension) == 4


# Count even numbers
def count_evens(nums):
    return len([1 for num in nums if not num%2])

assert count_evens([2, 1, 2, 3, 4]) == 3

assert count_evens([2, 2, 0]) == 3

assert count_evens([1, 3, 5]) == 0


# Revisit dict/set lab
# 1
food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}

s_out = ('{name} is from {city}, he likes {cake} cake, {fruit} fruit, '
         + '{salad} salad, and {pasta} pasta.').format(**food_prefs)

# 2
nums = [i for i in range(16)]
hexes = [hex(i) for i in range (16)]
hex_dict = dict(zip(nums, hexes))

# 3
hex_dict = {i: hex(i) for i in range(16)}

# 4
a_count = {k: food_prefs[k].count('a') for k in food_prefs.keys()}

# 5.a
s2 = {s for s in range(21) if not s%2}
s3 = {s for s in range(21) if not s%3}
s4 = {s for s in range(21) if not s%4}

# 5.b
divs = [2,3,4]
s = []
for div in divs:
    s.append({n for n in range(21) if not n%div})

# 5.c
s = [{n for n in range(21) if not n%div} for div in divs]
