# Problem: Find Kth Largest XOR Coordinate Value - https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/description/?envType=problem-list-v2&envId=bit-manipulation

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        prev_xor_row = [0 for _ in range(n+1)]
        left_cell = 0
        min_xors = []
        for i in range(m):
            xor_row = [0]
            for j in range(n):
                up = prev_xor_row[j]
                left = xor_row[-1]
                prev_diag = prev_xor_row[j-1]
                value = prev_diag ^ left ^ up ^ matrix[i][j]
                xor_row.append(value)
                heapq.heappush(min_xors, value)
                if len(min_xors) > k:
                    heapq.heappop(min_xors)
            prev_xor_row = xor_row[1:] + [0]
        return min_xors[0]
        