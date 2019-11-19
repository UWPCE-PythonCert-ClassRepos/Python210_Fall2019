#!/usr/bin/env python
seq = ( 2, 123.4567, 10000, 12345.67)
tuple = (1,2,3)

def task1(seq):
    my_tuple = seq[:]
    return 'file_{my_tuple[0]:03d} : {my_tuple[1]: 8.2f}, {my_tuple[2]:.2e}, {my_tuple[3]:.3e}'

def task2(seq):
    my_tuple = seq[:]
    return 'file_{:03d} : {: 8.2f}, {:.2e}, {:.3e}'.format(my_tuple[0], my_tuple[1], my_tuple[2], my_tuple[3])

def formatter(nums):
    """
    Task 3
    """
    formatted = "the " + str(len(nums)) + " numbers are: " + str(len(nums)*"{:d} ").format(*nums)
    return formatted

def task4(seq):
    t = ( 4, 30, 2017, 2, 27)
    s = f"'0{t[3]} {t[4]} {t[2]} 0{t[0]} {t[1]}'"
    print(s)

def task5():
    fruit = ['oranges', 1.3, 'lemons', 1.1]
    s = f"The weight of an {fruit[0]} is {fruit[1]} and the weight of a {fruit[2]} is {fruit[3]}"
    s2 = f"The weight of an {fruit[0].upper()} is {fruit[1]* 1.2} and the weight of a {fruit[2].upper()} is {fruit[3] * 1.2}"
    print(s)
    print(s2)

def task6():
    pass



def main():
    task1(seq)
    task2(seq)
    print(formatter(tuple))
    task4()
    task5()
if __name__ == '__main__':
    main()