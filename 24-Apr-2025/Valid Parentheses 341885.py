# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses


def valid(c):
    if c==']':
        return '['
    elif c=='}':
        return '{'
    if c==')':
        return '('

class Solution(object):
    def isValid(self, s):        
        stack = []
        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if stack and stack[-1]==valid(c):
                    stack.pop()
                else:
                    return False
                    
        return not stack
                
        