# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        columns = defaultdict(list)
        rows = defaultdict(list)
        for x, y in stones:
            rows[x].append(y)
            columns[y].append(x)
        ans = 0
        visited = set()
        for x, y in stones:
            if (x,y) not in visited:
                visited.add((x,y))
                queue = deque([(x,y)])
                while queue:
                    cx, cy = queue.popleft()
                    for ny in rows[cx]:
                        if (cx, ny) not in visited:
                            queue.append((cx,ny))
                            visited.add((cx,ny))
                    for nx in columns[cy]:
                        if (nx, cy) not in visited:
                            queue.append((nx,cy))
                            visited.add((nx,cy))
                ans += 1
        return len(stones) - ans