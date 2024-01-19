"""
1975. Maximum Matrix Sum
Medium
Topics
Hint
You are given an n x n integer matrix. You can do the following operation any number of times:

Choose any two adjacent elements of matrix and multiply each of them by -1.
Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using
the operation mentioned above.



Example 1:


Input: matrix = [[1,-1],[-1,1]]
Output: 4
Explanation: We can follow the following steps to reach sum equals 4:
- Multiply the 2 elements in the first row by -1.
- Multiply the 2 elements in the first column by -1.
Example 2:


Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
Output: 16
Explanation: We can follow the following step to reach sum equals 16:
- Multiply the 2 last elements in the second row by -1.


"""
class Solution(object):
    def maxMatrixSum(self, matrix):
        cnt=0
        for i in matrix:
            for j in i:
                if j <0:
                    cnt+=1
        total = sum([sum([abs(x) for x in i])
                       for i in matrix])
        if cnt %2==0:
            return total
        else:
            min_value= min([min([abs(x) for x in i])
                       for i in matrix])
            return total-2 * min_value