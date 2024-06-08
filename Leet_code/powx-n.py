class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n<0:
            isNeg = True
        else:
            isNeg = False
        
        def power(n):
            if n == 0:
                return 1
            res = power(n//2)
            res*=res

            return x*res if n%2 else res
        
        ans = power(abs(n))

        return ans if not isNeg else 1/ans
