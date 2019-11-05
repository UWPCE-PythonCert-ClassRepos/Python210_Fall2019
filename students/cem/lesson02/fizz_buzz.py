"""
Write a program that prints the numbers from 1 to 100 inclusive.
But for multiples of three print “Fizz” instead of the number.
For the multiples of five print “Buzz” instead of the number.
For numbers which are multiples of both three and five print “FizzBuzz” instead.
"""


def fizz_buzz():
    for x in range(1, 101):
        if not(x%3==0 or x %5==0):
            print(x)
        elif(x%3==0 and x %5==0):
            print("FizzBuzz")
        elif(x%3==0):
            print("Fizz")
        elif(x%5==0):
            print("Buzz")


if __name__ == '__main__':
    fizz_buzz()
