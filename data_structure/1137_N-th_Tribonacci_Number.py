"""
1137. N-th Tribonacci Number
Attempted
Easy
Topics
Companies
Hint
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.



Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537

"""
# Sliding window
class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        t0, t1, t2= 0,1,1
        for i in range(3, n+1):
            t_next= t0 +t1 + t2
            t0 , t1, t2 = t1, t2, t_next
        return t_next

# Dynamic programming
class Solution:
    def tribonacci(self, n: int) -> int:
        total_num=2
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        dp = [0] * (n +1)
        dp[1]=dp[2]=1
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
        return dp[n]


