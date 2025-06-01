# Problem: Watering Plants - https://leetcode.com/problems/watering-plants/

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans = 0
        vol = capacity

        for i, cur in enumerate(plants):
            isEnoughWater = cur <= vol
            ans += (0 if isEnoughWater else 2) * i + 1
            vol = (vol if isEnoughWater else capacity) - cur

        return ans