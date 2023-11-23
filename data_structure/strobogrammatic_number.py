"""
246. Strobogrammatic Number
Easy
563
981
company
Facebook
company
Uber
company
Google
Given a string num which represents an integer, return true if num is a strobogrammatic number.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).



Example 1:

Input: num = "69"
Output: true
Example 2:

Input: num = "88"
Output: true
Example 3:

Input: num = "962"
Output: false

"""


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        numbers = {
            '1': '1',
            '2': '#',
            '3': '#',
            '4': '#',
            '5': '#',
            '6': '9',
            '7': '#',
            '8': '8',
            '9': '6',
            '0': '0'
        }

        new_num = ""
        for c in num:
            new_num += numbers[c]
        return (new_num[::-1] == num)