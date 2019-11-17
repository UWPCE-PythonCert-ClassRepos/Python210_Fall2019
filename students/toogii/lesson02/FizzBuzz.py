#!/usr/bin/env python3


def FizzBuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print('FizzBuzz')
        if number % 3 == 0:
            print('Fizz')
        elif number % 5 == 0:
            print('Buzz')
        else:
            print(number)

if __name__ == '__main__':
    FizzBuzz()
