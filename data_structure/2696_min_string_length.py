"""
You are given a string s consisting only of uppercase English letters.

You can apply some operations to this string where, in one operation, you can remove any occurrence of one of the
substrings "AB" or "CD" from s.

Return the minimum possible length of the resulting string that you can obtain.

Note that the string concatenates after removing the substring and could produce new "AB" or "CD" substrings.


"""


class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        mode = True
        while mode:
            mode = False
            new_s = ''
            i = 0
            while i < len(s):
                if i < len(s) - 1 and s[i:i + 2] in ["AB", "CD"]:
                    i += 2
                    mode = True
                else:
                    new_s += s[i]
                    i += 1
            s = new_s
        return len(s)
