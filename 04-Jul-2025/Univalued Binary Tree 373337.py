# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def check(node, n):
            if not node:
                return True
            if node.val != n:
                return False
            return check(node.left, n) and check(node.right, n)
            
        if not root:
            return True
        num = root.val
        
        return check(root, num)