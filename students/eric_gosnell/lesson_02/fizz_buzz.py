"""
-----------------------------------------------------------------------
    Programmer: Eric Gosnell
    Lesson: 02
    Exercise: Fizz Buzz
    Created program 10.17.2019
-----------------------------------------------------------------------
"""


def fizz_buzz():
    """ Function counts down from 100 to 1 inclusive and prints number.
    Exception for multiples of 3: print 'Fizz'.
    Exception for multiples of 5: print 'Buzz'.
    Exception for multiples of both 3 and 5: print 'FizzBuzz'. """

    for i in range (1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print ("Fizz")
        elif i % 5 == 0:
            print ("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    fizz_buzz()
