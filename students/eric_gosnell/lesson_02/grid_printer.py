"""
-----------------------------------------------------------------------
    Programmer: Eric Gosnell
    Lesson: 02
    Exercise: Grid Printer
    Created program 10.17.2019
-----------------------------------------------------------------------
"""


def grid_print(x, y):
    """Function takes in x and y dimensions for grid height and width.
    X and Y dimensions are horizontal and vertical squares in the grid.
    Grid is a multi-dimensional list object with two types of rows -
    The frame row and the body row.  Iterations of each are determined
    by the x and y dimension.  Regardless of the arguments provided, the
    size of the grid grows proportionately."""

    grid_width = x
    grid_height = y
    frame_row = ("+" + "-" * grid_width) * grid_width + "+"
    body_row = ("|" + " " * grid_width) * grid_width + "|"

    for i in range(grid_height):
        print(frame_row)
        for j in range(grid_height - 1):
            print(body_row)
    print(frame_row)

if __name__ == "__main__":
    grid_print(4,4)
