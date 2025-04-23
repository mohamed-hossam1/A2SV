# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/


def op(x, y, operator):
    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '*':
        return x * y
    elif operator == '/':
        return int(x / y)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c in '+-*/':
                y = stack.pop()
                x = stack.pop()
                result = op(x, y, c)
                stack.append(result)
            else:
                stack.append(int(c))

        return stack[0]