# Problem: Search in a BST - https://leetcode.com/problems/search-in-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        cur = root
        while cur!=None:
            if cur.val == val:
                return cur
            if cur.val>val:
                cur = cur.left
            else:
                cur = cur.right
        return None
        