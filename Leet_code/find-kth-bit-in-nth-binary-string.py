class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def helper(n):
            if n == 1:
                return "0"
            
            curr = helper(n-1)
            result = (curr) + "1" + invert(curr)[::-1]

            return result
        
        def invert(s):
            new_s = ""

            for c in s:
                if c == "1":
                    new_s+="0"
                else:
                    new_s+="1"
            
            return new_s

        
        res = helper(n)[k-1]
        
        return res

        
