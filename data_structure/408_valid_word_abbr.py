"""
408. Valid Word Abbreviation
Solved
Easy
Topics
Companies
A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.



Example 1:

Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").
Example 2:

Input: word = "apple", abbr = "a2e"
Output: false
Explanation: The word "apple" cannot be abbreviated as "a2e".


"""

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_ptr = 0
        abbr_ptr = 0

        while abbr_ptr < len(abbr) and word_ptr < len(word):
            if abbr[abbr_ptr].isalpha():
                # The letter must match the current character in the word
                if abbr[abbr_ptr] != word[word_ptr]:
                    return False
                # Move both pointers
                abbr_ptr += 1
                word_ptr += 1
            # If the current character in abbr is a digit
            elif abbr[abbr_ptr].isdigit():
                if abbr[abbr_ptr]=='0':
                    return False
                # Read the full number
                num = 0
                while abbr_ptr < len(abbr) and abbr[abbr_ptr].isdigit():
                    # Calculate the number
                    num = num * 10 + int(abbr[abbr_ptr])
                    abbr_ptr += 1
                # Leading zeros are not allowed, check if num is zero but it has a leading zero
                if num == 0:
                    return False
                word_ptr += num
            else:
                # Invalid ch
                return False

        return word_ptr == len(word) and abbr_ptr == len(abbr)
