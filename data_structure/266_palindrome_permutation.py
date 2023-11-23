"""
266. Palindrome Permutation
Easy
1K
68
company
Facebook
company
Google
company
Uber
Given a string s, return true if a permutation of the string could form a
palindrome
 and false otherwise.



Example 1:

Input: s = "code"
Output: false
Example 2:

Input: s = "aab"
Output: true
Example 3:

Input: s = "carerac"
Output: true
"""
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        sets = set()
        for char in s:
            if char not in sets:
                sets.add(char)
            else:
                sets.remove(char)
        return (len(sets) <= 1)