# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

def minEatingSpeed(piles, h):
    left = 1
    right = max(piles)

    while left < right:
        mid = (left + right) // 2
        total = 0
        for pile in piles:
            total += (pile + mid - 1) // mid
        if total <= h:
            right = mid
        else:
            left = left + 1
    return left