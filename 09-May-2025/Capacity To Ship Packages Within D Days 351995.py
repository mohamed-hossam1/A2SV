# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def days_needed(capacity: int) -> int:
            day_count = 1
            current_load = 0
            for w in weights:
                if current_load + w <= capacity:
                    current_load += w
                else:
                    day_count += 1
                    current_load = w
            return day_count

        low = max(weights)
        high = sum(weights)
        result = high

        while low <= high:
            mid = (low + high) // 2
            needed = days_needed(mid)
            if needed <= days:
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return result