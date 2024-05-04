class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        res = 0
        val = 0
        
        for c in s:
            if c == "(":
                stack.append(0)

            else:
                
                mul = stack.pop()
                val = max(1, mul*2)

                stack[-1] += val

        return stack[0]         


        