def FizzBuzz():
    """Print numbers from 1 to 100 inclusive.
    For multiples of three print 'Fizz' and for multiples of five print 'Buzz'.
    For multiples of both print 'FizzBuzz' instead."""

    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)

if __name__ == '__main__':
    FizzBuzz()
