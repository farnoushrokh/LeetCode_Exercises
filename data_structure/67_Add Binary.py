"""
67. Add Binary
Easy
8.8K
875
company
Amazon
company
Facebook
company
Bloomberg
Given two binary strings a and b, return their sum as a binary string.



Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
Accepted
1.3M
Submissions
2.4M
Acceptance Rate
52.7%

"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return '{0:b}'.format(int(a, 2) + int(b, 2))

