### Author - Tommy Aguilu
### Version 1.0
### Class - Python 210A

#task1
fruits = ["apples", "pears", "oranges", "peaches"]
def fruit_loops(x):
    b=0
    for i in x:
        print(((str(b+1)+".")+ x[b]))
        b+=1

def fruit_sort(x):
    print("Fruits starting with p")
    for i in x:
        if i[0] == "p":
            print(i)

fruit_loops(fruits)
x = input("What fruit would you like to display? ")
x = int(x)
print(fruits[x-1])
add = input("What fruit would you like to add to the list? ")
fruits.insert(0, add)
fruit_loops(fruits)
fruit_sort(fruits)

#task 2
fruits = ["apples", "pears", "oranges", "peaches"]
def fruit_loops(x):
    print("Current list of fruits: ")
    b=0
    for i in x:
        print(((str(b+1)+".")+ x[b]))
        b+=1

def fruit_remove(x):
    b = input("what fruit do you want to remove from the list? ")
    x.pop(str(b))
fruit_loops(fruits)
b = input("what fruit do you want to remove from the list? ")
fruits.remove(b)
fruit_loops(fruits)

#task 3

fruits = ["apples", "pears", "oranges", "peaches"]
def fruit_loops(x):
    for i in x:
        choice = input("do you like " + str(i) + " yes/no ")
        if choice == "yes":
            "Great! It will stay on the list"
        elif choice == "no":
            x.remove(i)
        print("Current list of fruits: ")
        b = 0
        for i in x:
            print(((str(b + 1) + ".") + x[b]))
            b += 1

def fruit_remove(x):
    b = input("what fruit do you want to remove from the list? ")
    x.pop(str(b))
fruit_loops(fruits)

#task 4

fruits = ["apples", "pears", "oranges", "peaches"]
def fruit_loops(x):
    b = 0
    b2 = 0
    for i in x:
        c = (((str(b + 1) + ".") + x[b]))
        print(c[::-1])
        b += 1
    x.pop()
    for i in x:
        print(((str(b2 + 1) + ".") + x[b2]))
        b2 += 1

fruit_loops(fruits)