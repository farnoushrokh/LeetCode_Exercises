"""
69. Sqrt(x)
Easy
7.3K
4.3K
company
Amazon
company
Apple
company
Bloomberg
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.


Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        left= 2
        right = x//2
        while left <= right:
            pivot = left +(right- left)//2
            num= pivot * pivot
            if num >x:
                right= pivot -1
            elif num <x:
                left = pivot +1
            else:
                return pivot
        return int(right)