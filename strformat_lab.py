"""Write a format string that will take the following four element tuple:
( 2, 123.4567, 10000, 12345.67)
and produce:
'file_002 :   123.46, 1.00e+04, 1.23e+04'
Let’s look at each of the four tuple elements in turn:
The first element is used to generate a filename that can help with file sorting. The idea behind the “file_002” is that if you have a bunch of files that you want to name with numbers that can be sorted, you need to “pad” the numbers with zeros to get the right sort order.
To illustrate this further let’s look at an example: you need to find a string formatting operator that will “pad” the number with zeros for you.
The second element is a floating point number. You should display it with 2 decimal places shown.
The third value is an integer, but could be any number. You should display it in scientific notation, with 2 decimal places shown.
The fourth value is a float with a lot of digits – display it in scientific notation with 3 significant figures."""
#2 ways
print("file_{:0>3d}, {:.2f}, {:.2e}, {:.3e}".format(*(2, 123.4567, 10000, 12345.67)))
afile = (2, 123.4567, 10000, 12345.67)
print(f'file_{afile[0]:0>2d}, {afile[1]:.2f}, {afile[2]:.2e}, {afile[3]:.3e} ')

#wanted to make a variable length so i made it callable with any length tuple and i was lazy so i made the program input my formatting
def formatter(tup):
    a = tup
    b = len(a)
    c = "the " + "{:d}".format(b) + " numbers are: "
    i = 0
    for _ in tup:
        i += 1
        if i < len(tup):
            c += "{:d}, "
        else:
            c += "{:d}"

    return c.format(*a)


print(formatter((2, 3, 5, 7, 9, 23, 6)))
print(formatter((2, 3,)))

#this formats properly for task 3
b = (4, 30, 2017, 2, 27)
print('{3:0>2d}, {4:0>2d}, {2:0>2d}, {0:0>2d}, {1:0>2d},'.format(*b))
# returns lemon weights the a[0][:-1] edits the tuple of a tuple in this case the word oranges and returns orange etc
a = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {a[0][:-1]} is {a[1]} and the weight of a {a[2][:-1]} is {a[3]}")
#and the upper case
u = a[0][:-1]
v = a[2][:-1]
print(f"The weight of an {u.upper()} is {a[1] * 1.2} and the weight of a {v.upper} is {a[3] * 1.2}")

# Write some Python code to print a table of several rows, each with a name, an age and a cost.
name = ('jeri', 'felix', 'dyna', 'edgar', 'bonney', 'trevor', 'victim 679', 'prisoner 689700')
age = (21, 56, 46, 278, 1, 678, 456, 8)
cost = (1234.99, 56.33, 78.92, 1.11, 3.67, 199.95, 567.9, 12389.77)
for _ in range(8):
    print(f"{name[_]: >20}{age[_]: >20}{cost[_]: >20.2f}")

# Task Six
# Often it’s convenient to display data in columns. String formatting helps to make this straightforward.
word = ('Gladys', 21, 123.34)

line_new = '{:>25}  {:>25}  {:>25}'.format(word[0], word[1], word[2])
extra = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# extra task
for _ in range(10): print(f'{extra[_]: >5d}', end='')
