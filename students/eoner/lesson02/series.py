#crappy solution
def fibone(n):
    a = 0
    b = 1
    y = [0, 1]
    for i in range(n):
        c = a+b
        a = b
        b = c
        y.append(c)
        if (i == (n-1)):
            return (y[n])

#ok solution
def fibonacci(n):
    fib = [0, 1]
    for i in range(n):
        fib.append(fib[i] + fib[i+1])
    return fib[n]


def lucas(n):
    luc = [2, 1]
    for i in range(n):
        luc.append(luc[i] + luc[i+1])
    return luc[n]

def sum_series(n, f=0, s=1):
    sum = [f, s]
    for i in range(n):
        sum.append(sum[i] + sum[i+1])
    return sum[n]

if __name__ == "__main__":
    # run some tests
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    assert lucas(0) == 2
    assert lucas(1) == 1

    assert lucas(4) == 7

    # test that sum_series matches fibonacci
    assert sum_series(5) == fibonacci(5)
    assert sum_series(7, 0, 1) == fibonacci(7)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    # test if sum_series works for arbitrary initial values
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19

    print("tests passed")