#!/usr/bin/env python3

"""Print an entire range of 1-100"""


def fizzbuzz_range ():
    for number in range(1, 101):
        print(number)


"""Do math, use built in range function, and logic operator to return true for numbers divisible by 3 and 5"""


def fizzbuzz ():
    for number in range(1, 101):
        if not number % 3 and not number % 5:
            print("FizzBuzz")
        elif not number % 3:
            print('Fizz')
        elif not number % 5:
            print('Buzz')
        else:
            print(number)


if __name__ == '__main__':

    fizzbuzz()
