'''
fizz_buzz
K.Shaffer
10/21/19
'''

def fizzBuzz():
    for i in range(101):
        fb = ''
        if i % 3 == 0:
            fb += 'Fizz'
        if i % 5 == 0:
            fb += 'Buzz'
        if fb:
            print(fb)
        else:
            print(str(i))
fizzBuzz()