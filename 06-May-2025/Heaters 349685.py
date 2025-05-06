# Problem: Heaters - https://leetcode.com/problems/heaters/

def can(mid,houses,heaters):
    j = 0
    for house in houses:
        while j<len(heaters) and not (heaters[j] - mid <= house <= heaters[j]+mid):
            j+=1
        if j==len(heaters):
            return False
    return True 


class Solution:    
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        low,high = 0,10**9
        ans = -1
        while low<=high:
            mid = (low+high)//2
            if can(mid,houses,heaters):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans

