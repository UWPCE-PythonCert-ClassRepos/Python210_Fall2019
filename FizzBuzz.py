"""James Spaulding
    Homework 2: FizzBuzz
    Due: 10/22/2019
    Submitted: 10/21/2019
    part 2/3"""
def fizzBuzz1():
    n=0
    while n<101:
        if (n%3 == 0 and n%5 == 0):
            print('FizzBuzz')
            n=n+1
        elif n%5 == 0:
            print("Buzz!")
            n=n+1
        elif n%3== 0:
            print("Fizz!")
            n=n+1
        else:
            print(n, end="\n")
            n=n+1
    return
"""a better way"""
for i in range(1,101)
    fb=''
    if i%3==0:






