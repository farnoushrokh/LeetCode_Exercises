"""
796. Rotate String
Solved
Easy
Topics
Companies
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.


Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false

"""


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) < len(goal) or len(goal) < len(s):
            return False
        else:
            s_concat = s + s
            return goal in s_concat
