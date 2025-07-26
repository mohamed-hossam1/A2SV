# Problem: Binary Tree Paths - https://leetcode.com/problems/binary-tree-paths/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def traverse(node, path):
            path += ('->' if path != '' else '')+ str(node.val)

            if node.left == node.right:
                return [path]
            elif node.right and node.left:
                return traverse(node.right, path) + traverse(node.left, path)
            elif node.left:
                return traverse(node.left, path)
            else: 
                return traverse(node.right, path)
            
        return traverse(root, '')
