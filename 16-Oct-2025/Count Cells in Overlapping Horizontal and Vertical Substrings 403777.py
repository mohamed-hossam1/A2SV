# Problem: Count Cells in Overlapping Horizontal and Vertical Substrings - https://leetcode.com/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings/description/

class Solution:
    def countCells(self, grid, pattern):
        m, n = len(grid), len(grid[0])
        L = len(pattern)
        
        if L > m * n:
            return 0
        
        H = []
        for i in range(m):
            for j in range(n):
                H.append(grid[i][j])
        
        V = []
        for j in range(n):
            for i in range(m):
                V.append(grid[i][j])
        
        MOD1 = 10**9 + 7
        MOD2 = 10**9 + 9
        base = 31
        
        max_len = m * n
        pow1 = [1] * (max_len + 1)
        pow2 = [1] * (max_len + 1)
        for i in range(1, max_len + 1):
            pow1[i] = (pow1[i-1] * base) % MOD1
            pow2[i] = (pow2[i-1] * base) % MOD2
        
        ph1 = ph2 = 0
        for ch in pattern:
            ph1 = (ph1 * base + (ord(ch) - 96)) % MOD1
            ph2 = (ph2 * base + (ord(ch) - 96)) % MOD2
        
        pre1_H = [0] * (max_len + 1)
        pre2_H = [0] * (max_len + 1)
        for i in range(max_len):
            pre1_H[i+1] = (pre1_H[i] * base + (ord(H[i]) - 96)) % MOD1
            pre2_H[i+1] = (pre2_H[i] * base + (ord(H[i]) - 96)) % MOD2
        
        pre1_V = [0] * (max_len + 1)
        pre2_V = [0] * (max_len + 1)
        for i in range(max_len):
            pre1_V[i+1] = (pre1_V[i] * base + (ord(V[i]) - 96)) % MOD1
            pre2_V[i+1] = (pre2_V[i] * base + (ord(V[i]) - 96)) % MOD2
        
        def get_hash(pre1, pre2, l, r, pow1, pow2):
            h1 = (pre1[r] - pre1[l] * pow1[r-l]) % MOD1
            h2 = (pre2[r] - pre2[l] * pow2[r-l]) % MOD2
            return (h1, h2)
        
        diff_H = [0] * (max_len + 2)
        diff_V = [0] * (max_len + 2)
        
        for start in range(max_len - L + 1):
            h1, h2 = get_hash(pre1_H, pre2_H, start, start + L, pow1, pow2)
            if h1 == ph1 and h2 == ph2:
                diff_H[start] += 1
                diff_H[start + L] -= 1
        
        for start in range(max_len - L + 1):
            h1, h2 = get_hash(pre1_V, pre2_V, start, start + L, pow1, pow2)
            if h1 == ph1 and h2 == ph2:
                diff_V[start] += 1
                diff_V[start + L] -= 1
        
        horizontal_count = [0] * max_len
        vertical_count = [0] * max_len
        hc = 0
        for i in range(max_len):
            hc += diff_H[i]
            horizontal_count[i] = hc
        vc = 0
        for i in range(max_len):
            vc += diff_V[i]
            vertical_count[i] = vc
        ans = 0
        for i in range(max_len):
            r, c = divmod(i, n)
            if horizontal_count[i] > 0:
                v_idx = c * m + r
                if v_idx < max_len and vertical_count[v_idx] > 0:
                    ans += 1
        return ans