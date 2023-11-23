"""
258. Add Digits
Easy
4.6K
1.9K
company
American Express
company
Amazon
company
Google
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.



Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0


Constraints:

0 <= num <= 231 - 1


Follow up: Could you do it without any loop/recursion in O(1) runtime?

"""


class Solution:
    def addDigits(self, num: int) -> int:
        root = 0
        while num > 0:
            root += num % 10
            num = num // 10
            if num == 0 and root > 9:
                num = root
                root = 0
        return root
