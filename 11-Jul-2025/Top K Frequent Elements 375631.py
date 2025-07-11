# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums, k):
        fre = Counter(nums)
        min_heap = []
        for num, fren in fre.items():
            heapq.heappush(min_heap, (fren,num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)


        ans = [num for freq, num in min_heap]
        return ans
