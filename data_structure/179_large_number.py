"""
179. Largest Number
Solved
Medium
Topics
Companies
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.



Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"

"""


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted(nums, key=lambda x: x / (10 ** len(str(x)) - 1), reverse=True)
        str_nums = [str(num) for num in nums]
        res = ''.join(str_nums)
        res = str(int(res))
        return res
