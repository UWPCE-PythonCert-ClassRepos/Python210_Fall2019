#!/usr/bin/env python3

a_string = (2, 123.4567, 10000, 12345.67)
tup1 = (1,2,3,4,5,6)
tup2 = (1,2,3)
tup3 = (4, 30, 2017, 2, 27)
my_new_tup3_list = []


# Task One
def strip(str):
    first_string = str[0]
    first_string_formatted = "file_00{}".format(first_string)
    return first_string_formatted


def rounding(str):
    float_number = str[1]
    floating_number_rounded = round(float_number, 2)
    return floating_number_rounded


def scientific_notation(str):
    # 1.00e+04
    float_number = str[2]
    floating_number_rounded = f"{float_number: .2e}"
    return floating_number_rounded


def scientific_notation_three(str):
    # 1.23e+04
    float_number = str[3]
    floating_number_rounded = f"{float_number: .2e}"
    return floating_number_rounded


def print_all(str):
    first_num = strip(str)
    second_num = rounding(str)
    third_num = scientific_notation(str)
    fourth_num = scientific_notation_three(str)
    return f"{first_num} : {second_num} {third_num} {fourth_num}"


# Task One - Another Way
print(f"file_00{a_string[0]} : {a_string[1]:.2f} {a_string[2]:.2e} {a_string[3]: .2e}")

# Task Two
f"file_00{0} : {1:.2f} {2:.2e} {3:.3e}"


# Task Three
def formatter(in_tuple):
    length = len(in_tuple)
    print(("There are {} items and they are: " + ", ".join(["{}"] * length)).format(length, *in_tuple))


# Task Four
def modify_tuple(seq):
    """
    Use string formatting,
    Hint: use index numbers to specify positions.
    """

    print(f"{seq[3]:0>2d} {seq[4]:0>2d} {seq[2]:0>2d} {seq[0]:0>2d} {seq[1]:0>2d}")


# Task Five
task_5 = ['orange', 1.3, 'lemon', 1.1]
print(f"The weight of an {task_5[0]} is {task_5[1]} and the weight of a {task_5[2]} is {task_5[3]}")
print(f"The weight of an {task_5[0].upper()} is {task_5[1]} and the weight of a {task_5[2].upper()} is {task_5[3]*1.2}")


print(print_all(a_string))
formatter(tup1)
formatter(tup2)
modify_tuple(tup3)
