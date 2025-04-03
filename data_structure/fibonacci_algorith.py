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

class Solution:
    def fib(self, n: int) -> int:
        memo=[None]*100
        if n ==0:
            return 0
        if n==1:
            return 1
        if memo[n] is not None:
            return memo[n]
        memo[n] = self.fib(n-1) + self.fib(n-2)
        return memo[n]
