"""
1512. Number of Good Pairs
Easy
4.3K
204
company
Adobe
company
Amazon
company
Microsoft
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

Hint:
Count how many times each number appears. If a number appears n times, then n * (n – 1) // 2
good pairs can be made with this number.

"""

