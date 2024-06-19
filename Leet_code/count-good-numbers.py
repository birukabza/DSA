class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def power(base, exponent):

            if exponent == 0:
                return 1

            res = power(base, exponent//2)

            res = (res*res)%MOD

            return (base*res)%MOD if exponent%2 else res


        return (power(5, ((n + 1) // 2)) * power(4, (n // 2))) % MOD
