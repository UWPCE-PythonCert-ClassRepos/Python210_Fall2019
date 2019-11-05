#Task 1
def format_numbers(t1):
    format_string = "file_{:03d} :   {:.2f}, {:.2e}, {:.2e}".format(t1[0], t1[1], t1[2], t1[3])
    return format_string

print(format_numbers((2, 123.4567, 10000, 12345.67)))

#Task 2

def format_numbers_2(t1):
    format_string = f"file_{t1[0]:03d} :   {t1[1]:.2f}, {t1[2]:.2e}, {t1[3]:.2e}"
    return format_string

print(format_numbers_2((2, 123.4567, 10000, 12345.67)))

#Task 3
def formatter(t2):
    form_string = "the {:d} numbers are: {:d}" + ", {:d}"*(len(t2)-1)
    return form_string.format(len(t2), *t2)

print(formatter((2,3,4,5,6,5)))

#Task 4
def format_index(t3):
    format_string = f"{t3[3]:02d} {t3[4]:02d} {t3[2]} {t3[0]:02d} {t3[1]:02d}"
    return format_string

print(format_index((4, 30, 2017, 2, 27)))

#Task 5
def f_string_format(t4):
    format_string = f"The weight of an {t4[0].upper()} is {t4[1]*1.2} and the weitght of a {t4[2].upper()} is {t4[3]*1.2}"
    return format_string

print(f_string_format(['orange', 1.3, 'lemon', 1.1]))

#Task 6
def format_table(name, age, price):
    print("{:15}{:>10}{:>20}".format('Name','Age','Price'))
    print("-"*45)
    for x in range(len(name)):
        print("{:15}{:10d}{:20.2f}".format(name[x],age[x],price[x]))

name_list = ["Piccasso", "Davinci", "Monet", "Van Gohg", "Dali"]
age_list = [90,320,53,83,38]
price_list = [1323404,2003948,122367.43,288839.4623,534432]

format_table(name_list,age_list,price_list)

#Extra Task

t7 = (1,2,3,4,5,6,7,8,9,10)
print(("{:5}"*10).format(*t7))
