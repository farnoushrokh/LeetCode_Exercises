"""

110. Balanced Binary Tree
Easy
10.1K
594
company
Amazon
company
Adobe
company
Facebook
Given a binary tree, determine if it is
height-balanced
.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def height(self, root):
        if not root:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return abs(self.height(root.left) - self.height(root.right)) < 2 and self.isBalanced(
            root.left) and self.isBalanced(root.right)