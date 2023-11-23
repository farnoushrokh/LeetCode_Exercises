"""
243. Shortest Word Distance
Easy
1.2K
110
LinkedIn
company
Amazon
Oracle
Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2,
return the shortest distance between these two words in the list.



Example 1:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3
Example 2:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1


Constraints:

2 <= wordsDict.length <= 3 * 104
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.
word1 != word2

"""

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        lst1=[]
        lst2=[]
        final=[]
        for el in range(len(wordsDict)):
            if wordsDict[el] == word1:
                lst1.append(el)
            if wordsDict[el] ==word2:
                lst2.append(el)
        for i in lst1:
            for j in lst2:
                final.append(abs(i-j))
        return(min(final))