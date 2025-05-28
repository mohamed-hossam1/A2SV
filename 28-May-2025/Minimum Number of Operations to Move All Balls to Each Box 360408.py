# Problem: Minimum Number of Operations to Move All Balls to Each Box - https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = []
        for i in range(len(boxes)):
            distance = 0
            for j in range(len(boxes)):
                if boxes[j] == '1' and i != j:
                    distance += abs(i - j)
            result.append(distance)
        return result