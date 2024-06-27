class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime = [1]*(right+1)
        is_prime[0] = 0
        is_prime[1] = 0
        res = [-1, -1] 

        def prime_sieve(n):
            i = 2
            
            while i*i <= n:
                if is_prime[i]:
                    j = i*i
                    while j <=n:
                        is_prime[j] = 0
                        j+=i
                i+=1
            return is_prime
        prime_sieve(right)
        if sum(is_prime[left:]) < 2:
            return [-1, -1]

        start = None
        min_window = float("inf")
        for i in range(len(is_prime)):
            if is_prime[i] == 1 and i >= left:
                if not start:
                    start = i
                elif i - start < min_window:
                    res = [start, i]
                    min_window = i - start
                start = i

   
        return res

        