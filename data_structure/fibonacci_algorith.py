# classic way of fib
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(n=6))
print(fib(n=7))
print(fib(n=8))

""" if you give fib 50 the process took much longer. then you should use another function """

# memoization speeds up the execution of expensive recursive functions by storing previously calculated results
# in a cache

cache = {0: 0, 1: 1}


def fibonacci_of(n):
    if n in cache:
        return cache[n]
    else:
        cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)
        return cache[n]


print(fibonacci_of(n=6))
