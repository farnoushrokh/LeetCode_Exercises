"""
2062. Count Vowel Substrings of a String
Solved
Easy
Topics
Companies
Hint
A substring is a contiguous (non-empty) sequence of characters within a string.

A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels
present in it.

Given a string word, return the number of vowel substrings in word.



Example 1:

Input: word = "aeiouu"
Output: 2
Explanation: The vowel substrings of word are as follows (underlined):
- "aeiouu"
- "aeiouu"
Example 2:

Input: word = "unicornarihan"
Output: 0
Explanation: Not all 5 vowels are present, so there are no vowel substrings.
Example 3:

Input: word = "cuaieuouac"
Output: 7
Explanation: The vowel substrings of word are as follows (underlined):
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"

"""


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        new_word = []
        word_ = ""

        for el in word:
            if el in vowels:
                word_ += el
            else:
                new_word.append(word_)
                word_ = ""
        if word_:
            new_word.append(word_)

        cnt_vow = 0

        # create words based on vowels
        for seg in new_word:
            n = len(seg)
            for i in range(n):
                unique_vowels = set()
                for j in range(i, n):
                    unique_vowels.add(seg[j])
                    if unique_vowels == vowels:
                        cnt_vow += 1

        return cnt_vow