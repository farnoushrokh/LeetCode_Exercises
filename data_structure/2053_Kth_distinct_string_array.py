"""
2053. Kth Distinct String in an Array
Easy
Topics
Companies
Hint
A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than
k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.



Example 1:

Input: arr = ["d","b","c","b","c","a"], k = 2
Output: "a"
Explanation:
The only distinct strings in arr are "d" and "a".
"d" appears 1st, so it is the 1st distinct string.
"a" appears 2nd, so it is the 2nd distinct string.
Since k == 2, "a" is returned.
Example 2:

Input: arr = ["aaa","aa","a"], k = 1
Output: "aaa"
Explanation:
All strings in arr are distinct, so the 1st string "aaa" is returned.
Example 3:

Input: arr = ["a","b","a"], k = 3
Output: ""
Explanation:
The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".

"""


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dict_unq = {}
        cnt_unq = 0
        lst_unq = []
        if len(arr) >= k:
            for el in range(len(arr)):
                if arr[el] in dict_unq:
                    dict_unq[arr[el]] += 1
                else:
                    dict_unq[arr[el]] = 1
        for key, val in dict_unq.items():
            if val == 1:
                cnt_unq += 1
                lst_unq.append(key)
        if k > len(lst_unq):
            return ""
        else:
            return lst_unq[k - 1]
