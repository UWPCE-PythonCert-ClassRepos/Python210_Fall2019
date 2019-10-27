#!/usr/bin/env python3

#TASK-1-2:
def string_formatting_task_1_2(a: tuple) -> str:
    return ("file_" + "{:03d}" + ":   " +  "{:.2f}" + ",   " + "{:.2E}" + ",  " + "{:.2E}").format(a[0],a[1],a[2],a[3]) 


#TASK-3:

def string_formatting_task_3(a: tuple) -> str:
    return ("file_" + "{:03d}" + ":   " +  "{:.2f}" + ",   " + "{:.2E}" + ",  " + "{:.2E}").format(*a)

#TASK-4:

"""
( 4, 30, 2017, 2, 27)

use string formating to print:

'02 27 2017 04 30'
"""
def string_formatting_task_4(a: tuple) -> str:
    return ("{:02d} {} {} {:02d} {}").format(a[3],a[4],a[2],a[0],a[1])


"""
Here’s a task for you: Given the following four element list:

['oranges', 1.3, 'lemons', 1.1]

Write an f-string that will display:

The weight of an orange is 1.3 and the weight of a lemon is 1.1

Now see if you can change the f-string so that it displays the names of the fruit in upper case, and the weight 20% higher (that is 1.2 times higher).
"""

def string_formatting_task_5(lst: list) -> str:
    print(f'The weight of an {lst[0]} is {lst[1]} and the weight of a {lst[2]} is {lst[3]}')
    print(f'The weight of an {lst[0].upper()} is {lst[1] + 1.2} and the weight of a {lst[2].upper()} is {lst[3] + 1.2}')

 
