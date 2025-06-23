# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        m_map = {0: -1} 
        pre_sum = 0

        for i, num in enumerate(nums):
            pre_sum += num
            mod = pre_sum % k if k != 0 else pre_sum

            if mod in m_map:
                if i - m_map[mod] >= 2:
                    return True
            else:
                m_map[mod] = i 

        return False
