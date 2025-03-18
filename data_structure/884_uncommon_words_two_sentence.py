"""
884. Uncommon Words from Two Sentences
Solved
Easy
Topics
Companies
A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.



Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"

Output: ["sweet","sour"]

Explanation:

The word "sweet" appears only in s1, while the word "sour" appears only in s2.

Example 2:

Input: s1 = "apple apple", s2 = "banana"

Output: ["banana"]

"""
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        dict_s1={}
        dict_s2={}
        s1_word=s1.split()
        s2_word=s2.split()
        res=[]
        for el in s1_word:
            if el not in dict_s1:
                dict_s1[el] =1
            else:
                dict_s1[el] +=1
        for el in s2_word:
            if el not in dict_s2:
                dict_s2[el] =1
            else:
                dict_s2[el] +=1
        for word in dict_s1:
            if dict_s1[word]==1 and word not in dict_s2:
                res.append(word)
        for word in dict_s2:
            if dict_s2[word]==1 and word not in dict_s1:
                res.append(word)
        return res