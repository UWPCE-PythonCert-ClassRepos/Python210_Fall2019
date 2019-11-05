"""
Title: strformat_lab
Date: 10/25/2019
Dev: K.Shaffer

"""
# Task 1
n = 4
print("file_{:03} :   {:.2f}, {:.2E}, {:.2E}".format(2, 123.4567, 10000, 12345.67))

# Task 2
a = 2
b = 123.4567
c = 10000
d = 12345.67

print(f"file_{a:03} :   {b:.2f}, {c:.2E}, {d:.2E}")


# Task 3
def formatter(nums):
    formatted = "the " + str(len(nums)) + " numbers are: " + str(len(nums)*"{:d} ").format(*nums)
    return formatted


t = (1, 2, 3, 4, 5, 8, 9)
print(formatter(t))

# Task 4
nums = (4, 30, 2017, 2, 27)
print("{:02} {:d} {:d} {:02} {:d}".format(nums[3], nums[4], nums[2], nums[0], nums[1]))

# Task 5
els = ['oranges', 1.3, 'lemons', 1.1]

print(f"The weight of an {els[0][:-1]:s} is {els[1]:.1f} and the weight of a {els[2][:-1]:s} is {els[3]:.1f}")
print(f"The weight of an {els[0][:-1].upper():s} is {els[1]*1.2:.1f} and the weight of a {els[2][:-1].upper():s}"
      f" is {els[3]*1.2:.1f}\n")

# Task 6
rows = [["NAME", "AGE", "PRICE"],["Josh", 21, "$900"], ["Kathy", 30, "$1000"], ["Kevin", 25, "$90"],
        ["Louis", 19, "$12000"], ["Max", 10, "$0"]]

for row in rows:
    print('{:<8}{:<5}{:<8}'.format(row[0], row[1], row[2]))

print("\n")

t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print('{:^5}{:^5}{:^5}{:^5}{:^5}{:^5}{:^5}{:^5}{:^5}{:^5}'.format(t[0], t[1], t[2], t[3], t[4], t[5],
                                                                  t[6], t[7], t[8], t[9]))

