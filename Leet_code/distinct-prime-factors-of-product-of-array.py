class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        factors = set()

        
        def factorization(n):
            d = 2
            while d*d <= n:
                while n%d == 0:
                    factors.add(d)
                    n//=d
                d+=1
            if n > 1:
                factors.add(n)
        
        for n in nums:
            factorization(n)
        return len(factors)


           
        