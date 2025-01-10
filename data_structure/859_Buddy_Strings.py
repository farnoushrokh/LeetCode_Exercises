"""
859. Buddy Strings
Solved
Easy
Topics
Companies
Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise,
return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters
at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".


Example 1:

Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
Example 2:

Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.

"""

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        diffs=[]
        if len(s) != len(goal):
            return False
        else:
            for i in range(len(s)):
                if s[i] != goal[i]:
                    diffs.append(i)
        if len(diffs)==0:
            return len(set(s)) < len(s)
        elif len(diffs)==2:
            i, j = diffs
            return (s[i]==goal[j] and s[j]==goal[i])
        else:
            return False