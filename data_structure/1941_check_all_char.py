"""
1941. Check if All Characters Have Equal Number of Occurrences
Solved
Easy
Topics
Companies
Hint
Given a string s, return true if s is a good string, or false otherwise.

A string s is good if all the characters that appear in s have the same number of occurrences
(i.e., the same frequency).



Example 1:

Input: s = "abacbc"
Output: true
Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.
Example 2:

Input: s = "aaabb"
Output: false
Explanation: The characters that appear in s are 'a' and 'b'.
'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.

"""


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        s_dict = {}
        final = []
        for el in s:
            if el not in s_dict:
                s_dict[el] = 1
            else:
                s_dict[el] += 1
        for k, v in s_dict.items():
            final.append(v)
        if len(set(final)) == 1:
            return True
        else:
            return False
