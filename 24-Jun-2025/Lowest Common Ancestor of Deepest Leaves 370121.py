# Problem: Lowest Common Ancestor of Deepest Leaves - https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        self.max_depth = 0
        self.lca = None

        def dfs(node, depth):
            if not node:
                return depth - 1  
            
           
            self.max_depth = max(self.max_depth, depth)


            left = dfs(node.left, depth + 1)
            right = dfs(node.right, depth + 1)

           
            if left == right == self.max_depth:
                self.lca = node

            return max(left, right)

        dfs(root, 0)
        return self.lca