# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for c in s:
            if c==')':
                if type(stack[-1]) is int:
                    tmp = stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(tmp*2)
                else:
                    stack.pop()
                    stack.append(1)
                
                if len(stack)>1 and type(stack[-2]) is int:
                    tmp = stack[-2]+stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(tmp)
            else:
                stack.append(c)
        return(stack[-1])

            
