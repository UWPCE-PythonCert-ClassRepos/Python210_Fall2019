def print_grid(n):

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
    """ :m : number of rows and columns
        :n : size of grid panel
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


def main():
    print_grid2(5, 3)


if __name__ == "__main__":
    main()
