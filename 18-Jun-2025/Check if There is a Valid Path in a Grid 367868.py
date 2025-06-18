# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        path_match = {
            1: {'r': {1, 3, 5}, 'l': {1, 4, 6}},
            2: {'u': {2, 3, 4}, 'd': {2, 5, 6}},
            3: {'l': {1, 4, 6}, 'd': {5, 6, 2}},
            4: {'r': {1, 3, 5}, 'd': {2, 5, 6}},
            5: {'u': {2, 3, 4}, 'l': {1, 4, 6}},
            6: {'u': {2, 3, 4}, 'r': {1, 3, 5}},
        }
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        q = deque([(0, 0, grid[0][0])])
        while q:
            r, c, street = q.popleft()
            if r == m - 1 and c == n - 1:
                return True
            for nr, nc, direc in [(r + 1, c, 'd'), (r - 1, c, 'u'), (r, c + 1, 'r'), (r, c - 1, 'l')]:
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] in path_match[street].get(direc, set()):
                    q.append((nr, nc, grid[nr][nc]))
                    visited[nr][nc] = True
        return False