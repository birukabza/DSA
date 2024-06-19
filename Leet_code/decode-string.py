class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ""
        
        for c in s:
            if c.isdigit():
                if stack and isinstance(stack[-1],int):
                    curr_num = stack.pop()
                    stack.append(curr_num*10 + int(c))
                else:
                    stack.append(int(c))
            elif c == "]":
                curr_str = ""
                while True:
                    
                    if stack[-1] == "[":
                        stack.pop()
                        break

                    curr_str = stack.pop() + curr_str
                num = stack.pop()
                stack.append(curr_str*num)
            else:
                stack.append(c)
        
        return "".join(stack)


        