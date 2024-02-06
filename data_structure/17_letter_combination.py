"""

17. Letter Combinations of a Phone Number
Solved
Medium
Topics
Companies
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any
letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]


"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                      "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        word_lst = []
        if len(digits) == 0:
            return list()
        if len(digits) == 1:
            return [el for el in digits_map[(digits)]]
        else:
            for el in digits:
                if el in [i for i in digits_map.keys()]:
                    word_lst.append(digits_map[el])
            first_item = [el for el in word_lst[0]]
            for el in word_lst[1:]:
                first_item = [first_char + comb for first_char in first_item for comb in el]
            return first_item

