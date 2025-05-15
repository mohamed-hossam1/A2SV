# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def solve(i, j):
            if i == j:
                return nums[i]
            pick_left = nums[i] - solve(i + 1, j)
            pick_right = nums[j] - solve(i, j - 1)
            return max(pick_left, pick_right)
        
        return solve(0, len(nums) - 1) >= 0