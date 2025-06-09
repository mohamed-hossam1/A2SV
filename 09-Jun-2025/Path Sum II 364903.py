# Problem: Path Sum II - https://leetcode.com/problems/path-sum-ii/description/

class Solution(object):
    def pathSum(self, root, targetSum):
        ans = []
        def dfs(node, curSum=0, curNodes=[]):
            if not node: return

            curNodes.append(node.val)
            curSum += node.val

            if not node.left and not node.right:
                if curSum == targetSum:
                    ans.append(curNodes + [])
                return

            if node.left:
                dfs(node.left, curSum, curNodes)
                curNodes.pop()
            
            if node.right:
                dfs(node.right, curSum, curNodes)
                curNodes.pop()

        dfs(root)
        return ans