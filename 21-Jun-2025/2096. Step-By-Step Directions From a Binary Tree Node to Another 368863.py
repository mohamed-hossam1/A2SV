# Problem: 2096. Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/?envType=problem-list-v2&envId=depth-first-search


class Solution(object):
    def getDirections(self, root, startValue, destValue):
        """
        """
        def dfs(node, val, path):
            if not node:
                return False
            if node.val == val:
                return True
            if dfs(node.left, val, path):
                path.append('L')
                return True
            if dfs(node.right, val, path):
                path.append('R')
                return True
            return False
        
        start_path, dest_path = [], []
        dfs(root, startValue, start_path)
        dfs(root, destValue, dest_path)
        
        start_path.reverse()
        dest_path.reverse()
        
        i = 0
        while i < len(start_path) and i < len(dest_path) and start_path[i] == dest_path[i]:
            i += 1
        
        result = 'U' * (len(start_path) - i)
        result += ''.join(dest_path[i:])
        
        return result