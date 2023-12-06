"""
1925. Count Square Sum Triples
Easy
390
39
company
Amazon
Qualtrics
A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.

Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.



Example 1:

Input: n = 5
Output: 2
Explanation: The square triples are (3,4,5) and (4,3,5).
Example 2:

Input: n = 10
Output: 4
Explanation: The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).


"""
from math import sqrt

class Solution:
    def countTriples(self, n: int) -> int:
        res, limit = 0, n * n
        for i in range(1, n):
            for j in range(i + 1, n):
                k = i * i + j * j
                if k > limit: break
                if sqrt(k) % 1 == 0:
                    res += 2
        return res
