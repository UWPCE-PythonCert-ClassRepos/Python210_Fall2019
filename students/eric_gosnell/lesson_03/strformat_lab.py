"""**************************************
# Author: Eric Gosnell
# Lesson: 3
# Assignment: String formatting exercise
**************************************
"""

# Task 1 - "".format() method.

tuple_a = 2, 123.4567, 10000, 12345.67
print("file_{:03d} :{:9.2f}, {:.2e}, {:.2e}".format(*tuple_a))

# Task 2 - f'string instead of format method.

tuple_b = 2, 123.4567, 10000, 12345.67
print(f"file_{tuple_b[0]:03d} :{tuple_b[1]:9.2f}, {tuple_b[2]:.2e}, {tuple_b[3]:.2e}")

# Task 3 - formatting function with variable tuple argument size.


def formatter(t):
    l = len(t)
    return "The {} numbers are: ".format(l) + ",".join(["{}"]*l).format(*t)


tuple_c = 1, 2, 3, 4, 5, 6, 7, 8
print(formatter(tuple_c))

# Task 4 - Print a tuple in different specified order.

tuple_d = 4, 30, 2017, 2, 27
print("{3:02d} {4} {2} {0:02d} {1}".format(*tuple_d))

# Task 5 - Print a formatted list using f string.
# List processing done two different ways.

list_e = ["oranges", 1.3, "lemons", 1.1]
print(f"The weight of an {list_e[0][:-1]} is {list_e[1]}"
      f" and the weight of a {list_e[2][:-1]} is {list_e[3]}")

fruit_a, weight_a, fruit_b, weight_b = list_e
print(f"The weight of an {fruit_a[:-1].upper()} is {weight_a * 1.2}"
      f" and the weight of a {fruit_b[:-1].upper()} is {weight_b * 1.2}")

# Task 6 - Display data in columns.

list_f = [
    ["Volvo", 2, 29000],
    ["Volkswagen", 19, 3200],
    ["Ford", 22, 995]
]

for i in range(len(list_f)):
    print("{:>12}{:>12}{:>12}".format(*list_f[i]))

# Extra Task - Print tuple of 10 numbers in colums 5 characters wide.

tuple_f = range(1, 11)
for i in tuple_f:
    print("{:5}".format(i), end="")
