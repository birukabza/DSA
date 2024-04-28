class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {"]": "[", "}": "{", ")": "("}
        stack = []
        
        for c in s:
            if c not in closeToOpen:
                stack.append(c)
                continue
            
            if not stack or stack[-1]!=closeToOpen[c]:
                return False
            
            stack.pop()

        return not stack
            
                
        