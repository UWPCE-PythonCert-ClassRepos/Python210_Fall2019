def print_grid(n):
    """
    Prints a 2x2 grid with the size of panel depnding on given parameter

    :param: n : size of grid panel
    """
    print("+" + (" - " * n) + "+", end=' ')
    print((" - " * n) + "+")

    for i in range(n):
        print("|" + ("   " * n) + "|", end=' ')
        print(("   " * n) + "|")

    print("+" + (" - " * n) + "+", end=' ')
    print((" - " * n) + "+")

    for i in range(n):
        print("|" + ("   " * n) + "|", end=' ')
        print(("   " * n) + "|")

    print("+" + (" - " * n) + "+", end=' ')
    print((" - " * n) + "+")


def print_grid2(m, n):
    """
    Prints a grid based on the number of rows and columns entered and size of panel

    :param: m : number of rows and columns
    :param: n : size of grid panel
    """
    if m == 1:
        print("+" + (" - " * n) + "+")
        for j in range(n):
            print("|" + ("   " * n) + "|")
        print("+" + (" - " * n) + "+")

    else:
        print("+" + (" - " * n) + "+", end=' ')
        print(((" - " * n) + "+") * (m - 1))

        for i in range((m - 1)):
            for j in range(n):
                print("|" + ("   " * n) + "|", end=' ')
                print((("   " * n) + "|") * (m - 1))

            print("+" + (" - " * n) + "+", end=' ')
            print(((" - " * n) + "+") * (m - 1))


if __name__ == "__main__":
    print_grid(3)
    print_grid2(5, 3)
