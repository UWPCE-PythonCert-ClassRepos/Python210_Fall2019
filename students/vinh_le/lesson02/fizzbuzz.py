def fizzBuzz():
    """
    Prints the numbers from 1 to 100.
    But for multiples of three print “Fizz” instead of the number.
    For the multiples of five print “Buzz” instead of the number.
    For numbers which are multiples of both three and five print “FizzBuzz” instead.
    """
    for i in range(1, 100):
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == '__main__':
    fizzBuzz()
