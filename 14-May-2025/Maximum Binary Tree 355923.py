# Problem: Maximum Binary Tree - https://leetcode.com/problems/maximum-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> list[TreeNode]:
        if not nums:
            return
        val = max(nums)
        i = nums.index(val)
        node = TreeNode(val)
        node.left = self.constructMaximumBinaryTree(nums[0:i])
        node.right = self.constructMaximumBinaryTree(nums[i + 1:])
        return node

