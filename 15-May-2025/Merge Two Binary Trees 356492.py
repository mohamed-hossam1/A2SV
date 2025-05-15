# Problem: Merge Two Binary Trees - https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(a, b):
            if a is None: 
                return b
            if b is None: 
                return a
            
            return TreeNode(a.val + b.val, merge(a.left, b.left), merge(a.right, b.right))
        
        return merge(root1, root2)