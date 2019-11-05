#!/usr/bin/env python3

# In the break_me.py file write four simple Python functions:

# Each function, when called, should cause an exception to happen
# Each function should result in one of the four most common exceptions you’ll find.
# for review: NameError, TypeError, SyntaxError, AttributeError

# 1. A function that creates a NameError

def bad_function1():
    a = 1
    b = 2
    answer = a + c
    print(answer)

# 2. A function that creates a TypeError
def bad_function2():
    a = '1'
    b = 2
    answer = a + b
    print(answer)

# 3. A function that creates a SyntaxError
# def bad_function3():
#     None = 0
#     a = 1
#     answer = None * a
#     print(answer)

# 4. A function that creates an AttributeError
def bad_function4():
    from datetime import date

    today = date.todays()
    print(today)

# bad_function1()
# bad_function2()
# bad_function3()
bad_function4()
