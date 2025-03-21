"""
1952. Three Divisors
Easy
485
26
company
Microsoft
Given an integer n, return true if n has exactly three positive divisors. Otherwise, return false.

An integer m is a divisor of n if there exists an integer k such that n = k * m.



Example 1:

Input: n = 2
Output: false
Explantion: 2 has only two divisors: 1 and 2.
Example 2:

Input: n = 4
Output: true
Explantion: 4 has three divisors: 1, 2, and 4.


"""


class Solution:
    def isThree(self, n: int) -> bool:
        res = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                res.append(i)
                if i != n // i:
                    res.append(n // i)
            i += 1
        if len(res) == 3:
            return True
        else:
            return False