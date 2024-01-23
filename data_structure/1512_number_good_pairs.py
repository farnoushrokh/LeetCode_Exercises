"""
1512. Number of Good Pairs
Solved
Easy
Topics
Companies
Hint
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.



Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0


Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100

"""


class Solution(object):
    def numIdenticalPairs(self, nums):
        cnt = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    cnt += 1
        return cnt


# Second solution with o(n)
class Solution:

    # search for duplicate numbers
    def numIdenticalPairs(self, nums) -> int:

        # number of good pairs
        repeat = {}
        num = 0

        # for every element in nums
        for v in nums:

            # number of repeated digits
            if v in repeat:

                # count number of pairs based on duplicate values
                if repeat[v] == 1:
                    num += 1
                else:
                    num += repeat[v]

                # increment the number of counts
                repeat[v] += 1
            # number has not been seen before
            else:
                repeat[v] = 1
        # return
        return num