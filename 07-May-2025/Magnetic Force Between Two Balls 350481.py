# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

def can(mid,position,m): 
    prev_pos = position[0]
    count = 1
    for i in range(1,len(position)):
        if position[i] - prev_pos>=mid:
            count+=1
            prev_pos = position[i]
        if count==m:
            return True
    return False

    


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        low =1
        high = int(position[-1] / (m - 1.0)) + 1
        ans = 0
        while low<=high:
            mid = (low+high)//2
            if can(mid,position,m):
                ans = mid
                low = mid+1
            else:
                high = mid-1
        return ans

        














