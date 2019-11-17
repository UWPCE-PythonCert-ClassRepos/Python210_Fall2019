#/usr/bin/env python3
"""
dict_lab.py

created by: Philip Korte
"""

# dictionaries 1 -------------------------------------------------------------

my_dict = {'name':'Chris',
           'city':'Seattle',
           'cake':'chocolate'}

# display the dictionary
print(my_dict)

# delete the entry for cake
del my_dict['cake']

# display the dictionary
print(my_dict)

# add {'fruit':'mango'}
my_dict['fruit'] = 'mango'
print(my_dict)

# display the dictionary keys
# one way to do it
for k in my_dict.keys():
    print(k)
 # another way to do it
print(my_dict.keys())

# display the dictionary values
# one way to do it
for v in my_dict.values():
    print(v)
# another way to do it
print(my_dict.values())

# display whether or not 'cake' is a key in the dictionary
print('cake' in my_dict)

# display whether or not 'mango' is a value in the dictionary
print('mango' in my_dict.values())


# dictionaries 2 -------------------------------------------------------------

my_dict = {'name':'Chris',
           'city':'Seattle',
           'cake':'chocolate'}

# make the dictionary with same keys but the number of 't's of in each value as value
my_dict_num = {}
for k, v in my_dict.items():
    v = v.lower()
    my_dict_num[k] = v.count('t')
print(my_dict_num)

# sets -----------------------------------------------------------------------

# create set, 0 - 20, divisible by 2
s2 = set(range(0, 21, 2))
print(s2)

# create set, 0 - 20, divisible by 3
s3 = set(range(0, 21, 3))
print(s3)

# create set, 0 - 20, divisible by 4
s4 = set(range(0, 21, 4))
print(s4)

# is s3 a subset of s2?
print(s3.issubset(s2))

# is s4 a subset of s2?
print(s4.issubset(s2))

# sets 2 ---------------------------------------------------------------------

# create a set with the letters in 'python'
py_set = set('python')
print(py_set)

# add 'i' to the set
py_set.add('i')
print(py_set)

# create a frozenset with the letters in 'marathon'
frozen = frozenset('marathon') 
print(frozen)

# display the union of the two set (done two ways)
print(py_set.union(frozen))
print(frozen.union(py_set))

# display the intersection of the two sets (done two ways)
print(py_set.intersection(frozen))
print(frozen.intersection(py_set))
