class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1 or n ==2:
            return n if n == 2 else 0
        factors = []

        d = 2

        while d*d <= n:
            while n%d == 0:
                factors.append(d)
                n//=d
            d+=1
        if n > 1:
            factors.append(n)
            
        return sum(factors) 
        
        


        