"""
213. House Robber II
Solved
Medium
Topics
Companies
Hint
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if
two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can
rob tonight without alerting the police.



Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        money = 0
        n=len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            money= max(nums[0], nums[1])

        def rob_(nums):
            rob1, rob2 = 0, 0
            for num in nums:
                new_rob = max(rob1, rob2+ num)
                rob2 = rob1
                rob1 = new_rob
            return rob1
        money = max(rob_(nums[:-1]), rob_(nums[1:]))
        return money