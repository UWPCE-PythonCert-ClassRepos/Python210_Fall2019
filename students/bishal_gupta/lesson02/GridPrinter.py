## To print the horizontal character for the grid
def horizonatalgrid(a):
    print("+", end=" ")
    for i in range(a-1):
        print("- - - - +", end=" ")
    print("- - - - +")

# To print the vertical characters for the grid
def verticalgrid(a):
    print("|", end=" ")
    for i in range(a-1):
        print("        |", end=" ")
    print("         |")

# Now combine the horizontal and vertical lines to print the grid
def print_grid(a,b):
    horizonatalgrid(a)
    for i in range(b):
        for i in range(4):
            verticalgrid(a)
        horizonatalgrid(a)




