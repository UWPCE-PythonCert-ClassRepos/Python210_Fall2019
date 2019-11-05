# Eddie Oner Python | PYTHON 210 A Lesson 01 | Activity: Python Pushups Part 1 of 2

# Each function, when called, should cause an exception to happen
# Each function should result in one of the four most common exceptions you’ll find.
# for review: NameError, TypeError, SyntaxError, AttributeError


def NameError():
    print(hello)


def TypeError():
    x = int(123131231)
    y = str
    z = x*y

# Looks like sytax errors when parsing, before calling the function, not calling function since below will error when uncommented
# def SyntaxError():
#     print hello


def AttributeError():
    x = 8
    x.append(4)


# NameError()
# TypeError()
# AttributeError()