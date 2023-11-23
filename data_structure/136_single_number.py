"""
136. Single Number
Easy
15.5K
624
company
Amazon
company
Apple
company
Google
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1




"""

import functools
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic_={}

        for i in nums:
            if i in dic_:
                dic_[i] +=1
            else:
                dic_[i] =1
        for k,v in dic_.items():
            if v==1:
                return k

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return functools.reduce(lambda x, y: x ^ y, nums, 0)
