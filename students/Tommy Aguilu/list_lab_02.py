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