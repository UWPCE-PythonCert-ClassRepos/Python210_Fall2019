def print_grid(x, s):
    for i in range(x):
        print((((("+" + ("-"*s)))*x) + "+")+(("\n"+((("|" + (" "*s)))*x) + "|")*s))
    print(((("+" + ("-"*s)))*x) + "+")

print_grid(3,4) 