"""
94. Binary Tree Inorder Traversal
Easy
12.5K
663
company
Amazon
company
Adobe
company
Uber
Given the root of a binary tree, return the inorder traversal of its nodes' values.



Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        temp = root
        all_vals = list()
        def traverse(temp):
            if temp is None:
                return

            traverse(temp.left)
            all_vals.append(temp.val)
            traverse(temp.right)
        traverse(root)
        return all_vals