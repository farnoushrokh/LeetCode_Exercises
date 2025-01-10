"""
204. Count Primes
Solved
Medium
Topics
Companies
Hint
Given an integer n, return the number of prime numbers that are strictly less than n.



Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
"""
import numpy as np


class Solution:
    def countPrimes(self, n: int) -> int:
        is_prime = np.ones(n, dtype=bool)
        is_prime[:2] = False
        for i in range(2, int(np.sqrt(n) + 1)):
            if is_prime[i]:
                is_prime[i * i:n:i] = False
        return (np.sum(is_prime))
