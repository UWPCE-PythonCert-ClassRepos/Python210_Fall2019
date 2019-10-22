### Author - Tommy Aguilu
### Version 1.0
### Class - Python 210A

#function definition
def fizbuzz(x):
    x = int(x)
    for i in range(1, (x +1)):
        ###this must go first in order to capture ints that are divizable by 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            print("fizz buzz")
        elif i % 3 == 0 :
            print("buzz")
        elif i % 5 == 0:
            print("fizz")
        else:
            print(i)
def menu():
    imported_variable = input("range goes here ")
    return imported_variable

#I/O
imported_variable = menu()
try:
    fizbuzz(imported_variable)
except ValueError:
    print("please input numbers only and try again")
