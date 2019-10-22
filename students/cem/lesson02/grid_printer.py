"""
Writing a function that draws a grid:
"""


def grid_printer():
    plus = '+'
    minus = '-'+' '
    vertical_line = '|'
    space = ' ' * 7

    print(plus, minus * 4 + plus, minus * 4 + plus)
    print(vertical_line, space, vertical_line, space, vertical_line)
    print(vertical_line, space, vertical_line, space, vertical_line)
    print(vertical_line, space, vertical_line, space, vertical_line)
    print(vertical_line, space, vertical_line, space, vertical_line)
    print(plus, minus * 4 + plus, minus * 4 + plus)
    print(vertical_line, space, vertical_line, space, vertical_line)
    print(vertical_line, space, vertical_line, space, vertical_line)
    print(vertical_line, space, vertical_line, space, vertical_line)
    print(vertical_line, space, vertical_line, space, vertical_line)
    print(plus, minus * 4 + plus, minus * 4 + plus)


if __name__ == '__main__':
    grid_printer()


# Was not able to complete the second section of this
# def print_grid():
#     """
#     Write a function print_grid(n) that takes one integer argument and prints a grid just like before,
#     BUT the size of the grid is given by the argument.
#     """
#     plus = '+'
#     minus = '-'+' '
#     vertical_line = '|'
#     space = ' '
#
#     n=1
#     y=1
#
#     print(plus, minus * n + plus, minus * n + plus)
#
# def do_twice(x, f):
#     for x in range(x):
#         f()
#
# def print_beam():
#     print('+', '-')
#     print('+')
#
# do_twice(2, print_beam)
#
# def print_minus():
#     for i in range(3):
#         print('-', end=' ')
#
# # def print_post():
# #     for i in range(4):  # for (9)
# #         print('|')
#
# def print_post():
#     print('|         ')
#
# def do_three(f):
#     f()
#     f()
#     f()
#
# def do_twice_beam():
#     for i in range(1):
#         print('+', '+', '+')
#
# def small_square(f):
#     for f in range(3):
#         print('+', '+', '+')
#
# # small_square(1)
