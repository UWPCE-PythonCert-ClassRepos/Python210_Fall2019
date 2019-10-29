def print_grid(x, s):
    a = (((("+" + ("-"*s)))*x) + "+")
    b = ("\n"+((("|" + (" "*s)))*x) + "|")

    for i in range(x):
        print(a+(b*s))
    print(a)

print_grid(3,4) 