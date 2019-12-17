
# Task One
# ( 2, 123.4567, 10000, 12345.67) > 'file_002 :   123.46, 1.00e+04, 1.23e+04'
t=( 2, 123.4567, 10000, 12345.67)

def task_one(t):
    return ("file_{:03d} :{:9.2f}, {:.2e}, {:.2e}".format(*t))

task_one(t)

# Task Two
def task_two(t):
    return f"file_{t[0]:03d} :{t[1]:9.2f}, {t[2]:.2e}, {t[3]:.2e}"

task_two(t)

# Task Three
def formatter(seq):
    # do_something_here_to_make_a_format_string
    l = len(seq)
    return ("the {} numbers are: " + ", ".join(["{}"] * l)).format(l, *seq)

formatter((2, 3, 5))
formatter((2, 3, 5, 7, 9))

# Task Four

# Given a 5 element tuple: ( 4, 30, 2017, 2, 27), use string formating to print:'02 27 2017 04 30'
def string_format(t2):
    return "{:02} {} {} {:02} {}".format(t2[3], t2[4], t2[2], t2[0], t2[1])

string_format((4, 30, 2017, 2, 27))

# Task Five
# Given the following four element list:['oranges', 1.3, 'lemons', 1.1]
# Write an f-string that will display: The weight of an orange is 1.3 and the weight of a lemon is 1.1
# Now see if you can change the f-string so that it displays the names of the fruit in upper case, and the weight 20% higher (that is 1.2 times higher)

def fruity(l):
    return f"The weight of an {l[0][:-1]} is {l[1]} and the weight of a {l[2][:-1]} is {l[3]}"

fruity(['oranges', 1.3, 'lemons', 1.1])

def fruity_two(l):
    return f"The weight of an {l[0][:-1].upper()} is {l[1]*1.2} and the weight of a {l[2][:-1].upper()} is {l[3]*1.2}"

fruity_two(['oranges', 1.3, 'lemons', 1.1])

# Task Six
#‘First $99.01 Second $88.09 ‘ One way to do that is: {:20}{:10}{:20}{:8}'.format('First', '$99.01', 'Second', '$88.09')
#Write some Python code to print a table of several rows, each with a name, an age and a cost. 
# Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers.

bigList=[
    ["Yamaha", "R6", 120, 12999.99],
    ["Yamaha", "R1 - RACE", 180, 220000.00],
    ["Honda", "Grom", 32, 999.24]
]

def print_fancy(list):
    header= str("{} {:>10} {:>10}{:>15}".format("Brand", "Model", "HP", "Price"))
    print (header)
    print ("_"*(len(header)+2))
    for b in list:
        print ("{:<10s} {:10s} {:>5} {:16.2f}".format(b[0],b[1],b[2],b[3]))

print_fancy(bigList)  