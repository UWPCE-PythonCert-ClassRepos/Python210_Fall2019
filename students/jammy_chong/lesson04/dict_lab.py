#Dictionaries 1
dict1 = {'name':"Chris", 'city':"Seattle", 'cake':"Chocolate"}
print(dict1)

dict1.pop('cake')
print(dict1)

dict1['fruit'] = "Mango"
print(dict1.keys())
print(dict1.values())
print('cake' in dict1.keys())
print('Mango' in dict1.values())

#Dictionaries 2
dict1 = {'name':"Chris", 'city':"Seattle", 'cake':"Chocolate"}
for item in dict1:
    dict1[item] = dict1[item].count('t')

#Sets
numbers = list()
for i in range(21):
    numbers.append(i)

s2 = set()
s3 = set()
s4 = set()
s2.update(numbers[::2])
s3.update(numbers[::3])
s4.update(numbers[::4])
print(s2,s3,s4)
print(s3.issubset(s2))
print(s4.issubset(s2))

#Sets 2

python = set("Python")
python.update(["i"])
frozen_set = frozenset("marathon")
print(python.union(frozen_set))
print(python.intersection(frozen_set))
