### Author - Tommy Aguilu
### Version 1.0
### Class - Python 210A
### String Formatting

#task 1
print("file_00{0} : {1:.2f}, {2:.2E}, {3:.2E} ".format(2, 123.4567, 10000, 12345.67))

#task 2
x = "file_00{0} : {1:.2f}, {2:.2E}, {3:.2E} "
print(x.format(2, 123.4567, 10000, 12345.67))

#task 3
def tuple_string(a, b, c):
    x = ("the 3 numbers are: {0}, {1}, {2}".format(a, b, c))
    return x
print(tuple_string(1,2,3))

#task 4
def formatter(a):
    output = "{0}, {1}, {2}, {3}, {4}".format(*a)
    return output
values = (4, 30, 2017, 2, 27)
print(formatter(values))

#task 5
fruits = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {fruits[0]} is {fruits[1]} and the weight of a {fruits[2]} is {fruits[3]}")

#task6
print('{:20}{:8}\n{:20}{:8}\n{:20}{:8}\n{:20}{:8}'.format('First', '$99.01', 'Second', '$88.09', 'Third', '$99.09', "Fourth", "$47.23"))

