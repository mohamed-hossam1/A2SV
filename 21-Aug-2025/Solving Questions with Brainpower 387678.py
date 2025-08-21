# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            take = questions[i][0] + (dp[i + questions[i][1] + 1] if i + questions[i][1] + 1 < n else 0)
            skip = dp[i + 1]
            dp[i] = max(take, skip)

        return dp[0]