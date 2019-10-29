

def task1(tup):
    """Write a format string that will take the following four element tuple:
        ( 2, 123.4567, 10000, 12345.67)
            and produce:
        'file_002 :   123.46, 1.00e+04, 1.23e+04'"""

    print("=========Task 1=========")
    string_format = "file_{:003d} :{:9.2f}, {:.2e}, {:.2e}"
    print(string_format.format(tup[0], tup[1], tup[2], tup[3]))


def task2(tup):
    """Alternate implementation compared to task one"""

    print("=========Task 2=========")
    print(f"file_{tup[0]:003d} :{tup[1]:9.2f}, {tup[2]:.2e}, {tup[3]:.2e}")


def task3(tup):
    """"Dynamically Building up format strings
        Rewrite: "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)' """

    print("=========Task 3=========")
    #do_something_here_to_make_a_format_string
    #"the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
    tup_length = len(tup)
    string_format = ("the {} numbers are: " + ", ".join(["{}"] * tup_length)).format(tup_length, *tup)
    return string_format.format(tup)


def task4():
    """Given a 5 element tuple:
        ( 4, 30, 2017, 2, 27)
        use string formatting to print:
        '02 27 2017 04 30'"""

    print("=========Task 4=========")
    tup = (4, 30, 2017, 2, 27)
    print(f"{tup[3]:02d} {tup[4]} {tup[2]} {tup[0]:02d} {tup[1]}")

def task5():
    """Given the following four element list:
        ['oranges', 1.3, 'lemons', 1.1]
        Write an f-string that will display:
        The weight of an orange is 1.3 and the weight of a lemon is 1.1
        Now see if you can change the f-string so that it displays the names of the fruit in upper case, and the weight 20%
        higher (that is 1.2 times higher)."""

    print("=========Task 5=========")
    tup = ['oranges', 1.3, 'lemons', 1.1]
    print(f"The weight of an {tup[0][0:-1]} is {tup[1]:.1f} and the weight of {tup[2][0:-1]} is {tup[3]:.1f}")
    print(f"The weight of an {tup[0][0:-1].upper()} is {(tup[1] * 1.2):.1f} and the weight of {tup[2][0:-1].upper()} is {(tup[3] * 1.2):.1f}")


def task6():
    """Write some Python code to print a table of several rows, each with a name, an age and a cost.
     Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers."""
    print("=========Task 6=========")
    person1 = ("Fred", 22, 100)
    person2 = ("Todd", 55, 10000)
    person3 = ("Bob", 45, 100000)
    person4 = ("Sally", 30, 1000000)

    employee_list = [person1, person2, person3, person4]

    table_format = "{0:<10s} {1:3d} {2:>15d}"

    # Print Title and Title Bar
    print("{0:<10s} {1:3s} {2:<15s}".format("Name", "Age", "Cost"))
    print("{0:<10s} {1:3s} {2:>15s}".format(('-'*10), ('-'*3), ('-'*15)))

    # Print rows of each persons information
    for person in employee_list:
        print(table_format.format(person[0], person[1], person[2]))


    #Extra Task given a tuple with 10 consecutive numbers, can you work how to quickly print the tuple in columns that are 5 charaters wide
    print("=========Extra Task=========")
    tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print("".join(["{:5d}"] * (len(tup))).format(*tup))


if __name__ == "__main__":
    test_tuple = (2, 123.4567, 10000, 12345.67)
    task1(test_tuple)
    task2(test_tuple)
    print(task3(test_tuple))
    task4()
    task5()
    task6()