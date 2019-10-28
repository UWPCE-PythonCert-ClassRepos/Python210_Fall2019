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