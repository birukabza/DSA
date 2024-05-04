import math
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for token in tokens:
            if stack and token == "+":
                operand = stack.pop()
                stack[-1] = str(int(stack[-1]) + int(operand))
            elif stack and token == "-":
                operand = stack.pop()
                stack[-1] = str(int(stack[-1]) - int(operand))
            elif stack and token == '*':
                operand = stack.pop()
                stack[-1] = str(int(stack[-1]) * int(operand))
            elif stack and token == "/":
                operand = stack.pop()
                stack[-1] = str(math.trunc(int(stack[-1]) / int(operand)))
            else:
                stack.append(token)
                
        return int(stack[0])


        