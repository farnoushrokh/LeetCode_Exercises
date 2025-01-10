"""
1556. Thousand Separator
Solved
Easy
Topics
Hint
Given an integer n, add a dot (".") as the thousands separator and return it in string format.



Example 1:

Input: n = 987
Output: "987"
Example 2:

Input: n = 1234
Output: "1.234"

"""
class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        if len(str(n))>3:
            reversed_str_n = str(n)[::-1]
            formatted_str = '.'.join(reversed_str_n[i:i+3] for i in range(0, len(reversed_str_n), 3))
            formatted_str = formatted_str[::-1]
            return formatted_str
        else:
            return(str(n))