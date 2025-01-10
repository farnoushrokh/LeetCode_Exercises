"""
119. Pascal's Triangle II
Solved
Easy
Topics
Companies
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]

"""


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            res = [1]
            for i in range(1, rowIndex + 1):
                new_row = [1]
                for j in range(1, len(res)):
                    new_row.append(res[j - 1] + res[j])
                new_row.append(1)
                res = new_row

        return res

