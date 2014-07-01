def fibonacci_series():
    print 'The first 10 numbers in the '
    print 'Fibonacci series'

    for number in range(1,11):
        print fib(number)

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n -2)

if __name__ == '__main__':
    fibonacci_series()
