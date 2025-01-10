"""
1525. Number of Good Ways to Split a String
Solved
Medium
Topics
Companies
Hint
You are given a string s.

A split is called good if you can split s into two non-empty strings sleft and sright where their concatenation is
equal to s (i.e., sleft + sright = s) and the number of distinct letters in sleft and sright is the same.

Return the number of good splits you can make in s.



Example 1:

Input: s = "aacaba"
Output: 2
Explanation: There are 5 ways to split "aacaba" and 2 of them are good.
("a", "acaba") Left string and right string contains 1 and 3 different letters respectively.
("aa", "caba") Left string and right string contains 1 and 3 different letters respectively.
("aac", "aba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aaca", "ba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aacab", "a") Left string and right string contains 3 and 1 different letters respectively.
Example 2:

Input: s = "abcd"
Output: 1
Explanation: Split the string as follows ("ab", "cd").

"""
import collections

class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        s1=collections.Counter() #s1 is now empty
        s2=collections.Counter(s) #s2 is now has all string
        count=0
        for el in s:
            s1[el] +=1
            s2[el] -=1
            if s2[el]==0:
                s2.pop(el)
            if len(s1) == len(s2):
                count +=1
        return count