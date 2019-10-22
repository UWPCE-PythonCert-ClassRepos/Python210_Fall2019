### Author - Tommy Aguilu
### Version 1.0
### Class - Python 210A

#function definition
def grid_static_cell(x):
    x = int(x)
    print("+" + (" - " * x) + "+" + (" - " * x) + "+")
    for i in range(0, x):
        print("|" + ("   " * x) +"|" + ("   " * x) +"|")
    print("+" + (" - " * x) + "+" + (" - " * x) + "+")
    for i in range(0, x):
        print("|" + ("   " * x) +"|" + ("   " * x) +"|")
    print("+" + (" - " * x) + "+" + (" - " * x) + "+")

def grid_dynamic_cell(a, b):
    a = int(a)
    b = int(b)
    #box creation
    print(b * ("+" + (" - " * a)) + "+")
    for i in range(0, a):
        print(b * ("|" + ("   " * a)) +"|")

choice = input("Please specify static or dynamic ")
if choice == "static":
    x = input("length? ")
    grid_static_cell(x)
elif choice == "dynamic":
    a = input("Please specify cell size ")
    b = input("Please specify size of grids ")
    a = int(a)
    b = int(b)
    for i in range(0, b):
        grid_dynamic_cell(a, b)
    print(b * ("+" + (" - " * a)) + "+")