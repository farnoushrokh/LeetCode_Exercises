"""

108. Convert Sorted Array to Binary Search Tree
Easy
10.3K
509
company
Amazon
company
Microsoft
company
Apple
Given an integer array nums where the elements are sorted in ascending order, convert it to a
height-balanced
 binary search tree.



Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:


Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def helper(self, right, left):
        if left > right:
            return None
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def traverse(arr):
            if not arr: return
            m = (len(arr) - 1)//2
            node = TreeNode(arr[m])
            node.left = traverse(arr[:m])
            node.right = traverse(arr[m+1:])
            return node
        return traverse(nums)