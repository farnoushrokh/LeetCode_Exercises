"""
118. Pascal's Triangle
Easy
Topics
Companies
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[]
        for i in range(numRows):
            rows=[None for _ in range(i+1)]
            rows[0], rows[-1]=1,1
            for row in range(1, len(rows)-1):
                rows[row]= res[i-1][row-1] + res[i-1][row]
            res.append(rows)
        return res