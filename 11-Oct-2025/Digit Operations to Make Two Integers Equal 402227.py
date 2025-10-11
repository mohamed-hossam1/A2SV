# Problem: Digit Operations to Make Two Integers Equal - https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def minOperations(self, n: int, m: int) -> int:
        primes = {i for i in range(2, 10001) if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1))}
        if n in primes or m in primes:
            return -1
        def num_digits(n):
            i = 0
            while n > 0:
                n //= 10
                i += 1
            return i
        minimum = 10**(num_digits(n)-1)
        
        def neighbors(n):
            res = []
            p = 0
            q = n
            while q > 0:
                r = q%10
                inc,dec = n+(10**p), n-(10**p)
                if r < 9 and inc >= minimum and inc not in primes:
                    res.append(inc)
                if r > 0 and dec >= minimum and dec not in primes:
                    res.append(dec)
                q //= 10
                p += 1
            return res

        distances = defaultdict(int)
        distances[n] = 0
        queue = [(0,n)]
        while queue:
            d,n = heapq.heappop(queue)
            if n == m:
                return d + m
            for v in neighbors(n):
                if v not in distances or v in distances and d+n < distances[v]:
                    heapq.heappush(queue, (d+n,v))
                    distances[v] = d+n

        return -1


