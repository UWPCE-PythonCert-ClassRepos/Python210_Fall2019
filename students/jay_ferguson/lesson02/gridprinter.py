#!/usr/bin/env python3

def print_grid(cell_count, cell_size):
    """Print a grid of n sized cells of dimension x. Negative values print a plus."""

    cell_top_bottom = ("+" + "-" * (cell_size)) * cell_count + "+"
    cell_body = ("|" + " " * (cell_size)) * cell_count + "|"

    for i in range(cell_count):
        print(cell_top_bottom)
        for x in range(cell_size):
            print(cell_body)
    print(cell_top_bottom)

if __name__ == '__main__':

    cell_count = round(float(input("Count cells: ")))
    cell_size = round(float(input("Cell size: ")))
    print_grid(cell_count, cell_size)