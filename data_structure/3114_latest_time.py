"""
3114. Latest Time You Can Obtain After Replacing Characters
Solved
Easy
Topics
Companies
Hint
You are given a string s representing a 12-hour format time where some of the digits (possibly none) are replaced
with a "?".

12-hour times are formatted as "HH:MM", where HH is between 00 and 11, and MM is between 00 and 59. The earliest
12-hour time is 00:00, and the latest is 11:59.

You have to replace all the "?" characters in s with digits such that the time we obtain by the resulting string is a
valid 12-hour format time and is the latest possible.

Return the resulting string.



Example 1:

Input: s = "1?:?4"

Output: "11:54"

Explanation: The latest 12-hour format time we can achieve by replacing "?" characters is "11:54".

Example 2:

Input: s = "0?:5?"

Output: "09:59"

Explanation: The latest 12-hour format time we can achieve by replacing "?" characters is "09:59".
"""

class Solution(object):
    def findLatestTime(self, s):
        """
        :type s: str
        :rtype: str
        """
        s1 = list(s)
        for i in range(5):
            if s1[0] == '?':
                if s1[1] > '1' and s1[1] != '?':
                    s1[0] = '0'
                else:
                    s1[0] = '1'
            if s1[1] == '?':
                if s1[0] == '1':
                    s1[1] = '1'
                elif s1[0] == '0':
                    s1[1] = '9'
            if s1[3] == '?':
                s1[3] = '5'
            if s1[4] == '?':
                s1[4] = '9'
        return ''.join(s1)