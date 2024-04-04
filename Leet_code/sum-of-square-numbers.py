import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i, j = 0, int(math.sqrt(c))

        while i <=j:
            sumOfTwoNumbers = i*i + j*j
            if sumOfTwoNumbers == c:
                return True
            elif sumOfTwoNumbers > c:
                j-=1
            else:
                i+=1
        
        return False
