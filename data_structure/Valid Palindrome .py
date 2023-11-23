"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric
characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

"""
s = "A man, a plan, a canal: Panama"


class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''
        for i in range(len(s)):
            if (s[i].isalpha()):
                res += s[i].lower()
            elif (s[i].isdigit()):
                res += s[i]
        if res == res[-1::-1]:
            return True
        else:
            return False
