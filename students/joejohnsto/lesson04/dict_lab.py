# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 16:49:48 2019

@author: jjohnston
"""


# Dictionaries 1

myDict = {'name' : 'Chris', 'city' : 'Seattle', 'cake' : 'Chocolate'}
print(myDict)

myDict.pop('cake') 
# Alternative to delete:
    #del myDict['cake']

print(myDict)

myDict.update(fruit = 'Mango')
# Alternative to add:
    #myDict.update({'fruit' : 'Mango'})
    #myDict['fruit']['Mango']

print(myDict.keys())
print(myDict.values())

print('cake' in myDict)
# Alternative check if key exists:
    #print(myDict.get('cake', 'False'))
print('Mango' in myDict.values())


# Dictionaries 2

newDict = myDict.copy()
for k,v in myDict.items():
    newDict.update({k : v.lower().count('t')})
   
print(newDict)


# Sets 1

s2 = set(range(0,21,2))
s3 = set(range(0,21,3))
s4 = set(range(0,21,4))

print(s2, '\n', s3, '\n', s4)

print(s3.issubset(s2))
print(s4.issubset(s2))


# Sets 2

p_set = set('Python')
p_set.add('i')

m_set = frozenset('marathon')
print(p_set.union(m_set))
print(p_set.intersection(m_set))

