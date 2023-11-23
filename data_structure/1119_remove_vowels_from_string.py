"""
1119. Remove Vowels from a String
Easy
341
111
company
Amazon
Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.



Example 1:

Input: s = "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"
Example 2:

Input: s = "aeiou"
Output: ""


"""


class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        word = ''
        for el in s:
            if el not in vowels:
                word += el
        return word
