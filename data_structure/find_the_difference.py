"""
389. Find the Difference
Easy
4.7K
451
company
Google
company
Amazon
company
IBM
You are given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t.



Example 1:

Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.
Example 2:

Input: s = "", t = "y"
Output: "y"

"""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return [el for el in t if t.count(el) > s.count(el)][0]