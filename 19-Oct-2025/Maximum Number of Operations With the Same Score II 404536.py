# Problem: Maximum Number of Operations With the Same Score II - https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/description/

    def maxOperations(self, nums: List[int]) -> int:
        
        def dfs(score: int, cache: Dict, lo = 0, hi = len(nums) - 1) -> int:
            if hi <= lo:
                return 0
            if (lo, hi) not in cache:
                max_ops1 = 1 + dfs(score, cache, lo + 2, hi) if score == sum(nums[lo : lo + 2]) else 0
                max_ops2 = 1 + dfs(score, cache, lo, hi - 2) if score == sum(nums[hi - 1 : hi + 1]) else 0
                max_ops3 = 1 + dfs(score, cache, lo + 1, hi - 1) if score == nums[lo] + nums[hi] else 0
                cache[lo, hi] = max(max_ops1, max_ops2, max_ops3)
            return cache[lo, hi]
        
        return max(map(dfs, 
                       set([sum(nums[: 2]), sum(nums[-2 :]), nums[0] + nums[-1]]), 
                       (defaultdict() for _ in range(3))
                      )
                  )