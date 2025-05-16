# Problem: Even Odd Tree - https://leetcode.com/problems/even-odd-tree/description/

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        queue = [root]
        level = 0
        while queue:
            prev = float('-inf') if level % 2 == 0 else float('inf')
            for _ in range(len(queue)):
                node = queue.pop(0)
                if (level % 2 == 0 and (node.val % 2 == 0 or node.val <= prev)) or (level % 2 != 0 and (node.val % 2 != 0 or node.val >= prev)):
                    return False
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                prev = node.val
            level += 1
        return True