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