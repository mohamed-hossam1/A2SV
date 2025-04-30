# Problem: Asteroid Collision - https://leetcode.com/problems/asteroid-collision/

class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []
        for c in asteroids:
            while stack and c < 0 < stack[-1]:
                if stack[-1] < -c:
                    stack.pop()
                    continue
                elif stack[-1] == -c:
                    stack.pop() 
                break
            else:
                stack.append(c)
        return stack
