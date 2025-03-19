# Problem: Maximum Erasure Value  - https://leetcode.com/problems/maximum-erasure-value/

class Solution(object):
    def maximumUniqueSubarray(self, nums):
        l=0
        ans = 0
        cur = 0
        mp = defaultdict(int)

        for r in nums:
            cur +=r

            while mp[r]>0:
                mp[nums[l]]-=1
                cur-=nums[l]
                
                if mp[nums[l]]==0:
                    del mp[nums[l]]
                    
                l+=1

        
            mp[r]+=1
        
            ans = max(cur, ans)
        
        return ans
