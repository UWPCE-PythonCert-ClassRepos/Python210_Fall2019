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