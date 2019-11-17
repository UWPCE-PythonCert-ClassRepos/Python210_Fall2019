#!/usr/bin/env python3


def fizzbuzz_range ():
    for number in range(1, 101):
        print(number)
        """Print entire range 1-100 inclusive"""

def fizzbuzz ():
    for number in range(1, 101):
        if not number % 3 and not number % 5:
            """If divisible by 3 and 5 is true print Fizzbuzz"""
            print("FizzBuzz")
        elif not number % 3:
            """If divisible by 3 is true print Fizz"""
            print('Fizz')
        elif not number % 5:
            """If divisible by 5 is true print Buzz"""
            print('Buzz')
        else:
            """Just print the number if none of the above are true"""
            print(number)


if __name__ == '__main__':

    fizzbuzz()
