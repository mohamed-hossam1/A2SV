# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution(object):
    def removeDuplicateLetters(self, s):
        stack = []
        seen = set()
        counter = defaultdict(int)

        for c in s:
            counter[c] += 1

        for c in s:
            counter[c] -= 1  

            if c in seen:
                continue
            while stack and c < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())

            stack.append(c)
            seen.add(c)

        return "".join(stack)
