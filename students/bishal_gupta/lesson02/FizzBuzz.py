

def FizzBuzz():

    """
    
    Program in Python to iterate the numbers from 1 to 100 in inclusive.
    For numbers that are multiples of 3, the program prints Fizz
    For numbers that are multiples of 5, the program prints Buzz
    For numbers that are multiples of both 3 and 5, the program prints FizzBuzz
    For numbers that are neither multiples of 3 or 5, just program prints the number as is
    """

    n = 0
    n_max = 100

    while n != n_max:
        n += 1
        if (n % 3 == 0 and n % 5 != 0):
            print('Fizz')
        elif (n % 3 != 0 and n % 5 == 0):
            print('Buzz')
        elif (n % 3 == 0 and n % 5 == 0):
            print('FizzBuzz')
        else:
            print(n)

if __name__=='__main__':
    FizzBuzz()